#!/usr/bin/env python3
"""Regenerate custody-index.md and custody-index.json from evidence/*/capture.json.
Single source of truth for custody state + grade. Run from cases/doge-usaid-pepfar/evidence/."""
import json, glob
rows=[json.load(open(cj)) for cj in sorted(glob.glob("*/capture.json"))]
loc=sum(1 for r in rows if r.get("custody_state")=="LOCATOR-VERIFIED")
ver=sum(1 for r in rows if r.get("custody_state")=="VERIFIED")
idx={"generated":"2026-06-24","generator":"evidence/build-custody-index.py",
     "item_count":len(rows),"custody_states":{"VERIFIED":ver,"LOCATOR-VERIFIED":loc},
     "items":[{k:r.get(k) for k in ("item_id","grade","custody_state","track","source_url","sha256_transcript")} for r in rows]}
json.dump(idx,open("custody-index.json","w"),indent=2)
L=["# CANONICAL CUSTODY INDEX","",
   "*The single source of truth for the custody state and grade of every evidence item.*",
   "*Mechanically derived from `evidence/*/capture.json` by `build-custody-index.py` — do not hand-edit; regenerate.*","",
   "> **This index governs.** Where any other file (charge theory, evidence matrix, source",
   "> bundle, custody manifest) shows a custody state that conflicts with this table, **this",
   "> table is authoritative.** Per-row custody marks elsewhere are indicative/historical.","",
   f"**Generated:** 2026-06-24 · **Items:** {len(rows)} · **VERIFIED:** {ver} · **LOCATOR-VERIFIED:** {loc}","",
   "| Item | Grade | Custody | Track | sha256(transcript) |","|---|---|---|---|---|"]
for r in rows:
    h=(r.get("sha256_transcript") or "")[:12]
    L.append(f"| `{r['item_id']}` | {r.get('grade','')} | {r.get('custody_state','')} | {r.get('track') or '—'} | `{h}…` |")
L+=["","## Custody states","",
    "- **LOCATOR-VERIFIED** — canonical URL + verbatim text preserved as a hashed transcript; original-form bytes not yet held.",
    "- **VERIFIED** — original artifact (WARC/PDF/screenshot + headers) with metadata, hash, dual custody, off-platform backup. **0 items** (blocked by this environment's egress policy).","",
    "## Grade legend","",
    "P1 primary artifact · P2 named on-record statement · S1 reputable secondary · S2 expert/modeling · A1 analyst inference · T1 witness testimony.",
    "**`+ embedded P1` / `reported P1`** = held artifact is an outlet reproduction (S1); the underlying primary is pending capture — graded S1 to avoid inflation.","",
    "## Regenerate","","```bash","# from cases/doge-usaid-pepfar/evidence/",
    "python3 build-custody-index.py","for d in */; do (cd \"$d\" && sha256sum -c sha256.txt); done","```",""]
open("custody-index.md","w").write("\n".join(L)+"\n")
print(f"regenerated: {len(rows)} items, {loc} LOCATOR-VERIFIED, {ver} VERIFIED")
