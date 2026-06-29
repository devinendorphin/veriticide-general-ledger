# CANONICAL CUSTODY INDEX

*The single source of truth for the custody state and grade of every evidence item.*
*Mechanically derived from `evidence/*/capture.json` by `build-custody-index.py` — do not hand-edit; regenerate.*

> **This index governs.** Where any other file (charge theory, evidence matrix, source
> bundle, custody manifest) shows a custody state that conflicts with this table, **this
> table is authoritative.** Per-row custody marks elsewhere are indicative/historical.

**Generated:** 2026-06-29 · **Items:** 7 · **VERIFIED:** 7 · **LOCATOR-VERIFIED:** 0

| Item | Grade | Custody | Track | sha256(transcript) |
|---|---|---|---|---|
| `bot-count-deal-leverage-2022` | S1 (reputable secondary) | VERIFIED | legibility / the concern-is-fungible tell | `36cd862e5f62…` |
| `cyabra-gzero-coordinated-clusters-2024` | S1 (reputable secondary) + embedded S2 (Cyabra analysis) | VERIFIED | II(2)(d) / legibility — the swarm-substitution instance | `ae46d28b7dae…` |
| `incentive-redesign-blue-revenue-sharing` | S1/S2 (reputable secondary + analysis) | VERIFIED | II(3)(a) instrument — habitat economic substrate | `b04be7cfb49a…` |
| `musk-bot-purge-verdict-2024` | P2 (named on-record statements) + S1 | VERIFIED | II(2)(d) — the bare-verdict half of the act (crackdown declared) | `29be06cd7183…` |
| `musk-defeat-spam-bots-2022` | P2 (named on-record statement) + S1 | VERIFIED | II(2)(c) — the purge-claim origin (care-register frame) | `ff0386397441…` |
| `post-takeover-bot-persistence` | S1/S2 (reputable secondary + academic) | VERIFIED | legibility — no observable cessation | `2c9bbc50a57c…` |
| `research-api-foreclosure-2023` | S1 (reputable secondary) + embedded P1 (OSoMe/Botometer makers) | VERIFIED | II(2)(d) — measurement foreclosure | `ce79470f050b…` |

## Custody states

- **LOCATOR-VERIFIED** — canonical URL + verbatim text preserved as a hashed transcript; original-form bytes not yet held.
- **VERIFIED** — original artifact (WARC + PDF + screenshot) hashed into `<id>/original/manifest.json`. Full VERIFIED also assumes a second custodian + off-platform backup (see `../05-custody-manifest.md`).

## Grade legend

P1 primary artifact · P2 named on-record statement · S1 reputable secondary · S2 expert/modeling · A1 analyst inference · T1 witness testimony.
**`+ embedded P1` / `reported P1`** = held artifact is an outlet reproduction (S1); the underlying primary is pending capture — graded S1 to avoid inflation.

## Regenerate

```bash
# from cases/x-bot-swarm/evidence/
python3 build-custody-index.py
for d in */; do (cd "$d" && sha256sum -c sha256.txt); done
```

