# 05 — CUSTODY MANIFEST

> **✅ Custody update (2026-07-02, two steps).** Reset from an overclaimed `VERIFIED` to
> `HASHED-PENDING-BACKUP` in the audit, then verified against custody. **9 of 11 items are now true
> `VERIFIED`** (real content + a Wayback snapshot + an off-platform Drive custody receipt).
> **`selc-letter-2024-08` and `selc-letter-2025-04` remain `HASHED-PENDING-BACKUP`** — real captured
> content in-repo but no Wayback snapshot yet. The machine-derived `evidence/custody-index.md`
> governs; full audit: `docs/custody-status-2026-07-02.md`.

*Post-capture state. On 2026-06-30 (open-egress session) the evidence items were promoted from
URL-CITED to **original-form captured**. The canonical index `evidence/custody-index.md` **governs**;
this page is narrative. Honest limits (blocked sources, off-platform backup) are stated, not papered.*

## Current custody status: **9 VERIFIED · 2 HASHED-PENDING-BACKUP** (2026-07-02)

Per `evidence/custody-index.md` (mechanically derived): **9 VERIFIED · 2 HASHED-PENDING-BACKUP.** (6 original items + 5 P1/disposition items captured in the (b) run: `permit-appeal-p1`, `selc-letter-2024-08`, `selc-letter-2025-04`, `epa-action`, `board-mootness-denial`.)

| Item | Held original-form artifact | Custody |
|---|---|---|
| `unpermitted-operation` | SELC page (WARC + body) — ICN URL blocked wget; SELC is the held primary | VERIFIED |
| `permit-grant` | CNBC (WARC + body) | VERIFIED |
| `turbine-survey` | CNN (WARC + body) | VERIFIED |
| `appeal-challenge` | CNBC (WARC + body) | VERIFIED |
| `ej-harm` | NBC News (WARC + body) | VERIFIED |
| `chamber-defense` | Greater Memphis Chamber (WARC + body) | VERIFIED |

## Capture method (recorded for audit)

- **Document-only WARC + HTML body** via `wget` through the sanctioned Claude Code agent proxy
  (system-CA-trusted), 2026-06-30. WARC preserves the full request/response/headers — the strongest
  single original-form artifact.
- **PDF/PNG screenshots were deliberately omitted.** Behind the TLS-intercepting proxy, headless
  Chromium would render and capture certificate-error pages; recording a broken render as the source
  would corrupt custody. WARC (trusted via the system CA) is held instead.
- Each artifact hashed into `evidence/<id>/original/manifest.json` + `sha256sums.txt`; every
  `transcript.md` hashed in `<id>/sha256.txt`. All checksums **verified** post-run.

## Honest limits — what is NOT yet true

1. **Off-platform second custodian: OPEN.** Per repo `.gitignore`, the **binary artifacts
   (`*.html`, `*.warc`) are NOT committed** — only the integrity records (`manifest.json`,
   `sha256sums.txt`) are. The actual bytes currently live **only in this ephemeral build workspace**.
   Until they are copied off-platform (or to archive.org), the committed state proves *what was
   captured and its hash*, but the artifacts themselves are not yet durably preserved. This mirrors the
   redistricting packet's open condition and is the **decisive remaining step** for full VERIFIED.
2. **Three sources blocked automated capture:** Inside Climate News, TIME, and Tennessee Lookout
   returned empty/blocked to `wget`. Their facts are held via capturable equivalents (SELC, CNBC, NBC);
   the blocked URLs remain **secondary locators** in the transcripts, not held artifacts.
3. **Two facts remain PARTIAL regardless of capture:** the **exact turbine count** (party-contested)
   and the **"4× cancer risk" multiple** (needs independent re-derivation from EPA air-toxics data, not
   just capture of a secondary source). Capturing a page does not upgrade a contested figure.

## To complete full VERIFIED (next step, not done here)

1. Copy `evidence/*/original/*` to an off-platform custodian (archive.org Save Page Now via
   `capture.sh --archive-org`, plus a private backup). Record snapshot URLs in
   `original/archive-org-snapshots.txt`.
2. Obtain the **SCHD permit PDF** and the **SELC appeal filing PDF** as P1 originals (currently held
   via secondary coverage) and hash them in.
3. Re-derive the air-toxics risk figure independently, or leave it PARTIAL on the record.

*Custody manifest v2, 2026-06-30. Status: HASHED-PENDING-BACKUP (in-session hashes committed); off-platform backup
OPEN. The index governs; this narrative does not inflate past it.*

---

## archive.org pass (2026-06-30) — partial off-platform custody

Save Page Now **requires an archive.org login** (unavailable this session), so **new** snapshots could
not be created. Instead the Wayback **availability API** was queried for every captured source URL, and
existing third-party snapshots were recorded in each `original/archive-org-snapshots.txt` (committed).

- **10 of 12 source URLs** have an existing Internet-Archive snapshot (incl. the P1 `permit-appeal-p1`
  filing PDF, Wayback crawl 2026-06-08; the news items, crawls mid/late-June 2026). These are durable,
  third-party-held copies that survive this container.
- **2 URLs have no Wayback snapshot:** the two SELC letter PDFs on `interactive.localmemphis.com`
  (`selc-letter-2024-08`, `selc-letter-2025-04`). SPN-create was unavailable (login). These remain held
  **only** as in-container WARC + committed hash until backed up off-platform by other means.

**Honesty caveat — corroborant, not byte-match.** A Wayback snapshot is an **independent crawl at its
own timestamp** (recorded in the snapshots file), not a byte-identical copy of today's WARC. It
corroborates the URL and its content at a near date; the in-repo `manifest.json` hash remains the
exact-capture record. So off-platform custody is now **PARTIAL**: 10/12 URLs third-party-corroborated;
exact-byte off-platform backup of the WARC/PDF artifacts (and the 2 un-snapshotted letters) is still
open and would need an authenticated SPN or a manual copy out of this workspace.
