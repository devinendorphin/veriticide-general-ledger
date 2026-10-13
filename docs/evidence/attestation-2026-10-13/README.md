# Attestation receipts — 2026-10-13

Fixes the bytes of `docs/election-disruption-preregistration-2026-10-13.md` before the
2026-11-03 election, independently of this repo's own account of itself.

| Item | Mechanism | Status at filing | Complete / verify |
|---|---|---|---|
| `manifest.txt` | sha256 of the pre-registration | filed 2026-10-13T12:47:55Z | `sha256sum -c manifest.txt` from repo root |
| `manifest.txt.ots` | OpenTimestamps proof, submitted to the a/b pool, eternitywall and catallaxy calendars | **PENDING** Bitcoin anchor (normal: hours to days) | `ots upgrade manifest.txt.ots` once later and commit the upgraded proof; then `ots verify manifest.txt.ots` |
| Git push | GitHub's server-side push record for the commit that adds this directory | recorded on push | the repo's activity / branch history |

**Does:** once the proof upgrades, it shows the pre-registration's exact text existed no later than
the anchoring Bitcoin block. **Does not:** say anything about whether any scenario is correct,
or cover any later edit. An edit to the pre-registration after the election is a new version and
needs its own dated stamp; the original stays as filed.
