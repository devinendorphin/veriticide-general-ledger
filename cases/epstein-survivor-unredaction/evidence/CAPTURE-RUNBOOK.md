# CAPTURE RUNBOOK — DOJ Epstein survivor-unredaction case

*Companion to `capture.sh`, the packet `README.md`, and `../05-custody-manifest.md`. Built in a
full-egress environment, so capture ran in place.*

> **No-reproduction discipline (read first).** This packet captures **reporting about** the exposure
> of trafficking survivors — it does **not** capture, mirror, or reproduce the exposed "Epstein
> files" themselves, nor any survivor's name, image, or contact information. The cited outlets do not
> name survivors; the WARC/PDF/PNG of those pages therefore hold no survivor PII. **Do not** add the
> primary leaked documents to this store — that would replicate the very harm the case charges.

## Custody states

| State | Meaning |
|---|---|
| `LOCATOR-VERIFIED` | Canonical URL + structural text preserved as a hashed transcript; original-form bytes not yet held. |
| `VERIFIED` | Original artifact (WARC + PDF + screenshot) hashed into `<id>/original/manifest.json`. Full VERIFIED also assumes a second custodian + off-platform backup. |

## Run it

```bash
cd cases/epstein-survivor-unredaction/evidence
./capture.sh --promote --archive-org
```

Auto-detects Chromium (incl. Playwright's bundled build); `wget` produces the WARC; some news hosts
block `wget` (403) but Chromium PDF/PNG and archive.org still succeed — recorded honestly per item.
No video items, so `yt-dlp` is not required.

Per the repo `.gitignore`, only the integrity records (`manifest.json`, `sha256sums.txt`,
`archive-org-snapshots.txt`) are committed; large binaries are off-platform custody.

## Allowlist (for Custom-egress environments)

```
www.cnn.com
www.nbcnews.com
abcnews.com
*.abcnews.com
www.pbs.org
www.cbc.ca
www.courthousenews.com
www.ksat.com
www.aljazeera.com
web.archive.org
```
