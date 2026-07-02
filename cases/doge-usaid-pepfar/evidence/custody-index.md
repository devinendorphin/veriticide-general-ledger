# CANONICAL CUSTODY INDEX

*The single source of truth for the custody state and grade of every evidence item.*
*Mechanically derived from `evidence/*/capture.json` by `build-custody-index.py` — do not hand-edit; regenerate.*

> **This index governs.** Where any other file (charge theory, evidence matrix, source
> bundle, custody manifest) shows a custody state that conflicts with this table, **this
> table is authoritative.** Per-row custody marks elsewhere are indicative/historical.

**Generated:** 2026-07-02 · **Items:** 15 · **States:** HASHED-PENDING-BACKUP 13, LOCATOR-VERIFIED 2

| Item | Grade | Custody | Track | sha256(transcript) |
|---|---|---|---|---|
| `doge-savings-subset` | P1 | HASHED-PENDING-BACKUP | A | `1350f92b26d8…` |
| `gawande-democracynow` | P2 (named expert, former USAID global health head) via S1 | HASHED-PENDING-BACKUP | C / IV(4) | `667c45a25c2c…` |
| `hfac-letter-jan24` | P1 (direct PDF locator) | HASHED-PENDING-BACKUP | C | `1d7e7e564b45…` |
| `ig-firings-jan2025` | S1 (multiple reputable outlets) + reported P1 (Storch v. Hegseth ruling; USAID OIG report) — original ruling/report capture pending | HASHED-PENDING-BACKUP | D | `4ef72010cfe0…` |
| `meeks-demands` | P1 | HASHED-PENDING-BACKUP | D | `6492894c88c2…` |
| `musk-woodchipper-posts` | P1 | HASHED-PENDING-BACKUP | B / II(3)(d) | `d8cb4cdfca1b…` |
| `named-deaths` | S1/T1 (named individuals, multi-outlet) | HASHED-PENDING-BACKUP | C / IV(4) | `f9bdc495b352…` |
| `propublica-internal-memos` | S1 (ProPublica, reported) + embedded P1 (memos) — underlying memos pending | LOCATOR-VERIFIED | C / B | `f9565587fbc6…` |
| `rubio-hfac-testimony` | P2 | HASHED-PENDING-BACKUP | D | `e372a2dd69b4…` |
| `rubio-waivers-nonfunctional` | S1 (multi-outlet) + reported P1 (DOGE payment-veto account) | HASHED-PENDING-BACKUP | Defense-6 rebuttal / A / B / II(2)(c) | `c0c99fcadfcb…` |
| `schatz-record` | P1/P2 (congressional record) | HASHED-PENDING-BACKUP | C | `d81983349ea7…` |
| `secondary-accountability-removal` | S1 + legal (mirror) | HASHED-PENDING-BACKUP | D / B | `b83507940c50…` |
| `secondary-doge-savings-witnesses` | S1/S2 (multi-outlet mirror) | HASHED-PENDING-BACKUP | A | `77a634a17887…` |
| `secondary-mortality-modeling` | S2 (modeling/expert mirror) | HASHED-PENDING-BACKUP | C / IV(4) | `6caba69a75f3…` |
| `tamlyn-cable` | S1 (WaPo, reported) + embedded P1 (cable) — original cable pending | LOCATOR-VERIFIED | C | `3a5efa7c6872…` |

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
# from cases/doge-usaid-pepfar/evidence/
python3 build-custody-index.py
for d in */; do (cd "$d" && sha256sum -c sha256.txt); done
```

