# CANONICAL CUSTODY INDEX

*The single source of truth for the custody state and grade of every evidence item.*
*Mechanically derived from `evidence/*/capture.json` by `build-custody-index.py` — do not hand-edit; regenerate.*

> **This index governs.** Where any other file (charge theory, evidence matrix, source
> bundle, custody manifest) shows a custody state that conflicts with this table, **this
> table is authoritative.** Per-row custody marks elsewhere are indicative/historical.

**Generated:** 2026-07-02 · **Items:** 11 · **States:** HASHED-PENDING-BACKUP 11

| Item | Grade | Custody | Track | sha256(transcript) |
|---|---|---|---|---|
| `appeal-challenge` | P1 (appeal filing) + S1 (coverage) | HASHED-PENDING-BACKUP | RECOGNITION-LIVE — stay-triggering appeal (the Tier-4 falsifier) | `d4c054502316…` |
| `board-mootness-denial` | S1 (local broadcast, on-record ruling) | HASHED-PENDING-BACKUP | disposition — board denied appeal on mootness (~2025-12-15) | `3e3f1288dc06…` |
| `chamber-defense` | P1 (party statement, adverse interest) | HASHED-PENDING-BACKUP | COUNTER-REGISTER — benefit reframe (Move 6) + 'everyone runs backup' CONTROL | `62bac7a167c4…` |
| `ej-harm` | S1 | HASHED-PENDING-BACKUP | protected population + harm pathway — Boxtown, non-attainment, asthma/cancer | `5391caeb8cbe…` |
| `epa-action` | P1 (party/counsel press) — EPA + court track | HASHED-PENDING-BACKUP | recognition continues in court (2026); EPA context | `bbb8410273f8…` |
| `permit-appeal-p1` | P1 (the appeal legal filing itself) | HASHED-PENDING-BACKUP | authorization/recognition — the P1 appeal document | `d7a8cec0a895…` |
| `permit-grant` | S1 (embeds P1: SCHD permit) | HASHED-PENDING-BACKUP | authorization — SCHD permit, 15 turbines, 2025-07-02 | `1a88239a8434…` |
| `selc-letter-2024-08` | P1 (dated correspondence to the regulator) | HASHED-PENDING-BACKUP | foreseeability — early notice to SCHD (2024-08-26) | `2fed26c71907…` |
| `selc-letter-2025-04` | P1 (dated correspondence to the regulator) | HASHED-PENDING-BACKUP | foreseeability — SELC et al. to SCHD (2025-04-09) | `6646a4be5120…` |
| `turbine-survey` | S1 + ADV (SELC aerial/thermal imagery) | HASHED-PENDING-BACKUP | instrument scale — 'dozens'; count CONTESTED; May removals (CONTROL) | `5077718929aa…` |
| `unpermitted-operation` | S1 (secondary; embeds P1 permit + SCHD determination) | HASHED-PENDING-BACKUP | predicate / instrument — unpermitted operation + 'nonroad' exemption frame | `87372c314bf6…` |

## Custody states

- **LOCATOR-VERIFIED** — canonical URL + verbatim text preserved as a hashed transcript; original-form bytes not held.
- **HASHED-PENDING-BACKUP** — original-form artifacts (WARC/PDF/PNG) were captured and hashed into `<id>/original/manifest.json`, so the in-repo integrity record exists, **but no off-platform second custodian / backup is yet in place**, and captures made before this repo moved to an open-egress environment may include interstitial or error-page bytes for source hosts that were blocked at capture time (compare artifact sizes in the manifest). Not tribunal-grade.
- **VERIFIED** — original-form artifact hashed **and** independently backed up off-platform (a second custodian, e.g. the `the veriticide suite` Drive/GCP store) **and** confirmed to hold the real source content rather than an interstitial. This is the only tribunal-grade state.

*Reconciliation note (2026-07-02): items previously marked VERIFIED were reset to HASHED-PENDING-BACKUP because the off-platform backup that VERIFIED requires was never completed. See `docs/custody-status-2026-07-02.md`.*

## Grade legend

P1 primary artifact · P2 named on-record statement · S1 reputable secondary · S2 expert/modeling · A1 analyst inference · T1 witness testimony.
**`+ embedded P1` / `reported P1`** = held artifact is an outlet reproduction (S1); the underlying primary is pending capture — graded S1 to avoid inflation.

## Regenerate

```bash
# from cases/xai-boxtown-turbines/evidence/
python3 build-custody-index.py
for d in */; do (cd "$d" && sha256sum -c sha256.txt); done
```

