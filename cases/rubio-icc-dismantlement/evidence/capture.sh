#!/usr/bin/env bash
# capture.sh — original-form capture used to build this store (2026-10-10, open egress).
# For each URL: wget WARC (request+response) + response body into <item>/original/,
# then hash every artifact into original/manifest.json + sha256sums.txt.
# Never changes custody_state. VERIFIED still needs a 2nd custodian + off-platform backup.
# Requires the agent-proxy CA bundle path below; adjust --ca-certificate off-platform.
# usage: cap.sh <item_dir> <url>...   -> writes <item_dir>/original/{*.html|*.pdf,*.warc.gz,manifest.json,sha256sums.txt}
set -uo pipefail
item="$1"; shift; out="$item/original"; mkdir -p "$out"
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
for u in "$@"; do
  slug=$(printf '%s' "$u" | sed -E 's#^https?://##; s#[^A-Za-z0-9._-]#_#g' | cut -c1-80)
  ext=html; case "$u" in *.pdf) ext=pdf;; esac
  wget -q --ca-certificate=/root/.ccr/ca-bundle.crt -U "$UA" --timeout=60 --tries=2 \
       --warc-file="$out/$slug" --warc-cdx=off -O "$out/$slug.$ext" "$u"
  echo "  $? $(wc -c <"$out/$slug.$ext") $u"
done
python3 -I - "$out" <<'PY'
import sys,os,json,hashlib,datetime
d=sys.argv[1]; arts={}
for f in sorted(os.listdir(d)):
    if f in ("manifest.json","sha256sums.txt"): continue
    b=open(os.path.join(d,f),"rb").read(); arts[f]={"sha256":hashlib.sha256(b).hexdigest(),"bytes":len(b)}
m={"item":"./"+os.path.basename(os.path.dirname(os.path.abspath(d))),"captured_at":datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00","Z"),
   "capture_tool":"wget (WARC + response body) via Claude Code agent proxy, open egress","artifact_count":len(arts),"artifacts":arts}
json.dump(m,open(os.path.join(d,"manifest.json"),"w"),indent=2)
open(os.path.join(d,"sha256sums.txt"),"w").write("".join(f"{v['sha256']}  ./{k}\n" for k,v in arts.items()))
print("  manifest:",len(arts),"artifacts")
PY
