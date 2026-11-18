#!/usr/bin/env bash
# capture.sh — original-form capture used to build this store (2026-10-10, open egress).
# For each URL: wget WARC (request+response) + response body into <item>/original/,
# then hash every artifact into original/manifest.json + sha256sums.txt.
# Never changes custody_state. VERIFIED still needs a 2nd custodian + off-platform backup.
# Requires the agent-proxy CA bundle path below; adjust --ca-certificate off-platform.
# usage: cap.sh <item_dir> <url>...   -> writes <item_dir>/original/{*.html|*.pdf,*.warc.gz,manifest.json,sha256sums.txt}
#
# Response validation (added 2026-11-18, ported from cases/doge-usaid-pepfar/evidence/capture.sh):
# the 2026-10-10 version kept and hashed whatever wget wrote, so a 403/404 body or an empty
# file counted as an artifact. A URL is now KEPT only if a pre-flight GET returns 2xx AND
# the WARC's main-document response (after redirects) is 2xx AND the body is non-empty AND,
# for HTML, the page has real content (page_has_content: no bot challenge or login wall); otherwise its
# artifacts are deleted and it is recorded as not captured. Per-URL outcomes go to
# original/capture-report.{tsv,json}, which are not hashed into the manifest. See
# docs/custody-status-2026-07-02.md for why an error page must never count as a capture.
set -uo pipefail
item="$1"; shift; out="$item/original"; mkdir -p "$out"
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
CA=(--ca-certificate=/root/.ccr/ca-bundle.crt)
CURL_CA=(--cacert /root/.ccr/ca-bundle.crt)
[ -f /root/.ccr/ca-bundle.crt ] || { CA=(); CURL_CA=(); }

# final HTTP status after redirects; "000" = the connection never completed
preflight() {
  local c
  c="$(curl -sS -L "${CURL_CA[@]}" -A "$UA" -o /dev/null -w '%{http_code}' \
       --connect-timeout 20 --max-time 60 "$1" 2>/dev/null)" || c="000"
  printf '%s' "${c:(-3)}"
}
# status of the main document in a gzipped WARC: the first response that is not a redirect
# (wget follows 3xx itself and records each hop). Only line-initial status lines are read.
warc_status() {
  zcat -f "$1" 2>/dev/null | grep -aoE '^HTTP/[0-9.]+ [0-9]{3}' | grep -oE '[0-9]{3}$' | grep -m1 -v '^3'
}

# Is a saved HTML document (or a Chrome DOM dump) a real page? A 2xx status is not enough:
# bot challenges and login walls are served with 200, and some sites return an empty app
# shell. Judges the FIRST document in the file (wget -O with --page-requisites appends the
# page's assets after it): its visible text (scripts/styles removed) must reach
# MIN_VISIBLE_CHARS, and its title and opening text must not match a known interstitial.
# Calibrated 2026-11-18 on the DOGE re-capture: the six non-content pages had <= 22 visible
# characters; the shortest real page had 2,199. Prints the reason on failure.
MIN_VISIBLE_CHARS="${MIN_VISIBLE_CHARS:-500}"
page_has_content() {
  python3 -I - "$1" "$MIN_VISIBLE_CHARS" <<'PY'
import re, sys, html
path, minc = sys.argv[1], int(sys.argv[2])
raw = open(path, "rb").read(4_000_000).decode("utf-8", "replace")
if raw.lstrip().startswith("%PDF"):
    sys.exit(0)  # a PDF document fetched directly; judged by its HTTP status
m = re.search(r"(?is)</html\s*>", raw)
doc = raw[:m.end()] if m else raw
t = re.search(r"(?is)<title[^>]*>(.*?)</title>", doc)
title = html.unescape(t.group(1)).strip() if t else ""
d = re.sub(r"(?is)<(script|style|noscript|template|svg)[^>]*>.*?</\1>", " ", doc)
d = re.sub(r"(?s)<!--.*?-->", " ", d)
vis = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", d))).strip()
bad = re.compile(r"^(just a moment|attention required|access denied|are you a robot|"
                 r"verify you are human|log ?in\b|sign ?in\b|please enable (javascript|cookies)|"
                 r"security check|captcha|request blocked|403 forbidden|404 not found)", re.I)
if bad.search(title) or bad.search(vis[:200]):
    print(f'interstitial ("{(title or vis)[:60]}")'); sys.exit(1)
if len(vis) < minc:
    print(f"{len(vis)} visible characters (< {minc})"); sys.exit(1)
PY
}

: > "$out/capture-report.tsv"   # url<TAB>http_status<TAB>captured(yes|no)
for u in "$@"; do
  slug=$(printf '%s' "$u" | sed -E 's#^https?://##; s#[^A-Za-z0-9._-]#_#g' | cut -c1-80)
  ext=html; case "$u" in *.pdf) ext=pdf;; esac
  code="$(preflight "$u")"
  if ! [[ "$code" =~ ^2[0-9][0-9]$ ]]; then
    rm -f "$out/$slug.$ext" "$out/$slug.warc.gz"
    printf '%s\t%s\tno\n' "$u" "$code" >> "$out/capture-report.tsv"
    echo "  UNREACHABLE (http $code) — no artifacts kept: $u"; continue
  fi
  wget -q "${CA[@]}" -U "$UA" --timeout=60 --tries=2 \
       --warc-file="$out/$slug" --warc-cdx=off -O "$out/$slug.$ext" "$u"
  rc=$?
  ws="$(warc_status "$out/$slug.warc.gz")"
  why=""
  if [[ "$ws" =~ ^2[0-9][0-9]$ ]] && [ -s "$out/$slug.$ext" ] && [ "$ext" = html ] \
     && ! why="$(page_has_content "$out/$slug.$ext")"; then
    rm -f "$out/$slug.$ext" "$out/$slug.warc.gz"
    printf '%s\t%s\tno\n' "$u" "$ws" >> "$out/capture-report.tsv"
    echo "  http $ws but not page content: $why — discarded: $u"
  elif [[ "$ws" =~ ^2[0-9][0-9]$ ]] && [ -s "$out/$slug.$ext" ]; then
    printf '%s\t%s\tyes\n' "$u" "$ws" >> "$out/capture-report.tsv"
    echo "  ok (wget $rc, http $ws) $(wc -c <"$out/$slug.$ext") $u"
  else
    rm -f "$out/$slug.$ext" "$out/$slug.warc.gz"
    printf '%s\t%s\tno\n' "$u" "${ws:-none}" >> "$out/capture-report.tsv"
    echo "  main document non-2xx/empty (http ${ws:-none}) — discarded: $u"
  fi
done
python3 -I - "$out" <<'PY'
import sys,os,json,hashlib,datetime
d=sys.argv[1]; arts={}
skip={"manifest.json","sha256sums.txt","capture-report.tsv","capture-report.json"}
for f in sorted(os.listdir(d)):
    if f in skip: continue
    b=open(os.path.join(d,f),"rb").read(); arts[f]={"sha256":hashlib.sha256(b).hexdigest(),"bytes":len(b)}
rows=[l.rstrip("\n").split("\t") for l in open(os.path.join(d,"capture-report.tsv")) if l.strip()]
rep={"urls_total":len(rows),"urls_captured":sum(r[2]=="yes" for r in rows),
     "urls_failed":sum(r[2]!="yes" for r in rows),
     "results":[{"url":r[0],"http_status":r[1],"captured":r[2]=="yes"} for r in rows]}
json.dump(rep,open(os.path.join(d,"capture-report.json"),"w"),indent=2)
m={"item":"./"+os.path.basename(os.path.dirname(os.path.abspath(d))),"captured_at":datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00","Z"),
   "capture_tool":"wget (WARC + response body) via Claude Code agent proxy, open egress; 2xx-validated","artifact_count":len(arts),"artifacts":arts}
json.dump(m,open(os.path.join(d,"manifest.json"),"w"),indent=2)
open(os.path.join(d,"sha256sums.txt"),"w").write("".join(f"{v['sha256']}  ./{k}\n" for k,v in arts.items()))
print("  manifest:",len(arts),"artifacts; URLs captured",rep["urls_captured"],"/",rep["urls_total"])
PY
