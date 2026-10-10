# 05 — CUSTODY MANIFEST

*Track F for the Rubio / ICC packet. Convention Art. VI(6); Protocol §6.*

> **Authoritative source:** `evidence/custody-index.md` (machine-derived from each
> `capture.json`). If anything below diverges from it, **the index governs.**

---

## Custody states (same definitions as the sibling packets)

| State | Meaning |
|---|---|
| `LOCATOR-VERIFIED` | Canonical URL + verbatim text preserved as a hashed transcript; original-form bytes not held. |
| `HASHED-PENDING-BACKUP` | Original-form artifact captured + hashed in-repo, but no off-platform second custodian / backup yet. |
| `VERIFIED` | `HASHED-PENDING-BACKUP` plus an off-platform second custodian and confirmation the capture is real content. **0 items.** |

## This packet: 15 items, all `HASHED-PENDING-BACKUP`

**Captured 2026-10-10**, in a Claude Code cloud session with open egress through the agent proxy.
`capture.sh` runs `wget` with `--warc-file` for each URL (request + response record, gzip) and saves
the response body. Every artifact is hashed into `<id>/original/manifest.json` and
`sha256sums.txt`. Each `transcript.md` is hashed in `<id>/sha256.txt`.

**Real content, not interstitials.** Every body's extracted text was read on capture day, and the
quoted passages come from those bodies. The artifact sizes (28 KB – 676 KB HTML; 395 KB PDF) match
those of the first-pass reads.

**What is not held:** rendered screenshots or PDFs (no headless-browser pass was run); WARCs of
page requisites (images, scripts); any Wayback attestation.

## Failed custody steps (recorded, not hidden)

| Step | Result | Date |
|---|---|---|
| Wayback Save Page Now on the 9 Oct State statement | **Failed**: connection reset on `/save/`; the availability API returned **429** | 2026-10-10 |
| globalsecurity.org (ASP statement on the withdrawals) | **402** (licence/payment wall for AI retrieval); not captured | 2026-10-10 |
| thehill.com (Pillay Nobel) | **403**; same fact held via The National | 2026-10-10 |
| newarab.com (Khan 2021 Afghanistan "deprioritise") | **403**; owed | 2026-10-10 |
| euronews.com (14 Jul 2026 campaign report) | **406**; not needed (P1 mirror + Al Jazeera held) | 2026-10-10 |

## Path to VERIFIED

1. Off-platform second custodian: copy each item's `original/` to the operator's off-platform store
   (the "veriticide suite" Drive/GCP store named in the sibling packets) and record a receipt with
   matching hashes.
2. Third-party attestation: retry Wayback Save Page Now from a non-rate-limited network for every
   URL in `capture.json` → `source_urls`, and log the snapshot URLs.
3. Confirm the receipts match `manifest.json` hashes, then flip `custody_state` in `capture.json`
   and regenerate the index. **Never hand-edit the index.**

## Integrity check (run before and after any evidence change)

```bash
cd cases/rubio-icc-dismantlement/evidence
for d in */; do (cd "$d" && sha256sum -c sha256.txt && cd original && sha256sum -c sha256sums.txt); done
python3 build-custody-index.py
```

Last run: 2026-10-10. All 15 transcripts and all original artifacts pass.

## Privacy

No private identifiers are held. `captured_by` names the operator by handle, not email. The Khan
complainant is not named in any item; the sources do not name her.
