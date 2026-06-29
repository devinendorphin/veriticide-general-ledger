#!/usr/bin/env python3
"""
Veriticide Master Ledger — automated collector.

Usage:
    python scraper.py                   # run all sources
    python scraper.py --web-only        # skip Twitter
    python scraper.py --twitter-only    # skip web sources
    python scraper.py --dry-run         # print entries, don't write to ledger
"""

import argparse
import hashlib
from datetime import datetime, timezone
from pathlib import Path

import yaml

from formatter import format_entry
from sources.twitter import scrape_twitter
from sources.web import scrape_source

CONFIG_PATH = Path(__file__).parent / "config.yaml"


def load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def load_seen(seen_path: Path) -> set:
    if not seen_path.exists():
        return set()
    return set(seen_path.read_text().splitlines())


def save_seen(seen_path: Path, seen: set) -> None:
    seen_path.write_text("\n".join(sorted(seen)))


def item_hash(item: dict) -> str:
    key = item.get("url", "") + item.get("text", "")[:200]
    return hashlib.sha256(key.encode()).hexdigest()[:16]


_COLLECTION_HEADER = (
    "\n\n---\n\n"
    "## APPENDIX A — CONTINUOUS COLLECTION (SCRAPER ARCHIVE)\n\n"
    "*Auto-formatted entries from scraper runs, appended in capture order. "
    "Each entry follows the Track A format. Entries here are unreviewed — "
    "raw formatter output. Promote to the relevant cluster in Section II "
    "once reviewed and confirmed.*\n\n"
    "---\n"
)


def append_to_ledger(ledger_path: Path, entry: str) -> None:
    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    if not ledger_path.exists():
        ledger_path.write_text(
            "# Veriticide Master Ledger\n\n"
            "_Auto-collected entries. See Documentation & Standing Protocol v0.1._\n"
            + _COLLECTION_HEADER + "\n"
        )
    elif "CONTINUOUS COLLECTION" not in ledger_path.read_text():
        with open(ledger_path, "a") as f:
            f.write(_COLLECTION_HEADER + "\n")
    with open(ledger_path, "a") as f:
        f.write(entry + "\n")


def _build_manifest(stats: dict) -> str:
    ts = stats["run_ts"]
    mode = stats["mode"]

    lines = [
        "SCRAPER RUN MANIFEST",
        f"Run timestamp: {ts}",
        f"Mode: {mode}",
        "",
    ]

    web = stats.get("web")
    if web is not None:
        sources = web["sources"]
        ok = [s for s in sources if s["status"] == "ok"]
        failed = [s for s in sources if s["status"] != "ok"]
        lines.append(f"WEB SOURCES ({len(sources)} configured, {len(ok)} succeeded, {len(failed)} failed)")
        for s in ok:
            lines.append(f"  {s['name']}: {s['fetched']} item(s) fetched")
        for s in failed:
            lines.append(f"  FAILED — {s['name']}: {s['status']}")
        lines.append("")

    tw = stats.get("twitter")
    if tw is not None:
        accounts = tw["account_stats"]
        keywords = tw["keywords"]
        ok_accts = [a for a in accounts if a["status"] == "ok"]
        failed_accts = [a for a in accounts if a["status"] != "ok"]
        lines.append(
            f"TWITTER ({len(accounts)} accounts configured, "
            f"{len(keywords)} keywords, "
            f"max {tw['max_tweets_per_account']} tweets/account)"
        )
        for a in ok_accts:
            lines.append(f"  @{a['handle']}: {a['fetched']} fetched, {a['matched']} matched keywords")
        for a in failed_accts:
            lines.append(f"  FAILED — @{a['handle']}: {a['status']}")
        lines.append("")

    dedup = stats["dedup"]
    lines += [
        "DEDUPLICATION",
        f"  Total items fetched this run: {dedup['fetched']}",
        f"  Already in record (deduplicated): {dedup['deduped']}",
        f"  New items added: {dedup['added']}",
        "",
        "SELECTION DISCIPLINE NOTE",
        "  This record captures configured sources only (non-random selection).",
        "  Counter-evidence and NULL/CONTROL logs are not a byproduct of this",
        "  capture method — they require deliberate entry. See High-Variance",
        "  Account Method and the Reflexivity Clause for the required practice.",
    ]

    body = "\n".join(lines)
    return f"\n---\n\n{body}\n\n---\n"


def run(web: bool = True, twitter: bool = True, dry_run: bool = False) -> None:
    cfg = load_config()
    settings = cfg.get("settings", {})
    run_ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    ledger_path = (Path(__file__).parent / settings["ledger_file"]).resolve()
    seen_path = (Path(__file__).parent / settings["seen_file"]).resolve()

    seen = load_seen(seen_path)
    new_seen = set()
    total_new = 0
    items = []

    stats: dict = {
        "run_ts": run_ts,
        "mode": ("web+twitter" if (web and twitter) else ("web-only" if web else "twitter-only")),
        "dedup": {"fetched": 0, "deduped": 0, "added": 0},
    }

    if web:
        print("\n[web] Collecting web sources...")
        web_sources_stats = []
        for source_cfg in cfg.get("web_sources", []):
            print(f"  Scraping: {source_cfg['name']}")
            try:
                results = scrape_source(source_cfg)
                print(f"  Found {len(results)} item(s)")
                items.extend(results)
                web_sources_stats.append({"name": source_cfg["name"], "fetched": len(results), "status": "ok"})
            except Exception as e:
                print(f"  ERROR: {e}")
                web_sources_stats.append({"name": source_cfg["name"], "fetched": 0, "status": f"ERROR: {e}"})
        stats["web"] = {"sources": web_sources_stats}

    if twitter:
        print("\n[twitter] Collecting Twitter sources...")
        twitter_cfg = cfg.get("twitter", {})
        try:
            twitter_items, account_stats = scrape_twitter(twitter_cfg)
            print(f"  Found {len(twitter_items)} tweet(s) matching keywords")
            items.extend(twitter_items)
        except Exception as e:
            print(f"  ERROR: {e}")
            twitter_items, account_stats = [], []
        stats["twitter"] = {
            "account_stats": account_stats,
            "keywords": twitter_cfg.get("keywords", []),
            "max_tweets_per_account": twitter_cfg.get("max_tweets_per_account", 10),
        }

    stats["dedup"]["fetched"] = len(items)

    print(f"\n[formatter] Processing {len(items)} total item(s)...")
    deduped = 0
    for item in items:
        h = item_hash(item)
        if h in seen:
            deduped += 1
            continue

        entry = format_entry(item)

        if dry_run:
            print("\n" + "=" * 60)
            print(entry)
        else:
            append_to_ledger(ledger_path, entry)

        new_seen.add(h)
        total_new += 1

    stats["dedup"]["deduped"] = deduped
    stats["dedup"]["added"] = total_new

    if not dry_run:
        seen.update(new_seen)
        save_seen(seen_path, seen)
        append_to_ledger(ledger_path, _build_manifest(stats))

    print(f"\nDone. {total_new} new entry/entries added to ledger.")
    if not dry_run and total_new > 0:
        print(f"Ledger: {ledger_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Veriticide Ledger Collector")
    parser.add_argument("--web-only", action="store_true")
    parser.add_argument("--twitter-only", action="store_true")
    parser.add_argument("--dry-run", action="store_true", help="Print without saving")
    args = parser.parse_args()

    run(
        web=not args.twitter_only,
        twitter=not args.web_only,
        dry_run=args.dry_run,
    )
