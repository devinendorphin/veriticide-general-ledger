import xml.etree.ElementTree as ET

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}


def scrape_source(source_cfg: dict) -> list[dict]:
    src_type = source_cfg.get("type", "article_list")
    if src_type == "rss":
        return _scrape_rss(source_cfg)
    else:
        return _scrape_article_list(source_cfg)


def _scrape_rss(cfg: dict) -> list[dict]:
    results = []
    rss_url = cfg.get("rss_url", cfg["url"])
    try:
        resp = requests.get(rss_url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        root = ET.fromstring(resp.content)
    except Exception as e:
        print(f"  [rss] failed to fetch {rss_url}: {e}")
        return []

    ns = {"atom": "http://www.w3.org/2005/Atom"}
    # Handle both RSS 2.0 and Atom
    items = root.findall(".//item") or root.findall(".//atom:entry", ns)
    for item in items[:15]:
        title_el = item.find("title") or item.find("atom:title", ns)
        link_el = item.find("link") or item.find("atom:link", ns)
        desc_el = (
            item.find("description")
            or item.find("summary")
            or item.find("atom:summary", ns)
            or item.find("content")
            or item.find("atom:content", ns)
        )
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
            "captured_at": datetime.now(timezone.utc).isoformat(),
            "capture_method": "Web scrape (RSS)",
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
            from urllib.parse import urlparse
            base = urlparse(cfg["url"])
            href = f"{base.scheme}://{base.netloc}{href}"
        links.append((a.get_text(strip=True), href))

    for title, link in links[:12]:
        article_text = _fetch_article_text(link, cfg.get("content_selector"))
        if not article_text or len(article_text) < 80:
            continue
        results.append({
            "source_name": cfg["name"],
            "url": link,
            "title": title,
            "text": article_text[:4000],
            "captured_at": datetime.now(timezone.utc).isoformat(),
            "capture_method": "Web scrape",
        })

    return results


def _fetch_article_text(url: str, selector: str | None) -> str:
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
    except Exception:
        return ""
    soup = BeautifulSoup(resp.text, "lxml")
    if selector:
        el = soup.select_one(selector)
        if el:
            return el.get_text(separator=" ", strip=True)
    for tag in ["article", "main", ".content", "#content"]:
        el = soup.select_one(tag)
        if el:
            return el.get_text(separator=" ", strip=True)
    return soup.get_text(separator=" ", strip=True)[:4000]


def _strip_html(html: str) -> str:
    return BeautifulSoup(html, "lxml").get_text(separator=" ", strip=True)
