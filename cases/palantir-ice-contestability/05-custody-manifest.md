# 05 — CUSTODY MANIFEST

*Post-capture state (2026-06-30, open-egress session). `evidence/custody-index.md` **governs**; this
page is narrative. Honest limits stated, not papered.*

## Current custody status: **VERIFIED (in-session) — 9/9 items**

Per `evidence/custody-index.md`: **9 VERIFIED · 0 LOCATOR-VERIFIED.** Each item holds a transcript
(hashed) + an original-form WARC + body, hashed into `original/manifest.json`. All checksums verified
post-run.

| Item | Held artifact | Grade | Note |
|---|---|---|---|
| `contract` | USASpending award page (WARC) | P1 | **JS-shell capture (~3 KB)** — locator-grade; see caveat |
| `oversight-menendez` | Menendez letter **PDF** (WARC) | P1 | full document |
| `oversight-goldman` | Goldman press release (WARC) | P1 | full page |
| `instrument-scope` | American Immigration Council (WARC) | S1 | full page |
| `contestability` | Biometric Update (WARC) | S1 | the crux item |
| `harm-npr` | NPR (WARC) | S1 | full page |
| `harm-citizen-suit` | ACLU SoCal (WARC) | P1 | party press + suit |
| `counter-register` | ACLU roundup (WARC) | ADV | + Palantir position as reported |
| `medicaid-feed` | EFF (WARC) | ADV/S1 | PARTIAL item |

## Honest limits — what is NOT yet true

1. **`contract` is a JS-shell capture.** USASpending.gov is a JavaScript single-page app; `wget`
   preserved the **canonical locator** and the shell response (~3 KB), **not** the rendered award
   record. The substantive contract facts ($30M, ID 70CTD022FR0000170, sole-source, dates) are
   **corroborated via S1** (Axios/AIC) and the contract ID is fixed, but the **full P1 award record**
   needs the USASpending **API/JSON export** or the official PDF — a follow-up capture / step-one target.
2. **`counter-register` holds Palantir's defense only as reported.** Palantir's **verbatim** public
   statement (company blog/press) is a **pending** capture; the ACLU page is the charge-side aggregator
   with Palantir's position recorded second-hand.
3. **Off-platform backup: PARTIAL.** Binaries are git-ignored (only hashes committed). The Wayback
   availability pass found existing third-party snapshots for **5 of 9** source URLs (recorded in each
   `original/archive-org-snapshots.txt`); the other 4 have none and SPN-create was unavailable (login).
   Exact-byte off-platform backup of the WARCs is still open.
4. **PARTIAL facts** (the "100 percent" agent quote; the Medicaid-data feed) are **not** upgraded by
   capture and are excluded from the load-bearing spine.

## To complete (follow-ups, not done here)

1. Capture the **USASpending API/JSON** (or official PDF) for the full P1 award record.
2. Capture **Palantir's verbatim defense** for a first-party counter-register.
3. Pursue the **step-one disclosures**: contract performance-work-statement, data-source list,
   confidence-score methodology, error/audit records, and the contest mechanism (or its absence).
4. Off-platform backup of the WARC artifacts (authenticated SPN or manual copy).

*Custody manifest v1, 2026-06-30. Status: VERIFIED in-session; `contract` locator-grade; off-platform
backup PARTIAL. The index governs; this narrative does not inflate past it.*
