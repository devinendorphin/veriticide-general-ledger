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
import os
import sys
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


def append_to_ledger(ledger_path: Path, entry: str) -> None:
    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    if not ledger_path.exists():
        ledger_path.write_text(
            "# Veriticide Master Ledger\n\n"
            "_Auto-collected entries. See Documentation & Standing Protocol v0.1._\n\n"
        )
    with open(ledger_path, "a") as f:
        f.write(entry + "\n")


def run(web: bool = True, twitter: bool = True, dry_run: bool = False) -> None:
    cfg = load_config()
    settings = cfg.get("settings", {})

    ledger_path = (Path(__file__).parent / settings["ledger_file"]).resolve()
    seen_path = (Path(__file__).parent / settings["seen_file"]).resolve()

    seen = load_seen(seen_path)
    new_seen = set()
    total_new = 0

    items = []

    if web:
        print("\n[web] Collecting web sources...")
        for source_cfg in cfg.get("web_sources", []):
            print(f"  Scraping: {source_cfg['name']}")
            try:
                results = scrape_source(source_cfg)
                print(f"  Found {len(results)} item(s)")
                items.extend(results)
            except Exception as e:
                print(f"  ERROR: {e}")

    if twitter:
        print("\n[twitter] Collecting Twitter sources...")
        try:
            twitter_items = scrape_twitter(cfg.get("twitter", {}))
            print(f"  Found {len(twitter_items)} tweet(s) matching keywords")
            items.extend(twitter_items)
        except Exception as e:
            print(f"  ERROR: {e}")

    print(f"\n[formatter] Processing {len(items)} total item(s)...")
    for item in items:
        h = item_hash(item)
        if h in seen:
            continue

        entry = format_entry(item)

        if dry_run:
            print("\n" + "=" * 60)
            print(entry)
        else:
            append_to_ledger(ledger_path, entry)

        new_seen.add(h)
        total_new += 1

    if not dry_run:
        seen.update(new_seen)
        save_seen(seen_path, seen)

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
