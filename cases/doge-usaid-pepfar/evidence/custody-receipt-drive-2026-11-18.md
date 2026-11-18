# CUSTODY RECEIPT — doge-usaid-pepfar · Drive second custodian · 2026-11-18

*Off-platform copy of the 2026-11-18 original-form re-capture (hardened `capture.sh`, run without `--promote`). Every file was uploaded through the Drive v3 API and checked against the md5 Drive reported back. Per-file sha256 and md5 are in `custody-receipt-drive-2026-11-18.json`; per-URL content verdicts in `content-check-2026-11-18.json`.*

- **Drive folder:** `the veriticide suite/case-evidence/doge-usaid-pepfar/capture-2026-11-18/` (folder id `1y0Xnp8LuwG-SeebLATZUVuAkm5l-eelm`), one subfolder per item.
- **Files:** 320 · **bytes:** 3,275,271,636 · **md5 matches:** 320/320
- **URLs:** 89 · REAL-CONTENT 65 · NOT-CONTENT 6 (passed the capture gate, but no source content) · NOT-CAPTURED 18 (refused by the gate; nothing kept)

| Item | Files in Drive | REAL-CONTENT | NOT-CONTENT | NOT-CAPTURED |
|---|---|---|---|---|
| `doge-savings-subset` | 20 | 4 | 0 | 2 |
| `gawande-democracynow` | 12 | 2 | 0 | 0 |
| `hfac-letter-jan24` | 14 | 3 | 0 | 1 |
| `ig-firings-jan2025` | 36 | 9 | 0 | 3 |
| `meeks-demands` | 14 | 4 | 0 | 0 |
| `musk-woodchipper-posts` | 14 | 3 | 0 | 1 |
| `named-deaths` | 20 | 4 | 0 | 2 |
| `propublica-internal-memos` | 24 | 5 | 0 | 0 |
| `rubio-hfac-testimony` | 8 | 1 | 0 | 0 |
| `rubio-waivers-nonfunctional` | 24 | 5 | 0 | 2 |
| `schatz-record` | 12 | 2 | 0 | 0 |
| `secondary-accountability-removal` | 32 | 7 | 0 | 2 |
| `secondary-doge-savings-witnesses` | 60 | 12 | 3 | 2 |
| `secondary-mortality-modeling` | 26 | 4 | 3 | 2 |
| `tamlyn-cable` | 4 | 0 | 0 | 1 |

**NOT-CONTENT artifacts** (in Drive, but not evidence of the source):
- `secondary-doge-savings-witnesses` https://www.cato.org/blog/doge-produced-largest-peacetime-workforce-cut-record-spending-kept-rising-0: bot-challenge page (obfuscated JavaScript, no article) served with HTTP 200
- `secondary-doge-savings-witnesses` https://www.cato.org/news-releases/doge-cut-jobs-not-spending-heres-why: bot-challenge page (obfuscated JavaScript, no article) served with HTTP 200
- `secondary-doge-savings-witnesses` https://www.tiktok.com/@nytimes/video/7477627559505710378: TikTok app shell; no video or transcript content in the captured HTML
- `secondary-mortality-modeling` https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12230335/: blank Chrome render: 116 characters of text, only the print header, no article body; captured as a validated Chrome PDF/PNG render only (no WARC)
- `secondary-mortality-modeling` https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12274115/: blank Chrome render: 116 characters of text, only the print header, no article body; captured as a validated Chrome PDF/PNG render only (no WARC)
- `secondary-mortality-modeling` https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12447089/: blank Chrome render: 116 characters of text, only the print header, no article body; captured as a validated Chrome PDF/PNG render only (no WARC)

**Content check method.** Each captured page is REAL-CONTENT if a quotation of 25+ characters from the item's `transcript.md` appears in its text, or its own title matches the article named in the URL. Render-only captures (no WARC) also need article body text. Manual inspection overrides: Cato (obfuscated-JavaScript bot challenge served with HTTP 200), TikTok (app shell), PMC (blank renders). The Dispatch page has the real article but paywall truncation of the body is not ruled out.

**Custody state is unchanged by this receipt.** No item was promoted. Whether items move to VERIFIED is a separate, logged decision.
