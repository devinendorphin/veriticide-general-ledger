#!/usr/bin/env python3
"""
Veriticide Master Ledger — automated collector.

Usage:
    python scraper.py                   # run all sources
    python scraper.py --web-only        # skip Twitter
    python scraper.py --twitter-only    # skip web sources
    python scraper.py --dry-run         # print, don't write anything

Pipeline, and what each stage is allowed to assert:

    sources/  -> a capture: full bytes where obtainable, a labelled derivative
                 text layer, and a named gap wherever something was not obtained.
    capture   -> an evidence record under a content-version identity, written to
                 the capture store. No classification, no custody band.
    formatter -> a DRAFT analysis, written to a separate draft store, carrying
                 the layer and character ranges it was shown and whether any
                 prior-record search was performed.
    ledger    -> an Appendix A block that points at both and states the analysis
                 status. It never presents an unvalidated draft as an entry.

Analysis is never written into the evidence store, and evidence is never
inferred from analysis.
"""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml

import capture as capture_mod
import validate as validate_mod
from formatter import analyze_capture, render_draft, render_ledger_block

CONFIG_PATH = Path(__file__).parent / "config.yaml"


def load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def load_index(index_path: Path) -> dict:
    """content_version_id -> minimal record of a capture already collected."""
    if not index_path.exists():
        return {}
    try:
        return json.loads(index_path.read_text()).get("captures", {})
    except (json.JSONDecodeError, OSError):
        print(f"  [index] unreadable index at {index_path}; treating as empty")
        return {}


def save_index(index_path: Path, index: dict) -> None:
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text(json.dumps(
        {"schema": "veriticide.capture-index/1", "captures": index}, indent=2, sort_keys=True
    ) + "\n")


def load_legacy_seen(seen_path: Path) -> set:
    """
    The superseded prefix-key seen-file.

    Kept only so that migrating to content-version identity does not re-emit the
    whole historical corpus. See `decide` for the bounded role it retains.
    """
    if not seen_path or not seen_path.exists():
        return set()
    return set(x for x in seen_path.read_text().splitlines() if x.strip())


def decide(item: dict, index: dict, indexed_url_ids: set, legacy_seen: set) -> tuple:
    """
    Return (action, content_version_id, source_url_id).

    action is one of:
      "emit"              — not collected before under content-version identity
      "seen"              — this exact content version is already in the record
      "legacy-suppressed" — a different content version, but its legacy prefix
                            key was already emitted and this source has no
                            content-version history yet. Suppressed once so the
                            migration does not re-emit the corpus, recorded in
                            the index, and reported in the run manifest. Once a
                            source has any indexed version, legacy keys no longer
                            suppress it, so a later revision of that source is
                            emitted as the distinct version it is.
    """
    cvid = capture_mod.content_version_id(item)
    url_id = capture_mod.source_url_id(item.get("url", ""))
    if cvid in index:
        return "seen", cvid, url_id
    if url_id in indexed_url_ids:
        return "emit", cvid, url_id
    if capture_mod.legacy_item_hash(item) in legacy_seen:
        return "legacy-suppressed", cvid, url_id
    return "emit", cvid, url_id


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
        "DEDUPLICATION (content-version identity over complete captured material)",
        f"  Total items fetched this run: {dedup['fetched']}",
        f"  Already in record, same content version: {dedup['seen']}",
        f"  New items added: {dedup['added']}",
        f"  Suppressed by the superseded prefix key: {dedup['legacy_suppressed']}",
    ]
    for row in stats.get("legacy_suppressed_items", []):
        lines.append(f"    - {row['url']} (version {row['content_version_id']})")
    if stats.get("legacy_suppressed_items"):
        lines.append(
            "    These items were withheld because the superseded url+200-character"
        )
        lines.append(
            "    key had already emitted something for that source. That key cannot"
        )
        lines.append(
            "    distinguish a revision from the text it revised, so a correction may"
        )
        lines.append(
            "    be among them. They are now indexed under content-version identity;"
        )
        lines.append(
            "    any later revision of these sources will be emitted as a distinct"
        )
        lines.append("    version.")
    lines.append("")

    cap = stats["capture"]
    lines += [
        "CAPTURE LAYERS AND COMPLETENESS",
        f"  Captures with original-form bytes held: {cap['with_original']}",
        f"  Captures with NO original-form bytes: {cap['without_original']}",
    ]
    for layer, count in sorted(cap["layers"].items()):
        lines.append(f"  Analysis-text layer {layer}: {count}")
    if cap["gap_counts"]:
        lines.append("  Recorded capture gaps:")
        for gap, count in sorted(cap["gap_counts"].items(), key=lambda kv: -kv[1])[:10]:
            lines.append(f"    {count}x {gap[:150]}")
    lines.append("")

    an = stats["analysis"]
    lines += [
        "ANALYSIS (drafts, unreviewed)",
        f"  Provider/model: {an['provider']}/{an['model']}",
        f"  Drafts complete (structurally valid, still unreviewed): {an['complete']}",
        f"  Drafts incomplete or invalid: {an['incomplete']}",
        f"  Captures with no analysis performed: {an['none']}",
        f"  Prior-record retrieval performed: {'yes' if an['retrieval_performed'] else 'no'}",
        "",
        "COUNTER-EVIDENCE NOTE",
        "  No cross-record retrieval was performed for any capture in this run.",
        "  Drafts therefore report RETRIEVAL NOT PERFORMED rather than NONE ON",
        "  RECORD. Absence of cited counter-evidence in this run is absence of a",
        "  search, not evidence that no counter-evidence exists.",
        "",
        "SELECTION DISCIPLINE NOTE",
        "  This record captures configured sources only (non-random selection).",
        "  Counter-evidence and NULL/CONTROL logs are not a byproduct of this",
        "  capture method — they require deliberate entry. See High-Variance",
        "  Account Method and the Reflexivity Clause for the required practice.",
        "",
        "CUSTODY NOTE",
        "  No custody band was assigned or promoted by this run. Automated capture",
        "  hashes what it received; custody is adjudicated by the case-level",
        "  process (docs/custody-status-2026-07-02.md).",
    ]

    body = "\n".join(lines)
    return f"\n---\n\n{body}\n\n---\n"


def run(web: bool = True, twitter: bool = True, dry_run: bool = False) -> dict:
    cfg = load_config()
    settings = cfg.get("settings", {})
    run_ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    here = Path(__file__).parent

    ledger_path = (here / settings["ledger_file"]).resolve()
    index_path = (here / settings.get("capture_index", "../ledger/.capture-index.json")).resolve()
    capture_store = (here / settings.get("capture_store", "../ledger/captures")).resolve()
    draft_store = (here / settings.get("draft_store", "../ledger/drafts")).resolve()
    legacy_seen_path = (here / settings["seen_file"]).resolve() if settings.get("seen_file") else None

    index = load_index(index_path)
    indexed_url_ids = {rec.get("source_url_id") for rec in index.values()}
    legacy_seen = load_legacy_seen(legacy_seen_path)
    items = []

    stats: dict = {
        "run_ts": run_ts,
        "mode": ("web+twitter" if (web and twitter) else ("web-only" if web else "twitter-only")),
        "dedup": {"fetched": 0, "seen": 0, "added": 0, "legacy_suppressed": 0},
        "legacy_suppressed_items": [],
        "capture": {"with_original": 0, "without_original": 0, "layers": {}, "gap_counts": {}},
        "analysis": {"complete": 0, "incomplete": 0, "none": 0,
                     "provider": "none", "model": "none", "retrieval_performed": False},
    }

    if web:
        from sources.web import scrape_source
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
        from sources.twitter import scrape_twitter
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
    print(f"\n[capture] Processing {len(items)} total item(s)...")

    for item in items:
        action, cvid, url_id = decide(item, index, indexed_url_ids, legacy_seen)

        if action == "seen":
            stats["dedup"]["seen"] += 1
            continue

        if action == "legacy-suppressed":
            stats["dedup"]["legacy_suppressed"] += 1
            stats["legacy_suppressed_items"].append(
                {"url": item.get("url", ""), "content_version_id": cvid}
            )
            index[cvid] = {
                "source_url_id": url_id,
                "url": item.get("url", ""),
                "first_seen": run_ts,
                "emitted": False,
                "note": "suppressed once during migration from the prefix key; not analyzed",
            }
            indexed_url_ids.add(url_id)
            continue

        record = (
            capture_mod.write_capture(capture_store, item) if not dry_run
            else capture_mod.build_capture_record(item)
        )

        cap = stats["capture"]
        cap["with_original" if record["raw_original_held"] else "without_original"] += 1
        layer = record["analysis_text_layer"]
        cap["layers"][layer] = cap["layers"].get(layer, 0) + 1
        for gap in record["capture_gaps"]:
            cap["gap_counts"][gap] = cap["gap_counts"].get(gap, 0) + 1

        result = analyze_capture(record, item.get("text", ""), settings=settings)
        an = stats["analysis"]
        an["provider"], an["model"] = result.provider, result.model
        an["retrieval_performed"] = an["retrieval_performed"] or result.retrieval_performed
        if result.complete:
            an["complete"] += 1
        elif result.status == validate_mod.STATUS_NO_ANALYSIS:
            an["none"] += 1
        else:
            an["incomplete"] += 1

        if not dry_run and result.draft_text:
            draft_store.mkdir(parents=True, exist_ok=True)
            draft_path = draft_store / f"{record['item_id']}.md"
            draft_path.write_text(render_draft(record, result), encoding="utf-8")
            record["draft_path"] = str(draft_path)

        block = render_ledger_block(record, result)
        if dry_run:
            print("\n" + "=" * 60)
            print(block)
        else:
            append_to_ledger(ledger_path, block)

        index[cvid] = {
            "source_url_id": url_id,
            "url": item.get("url", ""),
            "first_seen": run_ts,
            "emitted": True,
            "analysis_status": result.status,
        }
        indexed_url_ids.add(url_id)
        stats["dedup"]["added"] += 1

    if not dry_run:
        save_index(index_path, index)
        append_to_ledger(ledger_path, _build_manifest(stats))

    print(f"\nDone. {stats['dedup']['added']} new capture(s) recorded.")
    if stats["dedup"]["legacy_suppressed"]:
        print(f"  {stats['dedup']['legacy_suppressed']} item(s) suppressed by the "
              "superseded prefix key — see the run manifest.")
    if not dry_run and stats["dedup"]["added"] > 0:
        print(f"Ledger: {ledger_path}")
        print(f"Capture store: {capture_store}")
        print(f"Draft store: {draft_store}")
    return stats


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
