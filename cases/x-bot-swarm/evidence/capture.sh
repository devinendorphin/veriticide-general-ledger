#!/usr/bin/env bash
#
# capture.sh — turn LOCATOR-VERIFIED evidence items into ORIGINAL-CAPTURED ones.
#
# Run this from cases/x-bot-swarm/evidence/ on a machine with OPEN EGRESS
# (your laptop, a cloud VM, or a Claude Code web env set to "Full" network access).
# It does NOT work in the default "Trusted" web environment — outbound fetches to
# news/source hosts are blocked there (that is the whole reason this script exists).
#
# For each evidence item it:
#   1. collects every https URL from the item's capture.json + transcript.md
#   2. preserves each URL in original form:  WARC (wget) + PDF + full-page PNG
#      (headless Chrome) + video (yt-dlp, for democracynow/youtube items)
#   3. optionally submits the URL to the Internet Archive (third-party attestation)
#   4. hashes every artifact into evidence/<id>/original/manifest.json
#   5. with --promote, flips the item's custody_state to VERIFIED in capture.json
#
# Honest-custody note: a bare run does NOT change custody_state (no overclaiming).
# Promotion to VERIFIED is a deliberate, separate step (--promote) and still assumes
# you complete the manifest's other two conditions out of band: a second custodian
# and an off-platform backup. Committing original/ to this repo is one custodian.
#
# Usage:
#   ./capture.sh                 # capture everything, do not change custody states
#   ./capture.sh --promote       # capture + mark successfully-captured items VERIFIED
#   ./capture.sh --archive-org   # also submit each URL to web.archive.org Save Page Now
#   ./capture.sh musk-woodchipper-posts tamlyn-cable    # only these items
#
# Dependencies (install what you can; the script degrades gracefully if some are missing):
#   wget            apt-get install wget        — WARC capture (request+response+headers)
#   google-chrome   or chromium                 — PDF + full-page screenshot
#   yt-dlp          pipx install yt-dlp         — video items
#   python3, sha256sum, curl                    — usually preinstalled
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

echo "Tools: wget=$(have wget && echo y || echo n)  chrome=${CHROME:-none}  yt-dlp=$(have yt-dlp && echo y || echo n)"
echo "Items: ${#ITEMS[@]}   promote=$PROMOTE   archive.org=$ARCHIVE_ORG"
echo

slug() { printf '%s' "$1" | sed -E 's#^https?://##; s#[^A-Za-z0-9._-]#_#g' | cut -c1-80; }

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

  if [ ${#urls[@]} -eq 0 ]; then echo "  (no URLs found)"; continue; fi

  for url in "${urls[@]}"; do
    s="$(slug "$url")"; base="$outdir/$s"
    echo "  -> $url"
    if have wget; then
      wget -q --no-warc-compression --warc-file="$base" \
           -e robots=off --page-requisites --span-hosts --timeout=45 --tries=2 \
           -O "$base.html" "$url" 2>>"$outdir/wget.log" \
        && echo "     warc+html ok" || echo "     wget failed (see original/wget.log)"
    fi
    if [ -n "$CHROME" ]; then
      "$CHROME" --headless=new --disable-gpu --no-sandbox --hide-scrollbars \
        --print-to-pdf="$base.pdf" "$url" >/dev/null 2>&1 && echo "     pdf ok" || true
      "$CHROME" --headless=new --disable-gpu --no-sandbox --window-size=1280,2000 \
        --screenshot="$base.png" "$url" >/dev/null 2>&1 && echo "     png ok" || true
    fi
    case "$url" in
      *democracynow.org*|*youtube.com*|*youtu.be*)
        have yt-dlp && yt-dlp -q -o "$base.%(ext)s" "$url" 2>>"$outdir/ytdlp.log" \
          && echo "     video ok" || true ;;
    esac
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
  done

  # hash everything captured into a per-item manifest
  ( cd "$outdir" && find . -type f ! -name manifest.json ! -name sha256sums.txt -print0 \
      | xargs -0 sha256sum 2>/dev/null > sha256sums.txt )
  python3 - "$item" <<'PY'
import json,sys,os,hashlib,datetime
item=sys.argv[1]; od=os.path.join(item,"original"); files={}
for root,_,fs in os.walk(od):
    for f in fs:
        if f in ("manifest.json","sha256sums.txt"): continue
        p=os.path.join(root,f); h=hashlib.sha256(open(p,'rb').read()).hexdigest()
        files[os.path.relpath(p,od)]={"sha256":h,"bytes":os.path.getsize(p)}
json.dump({"item":item,"captured_at":datetime.datetime.utcnow().isoformat()+"Z",
           "artifact_count":len(files),"artifacts":files},
          open(os.path.join(od,"manifest.json"),"w"),indent=2)
print(f"     {len(files)} artifact(s) hashed -> {od}/manifest.json")
PY

  if [ "$PROMOTE" -eq 1 ]; then
    python3 - "$item" <<'PY'
import json,sys,os,datetime
item=sys.argv[1]; cj=os.path.join(item,"capture.json"); d=json.load(open(cj))
man=os.path.join(item,"original","manifest.json")
n=json.load(open(man))["artifact_count"] if os.path.exists(man) else 0
if n>0:
    d["custody_state"]="VERIFIED"
    d["original_form_capture"]=f"CAPTURED: {n} artifact(s) in original/ (manifest.json). Complete VERIFIED by adding a 2nd custodian + off-platform backup."
    d["verified_at"]=datetime.datetime.utcnow().isoformat()+"Z"
    json.dump(d,open(cj,"w"),indent=2); print(f"     custody_state -> VERIFIED ({n} artifacts)")
else:
    print("     not promoted (0 artifacts captured)")
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
