# 05 — CUSTODY MANIFEST

> **⚠ Custody reconciliation (2026-07-02).** Counts and per-item marks on this page predate the
> 2026-07-02 custody audit and are **historical narrative**. The authoritative, machine-derived
> state is `evidence/custody-index.md`; where this page and the index disagree, **the index
> governs.** Items formerly marked `VERIFIED` are now `HASHED-PENDING-BACKUP`: original-form
> artifacts were hashed into `original/manifest.json` in-repo, but the off-platform second
> custodian that `VERIFIED` requires is not yet in place, and some pre-open-egress captures may
> hold interstitial/error-page bytes. Remediation plan: `docs/custody-status-2026-07-02.md`.

*Track F for the DOJ Epstein survivor-unredaction packet. Convention Art. VI(6); Protocol §6.*

> **Authoritative source:** `evidence/custody-index.md` governs. **No-reproduction discipline:** this
> store holds **reporting about** the exposure, never the exposed files or any survivor identity.

---

## Custody state

| State | Meaning |
|---|---|
| `VERIFIED` | Original artifact (WARC + PDF + screenshot) hashed into `<id>/original/manifest.json`. Full VERIFIED also assumes a second custodian + off-platform backup. |
| `LOCATOR-VERIFIED` | Canonical URL + structural text hashed; original-form bytes not yet held. |

## Items (all HASHED-PENDING-BACKUP)

Built full-egress; `capture.sh --promote --archive-org` ran in place. As of capture (2026-06-29):
**4 HASHED-PENDING-BACKUP · 0 LOCATOR-VERIFIED**, archive.org attestation on all four (7 snapshots).

| Item | Grade | Custody | Artifacts | archive.org |
|---|---|---|---|---|
| `victim-info-exposed` | S1 on P1 | HASHED-PENDING-BACKUP | 14 (ABC + NBC + KSAT) | 2 |
| `redaction-asymmetry` | S1 on P1 | HASHED-PENDING-BACKUP | 10 (CNN + Al Jazeera) | 2 |
| `technical-error-framing` | S1 on P2 | HASHED-PENDING-BACKUP | 10 (PBS + CBC) | 2 |
| `survivors-lawsuit` | S1 on P1 | HASHED-PENDING-BACKUP | 10 (Courthouse News + NBC) | 1 |

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
