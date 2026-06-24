# 05 — CUSTODY MANIFEST

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
| `VERIFIED` | Artifact preserved in `/evidence/` with original form + capture metadata + cryptographic hash + timestamp, held by ≥2 custodians, backed up off-platform. **No item is yet VERIFIED.** |

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

## Custody status summary

- **VERIFIED:** 0 items. *(No artifact yet preserved with hash + timestamp + dual custody.)*
- **CAPTURE-REQUIRED:** the primary artifacts (P1/P2) — the highest-leverage, least-protected
  items.
- **IN-LEDGER:** the secondary/expert corpus (S1/S2) — well-cited, single-copy, to be mirrored.

**The single most important next action for this entire packet is custody work, not more
argument.** The content already justifies emergency preservation, audit, inquiry, and
reporting. What converts it from a strong account into a usable evidentiary object is moving
the CAPTURE-REQUIRED items into `/evidence/` as VERIFIED. Begin with `musk-woodchipper-posts`.
