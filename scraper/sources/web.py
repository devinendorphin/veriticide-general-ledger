"""
Web collection.

Two layers are produced here and never conflated:

- raw_original: the bytes the source host served, preserved whole and hashed.
- a derivative text layer: either extracted_text (a DOM selection rendered to
  text) or feed_summary (the publisher's own summary field, which is not the
  article body and routinely omits corrections and qualifications).

Nothing is truncated. The previous collector clipped extracted article text at
4,000 characters, which removed later corrections from the record with no mark
in the output that anything had been removed. Where content genuinely could not
be obtained, the failure is recorded on the item as a capture gap rather than
being represented as short content.
"""

import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from capture import LAYER_EXTRACTED_TEXT, LAYER_FEED_SUMMARY

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}

MIN_ARTICLE_CHARS = 80


def scrape_source(source_cfg: dict) -> list[dict]:
    src_type = source_cfg.get("type", "article_list")
    if src_type == "rss":
        return _scrape_rss(source_cfg)
    return _scrape_article_list(source_cfg)


def _first(item, ns: dict, *paths):
    """
    First matching child element, or None.

    Selected explicitly rather than with `or`. An ElementTree element with no
    children is falsy, so an `or` chain over `find()` results discards exactly
    the elements this feed parser needs — an ordinary RSS <description> with no
    child elements evaluates false and the chain falls through to None. The
    item is then dropped for having "no text", and the run manifest reports the
    source as succeeding with zero items. Every RSS source in config.yaml was
    silently yielding nothing; a source that returns nothing must not be
    indistinguishable from a source with nothing to return.
    """
    for path in paths:
        found = item.find(path, ns) if ":" in path else item.find(path)
        if found is not None:
            return found
    return None


def _scrape_rss(cfg: dict) -> list[dict]:
    results = []
    rss_url = cfg.get("rss_url", cfg["url"])
    try:
        resp = requests.get(rss_url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        feed_bytes = resp.content
        root = ET.fromstring(feed_bytes)
    except Exception as e:
        print(f"  [rss] failed to fetch {rss_url}: {e}")
        return []

    ns = {"atom": "http://www.w3.org/2005/Atom"}
    items = root.findall(".//item") or root.findall(".//atom:entry", ns)
    for item in items[:15]:
        title_el = _first(item, ns, "title", "atom:title")
        link_el = _first(item, ns, "link", "atom:link")
        desc_el = _first(item, ns, "description", "summary", "atom:summary",
                         "content", "atom:content")
        title = title_el.text.strip() if title_el is not None and title_el.text else ""
        link = ""
        if link_el is not None:
            link = link_el.get("href") or (link_el.text or "").strip()
        text = _strip_html(desc_el.text or "") if desc_el is not None and desc_el.text else ""
        if not text:
            continue
        results.append({
            "source_name": cfg["name"],
            "url": link or cfg["url"],
            "title": title,
            "text": text,
            "text_layer": LAYER_FEED_SUMMARY,
            "raw_original": feed_bytes,
            "raw_original_url": rss_url,
            "raw_original_content_type": resp.headers.get("Content-Type", ""),
            "capture_complete": False,
            "capture_gaps": [
                "the stored raw original is the FEED document, not the article at "
                f"{link or cfg['url']}; the article body was not fetched",
                "the analysis text is the publisher's own feed summary, which may "
                "omit corrections, qualifications, and context present in the article",
            ],
            "captured_at": datetime.now(timezone.utc).isoformat(),
            "capture_method": "Web scrape (RSS feed summary)",
        })
    return results


def _scrape_article_list(cfg: dict) -> list[dict]:
    results = []
    try:
        resp = requests.get(cfg["url"], headers=HEADERS, timeout=15)
        resp.raise_for_status()
    except Exception as e:
        print(f"  [web] failed to fetch {cfg['url']}: {e}")
        return []

    soup = BeautifulSoup(resp.text, "lxml")
    link_sel = cfg.get("link_selector", "a")
    links = []
    seen = set()
    for a in soup.select(link_sel):
        href = a.get("href", "")
        if not href or href in seen:
            continue
        seen.add(href)
        if href.startswith("/"):
            base = urlparse(cfg["url"])
            href = f"{base.scheme}://{base.netloc}{href}"
        links.append((a.get_text(strip=True), href))

    for title, link in links[:12]:
        fetched = fetch_article(link, cfg.get("content_selector"))
        text = fetched["text"]
        if not text or len(text) < MIN_ARTICLE_CHARS:
            # A too-short extraction is a capture failure, not a short article.
            # It is dropped from the run and reported, never stored as content.
            print(
                f"  [web] no usable article text for {link} "
                f"({len(text)} chars; {'; '.join(fetched['gaps']) or 'selector matched nothing'})"
            )
            continue
        results.append({
            "source_name": cfg["name"],
            "url": link,
            "title": title,
            "text": text,
            "text_layer": LAYER_EXTRACTED_TEXT,
            "raw_original": fetched["raw"],
            "raw_original_url": link,
            "raw_original_content_type": fetched["content_type"],
            "capture_complete": fetched["raw"] is not None,
            "capture_gaps": fetched["gaps"],
            "captured_at": datetime.now(timezone.utc).isoformat(),
            "capture_method": "Web scrape (article extraction)",
        })

    return results


def fetch_article(url: str, selector: str | None) -> dict:
    """
    Fetch one article. Returns the full served bytes and the full extracted
    text, with any shortfall named in `gaps`. Nothing is clipped.
    """
    out = {"raw": None, "text": "", "content_type": "", "gaps": [], "selector_used": None}
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
    except Exception as e:
        out["gaps"].append(f"fetch failed: {e}; no original-form bytes held")
        return out

    out["raw"] = resp.content
    out["content_type"] = resp.headers.get("Content-Type", "")
    soup = BeautifulSoup(resp.text, "lxml")

    candidates = ([selector] if selector else []) + ["article", "main", ".content", "#content"]
    for cand in candidates:
        el = soup.select_one(cand)
        if el:
            out["text"] = el.get_text(separator=" ", strip=True)
            out["selector_used"] = cand
            if cand != selector and selector:
                out["gaps"].append(
                    f"configured selector {selector!r} matched nothing; fell back to {cand!r}, "
                    "which may include navigation chrome or omit article body"
                )
            return out

    out["text"] = soup.get_text(separator=" ", strip=True)
    out["selector_used"] = "whole document"
    out["gaps"].append(
        "no content selector matched; the extracted text is the whole document "
        "including navigation chrome, and is not a clean article body"
    )
    return out


def _strip_html(html: str) -> str:
    return BeautifulSoup(html, "lxml").get_text(separator=" ", strip=True)
