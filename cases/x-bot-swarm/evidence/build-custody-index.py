#!/usr/bin/env python3
"""Regenerate custody-index.md and custody-index.json from evidence/*/capture.json.
Single source of truth for custody state + grade. Run from cases/x-bot-swarm/evidence/.
Custody states are tallied generically (collections.Counter); see the emitted legend."""
import json, glob, datetime, collections
GEN=datetime.date.today().isoformat()
rows=[json.load(open(cj)) for cj in sorted(glob.glob("*/capture.json"))]
states=collections.Counter(r.get("custody_state","?") for r in rows)
idx={"generated":GEN,"generator":"evidence/build-custody-index.py",
     "item_count":len(rows),"custody_states":dict(states),
     "items":[{k:r.get(k) for k in ("item_id","grade","custody_state","track","source_url","sha256_transcript")} for r in rows]}
json.dump(idx,open("custody-index.json","w"),indent=2)
summary=", ".join(f"{k} {v}" for k,v in sorted(states.items()))
L=["# CANONICAL CUSTODY INDEX","",
   "*The single source of truth for the custody state and grade of every evidence item.*",
   "*Mechanically derived from `evidence/*/capture.json` by `build-custody-index.py` — do not hand-edit; regenerate.*","",
   "> **This index governs.** Where any other file (charge theory, evidence matrix, source",
   "> bundle, custody manifest) shows a custody state that conflicts with this table, **this",
   "> table is authoritative.** Per-row custody marks elsewhere are indicative/historical.","",
   f"**Generated:** {GEN} · **Items:** {len(rows)} · **States:** {summary}","",
   "| Item | Grade | Custody | Track | sha256(transcript) |","|---|---|---|---|---|"]
for r in rows:
    h=(r.get("sha256_transcript") or "")[:12]
    L.append(f"| `{r['item_id']}` | {r.get('grade','')} | {r.get('custody_state','')} | {r.get('track') or '—'} | `{h}…` |")
L+=["","## Custody states","",
    "- **LOCATOR-VERIFIED** — canonical URL + verbatim text preserved as a hashed transcript; original-form bytes not held.",
    "- **HASHED-PENDING-BACKUP** — original-form artifacts (WARC/PDF/PNG) were captured and hashed into `<id>/original/manifest.json`, so the in-repo integrity record exists, **but no off-platform second custodian / backup is yet in place**, and captures made before this repo moved to an open-egress environment may include interstitial or error-page bytes for source hosts that were blocked at capture time (compare artifact sizes in the manifest). Not tribunal-grade.",
    "- **VERIFIED** — original-form artifact hashed **and** independently backed up off-platform (a second custodian, e.g. the `the veriticide suite` Drive/GCP store) **and** confirmed to hold the real source content rather than an interstitial. This is the only tribunal-grade state.","",
    "*Reconciliation note (2026-07-02): items previously marked VERIFIED were reset to HASHED-PENDING-BACKUP because the off-platform backup that VERIFIED requires was never completed. See `docs/custody-status-2026-07-02.md`.*","",
    "## Grade legend","",
    "P1 primary artifact · P2 named on-record statement · S1 reputable secondary · S2 expert/modeling · A1 analyst inference · T1 witness testimony.",
    "**`+ embedded P1` / `reported P1`** = held artifact is an outlet reproduction (S1); the underlying primary is pending capture — graded S1 to avoid inflation.","",
    "## Regenerate","","```bash","# from cases/x-bot-swarm/evidence/",
    "python3 build-custody-index.py","for d in */; do (cd \"$d\" && sha256sum -c sha256.txt); done","```",""]
open("custody-index.md","w").write("\n".join(L)+"\n")
print(f"regenerated: {len(rows)} items, states={dict(states)}")
