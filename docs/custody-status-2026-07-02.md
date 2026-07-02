# CUSTODY STATUS & RECONCILIATION — 2026-07-02

*A custody self-audit and remediation record. This document is the authoritative account of what
was reconciled on 2026-07-02, why, and what remains. It sits beside `docs/provenance.md` (which
records changes to the ledger's form) and is pointed to from every case's `05-custody-manifest.md`
and every `evidence/custody-index.md`.*

---

## 1. The finding

Across the corpus, **54 evidence items in 6 cases were marked `VERIFIED`** in their `capture.json`
and canonical `custody-index.{md,json}`. That state was an **overclaim**, for two independent
reasons:

1. **No off-platform second custodian existed.** Every packet's own definition of `VERIFIED`
   requires "original artifact hashed **plus** a second custodian + off-platform backup." Per the
   repo `.gitignore`, the large binaries (WARC/PDF/PNG/HTML) are deliberately not committed; they
   were meant to live in **off-platform custody (a Google Drive / GCP store — "the veriticide
   suite"), which doubles as the manifest's required second custodian.** That backup was never
   completed. So the only custodian that ever existed for the originals was the operator's local
   capture machine, and the repo held **only the hashes**, not the artifacts and not a second copy.

2. **Some captures were interstitial / error pages, not real content.** Much of the corpus was
   captured in an earlier **blocked-egress** environment where source hosts returned `403` /
   login walls. The pipeline hashed whatever bytes came back and `capture.sh --promote` flipped
   the item to `VERIFIED` on `artifact_count > 0` alone — so an error page counted as a fulfilled
   capture. Example: `cases/doge-usaid-pepfar/evidence/doge-savings-subset/original/manifest.json`
   records `doge.gov_savings.html` at **0 bytes** and `doge.gov_savings.warc` at **~11 KB** (an
   interstitial), even though its `capture_method` field states *"original-form bytes not
   retrieved"* — while the same item was marked `VERIFIED`. (Secondary outlets in that same item —
   ABC, CBS, Al Jazeera — did capture real multi-MB content; the item was promoted on their
   strength despite the primary failing.)

The single most conspicuous symptom, flagged by the 2026-07-01 external assessment, was that
`cases/doge-usaid-pepfar/evidence/custody-index.md` said **"VERIFIED: 13"** in its header while its
own legend said **"VERIFIED … 0 items."** The same file gave two answers because the word was
overloaded: it meant "original bytes hashed in-repo" in the per-item rows and "tribunal-grade
dual-custody" in the legend.

## 2. What was reconciled (2026-07-02)

**Custody-state vocabulary, disambiguated into three honest states** (plus the pre-existing
`SCREENSHOT-HELD` used by the CTF-1 corpus):

| State | Meaning |
|---|---|
| `LOCATOR-VERIFIED` | Canonical URL + verbatim text preserved as a hashed transcript; original-form bytes not held. |
| `HASHED-PENDING-BACKUP` | Original-form artifacts captured and hashed into `<id>/original/manifest.json` (in-repo integrity record exists), **but no off-platform second custodian / backup yet**, and pre-open-egress captures may hold interstitial/error-page bytes. **Not tribunal-grade.** |
| `VERIFIED` | `HASHED-PENDING-BACKUP` **plus** an off-platform second custodian (the `the veriticide suite` Drive/GCP store) **and** confirmation the capture holds real source content, not an interstitial. **The only tribunal-grade state.** |

**Changes applied:**

- All **54** items previously `VERIFIED` were reset to `HASHED-PENDING-BACKUP` in their
  `capture.json` (with a `custody_reconciled` note; the old `verified_at` field was renamed
  `promoted_at` since the item is no longer verified).
- The **7 non-CTF-1 `build-custody-index.py` generators** were rewritten to a single canonical form:
  they tally states generically and emit the honest three-state legend above, resolving the
  "VERIFIED 13 / 0 items" contradiction. All eight `custody-index.{md,json}` were regenerated.
- **`capture.sh --promote`** (all 6 variants) now flips a captured item to `HASHED-PENDING-BACKUP`,
  **never to `VERIFIED`**. `VERIFIED` is reserved for the separate, deliberate off-platform-backup
  step. This stops the tool from manufacturing the overclaim on re-run.
- Each case's `05-custody-manifest.md` carries a dated reconciliation banner (the page's historical
  counts now defer explicitly to the governing index), and the prominent per-item marks, headline
  status lines, and the two factually-false "blocked by egress / 0 items" legend rows were corrected.
- No `transcript.md` or `sha256.txt` was altered; all transcript integrity hashes still verify.

**Post-reconciliation custody census:**

| Case | HASHED-PENDING-BACKUP | LOCATOR-VERIFIED | SCREENSHOT-HELD |
|---|---|---|---|
| doge-usaid-pepfar | 13 | 2 | — |
| xai-boxtown-turbines | 11 | — | — |
| election-redistricting | 9 | — | — |
| palantir-ice-contestability | 9 | 1 | — |
| x-bot-swarm | 8 | — | — |
| epstein-survivor-unredaction | 4 | — | — |
| rubio-usaid-denial | — | 2 | — |
| ctf1-corpus | — | — | 6 |
| **Total** | **54** | **5** | **6** |

**`VERIFIED` (tribunal-grade): 0 items** — honestly, until the off-platform backup below is done.

## 2a. Phase-2 pilot — x-bot-swarm (2026-07-02, DONE)

Ran the full remediation on x-bot-swarm as the proof case (operator direction: one clean case first, exclude Epstein). All 8 items were **re-captured in open egress** — real multi-MB WARC/HTML content this time, not interstitials. **7 of 8 were restored to true `VERIFIED`**, resting on three custodians: the git integrity records, **Internet-Archive Wayback snapshots** (independent third party; 7/8 items, 15 snapshots), and an **off-platform custody receipt** placed in Google Drive `the veriticide suite/case-evidence/x-bot-swarm/` (`custody-receipt-x-bot-swarm-2026-07-02.md`). The full per-artifact sha256 receipt is committed at `cases/x-bot-swarm/evidence/custody-receipt.md`.

`post-takeover-bot-persistence` was **held at `HASHED-PENDING-BACKUP`**: Cybernews returned an interstitial and ScienceDirect a JS shell (only the Chromium PDF renders are real), and it has no Internet-Archive snapshot. This is the honesty check working as intended.

**Practical note that shapes the rollout:** an agent cannot move the raw binaries (~130 MB for this one case) into Drive through the MCP tool — base64 through a chat tool would be millions of tokens. So the durable design is: **Internet Archive = the independent off-platform custodian** (already automated in `capture.sh --archive-org`), **Drive holds the human-readable custody receipt**, and the operator syncs the raw `original/*` bytes with **`evidence/backup-to-drive.sh` (rclone)** from a machine that has them. Corpus-wide `VERIFIED` count after the pilot: **7**.

## 3. Confirmations from the same pass

- **The public ledger body is present and substantial.** `ledger/ledger.md` is **7,456 lines / 56
  headings** on this branch — not empty. The README's description of it as the "source of record /
  cathedral" is accurate on this branch. (The 2026-07-01 assessment flagged that it *"appeared
  empty on main"* in an earlier read and asked for manual confirmation; this is that confirmation
  for `claude/repo-cleanup-gcp-sync-t70qvp`.)

## 4. Remediation plan — reaching true `VERIFIED`

The environment is now **open-egress** (verified: `cbsnews.com` and `web.archive.org` both return
`200`), so the two blockers can finally be cleared:

1. **Re-capture in open egress.** Re-run each case's `capture.sh --promote --archive-org`, which
   now produces real content for hosts that previously 403'd, and re-hashes into
   `original/manifest.json`. New captures carry a 2026-07-02 timestamp and new hashes (they replace
   interstitial bytes; this is a custody *correction*, recorded, not a silent overwrite).
2. **Establish the off-platform second custodian.** Copy each item's `original/*` into the
   `the veriticide suite` Google Drive folder (folder id `1GhLBKeIqr4wWMFwyRy7kSlIRJJsdyjIu`),
   preserving the case/item path, and record the Drive custodian in each `capture.json`.
3. **Flip to `VERIFIED`** only for items whose capture is confirmed real content **and** whose
   originals are backed up off-platform — as a logged, deliberate step, distinct from `--promote`.

*A recommended hardening (not yet applied): have `capture.sh` refuse to promote a URL whose WARC/HTML
is 0 bytes or below a small threshold, so an interstitial can never again be counted as a fulfilled
capture.*

## 5. Still open (from the 2026-07-01 assessment, not custody)

- Roll the Forum-Now toggle into the remaining case files (only Boxtown is done).
- Add a one-page reader's map (journalist / lawyer / community-documenter entry paths).
- Secure one human second custodian + one external legal/domain reviewer on the strongest case.
