# CANONICAL CUSTODY INDEX

*The single source of truth for the custody state and grade of every evidence item.*
*Mechanically derived from `evidence/*/capture.json` by `build-custody-index.py` — do not hand-edit; regenerate.*

> **This index governs.** Where any other file (charge theory, evidence matrix, source
> bundle, custody manifest) shows a custody state that conflicts with this table, **this
> table is authoritative.** Per-row custody marks elsewhere are indicative/historical.

**Generated:** 2026-07-02 · **Items:** 9 · **States:** HASHED-PENDING-BACKUP 9

| Item | Grade | Custody | Track | sha256(transcript) |
|---|---|---|---|---|
| `alexander` | P1 (Supreme Court opinion) | HASHED-PENDING-BACKUP | II(2)(d) — good-faith presumption + disentanglement burden | `acb0605b8b2d…` |
| `callais` | P1 (Supreme Court opinion) | HASHED-PENDING-BACKUP | II(2)(d) — §2 racial-vote-dilution enforcement narrowed/eviscerated | `a663661b1966…` |
| `hofeller-files` | S1 on P1 (the files) | HASHED-PENDING-BACKUP | II(3)(d) — effect computed in private / disavowed (operator intent) | `0f30d236dcae…` |
| `mapmaking-instrument` | S1 + P1 (Hofeller files exemplify the method) | HASHED-PENDING-BACKUP | II(3)(a) — the instrument that computes the effect at scale | `937e281ebfd9…` |
| `milligan-control` | P1 (Supreme Court opinion) | HASHED-PENDING-BACKUP | CONTROL — dilution recognized and remedied (direction opposite) | `d0ba67d10e17…` |
| `rucho-record` | P2 (named on-record statement) in P1 (legislative record) | HASHED-PENDING-BACKUP | II(3)(d) — admitted precise intended effect (operator) | `39b90e583b23…` |
| `rucho` | P1 (Supreme Court opinion) | HASHED-PENDING-BACKUP | II(2)(d) — partisan effect rendered non-justiciable | `dc568c49eea2…` |
| `shelby` | P1 (Supreme Court opinion) | HASHED-PENDING-BACKUP | II(2)(d) — measurement apparatus (preclearance) dismantled | `567efc80b3fc…` |
| `tx-ca-2025` | S1 on P1 (rulings / ballot measure) | HASHED-PENDING-BACKUP | Tier 3 realized harm + the race/party discriminator | `b264b5db36f5…` |

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
# from cases/election-redistricting/evidence/
python3 build-custody-index.py
for d in */; do (cd "$d" && sha256sum -c sha256.txt); done
```

