# CUSTODY RECEIPT (Drive) — 1.4-trellis-primaries · 2026-07-19

Off-platform second-custodian receipt for the 1.4 verification store. Records the Google Drive location of the durable custody *record set* (hash manifest + verification record). Per-artifact SHA-256 and exact source URLs are in `original/manifest.json`; the raw binaries are reproducible via `refetch.sh`.

## Drive location

Folder: **veriticide-evidence — 1.4-trellis-primaries**
`https://drive.google.com/drive/folders/1vZMCnGrcFRFWA-zL9NqljaE1dmvyKRba`

| File in Drive | Drive file id |
|---|---|
| `manifest.json` (sha256 + source_url per artifact) | `1drxG92yqe_Vu6BSpL-npMpAnsc6hCF0C` |
| `sha256sums.txt` | `1BYPRp_BnCuto3_Un5HJceqguU88fYig7` |
| `verification-record.md` | `1Ib48xSn-kBancpUg-vBbKj8Wk3jawjyd` |
| `capture.json` | `1OwuOAdVNcbQ56IkKDfLXeMZ3GC6aWvfE` |

## What is and is not in Drive

- **In Drive now:** the custody record set above — the durable, human- and machine-checkable index. This is the off-platform *second custodian of the record*.
- **Not in Drive (yet):** the raw PDF/HTML binaries (~61 MB). They could not be pushed from the ephemeral capture container (the Drive upload path takes content inline; multi-MB binaries can't be streamed that way, and rclone credentials aren't present in-container). This does **not** lose the documents: every one is public and is reproducible byte-for-byte from `original/manifest.json` via `refetch.sh`, then verifiable against these hashes.

## To complete byte-level custody (operator, on any machine with the bytes + rclone)

1. `cd docs/evidence/1.4-trellis-primaries && ./refetch.sh` — re-download all primaries and confirm hashes match the manifest (green = documentary core intact).
2. `rclone copy original "<remote>:" --drive-root-folder-id 1vZMCnGrcFRFWA-zL9NqljaE1dmvyKRba --checksum` — push the raw bytes into the same Drive folder.
3. Update `capture.json` custody_conditions: `off_platform_backup: true`; with a second independent custodian, custody_state → VERIFIED.

Custody state remains **HASHED-PENDING-BACKUP** until the raw bytes have an off-platform copy and a second independent custodian.
