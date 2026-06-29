# CAPTURE RUNBOOK — Prediction-markets case

*How to perform original-form preservation of this case's evidence. Companion to `capture.sh`,
the packet `README.md`, and `../05-custody-manifest.md`. Patterned on the shared
`../../doge-usaid-pepfar/evidence/CAPTURE-RUNBOOK.md` and the `../../x-bot-swarm/evidence/` runbook.*

---

## Status note (this packet is LOCATOR-VERIFIED, like the DOGE/Rubio packets)

This packet was built in a **Trusted/Custom-egress** environment in which the agent proxy returns
**HTTP 403** on the news/regulator source hosts and **throttles** web.archive.org Save Page Now
(**429**). Sanctioned **web search** was available (and is how every anchor except the Fed-accuracy
item was confirmed this session), but **original-form bytes could not be fetched**. So all eight
items are filed **LOCATOR-VERIFIED** (canonical URL + verbatim text + hashed transcript), pending a
separate open-egress `capture.sh --promote` run. (Contrast the `x-bot-swarm` packet, which was built
full-egress and reached VERIFIED in place.)

## Custody states

| State | Meaning |
|---|---|
| `LOCATOR-VERIFIED` | Canonical URL + verbatim text preserved as a hashed transcript; original-form bytes not yet held. |
| `VERIFIED` | Original artifact (WARC/PDF/screenshot) hashed into `<id>/original/manifest.json`. Full VERIFIED also requires a second custodian + off-platform backup (committing `original/` here is one custodian). |

## Run it (from an open-egress environment)

```bash
cd cases/prediction-markets/evidence
./capture.sh --promote --archive-org
```

The script auto-detects Chromium, including **Playwright's bundled build**
(`$PLAYWRIGHT_BROWSERS_PATH/chromium-*/chrome-linux/chrome`), so it works on Claude Code web/CI
images without installing a system Chrome. `wget` produces the WARC; Chromium produces PDF + PNG.

Per the repo `.gitignore`, only the small integrity records (`manifest.json`, `sha256sums.txt`,
`archive-org-snapshots.txt`) are committed; the large binaries (WARC/HTML/PDF/PNG) are kept in
off-platform custody, which doubles as the manifest's required second custodian.

## Priority captures (the underlying primaries)

- `vandyke-venezuela-insider-bet-2026` — capture the **DOJ release** and the **indictment** directly (P1).
- `cftc-withdraws-political-sports-ban-2026` — capture the **CFTC notice** and **Federal Register 2026-05105** directly (P1).
- `trump-cftc-thrive-post-2026` — capture the **Truth Social post** itself (P1), plus outlet corroboration.
- `fed-staff-forecast-accuracy` — **PENDING-PRIMARY**: locate and capture the **Federal Reserve staff finding/working paper** (Gap Register Priority 28(b)); the TS Imagine secondary is not sufficient.

## Allowlist for this case

For **Custom** network access (Claude Code web) — covers every source cited across this packet's
evidence items. `*.` is a wildcard subdomain match.

```
justice.gov
*.justice.gov
cnbc.com
*.cnbc.com
nbcnews.com
*.nbcnews.com
pbs.org
*.pbs.org
cnn.com
*.cnn.com
frontofficesports.com
theblock.co
cryptobriefing.com
aol.com
*.aol.com
cryptotimes.io
thehill.com
coindesk.com
slate.com
npr.org
*.npr.org
corporatecomplianceinsights.com
ropesgray.com
*.ropesgray.com
cftc.gov
*.cftc.gov
federalregister.gov
tsimagine.com
web.archive.org
```

> **Custom vs Full is a real security decision.** A `Full`-egress agent can reach any host; for a
> morally-hot case prefer `Custom` limited to exactly these sources.

## Honest-custody note

Several sources here are dynamic news sites; the WARC/PDF/PNG may capture a paywall/interstitial
shell rather than the rendered article. Where that occurs, the verbatim text is preserved in
`transcript.md` (hashed) and corroborated by the other outlets cited for the same item — no grade is
inflated on the strength of a single shell artifact. The `fed-staff-forecast-accuracy` item is the
one item not web-confirmed this session and is held at PENDING-PRIMARY regardless of capture state.
