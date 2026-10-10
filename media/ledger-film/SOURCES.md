# Ledger film — sources for every on-screen figure

`veriticide-ledger.mp4` (88.5 s, 1080p30) is rendered by `render.py` from this repository.
Re-run `python3 render.py veriticide-ledger.mp4` to regenerate. Counts are as of 2026-10-10.

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
