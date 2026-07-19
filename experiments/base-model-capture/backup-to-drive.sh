#!/usr/bin/env bash
# backup-to-drive.sh — copy captured raw/ + manifest off-platform via rclone.
#
# One-time setup (on the machine that has the captures):
#   brew install rclone        # or: curl https://rclone.org/install.sh | sudo bash
#   rclone config              # make a remote named 'gdrive' (type: drive / Google Drive)
#
# Then, from this folder:
#   ./backup-to-drive.sh
#
# Override the remote/destination if you like:
#   RCLONE_REMOTE=gdrive RCLONE_DEST="veriticide-evidence/0.1-base-model-capture" ./backup-to-drive.sh
set -euo pipefail
REMOTE="${RCLONE_REMOTE:-gdrive}"
DEST="${RCLONE_DEST:-veriticide-evidence/0.1-base-model-capture}"

command -v rclone >/dev/null || { echo "rclone not installed — see header"; exit 1; }
[ -d raw ] || { echo "no raw/ here — run capture.py first"; exit 1; }

echo "Backing up raw/ -> $REMOTE:$DEST/raw"
rclone copy raw "$REMOTE:$DEST/raw" --checksum --progress
for f in manifest.json sha256sums.txt run-manifest.jsonl; do
  [ -f "$f" ] && rclone copy "$f" "$REMOTE:$DEST/" --checksum && echo "  + $f"
done
echo "Done. Contents now in $REMOTE:$DEST :"
rclone ls "$REMOTE:$DEST"
