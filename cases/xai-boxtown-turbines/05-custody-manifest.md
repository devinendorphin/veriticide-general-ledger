# 05 — CUSTODY MANIFEST

*Honest custody status. This case is **below VERIFIED**: its sources are **URL-CITED**, not yet
captured in original form and hashed. This file states what exists, what does not, and what capture
would be required to promote it — matching the discipline of the redistricting packet's custody index,
without pretending to a custody it has not performed.*

## Current custody status: **URL-CITED (pre-original-form)**

| Item | What is held now | What is NOT held | To reach VERIFIED |
|---|---|---|---|
| `permit` (SCHD air permit, 2025-07-02) | URL + press confirmation | the permit PDF itself, byte-preserved | download PDF → `sha256` → manifest |
| `selc-appeal` (2025-07-16 filing) | URL + press confirmation | the filed appeal document | capture filing PDF → hash |
| `turbine-survey` (aerial imagery) | description via SELC/press | the original image files + capture metadata/date | obtain original imagery + provenance → hash |
| `nonattainment` (EPA designation) | secondary citation | the EPA designation record | capture from epa.gov → hash |
| `ej-burden` / "4× risk" | press citation of agency/advocacy data | the underlying air-toxics dataset + derivation | pull EPA air-toxics data → re-derive → record method |
| press items (P2) | live URLs | archived snapshots | archive (e.g., timestamped capture) → hash |

## Why this is filed honestly as below VERIFIED

- The **`.gitignore` + capture-runbook** pattern used in `cases/election-redistricting/evidence/` is the
  model; this case has **not** run it. No `evidence/` originals are committed.
- Per project custody discipline, a case on a **public-record spine** (permit + court filing + EPA
  data) **can** reach VERIFIED once originals are captured and hashed — the materials are public and
  durable. It simply **has not been done yet** in this session.
- Two facts remain **PARTIAL regardless of capture**: the **exact turbine count** (contested between
  parties) and the **"4× cancer risk" multiple** (requires independent re-derivation from EPA
  air-toxics data, not just capture of a secondary source).

## Capture runbook (next step, not done here)

1. Create `cases/xai-boxtown-turbines/evidence/{permit,selc-appeal,turbine-survey,epa-nonattainment,ej-data}/`.
2. Download each P1 original (permit PDF, appeal PDF, EPA records); archive each P2 article.
3. Write `sha256.txt` per item; build a `custody-index.json` (mirror the redistricting `build-custody-index.py`).
4. Re-derive the air-toxics risk figure independently; record the method, or leave it PARTIAL.
5. Only then promote the matrix rows from URL-CITED to VERIFIED.

*Custody manifest v1, 2026-06-30. Status: URL-CITED. The case asserts step one on a public-record spine
that is capturable to VERIFIED; it does not claim a custody it has not performed.*
