# CANONICAL CUSTODY INDEX

*The single source of truth for the custody state and grade of every evidence item.*
*Mechanically derived from `evidence/*/capture.json` by `build-custody-index.py` — do not hand-edit; regenerate.*

> **This index governs.** Where any other file (charge theory, evidence matrix, source
> bundle, custody manifest) shows a custody state that conflicts with this table, **this
> table is authoritative.** Per-row custody marks elsewhere are indicative/historical.

**Generated:** 2026-06-30 · **Items:** 11 · **VERIFIED:** 11 · **LOCATOR-VERIFIED:** 0

| Item | Grade | Custody | Track | sha256(transcript) |
|---|---|---|---|---|
| `appeal-challenge` | P1 (appeal filing) + S1 (coverage) | VERIFIED | RECOGNITION-LIVE — stay-triggering appeal (the Tier-4 falsifier) | `d4c054502316…` |
| `board-mootness-denial` | S1 (local broadcast, on-record ruling) | VERIFIED | disposition — board denied appeal on mootness (~2025-12-15) | `3e3f1288dc06…` |
| `chamber-defense` | P1 (party statement, adverse interest) | VERIFIED | COUNTER-REGISTER — benefit reframe (Move 6) + 'everyone runs backup' CONTROL | `62bac7a167c4…` |
| `ej-harm` | S1 | VERIFIED | protected population + harm pathway — Boxtown, non-attainment, asthma/cancer | `5391caeb8cbe…` |
| `epa-action` | P1 (party/counsel press) — EPA + court track | VERIFIED | recognition continues in court (2026); EPA context | `bbb8410273f8…` |
| `permit-appeal-p1` | P1 (the appeal legal filing itself) | VERIFIED | authorization/recognition — the P1 appeal document | `d7a8cec0a895…` |
| `permit-grant` | S1 (embeds P1: SCHD permit) | VERIFIED | authorization — SCHD permit, 15 turbines, 2025-07-02 | `1a88239a8434…` |
| `selc-letter-2024-08` | P1 (dated correspondence to the regulator) | VERIFIED | foreseeability — early notice to SCHD (2024-08-26) | `2fed26c71907…` |
| `selc-letter-2025-04` | P1 (dated correspondence to the regulator) | VERIFIED | foreseeability — SELC et al. to SCHD (2025-04-09) | `6646a4be5120…` |
| `turbine-survey` | S1 + ADV (SELC aerial/thermal imagery) | VERIFIED | instrument scale — 'dozens'; count CONTESTED; May removals (CONTROL) | `5077718929aa…` |
| `unpermitted-operation` | S1 (secondary; embeds P1 permit + SCHD determination) | VERIFIED | predicate / instrument — unpermitted operation + 'nonroad' exemption frame | `87372c314bf6…` |

## Custody states

- **LOCATOR-VERIFIED** — canonical URL + verbatim text preserved as a hashed transcript; original-form bytes not yet held.
- **VERIFIED** — original artifact (WARC + PDF + screenshot) hashed into `<id>/original/manifest.json`. Full VERIFIED also assumes a second custodian + off-platform backup (see `../05-custody-manifest.md`).

## Grade legend

P1 primary artifact · P2 named on-record statement · S1 reputable secondary · S2 expert/modeling · A1 analyst inference · T1 witness testimony.
**`+ embedded P1` / `reported P1`** = held artifact is an outlet reproduction (S1); the underlying primary is pending capture — graded S1 to avoid inflation.

## Regenerate

```bash
# from cases/election-redistricting/evidence/
python3 build-custody-index.py
for d in */; do (cd "$d" && sha256sum -c sha256.txt); done
```

