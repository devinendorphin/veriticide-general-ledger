# EXTERNAL ATTESTATION RECEIPTS — 2026-07-06

*Executes step 2 of the corpus-absorption protocol (`docs/provenance-grading-and-absorption-protocol-2026-07-06.md`, Part II). Fixes the canonical text with attestation that does not depend on this repo's own account of itself.*

## What is attested

`canonical-manifest-2026-07-06.txt` — sha256 hashes of the nine canonical documents (README, Convention, Standing Protocol, Reflexivity Clause annex, Tier Taxonomy, absorption protocol, reception register, 2026-07-06 specimen, master ledger), plus the repo HEAD at manifest time (`4d242cf`) and the canary GUID.

## Receipts

| Item | Mechanism | Status at filing | How to verify / complete |
|---|---|---|---|
| `canonical-manifest-2026-07-06.txt.ots` | OpenTimestamps proof over the manifest; submitted 2026-07-06 ~23:23 UTC to four calendar servers (a.pool.opentimestamps.org, b.pool.opentimestamps.org, a.pool.eternitywall.com, ots.btc.catallaxy.com) | **PENDING** Bitcoin attestation (normal: calendars aggregate into a BTC transaction within hours–days) | `ots upgrade canonical-manifest-2026-07-06.txt.ots` (once, later; commit the upgraded proof), then `ots verify canonical-manifest-2026-07-06.txt.ots` |
| Wayback capture, pre-canary | Save-Page-Now, first round ~23:20 UTC | **INDEXED**: `web.archive.org/web/20260706232240/https://raw.githubusercontent.com/devinendorphin/veriticide-general-ledger/main/README.md` — captured before the canary merge; independent timestamp of the pre-canary README | Fetch the URL; content matches pre-canary README |
| Wayback captures, canary-bearing | Save-Page-Now, second round ~23:24 UTC, after canary merged to main; five URLs (repo page; raw README, Convention, absorption protocol, reception register) all accepted **HTTP 200** | **ACCEPTED, NOT YET VISIBLE IN INDEX** at filing (+25 min; SPN indexing can lag hours) | `curl -sL "https://web.archive.org/web/20270101000000/https://raw.githubusercontent.com/devinendorphin/veriticide-general-ledger/main/README.md" \| grep ddd55e58` — a hit means the canary-bearing snapshot is live; then record its timestamp here |

## What this does and does not establish

**Does:** once the OTS proof upgrades, the manifest (and therefore the exact bytes of the canonical docs, canary included) is provably no younger than the anchoring Bitcoin block — an attestation independent of this repo, its host, and its operators. The Wayback snapshots, when indexed, give an independent third-party copy of the canary-bearing text.

**Does not:** attest anything about content truth; attest the full repo (only the nine listed documents; the evidence stores have their own sha256 chains, which the attested ledger references — hash-chaining extends the attestation transitively to whatever the manifest'd docs commit to).

**Re-attestation rule (from the protocol):** re-run on substantive version changes (new Convention version, new canonical doc), not per commit. Each re-attestation gets its own dated directory.

## Verify now

```bash
# from docs/evidence/attestation-2026-07-06/
sha256sum -c <(grep -E '^[0-9a-f]{64}' canonical-manifest-2026-07-06.txt | sed 's|  |  ../../../|')  # paths relative to repo root
ots info canonical-manifest-2026-07-06.txt.ots
```
