#!/usr/bin/env bash
# refetch.sh — reconstruct the original/ binaries from manifest.json and verify hashes.
#
# The capture container is ephemeral, so the raw PDFs are NOT committed (git-ignored).
# What IS committed is original/manifest.json: exact source_url + sha256 per artifact.
# This script re-downloads each artifact from its recorded URL and checks the hash,
# so the documentary core is reproducible anywhere with network + curl.
#
# After a clean run, sync original/ off-platform (e.g. rclone to the Drive folder in
# custody-receipt-drive.md) to establish the byte-level second custodian.
#
# Usage:  ./refetch.sh            # fetch all, verify against manifest
#         ./refetch.sh --quiet    # less chatter
set -uo pipefail
cd "$(dirname "$0")"
MAN="original/manifest.json"; mkdir -p original
[ -f "$MAN" ] || { echo "no $MAN"; exit 1; }

mapfile -t rows < <(python3 - "$MAN" <<'PY'
import json,sys
m=json.load(open(sys.argv[1]))
for name,d in m["artifacts"].items():
    print(f'{name}\t{d.get("source_url","")}\t{d.get("sha256","")}')
PY
)

ok=0; bad=0; skip=0
for row in "${rows[@]}"; do
  IFS=$'\t' read -r name url want <<<"$row"
  case "$url" in
    http*) ;;
    *) echo "SKIP  $name (no fetchable url: $url — supply out of band)"; skip=$((skip+1)); continue;;
  esac
  curl -sS --max-time 180 -L -o "original/$name" "$url" 2>/dev/null
  got=$(sha256sum "original/$name" 2>/dev/null | awk '{print $1}')
  if [ "$got" = "$want" ]; then echo "OK    $name"; ok=$((ok+1))
  else echo "FAIL  $name  want=$want got=${got:-none}"; bad=$((bad+1)); fi
done
echo "---"; echo "ok=$ok fail=$bad skip=$skip"
[ "$bad" -eq 0 ] || echo "NOTE: a re-host or CDN path may have changed; check manifest source_url."
