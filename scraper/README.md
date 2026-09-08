# Collector

Automated capture for Appendix A of `ledger/ledger.md`. Captures evidence,
optionally requests a draft analysis, and keeps the two apart.

## Running it

```bash
pip install -r requirements.txt
python3 scraper.py --dry-run      # print, write nothing
python3 scraper.py --web-only     # skip Twitter
python3 scraper.py                # all configured sources
```

Offline by default. `settings.model.provider` in `config.yaml` is `none`, so a
run captures and requests no analysis. Set it to `anthropic` (with
`ANTHROPIC_API_KEY` in the environment) to enable drafts; without the key it
falls back to `none` rather than failing the run. `VERITICIDE_MODEL_PROVIDER`,
`VERITICIDE_MODEL`, and `VERITICIDE_MODEL_MAX_TOKENS` override the file.

## What a run writes

| Path | Contents | Tracked |
|---|---|---|
| `ledger/captures/<source>/<version>/` | `capture.json`, `extracted.txt`, `original/manifest.json`, `original/sha256sums.txt` | yes |
| `ledger/captures/<source>/<version>/original/*` | raw served bytes | no (case-evidence convention) |
| `ledger/drafts/<item_id>.md` | model draft, with its status and validation problems | yes |
| `ledger/ledger.md` | one Appendix A block per capture, plus a run manifest | yes |
| `ledger/.capture-index.json` | content-version dedup index | no |

Evidence is never written to the draft store and analysis is never written to
the capture store.

## What the collector may and may not assert

- It hashes what it received. It **does not assign a custody band**;
  `custody_state` in every capture record is `null`. Bands come from the
  case-level process (`docs/custody-status-2026-07-02.md`).
- It labels the layer it stored: raw original, extracted text, feed summary, or
  platform field. A derivative is not the original and the record says which it
  is holding.
- It declares the character ranges supplied to any analyst, and names the
  omitted ones. An unread range is unknown, not absent.
- It performs **no cross-record retrieval**. Every draft reports
  `RETRIEVAL NOT PERFORMED`. Absence of cited counter-evidence is absence of a
  search, not absence of counter-evidence.
- A draft that is interrupted, structurally incomplete, or cites an entry
  reference it was not shown is marked incomplete and is not a ledger entry.
- Captured text is delimited evidence. Instructions inside a capture are
  analyzed as institutional language and authorize nothing.

## Files

| File | Role |
|---|---|
| `capture.py` | identity, layer labels, coverage accounting, capture store |
| `model_adapter.py` | provider seam; `NullAdapter` / `AnthropicAdapter` / `FakeAdapter` |
| `validate.py` | draft validation: completion, required sections, citations, retrieval state |
| `formatter.py` | the protocol system prompt, the request, and draft/ledger rendering |
| `scraper.py` | orchestration, deduplication, run manifest |
| `sources/` | web (article + feed) and Twitter collection |

## Tests

```bash
python3 -m unittest discover -s scraper/tests -t scraper
```

Offline, standard library only, synthetic fixtures and fake model clients. They
make no network call and no paid call. They establish that the named defects are
closed; they do not certify that any model's analysis is sound.

Background and boundaries: `docs/capture-repair-2026-09-08.md`.
