# CANONICAL CUSTODY INDEX

*The single source of truth for the custody state and grade of every evidence item.*
*Mechanically derived from `evidence/*/capture.json` by `build-custody-index.py` — do not hand-edit; regenerate.*

> **This index governs.** Where any other file (charge theory, evidence matrix, source
> bundle, custody manifest) shows a custody state that conflicts with this table, **this
> table is authoritative.** Per-row custody marks elsewhere are indicative/historical.

**Generated:** 2026-07-02 · **Items:** 8 · **States:** HASHED-PENDING-BACKUP 1, VERIFIED 7

| Item | Grade | Custody | Track | sha256(transcript) |
|---|---|---|---|---|
| `bot-count-deal-leverage-2022` | S1 (reputable secondary) | VERIFIED | legibility / the concern-is-fungible tell | `e8d328b69af1…` |
| `cyabra-gzero-coordinated-clusters-2024` | S1 (reputable secondary) + embedded S2 (Cyabra analysis) | VERIFIED | II(2)(d) / legibility — the swarm-substitution instance | `56fa404ce55b…` |
| `incentive-redesign-blue-revenue-sharing` | S1/S2 (reputable secondary + analysis) | VERIFIED | II(3)(a) instrument — habitat economic substrate | `b04be7cfb49a…` |
| `musk-bot-purge-verdict-2024` | P2 (named on-record statements) + S1 | VERIFIED | II(2)(d) — the bare-verdict half of the act (crackdown declared) | `a972e0926e08…` |
| `musk-defeat-spam-bots-2022` | P2 (named on-record statement) + S1 | VERIFIED | II(2)(c) — the purge-claim origin (care-register frame) | `ff0386397441…` |
| `paid-lift-operations` | P1 (DOJ/court + Treasury) + S1 (Guardian/Forbidden Stories) | VERIFIED | II(3)(c) legibility + II(3)(a) habitat — the paid-lift node (NOT Musk-attributed) | `56de605d3349…` |
| `post-takeover-bot-persistence` | S1/S2 (reputable secondary + academic) | HASHED-PENDING-BACKUP | legibility — no observable cessation | `2c9bbc50a57c…` |
| `research-api-foreclosure-2023` | S1 (reputable secondary) + embedded P1 (OSoMe/Botometer makers) | VERIFIED | II(2)(d) — measurement foreclosure | `ce79470f050b…` |

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
# from cases/x-bot-swarm/evidence/
python3 build-custody-index.py
for d in */; do (cd "$d" && sha256sum -c sha256.txt); done
```

