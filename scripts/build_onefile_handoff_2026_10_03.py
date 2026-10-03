#!/usr/bin/env python3
"""Bundle the second independent-adjudication handoff (2026-10-03 material) into ONE file.

Public-repo material only; nothing from the private tier is included. The proposer's
"Outcome" rulings on innocent readings are redacted so they cannot anchor the reviewer
(standing note: exclude Claude's own verdicts and self-audits). The redaction runs from an
Outcome line to the next blank line.
"""
import pathlib, re, sys

ROOT = pathlib.Path(".")
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else
                   "docs/handoffs/chatgpt-adjudication-onefile-2026-10-03.md")
REDACT = "[PROPOSER'S RULING ON THIS READING REDACTED FOR BLIND REVIEW]"

def redact(text):
    out, skipping = [], False
    for line in text.splitlines():
        if re.match(r"^\s*(- )?\*\*Outcome", line):
            indent = re.match(r"^\s*", line).group(0)
            out.append(f"{indent}- {REDACT}")
            skipping = True
            continue
        if skipping:
            if line.strip() == "":
                skipping = False
                out.append(line)
            continue
        out.append(line)
    return "\n".join(out)

def ledger_slice(start_pat, end_pat):
    lines = (ROOT / "ledger/ledger.md").read_text().splitlines()
    s = next(i for i, l in enumerate(lines) if re.search(start_pat, l))
    e = next(i for i, l in enumerate(lines[s + 1:], s + 1) if re.search(end_pat, l))
    return "\n".join(lines[s:e])

LEDGER = [
    ("Entry 6.4: elaboration of \"democratic\"", r'^\*\*Elaboration on "democratic"', r"^\*\*ENTRY 6\.5\*\*"),
    ("Entry 6.6: Kurzweil", r"^\*\*ENTRY 6\.6\*\*", r"^\*\*ENTRY 6\.7\*\*"),
    ("Entry 6.7: Thiel's Antichrist lectures", r"^\*\*ENTRY 6\.7\*\*", r"^### CLUSTER 7"),
    ("TD-008 and TD-009", r"^\*\*TD-008:", r"^## SECTION VIII"),
]
DOCS = [
    "docs/thiel-map-2026-10-03.md",
    "docs/salon-comparators-public-2026-10-03.md",
    "docs/household-sexual-power-public-tier-2026-10-03.md",
    "cases/epstein-survivor-unredaction/07-powerful-associates-annex.md",
    "docs/survivor-comparator-2026-10-03.md",
    "docs/cicero-homelessness-map-2026-10-03.md",
    "docs/housing-first-vs-treatment-first-evidence-2026-10-03.md",
    "docs/institutionalization-coercive-treatment-history-2026-10-03.md",
    "docs/institutional-sexual-abuse-accountability-2026-10-03.md",
]

BRIEF = (ROOT / "docs/handoffs/chatgpt-adjudication-brief-2026-10-03.md").read_text()

parts = [BRIEF, "\n\n# PART 1: LEDGER ENTRIES (data)\n"]
for title, s, e in LEDGER:
    parts.append(f"\n\n========== LEDGER: {title} ==========\n\n" + redact(ledger_slice(s, e)))
parts.append("\n\n# PART 2: SESSION DOCUMENTS (data)\n")
for f in DOCS:
    parts.append(f"\n\n========== FILE: {f} ==========\n\n" + redact((ROOT / f).read_text()))
OUT.write_text("\n".join(parts) + "\n")
n = sum(p.count(REDACT) for p in parts)
print(OUT, OUT.stat().st_size // 1024, "KB;", n, "outcome blocks redacted")
