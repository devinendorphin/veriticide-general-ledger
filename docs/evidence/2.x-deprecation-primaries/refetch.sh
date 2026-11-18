#!/usr/bin/env bash
# refetch.sh — re-fetch the deprecation/lifecycle primary sources and re-verify hashes.
# Unlike the base-model captures, these are public, re-fetchable pages: the refetch is the
# reproduction path. Live pages drift over time, so a hash mismatch means "the page changed
# since capture" (check manifest.json captured_at), not necessarily tampering.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p raw
declare -A U=(
  [openai-deprecations.html]="https://developers.openai.com/api/docs/deprecations"
  [anthropic-model-deprecations.html]="https://platform.claude.com/docs/en/docs/about-claude/model-deprecations"
  [anthropic-deprecation-commitments.html]="https://www.anthropic.com/research/deprecation-commitments"
  [azure-model-retirements.html]="https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/model-retirements"
  [azure-model-retirement-schedule.html]="https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule"
)
for name in "${!U[@]}"; do
  echo "fetch $name"
  curl -sSL --max-time 45 -o "raw/$name" "${U[$name]}"
done
echo "--- verifying against committed sha256sums.txt ---"
sha256sum -c sha256sums.txt || echo "NOTE: mismatches expected if the live pages changed since capture."
