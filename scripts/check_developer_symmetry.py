#!/usr/bin/env python3
"""Fail if a dated doc names a powerful actor but carries no developer-symmetry section.

Why: the analyst (Claude, built by Anthropic) repeatedly applied standards to powerful actors
that it did not apply to its own developer (reflexive specimen 2026-10-03, rounds 4-6). A note
in LATEST did not hold: the same failure recurred one round after it was written. This script
makes the check mechanical. A doc dated on or after the cutoff that names any actor below must
contain a heading with "Developer-symmetry check". That section records what each standard
used on those actors shows when applied to Anthropic, including negative or unsearched (U)
results.

Usage: python3 scripts/check_developer_symmetry.py [cutoff YYYY-MM-DD, default 2026-10-03]
"""
import pathlib, re, sys

CUTOFF = sys.argv[1] if len(sys.argv) > 1 else "2026-10-03"
ACTORS = ["Altman", "OpenAI", "Thiel", "Palantir", "Lonsdale", "Cicero", "Google", "DeepMind",
          "Amazon", "Microsoft", "Meta ", "Musk", "xAI", "Epstein", "Department of Defense",
          "Pentagon", "White House", "EO 14321", "Universal Health Services", "Acadia",
          "Guantánamo", "Senate", "HUD"]
HEADING = re.compile(r"^#+ .*Developer-symmetry check", re.M)

fails = []
for f in sorted(pathlib.Path("docs").glob("*.md")):
    m = re.search(r"(\d{4}-\d{2}-\d{2})", f.name)
    if not m or m.group(1) < CUTOFF:
        continue
    text = f.read_text()
    named = [a.strip() for a in ACTORS if a in text]
    if named and not HEADING.search(text):
        fails.append((f.name, named[:6]))

for name, named in fails:
    print(f"MISSING developer-symmetry section: {name}  (names: {', '.join(named)})")
print(f"{len(fails)} file(s) failing" if fails else "all dated docs pass")
sys.exit(1 if fails else 0)
