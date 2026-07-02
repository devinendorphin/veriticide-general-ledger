# CAPTURE RUNBOOK — X bot-swarm case

*How to perform original-form preservation of this case's evidence. Companion to `capture.sh`,
the packet `README.md`, and `../05-custody-manifest.md`. Patterned on the shared
`../../doge-usaid-pepfar/evidence/CAPTURE-RUNBOOK.md`.*

---

## Status note (this packet differs from the DOGE/Rubio packets)

The DOGE and Rubio packets were built in a **Trusted**-network environment that blocked source
hosts (403), so their items were filed `LOCATOR-VERIFIED` pending a separate open-egress run. **This
packet was built in a full-egress environment** (source hosts return HTTP 200, including `x.com`),
so original-form capture was run **in place** at build time. If you are re-running it, the procedure
below reproduces the capture.

## Custody states

| State | Meaning |
|---|---|
| `LOCATOR-VERIFIED` | Canonical URL + verbatim text preserved as a hashed transcript; original-form bytes not yet held. |
| `VERIFIED` | Original artifact (WARC/PDF/screenshot) hashed into `<id>/original/manifest.json`. Full VERIFIED also requires a second custodian + off-platform backup (committing `original/` here is one custodian). |

## Run it

```bash
cd cases/x-bot-swarm/evidence
./capture.sh --promote --archive-org
```

The script auto-detects Chromium, including **Playwright's bundled build**
(`$PLAYWRIGHT_BROWSERS_PATH/chromium-*/chrome-linux/chrome`), so it works on Claude Code web/CI
images without installing a system Chrome. `wget` produces the WARC; Chromium produces PDF + PNG.
There are no video items in this packet, so `yt-dlp` is not required.

Per the repo `.gitignore`, only the small integrity records (`manifest.json`, `sha256sums.txt`,
`archive-org-snapshots.txt`) are committed; the large binaries (WARC/HTML/PDF/PNG) are kept in
off-platform custody, which doubles as the manifest's required second custodian.

## Options A/B/C (other environments)

If you ever need to run this from a **Trusted** web environment, a throwaway VM, or your own
laptop, the three options in the shared runbook
(`../../doge-usaid-pepfar/evidence/CAPTURE-RUNBOOK.md`) apply verbatim — use the allowlist below.

## Allowlist for this case

For **Custom** network access (Claude Code web) — covers every source cited across this packet's
evidence items. `*.` is a wildcard subdomain match.

```
x.com
twitter.com
*.twitter.com
cbsnews.com
*.cbsnews.com
foxbusiness.com
*.foxbusiness.com
gzeromedia.com
*.gzeromedia.com
cybernews.com
sciencedirect.com
*.sciencedirect.com
theconversation.com
techcrunch.com
*.techcrunch.com
cjr.org
*.cjr.org
independenttechresearch.org
osome.iu.edu
*.iu.edu
web.archive.org
```

> **Custom vs Full is a real security decision.** A `Full`-egress agent can reach any host; for a
> morally-hot case prefer `Custom` limited to exactly these sources. (This packet's own capture
> ran in a Full-egress session; the allowlist is provided for reproducibility under Custom.)

## Honest-custody note

`x.com` status pages are JavaScript-heavy; the WARC/PDF/PNG of a tweet URL may capture a
login/interstitial shell rather than the rendered post. Where that occurs, the tweet text is
preserved verbatim in `transcript.md` (hashed) and corroborated by the CBS News / Fox Business
captures, which render fully. This limitation is recorded per-item in `original/manifest.json`
artifact sizes and in `05-custody-manifest.md`; it is not papered over.
