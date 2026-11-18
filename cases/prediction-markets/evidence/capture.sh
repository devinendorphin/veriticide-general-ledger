#!/usr/bin/env bash
#
# capture.sh — turn LOCATOR-VERIFIED evidence items into ORIGINAL-CAPTURED ones.
#
# Run this from cases/prediction-markets/evidence/ on a machine with OPEN EGRESS
# (your laptop, a cloud VM, or a Claude Code web env set to "Full"/"Custom" network access).
# It does NOT work in a "Trusted" web environment — outbound fetches to news/regulator
# hosts are blocked there (HTTP 403; that is the whole reason this script exists, and is
# exactly the state in which this packet was built — see CAPTURE-RUNBOOK.md).
#
# For each evidence item it:
#   1. collects every https URL from the item's capture.json + transcript.md
#   2. VALIDATES that each URL is genuinely reachable (HTTP 2xx) BEFORE capturing —
#      a blocked/404/403/dead URL produces NO artifacts (see "Response validation")
#   3. preserves each reachable URL in original form:  WARC (wget) + PDF + full-page
#      PNG (headless Chrome) + video (yt-dlp, for youtube items)
#   4. optionally submits reachable URLs to the Internet Archive (3rd-party attestation)
#   5. hashes every artifact into evidence/<id>/original/manifest.json and records a
#      per-URL outcome in evidence/<id>/original/capture-report.json
#   6. with --promote, flips the item's custody_state to HASHED-PENDING-BACKUP in
#      capture.json, but ONLY if EVERY one of the item's URLs captured cleanly. VERIFIED is
#      reserved for the separate off-platform-backup step; --promote never sets VERIFIED.
#
# Response validation (why this exists): an earlier version hashed whatever wget/Chrome
# produced and promoted the item if ANY file existed. In a partially-blocked network
# that silently "captured" Chrome "This site can't be reached" screenshots and wget
# 403/404 pages, then stamped the item VERIFIED (reset 2026-07-02; see
# docs/custody-status-2026-07-02.md). This version refuses to do that:
#   - a URL is CAPTURED only if a pre-flight GET returns 2xx AND (when wget ran) the
#     WARC's response record carries a 2xx status; otherwise it is recorded FAILED and
#     any stale/partial artifacts for it are deleted.
#   - an item is PROMOTED to HASHED-PENDING-BACKUP only if it had >=1 URL and ZERO failed URLs.
#     If even one source is unreachable, custody_state is left unchanged and the item
#     records exactly which URLs are missing.
#
# Honest-custody note: a bare run does NOT change custody_state (no overclaiming).
# Promotion to HASHED-PENDING-BACKUP is a deliberate step (--promote); reaching VERIFIED still assumes
# you complete the manifest's other two conditions out of band: a second custodian
# and an off-platform backup. Committing original/ to this repo is one custodian.
#
# Usage:
#   ./capture.sh                 # capture everything, do not change custody states
#   ./capture.sh --promote       # capture + mark fully-captured items HASHED-PENDING-BACKUP
#   ./capture.sh --archive-org   # also submit each reachable URL to web.archive.org
#   ./capture.sh vandyke-venezuela-insider-bet-2026 cftc-withdraws-political-sports-ban-2026   # only these items
#
# Dependencies (install what you can; the script degrades gracefully if some are missing):
#   wget            apt-get install wget        — WARC capture (request+response+headers)
#   google-chrome   or chromium                 — PDF + full-page screenshot
#   yt-dlp          pipx install yt-dlp         — video items
#   python3, sha256sum, curl                    — required (curl is the reachability gate)
#
set -uo pipefail

PROMOTE=0
ARCHIVE_ORG=0
ITEMS=()
for arg in "$@"; do
  case "$arg" in
    --promote)     PROMOTE=1 ;;
    --archive-org) ARCHIVE_ORG=1 ;;
    -*)            echo "unknown flag: $arg" >&2; exit 2 ;;
    *)             ITEMS+=("$arg") ;;
  esac
done

# default: every directory that has a capture.json
if [ ${#ITEMS[@]} -eq 0 ]; then
  while IFS= read -r d; do ITEMS+=("$(dirname "$d")"); done \
    < <(find . -maxdepth 2 -name capture.json | sort)
fi

have() { command -v "$1" >/dev/null 2>&1; }
CHROME=""
for c in google-chrome google-chrome-stable chromium chromium-browser; do
  have "$c" && { CHROME="$c"; break; }
done
# Fallback: Playwright-bundled Chromium (Claude Code web / CI images set
# PLAYWRIGHT_BROWSERS_PATH; the binary is at .../chromium-*/chrome-linux/chrome).
if [ -z "$CHROME" ]; then
  for c in "${PLAYWRIGHT_BROWSERS_PATH:-/opt/pw-browsers}"/chromium-*/chrome-linux/chrome; do
    [ -x "$c" ] && { CHROME="$c"; break; }
  done
fi

if ! have curl; then
  echo "FATAL: curl is required (it is the reachability gate that prevents archiving error pages)." >&2
  exit 3
fi

UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

echo "Tools: wget=$(have wget && echo y || echo n)  chrome=${CHROME:-none}  yt-dlp=$(have yt-dlp && echo y || echo n)"
echo "Items: ${#ITEMS[@]}   promote=$PROMOTE   archive.org=$ARCHIVE_ORG"
echo

slug() { printf '%s' "$1" | sed -E 's#^https?://##; s#[^A-Za-z0-9._-]#_#g' | cut -c1-80; }

# pre-flight reachability check: echo the final HTTP status code (follows redirects).
# "000" means the connection never completed (DNS/tunnel/proxy refusal).
preflight() {
  local c
  c="$(curl -sS -L -A "$UA" -o /dev/null -w '%{http_code}' \
       --connect-timeout 20 --max-time 60 "$1" 2>/dev/null)" || c="000"
  # -L can emit one code per redirect hop; keep the final 3-digit code only
  printf '%s' "${c:(-3)}"
}

# status of the main document in a wget WARC: the first response that is not a redirect.
# wget follows 3xx itself and records each hop as its own response, so the FIRST status
# of a redirected URL is the 301/302, not the page (fixed 2026-11-18; PMC and House pages
# were losing their WARC to this). Only status lines at the start of a line are read.
warc_status() {
  grep -aoE '^HTTP/[0-9.]+ [0-9]{3}' "$1" 2>/dev/null | grep -oE '[0-9]{3}$' | grep -m1 -v '^3'
}

# Is a saved page real content? A 2xx status is not enough: bot challenges and login walls
# are served with 200, some sites return an empty app shell, and a Chrome print can catch a
# challenge or a not-yet-loaded page. One checker serves the wget HTML, Chrome's DOM dump and
# the text of a Chrome PDF. For HTML it judges the FIRST document in the file (wget -O with
# --page-requisites appends the page's assets after it). The visible text (scripts/styles
# removed) must reach MIN_VISIBLE_CHARS, the title and opening must not start like an
# interstitial, and the first 1,500 characters must not contain a challenge phrase.
# Calibrated 2026-11-18 on the DOGE re-capture (non-content pages <= 22 visible characters,
# shortest real page 2,199); the phrase list was extended after an Imperva challenge printed
# by Chrome (817 characters) passed the length floor alone. Prints the reason on failure.
MIN_VISIBLE_CHARS="${MIN_VISIBLE_CHARS:-500}"
content_check() {  # content_check html|text FILE
  python3 -I - "$1" "$2" "$MIN_VISIBLE_CHARS" <<'PY'
import re, sys, html
mode, path, minc = sys.argv[1], sys.argv[2], int(sys.argv[3])
raw = open(path, "rb").read(4_000_000).decode("utf-8", "replace")
title = ""
if mode == "html":
    if raw.lstrip().startswith("%PDF"):
        sys.exit(0)  # a PDF document fetched directly; judged by its HTTP status
    m = re.search(r"(?is)</html\s*>", raw)
    doc = raw[:m.end()] if m else raw
    t = re.search(r"(?is)<title[^>]*>(.*?)</title>", doc)
    title = html.unescape(t.group(1)).strip() if t else ""
    d = re.sub(r"(?is)<(script|style|noscript|template|svg)[^>]*>.*?</\1>", " ", doc)
    d = re.sub(r"(?s)<!--.*?-->", " ", d)
    vis = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", d))).strip()
else:  # text of a Chrome PDF: drop the print header/footer lines (date, URL, page count)
    keep = [l for l in raw.splitlines() if l.strip()
            and not re.match(r"^\s*(https?://\S+|\d+/\d+|\d{1,2}/\d{1,2}/\d{2,4},.*)\s*$", l)]
    vis = re.sub(r"\s+", " ", " ".join(keep)).strip()
start = re.compile(r"^(just a moment|attention required|access denied|are you a robot|"
                   r"verify you are human|log ?in\b|sign ?in\b|please enable (javascript|cookies)|"
                   r"security check|captcha|request blocked|403 forbidden|404 not found)", re.I)
phrase = re.compile(r"additional security check|verify (that )?(an actual human|you are (a )?human)|"
                    r"checking (if the site connection is secure|your browser)|"
                    r"enable javascript and cookies to continue|pardon our interruption|"
                    r"press (&|and) hold|are you a robot|request unsuccessful\. incapsula|"
                    r"protected and accelerated by imperva|cloudflare ray id|ddos protection by", re.I)
if start.search(title) or start.search(vis[:200]):
    print(f'interstitial ("{(title or vis)[:60]}")'); sys.exit(1)
hit = phrase.search(vis[:1500])
if hit:
    print(f'challenge page ("{hit.group(0)}")'); sys.exit(1)
if len(vis) < minc:
    print(f"{len(vis)} visible characters (< {minc})"); sys.exit(1)
PY
}
page_has_content() { content_check html "$1"; }

# Does a Chrome PDF render carry real page text? A page printed before its content loads
# comes out blank; a print can also land on a challenge. Needs pdftotext (poppler-utils);
# without it the check is skipped with a warning.
pdf_has_text() {
  command -v pdftotext >/dev/null 2>&1 \
    || { echo "     (pdftotext not installed: PDF text not checked)"; return 0; }
  local tmp why rc; tmp="$(mktemp)"
  pdftotext "$1" "$tmp" 2>/dev/null
  why="$(content_check text "$tmp")"; rc=$?; rm -f "$tmp"
  [ "$rc" -eq 0 ] || echo "     pdf not page content: $why"
  return "$rc"
}

# Is a headless-Chrome render of $1 a real page, or Chrome's "This site can't be
# reached" interstitial?  Chrome returns exit 0 and writes a non-empty PNG/PDF even
# for connection errors, so file existence is NOT proof of capture. We re-fetch the
# DOM and look for Chrome's neterror/interstitial internals, which never appear in
# normal site HTML.  Returns 0 = real page, 1 = error page / failed.
chrome_render_real() {
  local dom
  dom="$("$CHROME" --headless=new --disable-gpu --no-sandbox \
          --virtual-time-budget=8000 --dump-dom "$1" 2>/dev/null)"
  grep -qE 'id="main-frame-error"|interstitial-wrapper|chrome-error://' <<<"$dom" && return 1
  local tmp why; tmp="$(mktemp)"; printf '%s' "$dom" > "$tmp"
  why="$(page_has_content "$tmp")"; local rc=$?; rm -f "$tmp"
  [ "$rc" -eq 0 ] || { echo "     chrome DOM not page content: $why"; return 1; }
  return 0
}

for item in "${ITEMS[@]}"; do
  item="${item%/}"
  [ -f "$item/capture.json" ] || { echo "skip $item (no capture.json)"; continue; }
  echo "== $item =="
  outdir="$item/original"; mkdir -p "$outdir"

  # collect URLs: source_url (if http) + every https URL in the transcript, deduped
  mapfile -t urls < <(
    { python3 -c "import json,sys;u=json.load(open('$item/capture.json')).get('source_url','');print(u) if u.startswith('http') else None" 2>/dev/null
      grep -oE 'https://[^ )<>\"`]+' "$item/transcript.md" 2>/dev/null; } \
    | sed -E 's/[.,);]+$//' | sort -u | grep -E '^https://' )

  if [ ${#urls[@]} -eq 0 ]; then echo "  (no URLs found)"; echo; continue; fi

  # reset the per-item outcome report for this run
  : > "$outdir/capture-report.tsv"   # url<TAB>http_status<TAB>captured(yes|no)

  for url in "${urls[@]}"; do
    s="$(slug "$url")"; base="$outdir/$s"
    echo "  -> $url"

    code="$(preflight "$url")"
    if ! [[ "$code" =~ ^2[0-9][0-9]$ ]]; then
      echo "     UNREACHABLE (http $code) — no artifacts kept"
      rm -f "$base".*               # drop any stale/partial artifacts from a prior run
      printf '%s\t%s\tno\n' "$url" "$code" >> "$outdir/capture-report.tsv"
      continue
    fi

    captured_any=0   # the AUTHORITATIVE capture signal (WARC, or video, or a
                     # VALIDATED browser render when wget is unavailable)
    warc_ok=0

    if have wget; then
      # wget exits non-zero if ANY page requisite fails (e.g. a blocked CDN asset),
      # even when the main document downloaded fine — so judge the WARC by its
      # main-document response status, not by wget's overall exit code.
      wget -q --no-warc-compression --warc-file="$base" \
           -e robots=off --page-requisites --span-hosts --timeout=45 --tries=2 \
           -U "$UA" -O "$base.html" "$url" 2>>"$outdir/wget.log" || true
      ws="$(warc_status "$base.warc")"
      if [[ "$ws" =~ ^2[0-9][0-9]$ ]] && [ -s "$base.html" ] \
         && ! why="$(page_has_content "$base.html")"; then
        echo "     http $ws but not page content: $why — discarding warc+html"
        rm -f "$base.warc" "$base.html"
      elif [[ "$ws" =~ ^2[0-9][0-9]$ ]] && [ -s "$base.html" ]; then
        echo "     warc+html ok (http $ws)"; captured_any=1; warc_ok=1
      else
        echo "     wget main doc non-2xx/empty (http ${ws:-none}) — discarding warc+html"
        rm -f "$base.warc" "$base.html"
      fi
    fi

    if [ -n "$CHROME" ]; then
      # Chrome writes a non-empty PNG/PDF even for "site can't be reached" errors, so
      # VALIDATE the render before keeping it. PDF/PNG are supplementary proof only —
      # when wget ran, they never by themselves mark a URL captured (the WARC does).
      if chrome_render_real "$url"; then
        "$CHROME" --headless=new --disable-gpu --no-sandbox --hide-scrollbars \
          --virtual-time-budget=8000 --run-all-compositor-stages-before-draw \
          --print-to-pdf="$base.pdf" "$url" >/dev/null 2>&1 || true
        if [ -s "$base.pdf" ] && pdf_has_text "$base.pdf"; then
          echo "     pdf ok"
          "$CHROME" --headless=new --disable-gpu --no-sandbox --window-size=1280,2000 \
            --virtual-time-budget=8000 --run-all-compositor-stages-before-draw \
            --screenshot="$base.png" "$url" >/dev/null 2>&1 || true
          [ -s "$base.png" ] && echo "     png ok" || rm -f "$base.png"
        else
          echo "     pdf render blank or missing — discarding pdf/png"
          rm -f "$base.pdf" "$base.png"
        fi
        # only let a browser render count as capture if we have no WARC for this URL
        if [ "$warc_ok" -eq 0 ] && { [ -s "$base.pdf" ] || [ -s "$base.png" ]; }; then
          captured_any=1
        fi
      else
        echo "     chrome render was an error page — discarding pdf/png"
        rm -f "$base.pdf" "$base.png"
      fi
    fi

    case "$url" in
      *youtube.com*|*youtu.be*)
        if have yt-dlp && yt-dlp -q -o "$base.%(ext)s" "$url" 2>>"$outdir/ytdlp.log"; then
          echo "     video ok"; captured_any=1
        fi ;;
    esac

    if [ "$captured_any" -eq 1 ]; then
      printf '%s\t%s\tyes\n' "$url" "$code" >> "$outdir/capture-report.tsv"
      if [ "$ARCHIVE_ORG" -eq 1 ] && have curl; then
        # Save Page Now replies either 200 with `content-location: /web/...` (relative)
        # or 302 with `location: https://web.archive.org/web/...` (absolute). Handle both.
        hdrs="$(curl -sS -I --max-time 60 "https://web.archive.org/save/$url" 2>/dev/null)"
        snap="$(printf '%s' "$hdrs" | awk 'tolower($1)=="location:"{print $2}'        | tr -d '\r' | tail -1)"
        [ -z "$snap" ] && snap="$(printf '%s' "$hdrs" | awk 'tolower($1)=="content-location:"{print "https://web.archive.org" $2}' | tr -d '\r' | tail -1)"
        case "$snap" in
          https://web.archive.org/*) echo "$snap" >> "$outdir/archive-org-snapshots.txt"; echo "     archive.org: $snap" ;;
          *) echo "     archive.org: no snapshot URL returned" ;;
        esac
      fi
    else
      echo "     reachable but no artifact retained — recording as not captured"
      printf '%s\t%s\tno\n' "$url" "$code" >> "$outdir/capture-report.tsv"
    fi
  done

  # hash everything captured into a per-item manifest + structured capture report
  ( cd "$outdir" && find . -type f ! -name manifest.json ! -name sha256sums.txt \
       ! -name capture-report.tsv ! -name capture-report.json -print0 \
      | xargs -0 -r sha256sum 2>/dev/null > sha256sums.txt )
  python3 - "$item" <<'PY'
import json,sys,os,hashlib,datetime
item=sys.argv[1]; od=os.path.join(item,"original"); files={}
skip={"manifest.json","sha256sums.txt","capture-report.tsv","capture-report.json"}
for root,_,fs in os.walk(od):
    for f in fs:
        if f in skip: continue
        p=os.path.join(root,f); h=hashlib.sha256(open(p,'rb').read()).hexdigest()
        files[os.path.relpath(p,od)]={"sha256":h,"bytes":os.path.getsize(p)}
# parse the per-URL outcome report
rows=[]; ok=0; fail=0
tsv=os.path.join(od,"capture-report.tsv")
if os.path.exists(tsv):
    for line in open(tsv):
        line=line.rstrip("\n")
        if not line: continue
        url,code,cap=line.split("\t")
        rows.append({"url":url,"http_status":code,"captured":cap=="yes"})
        ok += (cap=="yes"); fail += (cap!="yes")
json.dump({"item":item,"captured_at":datetime.datetime.utcnow().isoformat()+"Z",
           "artifact_count":len(files),
           "urls_total":len(rows),"urls_captured":ok,"urls_failed":fail,
           "artifacts":files},
          open(os.path.join(od,"manifest.json"),"w"),indent=2)
json.dump({"item":item,"urls_total":len(rows),"urls_captured":ok,"urls_failed":fail,
           "results":rows},
          open(os.path.join(od,"capture-report.json"),"w"),indent=2)
print(f"     {len(files)} artifact(s) hashed; URLs captured {ok}/{len(rows)} (failed {fail})")
PY

  if [ "$PROMOTE" -eq 1 ]; then
    python3 - "$item" <<'PY'
import json,sys,os,datetime
item=sys.argv[1]; cj=os.path.join(item,"capture.json"); d=json.load(open(cj))
rep=os.path.join(item,"original","capture-report.json")
r=json.load(open(rep)) if os.path.exists(rep) else {"urls_total":0,"urls_captured":0,"urls_failed":0,"results":[]}
total,okc,failc=r["urls_total"],r["urls_captured"],r["urls_failed"]
if total>0 and failc==0:
    d["custody_state"]="HASHED-PENDING-BACKUP"
    d["original_form_capture"]=(f"CAPTURED: all {okc} source URL(s) preserved in original/ "
        f"(manifest.json + capture-report.json). Complete VERIFIED by adding a 2nd "
        f"custodian + off-platform backup.")
    d["promoted_at"]=datetime.datetime.utcnow().isoformat()+"Z"
    json.dump(d,open(cj,"w"),indent=2)
    print(f"     custody_state -> HASHED-PENDING-BACKUP ({okc}/{total} URLs captured)")
else:
    missing=[x["url"] for x in r["results"] if not x["captured"]]
    d["original_form_capture"]=(f"PARTIAL: {okc}/{total} URL(s) captured; "
        f"{failc} unreachable in this run. Not promoted. Missing: "
        + ("; ".join(missing) if missing else "none"))
    json.dump(d,open(cj,"w"),indent=2)
    if total==0:
        print("     not promoted (no URLs found)")
    else:
        print(f"     NOT promoted — {failc}/{total} URL(s) unreachable (custody_state unchanged)")
PY
  fi
  echo
done

# rebuild the canonical index from the (possibly updated) capture.json files
if [ -f build-custody-index.py ]; then
  python3 build-custody-index.py
fi
echo "Done. Review original/ in each item, commit, and back up off-platform."
echo "Reminder: VERIFIED in the manifest also requires a 2nd custodian + off-platform copy."
