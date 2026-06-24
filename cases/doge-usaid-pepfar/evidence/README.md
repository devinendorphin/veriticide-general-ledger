# /evidence — Capture & Custody Store

*Track F of the case packet. Each subdirectory preserves one source artifact with capture
metadata and an integrity hash. This file defines the custody states actually achievable in
this environment and records, honestly, the constraint that bounds them.*

---

## The egress constraint (recorded as part of the chain)

This capture pass was performed inside the project's remote execution environment. That
environment's **network policy denies general outbound web egress**: direct `curl` to
`archive.org` and `WebFetch` to news/source hosts both returned **403 (policy denial)** from
the egress proxy (logged in the proxy's `recentRelayFailures`). Per the proxy operating rules,
policy denials are **reported, not routed around**.

The **one sanctioned external channel that functions is web search.** It returns canonical
source URLs and verbatim text snippets, but it returns *model-/engine-extracted content*, not
the raw bytes of the source. Therefore this pass can achieve **content/locator verification**
but **not** full forensic original-form preservation (WARC, raw HTML, screenshot, server
headers). That step must be completed from an environment with permitted egress. This is the
same constraint the master ledger flagged ("direct document fetches blocked by the remote
environment network policy"); it travels with the packet rather than being papered over.

## Custody states

| State | Meaning | Achievable here? |
|---|---|---|
| `LOCATOR-VERIFIED` | Canonical source URL confirmed, and key verbatim text confirmed via sanctioned web search. Stored as a transcript with an integrity hash. Original-form preservation pending. | **Yes — this pass.** |
| `VERIFIED` | Original artifact preserved (PDF / screenshot / WARC / raw HTML) with capture metadata, hash, dual custody, off-platform backup. | No — requires permitted egress. |

**Every item in this store is currently `LOCATOR-VERIFIED`.** None is `VERIFIED`. That
distinction is the honest state of the chain and is recorded in each item's `capture.json`.

## What `LOCATOR-VERIFIED` is worth

It is a real advance over the packet's prior state and not a substitute for custody:

- It **pins the canonical primary source** (exact URL, outlet, date) so a custodian with
  egress can go straight to original-form capture.
- It **confirms the verbatim text** the case quotes, removing the risk that a quote was
  mis-remembered or mis-attributed.
- It **distinguishes** quoted verbatim snippets from search-engine synthesis (marked in each
  transcript).

It does **not** prove the artifact is unaltered at source, preserve it against takedown, or
supply server-side provenance. Do not cite a `LOCATOR-VERIFIED` item as though it were
forensically preserved.

## Layout per item

```
<item-id>/
  transcript.md     # canonical locator + verbatim text (quoted) + corroborating sources
  capture.json      # capture metadata + sha256 of transcript.md + custody state
  sha256.txt        # sha256(transcript.md), computed at capture
```

## Index

| Item | Track(s) | State |
|---|---|---|
| `musk-woodchipper-posts` | B (authorization), II(3)(d) (mental element) | LOCATOR-VERIFIED |
| `doge-savings-subset` | A (instrument) | LOCATOR-VERIFIED |
| `tamlyn-cable` | C (foreseeability, inside-chain) | LOCATOR-VERIFIED |
| `propublica-internal-memos` | C (foreseeability, executing tier) | LOCATOR-VERIFIED |
| `rubio-hfac-testimony` | D (dismissal) | LOCATOR-VERIFIED |
| `meeks-demands` | D (terminal-node / non-response) | LOCATOR-VERIFIED |
| `hfac-letter-jan24` | C (foreseeability — warning on day of freeze; direct PDF locator) | LOCATOR-VERIFIED |
| `schatz-record` | C (foreseeability / realized mortality in congressional record) | LOCATOR-VERIFIED |
| `gawande-democracynow` | C (realized mortality, former USAID global-health head) | LOCATOR-VERIFIED |
| `named-deaths` | C / IV(4) (realized individual harm — consolidated) | LOCATOR-VERIFIED |

**10 items, all integrity-verified.** Second capture pass (2026-06-24) added the four items
below `meeks-demands`. The `named-deaths` artifact consolidates the realized-harm spine
(Babagana, Suza Kenyaba, Evan Anzoo, Pe Kha Lau, Peter, Peter Lokoyen, the Liberian mother and
unborn son, ≥54 Turkana children) and corrects the "mostly children" demographic to
*people without exit dependent on a withdrawn system, heavily pediatric.* The pass also
surfaced the **Rubio-waivers** defense and its rebuttal (now Defense 6 in
`../03-adversarial-check.md`) and a **date discrepancy** on the congressional letter (ledger
"Feb 10" vs. located "Jan 24") flagged in `hfac-letter-jan24/transcript.md` for reconciliation.

## Verifying integrity

From this directory: `sha256sum -c */sha256.txt` (run after re-deriving paths) or compare
each `sha256.txt` against `sha256sum <item>/transcript.md`. Any mismatch is a change and must
be logged, per the custody manifest's integrity rules.

## Next custody action (for an operator with egress)

In priority order: capture `musk-woodchipper-posts` (X post + archive.org snapshot),
`tamlyn-cable` and `propublica-internal-memos` (article pages + embedded documents), then
`doge-savings-subset` (multi-date snapshots to preserve the deletion behavior), then the
congressional records. Promote each from `LOCATOR-VERIFIED` to `VERIFIED` and update its
`capture.json`.
