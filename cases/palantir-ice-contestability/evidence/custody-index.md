# CANONICAL CUSTODY INDEX

*The single source of truth for the custody state and grade of every evidence item.*
*Mechanically derived from `evidence/*/capture.json` by `build-custody-index.py` — do not hand-edit; regenerate.*

> **This index governs.** Where any other file (charge theory, evidence matrix, source
> bundle, custody manifest) shows a custody state that conflicts with this table, **this
> table is authoritative.** Per-row custody marks elsewhere are indicative/historical.

**Generated:** 2026-06-30 · **Items:** 10 · **VERIFIED:** 9 · **LOCATOR-VERIFIED:** 1

| Item | Grade | Custody | Track | sha256(transcript) |
|---|---|---|---|---|
| `contestability` | S1 (journalism) + court testimony | VERIFIED | contestability failure — ELITE scores vs warrant standard | `b5b524a32dfa…` |
| `contract` | P1 (federal award record — structured JSON) | VERIFIED | authorization/instrument — the ICE sole-source award | `ab9fbaace817…` |
| `counter-register` | ADV (aggregator) + Palantir position as reported | VERIFIED | counter-register + charge aggregator | `da0be6fc7761…` |
| `harm-citizen-suit` | P1 (party press + court filing) | VERIFIED | harm specimen — U.S. citizen wrongful arrest | `1b64a92f8aa1…` |
| `harm-npr` | S1 (journalism) | VERIFIED | harm pathway — people caught in the surveillance web | `849385241e31…` |
| `instrument-scope` | S1 (policy journalism) | VERIFIED | instrument scope — data fusion + functions | `339a5f343e98…` |
| `medicaid-feed` | ADV/S1 (EFF report) | VERIFIED | NULL/PARTIAL — Medicaid-data feed | `377e22317b56…` |
| `oversight-goldman` | P1 (congressional press) | VERIFIED | recognition-live — Goldman/Wyden/Velazquez demand | `bc5eda4060c9…` |
| `oversight-menendez` | P1 (congressional letter) | VERIFIED | authorization/foreseeability — congressional oversight | `ea43a123b5af…` |
| `palantir-defense` | P1 (company's own published statement) | LOCATOR-VERIFIED | counter-register (first-party) — the neutral-tool defense | `63e5ac4f9a1f…` |

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

