#!/usr/bin/env python3
"""Regenerate custody-index.{md,json} from evidence/*/capture.json.
Run from cases/yacinemtb-corpus/evidence/. This corpus is SCREENSHOT-HELD (no canonical
URLs / original-form bytes), so it cannot reach VERIFIED; the builder tallies states generically."""
import json, glob, datetime, collections
GEN=datetime.date.today().isoformat()
rows=[json.load(open(cj)) for cj in sorted(glob.glob("*/capture.json"))]
states=collections.Counter(r.get("custody_state","?") for r in rows)
idx={"generated":GEN,"generator":"evidence/build-custody-index.py",
     "item_count":len(rows),"account_level_verdict":"DECLINED (high-variance account)",
     "custody_states":dict(states),
     "items":[{k:r.get(k) for k in ("item_id","classification","register","reach","custody_state","screenshot","sha256_transcript")} for r in rows]}
json.dump(idx,open("custody-index.json","w"),indent=2)
L=["# CANONICAL CUSTODY INDEX — @yacineMTB corpus packet","",
   "*Mechanically derived from `evidence/*/capture.json` by `build-custody-index.py` — regenerate, do not hand-edit.*","",
   "> **This index governs** custody state. **ACCOUNT-LEVEL VERDICT: DECLINED** (high-variance account).",
   "> This packet records *acts* (specimens), not the account. See `../00-charge-theory.md`.","",
   f"**Generated:** {GEN} · **Items:** {len(rows)} · **States:** "+", ".join(f"{k} {v}" for k,v in states.items()),"",
   "| Item | Class | Register | Reach | Custody | sha256(transcript) |","|---|---|---|---|---|---|"]
for r in rows:
    h=(r.get("sha256_transcript") or "")[:12]
    L.append(f"| `{r['item_id']}` | {r.get('classification','')} | {r.get('register','')} | {r.get('reach','')} | {r.get('custody_state','')} | `{h}…` |")
L+=["","## Custody states","",
    "- **SCREENSHOT-HELD** — verbatim text preserved as a hashed transcript from an operator-supplied screenshot; **no canonical URL and no original-form web bytes**. This corpus cannot reach VERIFIED without locating canonical tweet URLs (deliberately not pursued — private individual; corpus deprioritized/not load-bearing in the ledger).",
    "- **LOCATOR-VERIFIED / VERIFIED** — not applicable to this packet (no URLs captured).","",
    "## Not in this evidence store","",
    "Counter-evidence (5), the NULL/SINCERE-UNBOUNDED entries, the algorithm meta-post, and the",
    "`@glubose` companion counter-speech are tabulated in `../02-source-bundle.md`, not as separate",
    "evidence dirs — they are part of the same high-variance record and are preserved there.","",
    "## Regenerate","","```bash","# from cases/yacinemtb-corpus/evidence/",
    "python3 build-custody-index.py","for d in */; do (cd \"$d\" && sha256sum -c sha256.txt); done","```",""]
open("custody-index.md","w").write("\n".join(L)+"\n")
print(f"regenerated: {len(rows)} items, states={dict(states)}")
