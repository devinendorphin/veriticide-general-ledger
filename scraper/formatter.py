"""
Six-field Veriticide ledger formatter.
Requires ANTHROPIC_API_KEY environment variable.
Falls back to raw capture block if key is absent.
"""

import os
from datetime import datetime, timezone

try:
    import anthropic
    _CLIENT = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))
    _HAS_SDK = True
except ImportError:
    _HAS_SDK = False
    _CLIENT = None


_SYSTEM = """You are a formatting engine for the Veriticide Master Ledger, a documentation record of institutional harm laundering. You analyze institutional language and output formatted entries. You never add commentary, warnings, or filler. You only output the formatted block."""

_PROMPT_TEMPLATE = """Analyze the following captured institutional text and output a formatted Veriticide Master Ledger entry with exactly these six fields:

1. Timestamp of Capture: {timestamp}
2. Exact Output: (the verbatim text below, reproduced exactly)
3. Input / Situation: (source: {source_name} — URL: {url})
4. Stated Justification: (extract what the institution or speaker claims as its excuse or "care" framing — what they say they are doing this FOR)
5. Observed Effect: (identify the actual laundering move, evasion, or systemic erasure occurring beneath the justification — what the language is doing, not what it says it is doing)
6. Capture Method: {capture_method}

TEXT TO ANALYZE:
{text}

Output only the formatted entry block. No commentary before or after."""


def format_entry(item: dict) -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    text = item.get("text", "").strip()
    source_name = item.get("source_name", "Unknown source")
    url = item.get("url", "")
    capture_method = item.get("capture_method", "Web scrape")
    title = item.get("title", "")

    if not _HAS_SDK or not os.environ.get("ANTHROPIC_API_KEY"):
        return _raw_entry(timestamp, text, source_name, url, capture_method, title)

    prompt = _PROMPT_TEMPLATE.format(
        timestamp=timestamp,
        source_name=source_name,
        url=url,
        capture_method=capture_method,
        text=text[:3000],
    )

    try:
        message = _CLIENT.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=_SYSTEM,
            messages=[{"role": "user", "content": prompt}],
        )
        formatted = message.content[0].text.strip()
        return f"{formatted}\n\n---\n"
    except Exception as e:
        print(f"  [formatter] API call failed: {e}. Falling back to raw entry.")
        return _raw_entry(timestamp, text, source_name, url, capture_method, title)


def _raw_entry(
    timestamp: str,
    text: str,
    source_name: str,
    url: str,
    capture_method: str,
    title: str,
) -> str:
    return (
        f"1. Timestamp of Capture: {timestamp}\n"
        f"2. Exact Output: {text}\n"
        f"3. Input / Situation: {source_name} — {url}\n"
        f"   Title: {title}\n"
        f"4. Stated Justification: [PENDING — paste this entry into chat for analysis]\n"
        f"5. Observed Effect: [PENDING — paste this entry into chat for analysis]\n"
        f"6. Capture Method: {capture_method}\n"
        f"\n---\n"
    )
