#!/usr/bin/env bash
# backup-to-drive.sh — sync this case's raw original-form binaries to the off-platform
# custodian (the veriticide suite / case-evidence / x-bot-swarm) using rclone.
#
# WHY THIS EXISTS: the raw WARC/HTML/PDF/PNG for this case total ~130 MB. An MCP/agent
# tool cannot practically move that (base64 through a chat tool = millions of tokens),
# so the operator runs this from a machine that HAS the binaries + rclone configured.
#
# Prereq (one-time):
#   rclone config          # create a remote named 'gdrive' (type: drive)
# Then, from cases/x-bot-swarm/evidence/:
#   ./backup-to-drive.sh
#
# The Drive folder id below is 'the veriticide suite/case-evidence/x-bot-swarm'.
set -euo pipefail
REMOTE="${RCLONE_REMOTE:-gdrive}"
DRIVE_FOLDER_ID="1-znznciSoHZ2lKXjViic7eUhM-dJynZ8"
for d in */original; do
  item="$(dirname "$d")"
  echo "== syncing $item/original -> Drive/$item"
  rclone copy "$d" "$REMOTE:" --drive-root-folder-id "$DRIVE_FOLDER_ID" \
    --drive-import-formats "" --checksum --progress \
    --include "*.warc" --include "*.html" --include "*.pdf" --include "*.png" \
    --include "manifest.json" --include "sha256sums.txt" --include "archive-org-snapshots.txt" \
    --drive-server-side-across-configs
done
echo "Done. Verify counts in the Drive folder against custody-receipt.md sha256 list."
