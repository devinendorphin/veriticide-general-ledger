#!/usr/bin/env bash
# One-time setup. Run this first.
set -e

echo "Setting up Veriticide Ledger scraper..."

# Check Python
if ! command -v python3 &>/dev/null; then
    echo "ERROR: python3 not found. Install Python 3.10 or later."
    exit 1
fi

cd "$(dirname "$0")/../scraper"

python3 -m pip install -r requirements.txt --quiet

echo ""
echo "Setup complete."
echo ""
echo "To run the collector:"
echo "  cd scraper"
echo "  ANTHROPIC_API_KEY=your_key_here python3 scraper.py"
echo ""
echo "Without an API key (raw capture only):"
echo "  python3 scraper.py"
echo ""
echo "To test without writing to the ledger:"
echo "  python3 scraper.py --dry-run"
