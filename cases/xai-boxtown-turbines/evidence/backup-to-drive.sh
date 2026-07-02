#!/usr/bin/env bash
# backup-to-drive.sh — sync this case's raw original-form binaries to the off-platform
# custodian (the veriticide suite/case-evidence/xai-boxtown-turbines) via rclone. Run from a machine
# that HAS the binaries + rclone configured (an agent can't move them as base64).
#   rclone config   # one-time: remote 'gdrive' (type drive); then from this dir: ./backup-to-drive.sh
set -euo pipefail
REMOTE="${RCLONE_REMOTE:-gdrive}"; DRIVE_FOLDER_ID="1dEYYxVV5ijNEtyd16yNFm0vuggPryKj4"
for d in */original; do item="$(dirname "$d")"; echo "== $item"
  rclone copy "$d" "$REMOTE:" --drive-root-folder-id "$DRIVE_FOLDER_ID" --checksum --progress \
    --include "*.warc" --include "*.html" --include "*.pdf" --include "*.png" --include "*.json" --include "*.bin" \
    --include "manifest.json" --include "sha256sums.txt" --include "archive-org-snapshots.txt"
done
echo "Done. Verify against custody-receipt.md."
