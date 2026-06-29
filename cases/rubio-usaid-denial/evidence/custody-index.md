# CANONICAL CUSTODY INDEX

*The single source of truth for the custody state and grade of every evidence item.*
*Mechanically derived from `evidence/*/capture.json` by `build-custody-index.py` — do not hand-edit; regenerate.*

> **This index governs.** Where any other file (charge theory, evidence matrix, source
> bundle, custody manifest) shows a custody state that conflicts with this table, **this
> table is authoritative.** Per-row custody marks elsewhere are indicative/historical.

**Generated:** 2026-06-24 · **Items:** 2 · **VERIFIED:** 0 · **LOCATOR-VERIFIED:** 2

| Item | Grade | Custody | Track | sha256(transcript) |
|---|---|---|---|---|
| `rubio-acting-administrator` | P1 (State Dept official) + S1 | LOCATOR-VERIFIED | B / II(3)(d) | `43347d81d0f5…` |
| `wapo-factchecker-four-pinocchios` | S1 (independent fact-check) | LOCATOR-VERIFIED | D / II(2)(d) | `93cc853e9ad2…` |

## Custody states

- **LOCATOR-VERIFIED** — canonical URL + verbatim text preserved as a hashed transcript; original-form bytes not yet held.
- **VERIFIED** — original artifact (WARC/PDF/screenshot + headers) with metadata, hash, dual custody, off-platform backup. **0 items** (blocked by this environment's egress policy).

## Grade legend

P1 primary artifact · P2 named on-record statement · S1 reputable secondary · S2 expert/modeling · A1 analyst inference · T1 witness testimony.
**`+ embedded P1` / `reported P1`** = held artifact is an outlet reproduction (S1); the underlying primary is pending capture — graded S1 to avoid inflation.

## Regenerate

```bash
# from cases/doge-usaid-pepfar/evidence/
python3 build-custody-index.py
for d in */; do (cd "$d" && sha256sum -c sha256.txt); done
```

