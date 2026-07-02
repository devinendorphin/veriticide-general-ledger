# CAPTURE RUNBOOK — xAI / Boxtown turbines case

*How this case's evidence was preserved, and how to complete it. Companion to `../05-custody-manifest.md`.
Patterned on `../../election-redistricting/evidence/CAPTURE-RUNBOOK.md`.*

## As-built state (2026-06-30, open-egress session)

A tailored, **document-only WARC** run preserved each item's canonical source (WARC + HTML body) via
`wget` through the sanctioned agent proxy, hashed into `<id>/original/manifest.json`, and promoted the
items to **VERIFIED** in their `capture.json`. Result: **6 VERIFIED · 0 LOCATOR-VERIFIED**
(`custody-index.md` governs).

Deviations from the shared `capture.sh`, recorded honestly:
- **`--page-requisites --span-hosts` dropped.** The shared script pulls every page asset across hosts;
  on media-heavy news pages this hung. The custody target is the **document**, not its ad/CDN graph, so
  a lean document-only WARC was used.
- **PDF/PNG omitted.** Headless Chromium behind the TLS-intercepting proxy would capture cert-error
  pages; recording a broken render as the source corrupts custody. WARC (system-CA-trusted) is held.
- **3 sources blocked `wget`** (Inside Climate News, TIME, Tennessee Lookout → empty). Their empty
  captures were **purged** (not hashed as artifacts). `unpermitted-operation` was re-pointed to a
  capturable SELC primary; the blocked URLs remain secondary locators in the transcripts.

## Two conditions still open for FULL VERIFIED

1. **Off-platform second custodian.** The binaries (`*.html`, `*.warc`) are git-ignored — only the
   hashes are committed. Copy `*/original/*` off-platform and/or run archive.org Save Page Now.
2. **P1 PDFs.** Capture the **SCHD permit PDF** and the **SELC appeal filing PDF** directly (currently
   held via secondary coverage) and hash them in.

## Run / re-run (from an open-egress environment)

```bash
cd cases/xai-boxtown-turbines/evidence
./capture.sh --promote --archive-org      # shared script (full WARC+PDF+PNG; needs chromium on PATH)
python3 build-custody-index.py
for d in */; do (cd "$d" && sha256sum -c sha256.txt); done
```

The lean run actually used here is reproducible without chromium: document-only `wget --warc-file`
per `source_url` (+ any `Also:` URL in the transcript), purge any `*.html` ≤ 500 B and its `*.warc`,
re-hash, then `build-custody-index.py`.

## Allowlist for this case (Custom network access)

```
selc.org
*.selc.org
cnbc.com
*.cnbc.com
cnn.com
*.cnn.com
nbcnews.com
*.nbcnews.com
time.com
insideclimatenews.org
tennesseelookout.com
memphischamber.com
datacenterdynamics.com
*.datacenterdynamics.com
epa.gov
*.epa.gov
web.archive.org
```

## Honest-custody note

The **decisive upgrade is not on this list**: it is the **SCHD permit record + the actual emissions/
stack-test data + independent ambient air monitoring** around Boxtown — the materials that would move
`item 5` (realized harm) from risk to measured, and that the case's **step-one demand** asks be
preserved, disclosed, and audited. Recorded here so the gap is explicit.
