# CAPTURE RUNBOOK — turning LOCATOR-VERIFIED into VERIFIED

*How to perform original-form preservation of this case's evidence from an open-egress
environment. Companion to `capture.sh`, `README.md`, and `../05-custody-manifest.md`.*

---

## Why this exists

Every item in `evidence/` is currently **`LOCATOR-VERIFIED`** (canonical URL + verbatim text +
integrity hash) but **not `VERIFIED`** (original bytes: WARC / PDF / screenshot / video +
headers). The environment the packet was built in runs the default **Trusted** network policy,
which blocks outbound fetches to news/source hosts (`curl archive.org` and `WebFetch` of source
pages return `403` from the egress proxy). Original-form capture therefore has to run somewhere
with **open egress**. This runbook is that procedure, so it travels with the repo instead of
living in a chat log.

---

## Option A — A Claude Code web environment with looser network access (recommended)

Claude Code web environments have four network-access levels: **None**, **Trusted** *(default —
what blocked us)*, **Full** *(any domain)*, **Custom** *(your own allowlist)*.

1. At **claude.ai/code**, click the **cloud icon** (it appears wherever you start a cloud session
   or configure a routine — there is no separate "Environments" page).
2. **Create a new environment** (keep the restricted one as-is) or open one for editing.
3. In the dialog, use the **Network access** selector and choose **Custom** (recommended) or
   **Full** (simplest).
4. For **Custom**: an **Allowed domains** field appears — paste the [allowlist](#allowlist-for-this-case)
   below, one domain per line, and tick **"Also include default list of common package managers"**
   so git/python keep working.
5. Start a session in that environment and run:
   ```bash
   cd cases/doge-usaid-pepfar/evidence
   ./capture.sh --promote --archive-org
   ```

> **Custom vs Full is a real security decision.** A `Full`-egress agent session can reach *any*
> host; for a morally-hot case file, `Custom` limits the agent to exactly this case's sources.
> Prefer `Custom`.
>
> Claude Code on the web is a research preview for Pro/Max/Team (and Enterprise premium seats);
> if the network selector isn't visible, that is the gating.

---

## Option B — A throwaway cloud VM (neutral IP / unattended runs)

Open egress is the **default** on a normal VM — you don't configure anything to get it.

```bash
# 1. Create a small Ubuntu VM (DigitalOcean / Hetzner / AWS EC2 / GCP), smallest tier.
# 2. SSH in, install tools:
sudo apt-get update && sudo apt-get install -y wget git python3 chromium-browser curl
sudo snap install yt-dlp 2>/dev/null || pipx install yt-dlp || pip3 install yt-dlp

# 3. Clone, capture, push:
git clone https://github.com/devinendorphin/veriticide-general-ledger
cd veriticide-general-ledger/cases/doge-usaid-pepfar/evidence
./capture.sh --promote --archive-org
git add -A && git commit -m "Original-form capture (VERIFIED)" && git push

# 4. Destroy the VM when done.
```

---

## Option C — Your own laptop/desktop

The simplest of all. A normal computer has open egress by default. Install `wget`, a
Chrome/Chromium, and `yt-dlp`, then run `./capture.sh --promote --archive-org` from this
directory. (On macOS: `brew install wget yt-dlp` and use the installed Google Chrome.)

---

## Allowlist for this case

For **Custom** network access (Option A) — covers every source cited across the 14 evidence
items. `*.` is a wildcard subdomain match.

```
x.com
doge.gov
web.archive.org
archive.org
*.washingtonpost.com
*.propublica.org
*.npr.org
*.democracynow.org
*.senate.gov
*.house.gov
*.cato.org
*.pbs.org
*.cbsnews.com
abcnews.go.com
*.thehill.com
*.aljazeera.com
theintercept.com
*.cnn.com
*.nytimes.com
*.fortune.com
citizensforethics.org
*.hrw.org
*.cgdev.org
thedispatch.com
*.kff.org
*.unaids.org
*.nih.gov
*.medrxiv.org
*.ucla.edu
*.oxfam.org
*.wfp.org
*.nbcnews.com
*.newsweek.com
```

---

## What a run produces

Per item, under `evidence/<id>/original/`:

- `*.warc` — full request/response incl. headers (the forensic artifact)
- `*.pdf`, `*.png` — human-readable + visual proof (headless Chrome)
- `*.mp4` — video items (Democracy Now / YouTube), via `yt-dlp`
- `manifest.json`, `sha256sums.txt` — SHA-256 of every artifact (the integrity record)
- `archive-org-snapshots.txt` — third-party Internet Archive snapshot URLs (with `--archive-org`)

With `--promote`, each successfully-captured item's `capture.json` flips to `custody_state:
VERIFIED` and `build-custody-index.py` regenerates `custody-index.md`.

---

## Completing true VERIFIED status (two manual conditions)

`capture.sh` preserves bytes and hashes; it does **not** by itself satisfy the full manifest
definition of `VERIFIED`, which also requires:

1. **A second custodian** — committing `original/` to this repo is one custodian; add a second
   (another person/org, or a separate archive). The `--archive-org` snapshots help here.
2. **Off-platform backup** — at least one copy outside any system controlled by the institutions
   being documented.

A bare `capture.sh` run never sets `VERIFIED` (no overclaiming). Promotion is an explicit choice
(`--promote`), and even then you should confirm conditions 1–2 before treating an item as
tribunal-grade.

---

## Git / size note

Original artifacts are large binaries (WARC, video). The **integrity record**
(`original/manifest.json` + `original/sha256sums.txt`) is small and should always be committed.
Commit the binaries deliberately, or keep them in off-platform custody (which doubles as the
"second custodian"). To force-commit one ignored artifact:
`git add -f cases/doge-usaid-pepfar/evidence/<id>/original/<file>`.

---

## What open egress still cannot get

The two deepest primaries — the **actual Tamlyn cable** and the **underlying ProPublica internal
memos** — are not public artifacts. `capture.sh` forensically preserves the outlets'
*reproductions*; the originals behind them require FOIA, a litigation subpoena, or a source.
This is exactly why those items are graded **`S1 + embedded P1 (pending)`** in
`custody-index.md` rather than held P1 — and that grade should not be promoted on the strength of
original-form capture of the *reporting* alone.
