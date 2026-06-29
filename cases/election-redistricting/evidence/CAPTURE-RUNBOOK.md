# CAPTURE RUNBOOK — Redistricting / Performed-Ignorance case

*How to perform original-form preservation of this case's evidence. Companion to the packet
`README.md` and `../05-custody-manifest.md`. Patterned on the shared
`../../doge-usaid-pepfar/evidence/CAPTURE-RUNBOOK.md`.*

---

## Status note (this packet's as-built state)

This packet was built **without a confirmed open-egress capture run**, so every item is filed
`LOCATOR-VERIFIED`: canonical URL + verbatim text preserved as a hashed `transcript.md`, original-form
bytes not yet held. This is the **DOGE/Rubio** as-built state, not the x-bot-swarm/Epstein VERIFIED
state. The spine, however, is unusually strong for this repo — **P1 public-record SCOTUS opinions** and
a **published leaked corpus** — so promotion is expected to be clean once a capture run is performed.

## Custody states

| State | Meaning |
|---|---|
| `LOCATOR-VERIFIED` | Canonical URL + verbatim text preserved as a hashed `transcript.md`; original-form bytes not yet held. |
| `VERIFIED` | Original artifact (WARC/PDF/screenshot) hashed into `<id>/original/manifest.json`. Full VERIFIED also requires a second custodian + off-platform backup. |

## Run it (from an open-egress environment)

```bash
cd cases/election-redistricting/evidence
# pull each source_url to WARC + PDF + PNG, hash into <id>/original/manifest.json,
# optionally submit to web.archive.org, then flip captured items to VERIFIED:
../../doge-usaid-pepfar/evidence/capture.sh --promote --archive-org   # shared script; or copy in a local capture.sh
python3 build-custody-index.py
for d in */; do (cd "$d" && sha256sum -c sha256.txt); done
```

The shared `capture.sh` auto-detects Chromium (including Playwright's bundled build at
`$PLAYWRIGHT_BROWSERS_PATH/chromium-*/chrome-linux/chrome`). Per the repo `.gitignore`, only the small
integrity records (`manifest.json`, `sha256sums.txt`, `archive-org-snapshots.txt`) are committed.

## Priority capture order

1. `hofeller-files` — the computed-in-private / disavowed-in-public anchor (the agnotology smoking gun).
2. `rucho` + `rucho-record` — the admitted target meeting the non-justiciability holding (the conjunction).
3. `callais` — the 2026 §2 evisceration (most recent measurement removal).
4. `tx-ca-2025` — the live race/party discriminator (keeps the case from being one-sided).

## Allowlist for this case

For **Custom** network access (Claude Code web) — covers every source cited across this packet.
`*.` is a wildcard subdomain match.

```
supremecourt.gov
*.supremecourt.gov
law.cornell.edu
*.law.cornell.edu
supreme.justia.com
*.justia.com
oyez.org
*.oyez.org
scotusblog.com
*.scotusblog.com
commoncause.org
*.commoncause.org
npr.org
*.npr.org
en.wikipedia.org
cbsnews.com
*.cbsnews.com
calmatters.org
ballotpedia.org
brennancenter.org
*.brennancenter.org
naacpldf.org
*.naacpldf.org
web.archive.org
```

> **Custom vs Full is a real security decision.** Prefer `Custom` limited to exactly these sources for
> a morally-hot case. The legal anchors are public government/court hosts, so capture is low-risk.

## Honest-custody note

Court slip opinions are stable PDFs and should capture cleanly. The **decisive upgrade is not on this
list**: it is the **map-drawing working files and the partisan/racial datasets** behind specific
enacted maps — the optimizer inputs that prove the effect was computed. Those are ordinarily withheld;
their preservation/disclosure is the **step-one demand** this packet asserts, recorded here so the gap
is explicit rather than papered over.
