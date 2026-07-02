# CANONICAL CUSTODY INDEX

*The single source of truth for the custody state and grade of every evidence item.*
*Mechanically derived from `evidence/*/capture.json` by `build-custody-index.py` — do not hand-edit; regenerate.*

> **This index governs.** Where any other file (charge theory, evidence matrix, source
> bundle, custody manifest) shows a custody state that conflicts with this table, **this
> table is authoritative.** Per-row custody marks elsewhere are indicative/historical.

**Generated:** 2026-07-02 · **Items:** 4 · **States:** HASHED-PENDING-BACKUP 4

| Item | Grade | Custody | Track | sha256(transcript) |
|---|---|---|---|---|
| `redaction-asymmetry` | S1 (CNN) on P1 conduct | HASHED-PENDING-BACKUP | Redaction Inversion — load-bearing (II(2)(d)) | `7c8bfa297d4f…` |
| `survivors-lawsuit` | S1 on P1 court filing | HASHED-PENDING-BACKUP | realized harm (Tier 3) + inversion (Move 3 / DARVO) | `b64436df7c11…` |
| `technical-error-framing` | S1 (PBS/CBC) on P2 govt characterization | HASHED-PENDING-BACKUP | Move 5 — euphemism | `b95936362e9c…` |
| `victim-info-exposed` | S1 (multiple outlets) on P1 (DOJ releases) | HASHED-PENDING-BACKUP | II(2)(d) — predicate exposure | `3469d38cc44b…` |

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
# from cases/epstein-survivor-unredaction/evidence/
python3 build-custody-index.py
for d in */; do (cd "$d" && sha256sum -c sha256.txt); done
```

