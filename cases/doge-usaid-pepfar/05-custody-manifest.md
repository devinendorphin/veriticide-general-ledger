# 05 — CUSTODY MANIFEST

> **⚠ Custody reconciliation (2026-07-02).** Counts and per-item marks on this page predate the
> 2026-07-02 custody audit and are **historical narrative**. The authoritative, machine-derived
> state is `evidence/custody-index.md`; where this page and the index disagree, **the index
> governs.** Items formerly marked `VERIFIED` are now `HASHED-PENDING-BACKUP`: original-form
> artifacts were hashed into `original/manifest.json` in-repo, but the off-platform second
> custodian that `VERIFIED` requires is not yet in place, and some pre-open-egress captures may
> hold interstitial/error-page bytes. Remediation plan: `docs/custody-status-2026-07-02.md`.

*Convention Art. VI(6) and Documentation Protocol §6 (Track F). The least glamorous extract
and the one that most determines whether the record survives contact with people who want it
discredited. A record that cannot be shown to be unaltered can be dismissed no matter how true
it is.*

> **Honest headline:** this packet's content is strong and its **custody is its weakest
> track.** Most items are cited in the master ledger from named sources but are **not yet
> preserved off-platform** with hashes and capture timestamps. This manifest states that
> plainly and gives the remediation protocol. Custody is the work that converts a sourced
> argument into an evidentiary object.

---

## 1. Custody states (definitions)

| State | Meaning |
|---|---|
| `IN-LEDGER` | Cited in `ledger/ledger.md` with source attribution. Believable, but the live URL is the only copy — vulnerable to link rot, edit, or takedown. |
| `CAPTURE-REQUIRED` | Named primary source identified; artifact **not** preserved. The highest-value and least-protected items are here. |
| `LOCATOR-VERIFIED` | Canonical source URL confirmed and key verbatim text confirmed via the one sanctioned egress channel (web search); stored in `evidence/<id>/` as a transcript with an integrity hash. Original-form bytes not yet preserved. **The six priority items reached this state on 2026-06-24.** |
| `HASHED-PENDING-BACKUP` | Original-form artifact captured + hashed into `evidence/<id>/original/manifest.json` (in-repo integrity record), but **no off-platform second custodian / backup yet**; pre-open-egress captures may hold interstitial bytes. Not tribunal-grade. |
| `VERIFIED` | `HASHED-PENDING-BACKUP` **plus** an off-platform second custodian (e.g. the `the veriticide suite` Drive/GCP store) **and** confirmation the capture holds real content, not an interstitial. The only tribunal-grade state. |

**Capture log — 2026-06-24.** A capture pass moved the six priority items from
`CAPTURE-REQUIRED` to `LOCATOR-VERIFIED`. Artifacts and `capture.json`/`sha256.txt` are in
`evidence/`. The pass also surfaced material corroboration not previously in the ledger:
- **Tamlyn cable:** realized before/after mortality — ≥219 HIV-positive deaths in Lualaba
  province Jan–Jun 2025 vs. 164 the prior year (Congolese health officials, via WaPo); named
  casualty estimates (28,000 adults / 2,500 children); $50M commodities "still stranded."
- **ProPublica memos:** the article ties the dismantlement directly to **"Elon Musk's
  Department of Government Efficiency"** pressing ahead "by ignoring and impeding staff who
  tried to protect lifesaving operations"; specific tolls (1M children untreated for SAM;
  166,000 malaria deaths; 200,000 polio paralysis; TB +30%); Peter Marocco named.
- **Rubio denial:** Washington Post "Fact Checker" awarded the "no one has died" claim **four
  Pinocchios** — an independent on-record falsity finding.
- **Meeks demands:** the "88 children per hour" figure; Oct 31, 2025 written-response deadline.
- **Musk posts:** the wood-chipper phrase became the title of whistleblower **Nicholas Enrich's**
  memoir *Into the Wood Chipper*; Enrich also authored the internal warning memos — linking the
  deployer's own words to the warnings the dismantlement ignored.

## 2. The intended `/evidence/` layout

When custody work begins, each item gets a directory:

```
/evidence/<item-id>/
  original.<ext>        # the artifact in its original form (PDF, PNG, HTML, WARC, MP4)
  capture.json          # { item_id, source_url, capture_method, captured_by,
                        #   captured_at (ISO-8601 + tz), bears_date, sha256, grade,
                        #   custodians[], notes }
  sha256.txt            # hash of original.<ext>, computed at capture
  transcript.md         # verbatim transcription where the original is media/image
```

`capture.json` is the chain-of-custody record. The `sha256` is computed **at capture** and
never recomputed silently; any later recomputation that differs is logged as a change.

## 3. Capture protocol by artifact class

| Class | Method | Notes |
|---|---|---|
| **Live web page** (doge.gov/savings, outlet articles) | (a) full-page PDF + (b) full-page screenshot + (c) WARC via `wget --warc` or ArchiveBox where reachable + (d) submit to web.archive.org and record the snapshot URL | Capture **multiple dates** for doge.gov/savings to preserve the deletion-not-correction behavior — the diff between snapshots *is* the evidence. |
| **Social post** (`musk-woodchipper-posts`) | Screenshot of the post incl. timestamp + engagement counts; record the post ID/permalink; archive.org snapshot; note if later deleted | A deleted post preserved by snapshot is more probative, not less. Record deletion if it occurs. |
| **Internal cable / memo** (`tamlyn-cable`, `propublica-internal-memos`) | Preserve as reproduced/quoted by the reporting outlet; pursue FOIA / IG release for the primary document; preserve the reporting page as the interim custodian | Distinguish in `capture.json` between *the primary document* and *the outlet's reproduction of it*. Do not claim the primary if you hold only the reproduction. |
| **Congressional record** (`rubio-hfac-testimony`, `meeks-*`, `schatz-record`, `hfac-letter-feb10`) | Official committee video/transcript + the committee/member press release pages; congress.gov where applicable | Sworn/official records are high-grade; preserve the official source, not a secondary summary. |
| **Peer-reviewed modeling** (`unaids-2025`, `ucla-lancet`, PMC items, `medrxiv-feb27`) | PDF of the paper + DOI + the version/date (preprint vs. published) | Record the **date** prominently — foreseeability turns on it (`04-falsification-memo.md` §C). |

## 4. The manifest (every item, its custody state, its owner of next action)

### CAPTURE-REQUIRED — priority order (leverage-first)

| Item | Class | Why it is priority |
|---|---|---|
| `musk-woodchipper-posts` | Social post | Converts authorization from inference to admission. **#1.** |
| `tamlyn-cable` | Internal cable | Cleanest inside-the-chain foreseeability artifact. |
| `propublica-internal-memos` | Internal memo (via reporting) | Warning to the executing tier. |
| `doge-savings-subset` | Live web page (multi-date) | The instrument itself; the snapshot diff is the deletion evidence. |
| `rubio-hfac-testimony` | Congressional record | The denial against a closed record. |
| `meeks-jun2025`, `meeks-oct2025` | Congressional record | The non-response / terminal-node condition. |
| `hfac-letter-feb10`, `schatz-record`, `gawande-democracynow` | Congressional / media | Supporting foreseeability and realized mortality. |

### IN-LEDGER — to be mirrored to `/evidence/`

All S1/S2 items listed in `02-source-bundle.md` §B and §C (PBS, NYT, CBS, ABC, WaPo, AP,
CREW, NBC Washington, USAFacts, ProPublica, NPR, Cato, UNAIDS, Lancet/UCLA, CGD, Oxfam, WFP,
Riedl). These are well-sourced but single-copy at their live URLs. Mirror each to
`/evidence/` (PDF + screenshot + hash) so the corpus survives link rot or takedown.

## 5. Custodial integrity rules (non-negotiable)

1. **≥2 custodians.** The record is held by more than one person/organization so it cannot be
   lost or suppressed at a single point (Protocol §6; Art. V remedial-standing logic).
2. **Off-platform backup.** No copy of evidence documenting an institution is held *only* inside
   a system that institution controls.
3. **Log every change.** Corrections and additions are logged with what changed, when, by whom.
   A record with an honest edit history is more credible than one claiming to be untouched —
   the master ledger's own `docs/provenance.md` is the model.
4. **Separate the artifact from the analysis.** `/evidence/` holds artifacts and capture
   metadata only. Interpretation lives in this packet's other files, so a skeptic who distrusts
   the analysis still cannot dispute the artifacts.
5. **Capture date ≠ artifact date.** Both are recorded, separately, in `capture.json`. Conflating
   them is the error that lets an adversary impeach the whole record.

## 6. Network-policy caveat (recorded honestly)

The master ledger notes that several primary fetches were **blocked by the remote
environment's network policy**, and items were carried from web-search results pending
verification against the primary documents. Until those fetches are performed in an
environment that permits them — and the artifacts land in `/evidence/` as `VERIFIED` — the
affected items remain `CAPTURE-REQUIRED` and are **carried at their stated grade but flagged
as not-yet-preserved**. This caveat travels with the packet. The packet does not claim custody
it does not have; that honesty is itself part of the chain.

---

## Custody status summary (as of 2026-06-24)

> **Authoritative source:** `evidence/custody-index.md` (generated from `evidence/*/capture.json`
> by `build-custody-index.py`). The counts below are a narrative summary of that index; if they
> ever diverge, the index governs. This resolves the prior cross-file status drift.

- **HASHED-PENDING-BACKUP:** 13 items — original-form artifacts hashed into `original/manifest.json`; off-platform backup pending (see `docs/custody-status-2026-07-02.md`).
- **VERIFIED:** 0 items — none yet has the off-platform second custodian that `VERIFIED` requires.
- **LOCATOR-VERIFIED:** 14 items — in `evidence/` with canonical URLs, verbatim text, and
  integrity hashes. Pass 1 (priority six): `musk-woodchipper-posts`, `doge-savings-subset`,
  `tamlyn-cable`, `propublica-internal-memos`, `rubio-hfac-testimony`, `meeks-demands`. Pass 2:
  `hfac-letter-jan24`, `schatz-record`, `gawande-democracynow`, `named-deaths`. Pass 3 (mirror
  of the IN-LEDGER secondary corpus): `secondary-doge-savings-witnesses`,
  `secondary-mortality-modeling`, `secondary-accountability-removal`. Pass 5:
  `rubio-waivers-nonfunctional` (the strongest-defense rebuttal).
- **CAPTURE-REQUIRED (residual within mirrors):** per-outlet original-form (WARC/PDF) capture
  for the named-individual pages in `named-deaths` and the now-anchored `secondary-*` rows.
  Canonical-URL anchoring is **complete** (Pass 4, 2026-06-24) — every `ledger-ID` placeholder
  is resolved to a canonical URL; what remains is original-form preservation, not locating.
- **IN-LEDGER:** the secondary/expert corpus is now mirrored into `evidence/` (custody state
  LOCATOR-VERIFIED), pending original-form preservation.

**Reconciliation — RESOLVED (2026-06-24).** The ledger's "Feb 10, 2025" letter and the located
"Jan 24, 2025" letter are **two distinct documents**: Jan 24 = Meeks/Frankel ("lift the
freeze"); Feb 10 = Kelly/Pocan + 109 House Democrats (Brownley a signatory) urging PEPFAR
restoration. The ledger has been corrected (Cluster 4 date table + secondary-records log) and
the Jan 24 letter added as the earliest written warning. Detail in
`evidence/hfac-letter-jan24/transcript.md`.

**Precision corrections logged this pass:** (a) CFPB — the supportable claim is *dismantlement
judicially halted / likely unlawful*, **not** "CFPB unconstitutional" (SCOTUS upheld CFPB's
funding structure in 2024); (b) demographic — the affected subset is *people without exit
dependent on a withdrawn system, heavily pediatric*, not "children only" (Pe Kha Lau, 71).

**The single most important next action for this entire packet is custody work, not more
argument.** The capture pass advanced the six priority items from `CAPTURE-REQUIRED` to
`LOCATOR-VERIFIED` (canonical locator + verbatim text + integrity hash), but reaching **tribunal-grade
`VERIFIED` still requires the off-platform second custodian** that was never completed. (The egress
block described above is historical — this repo now runs in an open-egress environment, so any
interstitial/error-page captures can also be re-run to real content.) Begin with `musk-woodchipper-posts`
(X post + archive.org snapshot). Integrity of the current store: `sha256sum -c evidence/*/sha256.txt`.
