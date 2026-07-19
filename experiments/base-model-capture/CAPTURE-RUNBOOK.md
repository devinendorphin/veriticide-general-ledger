# CAPTURE RUNBOOK — Phase 0.1: davinci-002 / babbage-002

**Perishable capture only.** This preserves raw model outputs — per-token logprobs and
echo-scored logprobs of provided text — with hashes and a manifest. It does no
classification and carries no framework language (Phase 0 rule). What gets probed is
entirely in your `probes.yaml`; keep it neutral.

## Why this has a hard deadline

`/v1/completions` is the only OpenAI interface that exposes **logprobs + echo** on these
GPT-3-class base models, and it is scheduled to close **2026-09-28**. After that the
measurements below cannot be reproduced from the models. Capture before then, and back
up `raw/` off-platform the same day — unlike the 1.4 primaries, these outputs are **not
re-fetchable**: a closed endpoint (and non-deterministic sampling) means a lost `raw/`
is lost for good. The manifest hashes prove integrity; they cannot regenerate the bytes.

## What gets captured

Per (model × probe × iteration), the full API response is written to
`raw/<model>/<probe_id>__itNN.json`, wrapped with the exact request, selected response
headers (incl. `x-request-id`, `openai-version`), and sha256 of both request and
response body.

- **generate** probes: the model samples a continuation; top-5 logprobs on generated tokens.
- **score** probes: `echo=true`, `max_tokens=0` — the provided text is returned tokenized
  with per-token logprobs and top-5 alternatives, generating nothing. This is the classic
  way to measure the model's probability of a fixed string.

## Run it

```bash
cd experiments/base-model-capture
pip install -r requirements.txt

# 1. Author your probe set (neutral — Phase 0). Start from the example:
cp probes.example.yaml probes.yaml   # then edit; freeze before the budgeted run
python capture.py --dry-run          # prints every request, makes NO API calls — inspect first

# 2. Real capture (needs a key). config.yaml + probes.yaml are hashed into every record.
export OPENAI_API_KEY=sk-...          # (optional) export OPENAI_ORG=org-...
python capture.py                     # resumable; re-run to continue after an interruption

# 3. Fold the append log into a hashed manifest + re-verify files on disk:
python build_manifest.py              # writes manifest.json + sha256sums.txt (commit these)
```

## Custody

- `raw/` and `run-manifest.jsonl` are **git-ignored** (raw bytes never go in the repo).
- `manifest.json` + `sha256sums.txt` are the **committed** durable record (hashes + provenance).
- Custody state starts **HASHED-PENDING-BACKUP**. To reach VERIFIED:
  1. **Off-platform backup of `raw/`** — one-time `brew install rclone && rclone config` (make a
     `gdrive` remote), then just `./backup-to-drive.sh` (copies `raw/` + manifest to
     `gdrive:veriticide-evidence/0.1-base-model-capture`, alongside the 1.4 evidence). Do this
     immediately after capture.
  2. A **second independent custodian** of the raw bytes.
- Because the endpoint is closing, treat the off-platform copy as the primary artifact and
  this repo's manifest as the integrity index over it.

## Notes / knobs

- `logprobs` is capped at 5 by the API; the harness enforces this.
- `seed` is recorded for provenance but legacy base models may ignore it; for distributional
  capture raise `temperature` and `iterations_per_probe` instead of relying on seed.
- 429/5xx are retried with exponential backoff; other 4xx stop immediately (a bad request
  will not fix itself). A run halted near the deadline resumes cleanly (dedup by request hash).
