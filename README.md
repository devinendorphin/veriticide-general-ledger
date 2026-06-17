# Veriticide Master Ledger

Documentation infrastructure for Track A of the Standing Protocol — automated capture of institutional harm laundering across policy, government, and media sources.

---

## What this collects

- **Cicero Institute** — all research publications and news releases
- **Federal government** — HUD press releases, SAMHSA, CDC newsroom
- **Twitter/X** — specified accounts, filtered by keywords (homeless, encampment, drug policy, care framing, etc.)
- Add any URL to `scraper/config.yaml` to include it

---

## First-time setup

```bash
bash scripts/setup.sh
```

---

## Running the collector

**With auto-formatting (requires Claude API key):**
```bash
cd scraper
ANTHROPIC_API_KEY=sk-ant-... python3 scraper.py
```

**Without API key (captures raw text, format later by pasting into chat):**
```bash
cd scraper
python3 scraper.py
```

**Web sources only (skip Twitter):**
```bash
python3 scraper.py --web-only
```

**Test run (prints entries, does not write to ledger):**
```bash
python3 scraper.py --dry-run
```

---

## Output

Formatted entries are appended to `ledger/ledger.md`.

The tool tracks what it has already captured in `ledger/.seen_hashes.txt` — re-running will only add new items.

---

## Adding sources

Edit `scraper/config.yaml`:

- Add Twitter accounts under `twitter.accounts`
- Add keywords under `twitter.keywords`
- Add websites under `web_sources`

---

## Getting a Claude API key (for auto-formatting)

The API requires **purchased credits** — there is no free tier.

1. Go to console.anthropic.com
2. Create an account
3. Add credits (minimum purchase applies — check console for current amounts)
4. API Keys → Create Key

**Cost estimate**: The tool uses Claude Haiku, the cheapest available model ($1.00 per million input tokens / $5.00 per million output tokens). A typical formatted entry uses roughly 500–1000 tokens. At that rate, $5 of credits formats approximately 5,000–10,000 entries.

**No API key**: The tool still runs without one — it captures raw text and leaves fields 4 and 5 blank with a `[PENDING]` marker. You can then paste those raw entries here for manual formatting.

---

## Framework documents

| Document | Purpose |
|---|---|
| Declaration on Veriticide v0.1 | Definitional foundation |
| Draft Convention on Veriticide v0.2 | Legal instrument |
| Veriticide Stack Tier Taxonomy v0.1 | Tiered harm classification |
| Documentation & Standing Protocol v0.1 | This ledger's operating protocol |
| Reflexivity Clause v0.1 | Interested dismissal as self-referential instance |
