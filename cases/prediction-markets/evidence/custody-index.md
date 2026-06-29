# CANONICAL CUSTODY INDEX

*The single source of truth for the custody state and grade of every evidence item.*
*Mechanically derived from `evidence/*/capture.json` by `build-custody-index.py` — do not hand-edit; regenerate.*

> **This index governs.** Where any other file (charge theory, evidence matrix, source
> bundle, custody manifest) shows a custody state that conflicts with this table, **this
> table is authoritative.** Per-row custody marks elsewhere are indicative/historical.

**Generated:** 2026-06-29 · **Items:** 8 · **VERIFIED:** 0 · **LOCATOR-VERIFIED:** 8

| Item | Grade | Custody | Track | sha256(transcript) |
|---|---|---|---|---|
| `cftc-withdraws-political-sports-ban-2026` | S1 + embedded P1 (CFTC notice / Federal Register 2026-05105) | LOCATOR-VERIFIED | II(2)(d) — the apex act (permissive-posture foreclosure of the protective wall) + II(3)(d) | `41092ce332ab…` |
| `fed-staff-forecast-accuracy` | S1 (single secondary; PENDING-PRIMARY) | LOCATOR-VERIFIED | CONTROL / good-faith anchor (Art. V protected-activity reference) | `c4c364ade1de…` |
| `kalshi-candidate-enforcement-2026` | P2 (named enforcement actions) + S1 | LOCATOR-VERIFIED | II(3)(c) foreseeability + partial CONTROL (the exclusion wall, applied) | `b40ffc815ac4…` |
| `prediction-market-conflict-coverage-2026` | S1 (multiple independent outlets) | LOCATOR-VERIFIED | II(2)(c) corroboration — declaration-mode + convergence (context) | `6337a8a5c23b…` |
| `trump-cftc-thrive-post-2026` | P2 (Presidential statement) + S1 | LOCATOR-VERIFIED | Track B constructive authorization (executive endorsement) + Move 6 benefit reframe | `7482ee2beb64…` |
| `trumpjr-dual-platform-roles-2026` | S1 (multiple independent outlets) | LOCATOR-VERIFIED | II(2)(c) — the operator node of the vertical stack | `bd9a1da029bd…` |
| `truth-predict-competitor-2026` | S1 | LOCATOR-VERIFIED | II(2)(c) — the competitor node of the vertical stack | `87fed61cbcb6…` |
| `vandyke-venezuela-insider-bet-2026` | P1 (DOJ charging release) + S1 | LOCATOR-VERIFIED | II(2)(d) + II(3)(c) — the outcome channel made concrete; foreseeability anchor | `951faf635dee…` |

## Custody states

- **LOCATOR-VERIFIED** — canonical URL + verbatim text preserved as a hashed transcript; original-form bytes not yet held.
- **VERIFIED** — original artifact (WARC + PDF + screenshot) hashed into `<id>/original/manifest.json`. Full VERIFIED also assumes a second custodian + off-platform backup (see `../05-custody-manifest.md`).

## Grade legend

P1 primary artifact · P2 named on-record statement · S1 reputable secondary · S2 expert/modeling · A1 analyst inference · T1 witness testimony.
**`+ embedded P1` / `reported P1`** = held artifact is an outlet reproduction (S1); the underlying primary is pending capture — graded S1 to avoid inflation.

## Regenerate

```bash
# from cases/prediction-markets/evidence/
python3 build-custody-index.py
for d in */; do (cd "$d" && sha256sum -c sha256.txt); done
```

