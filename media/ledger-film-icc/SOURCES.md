# Ledger film, ICC cut — sources for every on-screen figure

`veriticide-ledger-icc.mp4` (174.0 s, 1080p30, silent text over a low ambient tone) is rendered by
`render.py` beside this file: `python3 render.py veriticide-ledger-icc.mp4`.

- **First half (0:00–1:28.5):** identical scenes to `media/ledger-film/render.py` on branch
  `ccr-9ccea43f-ymg1wk`. The scene definitions diff clean. Sampled frames at 4, 20, 30, 45, 62
  and 80 s match the original render; the only differences are a few pixels of the progress
  hairline, which scales with total length. Its counts are **as of 2026-10-10, 05:00 UTC**, before
  this case existed ("8 cases," "65 hashed items"). They are kept unchanged on purpose: the second
  half is the ninth case.
- **Second half (1:28.5–2:54):** the ninth case file, `cases/rubio-icc-dismantlement/`, replacing
  the earlier cut's Rubio/USAID appendix.

## First half (unchanged sources, from the original SOURCES.md)

| On screen | Source |
|---|---|
| 7,993 lines | `wc -l ledger/ledger.md` |
| 188 commits | `git rev-list --count HEAD` (full, unshallowed history) |
| 65 hashed items · 8 cases | `cases/*/evidence/*/sha256.txt` |
| 19 of 65 VERIFIED | `cases/*/evidence/custody-index.json` (Boxtown 9, X 7, Palantir 3), matching the README Custody column |
| Classifications, six moves, six tiers | `CLAUDE.md`; `docs/documentation-standing-protocol-v0.1.md` §2; `docs/veriticide-stack-tier-taxonomy-v0.1.md` |
| Ledger scroll / hash wall | Read live from `ledger/ledger.md` lines 151–260 and the case `sha256.txt` files |
| First commit 21 Jun 2026 → eight case files 30 Jun 2026 | `git log --reverse`; first commit touching each `cases/*/` (last of the eight: 2026-06-30) |
| IIMM mandated 27 Sep 2018 → operational 30 Aug 2019 | HRC res. 39/2; IIMM first report, A/HRC/42/… — <https://iimm.un.org/sites/default/files/2020/07/HRC-42-IIMM-report.pdf>, <https://burmacampaign.org.uk/media/IIMM-Annual-Report-2019.pdf> |

## BOUNDARY

The "337 days / 9 days" comparison is **mandate-to-readiness time only**. It does not
establish equivalence: the Mechanism runs field investigation, witness protection, and
tribunal-grade custody; 46 of the ledger's 65 items are not yet VERIFIED. The film says so on screen.
"Eight case files" means the six-extract dossier structure existed by 2026-06-30; the files
have been revised since. The film asserts step one (a basis to demand preservation,
disclosure, audit, inquiry), not step two.

## Appendix — the Rubio case (`cases/rubio-usaid-denial/`)
| On screen | Source |
|---|---|
| Band 2 · Tier 4 · single named respondent | `README.md` case table; `00-charge-theory.md` (Tier placement, Named respondent) |
| Escalation ladder, rungs 1–5 | `00-charge-theory.md`, "The act" table |
| Element grades (instrument contested; legibility strong; mental element strongest; conscription N/A) | `00-charge-theory.md`, "The elements" table |
| Five steel-manned defenses | `03-adversarial-check.md`, Defenses 1–5 |
| Four falsifiers; "if the denial was actually argued, it is protected" | `04-falsification-memo.md` §A–C |
| "Does not establish" list | `00-charge-theory.md`, "What this charge theory does NOT establish" |
| Active soft / dormant hard vehicles | `00-charge-theory.md`, Forum-Now block |
| 2 items, HASHED-PENDING-BACKUP, full hashes | `evidence/custody-index.md`; `evidence/*/sha256.txt` |

Condensations of the defenses and falsifiers are paraphrased; the quotes in the ladder are verbatim
## Second half — `cases/rubio-icc-dismantlement/`

| On screen | Source |
|---|---|
| Band 2 · Tier 4, correction-environment form · single named respondent | `README.md` case table; `00-charge-theory.md` (Tier placement; Named respondent) |
| Three forms of the act, with dates and quotes | `00-charge-theory.md` "The act"; verbatim quotes from `evidence/state-icc-designation-chain`, `state-albanese-designation`, `state-palestinian-ngo-designations`, `state-icc-institution-designation` (P1) |
| "Albanese has done nothing more than speak" — Judge Leon | `evidence/us-court-rulings-eo14203` (S1, Al Jazeera report of the 13 May 2026 D.D.C. opinion; opinion P1 owed) |
| Disconfirming-test rows | `00-charge-theory.md`, "What the disconfirming test removed" |
| Element grades | `00-charge-theory.md`, "The elements" |
| "effects reported 17 months before" | `evidence/ap-sanctions-operational-effects` (AP, May 2025) → institutional designation 9 Oct 2026 |
| Five steel-manned defenses (condensed) | `03-adversarial-check.md`, Defenses 1, 2, 3, 4, 8 |
| Four falsifiers (condensed) | `04-falsification-memo.md` §A.1, §B.1, §C.2, §F |
| "Does not establish" list | `00-charge-theory.md`, "What this charge theory does NOT establish" |
| Active soft / dormant hard vehicles | `00-charge-theory.md`, Forum-Now |
| 15 items · WARC + body · HASHED-PENDING-BACKUP · 0 VERIFIED; the three hashes | `evidence/custody-index.md`; `evidence/*/sha256.txt` |
| "not yet reviewed" | `README.md` footer; the blind review handoff `docs/handoffs/chatgpt-review-rubio-icc-2026-10-10.md` is written but not yet run |

## The time scene

| On screen | Source |
|---|---|
| IIMM 337 days; first eight case files 9 days | as in the first half (original SOURCES.md) |
| **requested 05:42:12 UTC** | Claude Code session record `session_01FA7tS5vTL8uG3kaewqUGXD`, `created_at` 2026-10-10T05:42:12.555Z (the operator's request opened the session) |
| **pushed 06:02:47 UTC** | commit `de24972` (case packet, 15 evidence items, ledger Cluster 11 + TD-010), author date 2026-10-10T06:02:47Z |
| **00:20:35** | the difference between the two |
| first primary source fetched 05:43:30 UTC (not on screen) | file timestamp of the first captured State Department page |
| "announced the day before" | State Department press statement dated 9 Oct 2026 (`evidence/state-icc-institution-designation`) |
| "111 days of protocol" | first commit 21 Jun 2026 (as in the first half) → 10 Oct 2026 |

## BOUNDARY

The clock measures **one session's wall time** from request to pushed case. It does not establish
equivalence with the Myanmar Mechanism, which runs field investigation, witness protection and
tribunal-grade custody. It does not establish that the case is correct. The case is not yet
independently reviewed, and none of its 15 items is VERIFIED. The speed rests on the protocol,
the case grammar, the capture tooling and the eight earlier cases, built over 111 days. The film
says this on screen. The work was done by an AI analyst (Claude) at the operator's direction.
The film asserts step one only.
