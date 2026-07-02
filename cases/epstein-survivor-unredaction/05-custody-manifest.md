# 05 — CUSTODY MANIFEST

*Track F for the DOJ Epstein survivor-unredaction packet. Convention Art. VI(6); Protocol §6.*

> **Authoritative source:** `evidence/custody-index.md` governs. **No-reproduction discipline:** this
> store holds **reporting about** the exposure, never the exposed files or any survivor identity.

---

## Custody state

| State | Meaning |
|---|---|
| `VERIFIED` | Original artifact (WARC + PDF + screenshot) hashed into `<id>/original/manifest.json`. Full VERIFIED also assumes a second custodian + off-platform backup. |
| `LOCATOR-VERIFIED` | Canonical URL + structural text hashed; original-form bytes not yet held. |

## Items (all VERIFIED)

Built full-egress; `capture.sh --promote --archive-org` ran in place. As of capture (2026-06-29):
**4 VERIFIED · 0 LOCATOR-VERIFIED**, archive.org attestation on all four (7 snapshots).

| Item | Grade | Custody | Artifacts | archive.org |
|---|---|---|---|---|
| `victim-info-exposed` | S1 on P1 | VERIFIED | 14 (ABC + NBC + KSAT) | 2 |
| `redaction-asymmetry` | S1 on P1 | VERIFIED | 10 (CNN + Al Jazeera) | 2 |
| `technical-error-framing` | S1 on P2 | VERIFIED | 10 (PBS + CBC) | 2 |
| `survivors-lawsuit` | S1 on P1 | VERIFIED | 10 (Courthouse News + NBC) | 1 |

Integrity: `for d in evidence/*/; do (cd "$d" && sha256sum -c sha256.txt); done` (all `OK`). Per-artifact
hashes in `<id>/original/manifest.json`. Index: `evidence/custody-index.md`.

## Honest-custody notes

1. **No-reproduction is the governing rule (`04-falsification-memo.md` §F).** The captured artifacts
   are news pages that **do not name survivors**; the packet adds no survivor identifying detail. The
   **primary leaked files are deliberately NOT captured** — mirroring them would replicate the harm
   this case charges. This is a custody *limit by design*, not a gap to close.
2. **Repo holds only integrity records.** Per `.gitignore`, the large WARC/HTML/PDF/PNG binaries are
   off-platform custody; only `manifest.json`, `sha256sums.txt`, and `archive-org-snapshots.txt` are
   tracked — so even the captured news-page bytes are not committed to the repo.
3. **Some news hosts block `wget`** (403); those items still reached VERIFIED via Chromium PDF/PNG +
   archive.org. Recorded per item in the manifests.
4. **Grade is S1-on-P1.** The upgrade path is the **court complaint** (a P1 the packet can cite
   without reproducing survivor identities) — named in the falsification memo, not pursued here to
   avoid handling victim-identifying exhibits.

## What this packet does not claim

It does not hold or mirror the leaked files; it does not reproduce any survivor identity; it does not
assert intent; and it does not name the responsible officials. It preserves hashed reporting about a
state exposure of a vulnerable population, declares its limits, and stops there.
