# CANONICAL CUSTODY INDEX

*The single source of truth for the custody state and grade of every evidence item.*
*Mechanically derived from `evidence/*/capture.json` by `build-custody-index.py` — do not hand-edit; regenerate.*

> **This index governs.** Where any other file (charge theory, evidence matrix, source
> bundle, custody manifest) shows a custody state that conflicts with this table, **this
> table is authoritative.** Per-row custody marks elsewhere are indicative/historical.

**Generated:** 2026-10-10 · **Items:** 15 · **States:** HASHED-PENDING-BACKUP 15

| Item | Grade | Custody | Track | sha256(transcript) |
|---|---|---|---|---|
| `ap-sanctions-operational-effects` | S1 (AP via PBS; interested/anonymous sources flagged) | HASHED-PENDING-BACKUP | A / C | `2b97fb891cfe…` |
| `civil-society-record` | S1-advocacy (interested parties) | HASHED-PENDING-BACKUP | C | `66e2bf3c553d…` |
| `eo-14203` | P1 (White House) | HASHED-PENDING-BACKUP | B | `ae695ad30270…` |
| `icc-institution-response` | P1 (ICC; interested party) | HASHED-PENDING-BACKUP | D / C | `d0d14278d0bc…` |
| `icc-non-ally-docket` | P1 (ICC) | HASHED-PENDING-BACKUP | C | `71e299b39650…` |
| `icc-palestine-warrants-2024` | P1 (ICC press release; decisions not captured) | HASHED-PENDING-BACKUP | C | `7df85db86312…` |
| `khan-removal-2026` | S1 (JURIST; Al Jazeera) — counter-evidence | HASHED-PENDING-BACKUP | counter / C | `72719cd5d057…` |
| `rome-statute-text` | P1 (ICC-hosted PDF) | HASHED-PENDING-BACKUP | reference | `1e8c73eb6f51…` |
| `state-albanese-designation` | P1 (State Dept) | HASHED-PENDING-BACKUP | D | `d7fddf1241ca…` |
| `state-icc-campaign-launch` | P1 (State Media Note, U.S. Mission mirror) + S1 (Al Jazeera, video quotes) | HASHED-PENDING-BACKUP | A / B / C | `c249c774441d…` |
| `state-icc-designation-chain` | P1 (State Dept, four releases) | HASHED-PENDING-BACKUP | A / B / D | `ef3797f44ede…` |
| `state-icc-institution-designation` | P1 (State Dept press statement + fact sheet + index) | HASHED-PENDING-BACKUP | A / B | `666096c38ba4…` |
| `state-palestinian-ngo-designations` | P1 (State Dept) | HASHED-PENDING-BACKUP | D | `a67076facef1…` |
| `un-and-states-reaction` | P1-reported (UN News) + S1 | HASHED-PENDING-BACKUP | C / D | `2b0cb4471f49…` |
| `us-court-rulings-eo14203` | S1 (party-interest flagged; opinions P1 owed) | HASHED-PENDING-BACKUP | D / F | `d7a4dd232065…` |

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
# from cases/rubio-icc-dismantlement/evidence/
python3 build-custody-index.py
for d in */; do (cd "$d" && sha256sum -c sha256.txt); done
```

