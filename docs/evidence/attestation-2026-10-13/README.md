# Attestation receipts — 2026-10-13

Fixes the bytes of `docs/election-disruption-preregistration-2026-10-13.md` (v1, unchanged since filing) and of its v1.1, v1.2 and v1.3 revisions (v1.3 is current; v1.2 is withdrawn for use) before the
2026-11-03 election, independently of this repo's own account of itself.

| Item | Mechanism | Status at filing | Complete / verify |
|---|---|---|---|
| `manifest.txt` | sha256 of the pre-registration | filed 2026-10-13T12:47:55Z | `sha256sum -c manifest.txt` from repo root |
| `manifest.txt.ots` | OpenTimestamps proof, submitted to the a/b pool, eternitywall and catallaxy calendars | **PENDING** Bitcoin anchor (normal: hours to days) | `ots upgrade manifest.txt.ots` once later and commit the upgraded proof; then `ots verify manifest.txt.ots` |
| `manifest-v1.1.txt` / `.ots` | sha256 of v1.1 (`docs/election-disruption-preregistration-v1.1-2026-10-13.md`), the revision after external review; OpenTimestamps proof submitted 2026-10-13 | **PENDING** Bitcoin anchor | same as above, for `manifest-v1.1.txt.ots` |
| `manifest-v1.2.txt` / `.ots` | sha256 of v1.2 (`docs/election-disruption-preregistration-v1.2-2026-10-13.md`), which adds the off-procedure rule, capture, and Scenario 6; OpenTimestamps proof submitted 2026-10-13 | **PENDING** Bitcoin anchor | `ots upgrade manifest-v1.2.txt.ots`, then `ots verify` |
| `manifest-v1.3.txt` / `.ots` | sha256 of v1.3 (`docs/election-disruption-preregistration-v1.3-2026-10-13.md`), which is v1.1 plus Scenario 6 and supersedes v1.2; OpenTimestamps proof submitted 2026-10-13 | **PENDING** Bitcoin anchor | `ots upgrade manifest-v1.3.txt.ots`, then `ots verify` |
| Git push | GitHub's server-side push record for the commit that adds this directory | recorded on push | the repo's activity / branch history |

**Does:** once the proof upgrades, it shows the pre-registration's exact text existed no later than
the anchoring Bitcoin block. **Does not:** say anything about whether any scenario is correct,
or cover any later edit. An edit to the pre-registration after the election is a new version and
needs its own dated stamp; the original stays as filed.
