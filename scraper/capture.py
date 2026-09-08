"""
Capture identity, layer labelling, and coverage accounting.

This module is the evidence layer of the collector. It holds no network or
model dependencies so that its behaviour can be tested offline.

Three distinctions it is built to keep visible:

1. LAYER — what a stored string actually is. Bytes as served by the source
   host are not the same artifact as text pulled out of a DOM selection, and
   neither is the same artifact as a publisher's own feed summary. Each is
   labelled; none is silently substituted for another.

2. IDENTITY — a capture's content-version id is a digest over the *complete*
   captured material, not over a prefix of it. Two revisions of one article
   are therefore two versions, linked under one source-url id. The previous
   key (url + first 200 characters of text) collapsed a later correction into
   the revision it corrected.

3. COVERAGE — what was supplied to a downstream analyst, and what was not.
   An omission that is not recorded is indistinguishable, downstream, from
   text that never existed.

BOUNDARY. This module establishes what was captured, under what identity, and
which ranges of it were forwarded. It does not establish that the capture is
complete with respect to the source (the host may have served a paywall, an
interstitial, or a partial render), that the source is authentic, or that any
custody band applies. Custody bands are assigned by the case-level custody
process, never by this code.
"""

import hashlib
import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

# --- Layers -----------------------------------------------------------------
# What a stored string is. Never infer one from another.

LAYER_RAW_ORIGINAL = "raw_original"        # bytes as served by the source host
LAYER_EXTRACTED_TEXT = "extracted_text"    # derivative: DOM selection -> text
LAYER_FEED_SUMMARY = "feed_summary"        # derivative: publisher's summary field
LAYER_PLATFORM_FIELD = "platform_field"    # derivative: an API/GraphQL text field
LAYER_MODEL_EXCERPT = "model_excerpt"      # derivative: what a model was shown

DERIVATIVE_LAYERS = (
    LAYER_EXTRACTED_TEXT,
    LAYER_FEED_SUMMARY,
    LAYER_PLATFORM_FIELD,
    LAYER_MODEL_EXCERPT,
)

_LAYER_DESCRIPTIONS = {
    LAYER_RAW_ORIGINAL: "bytes as served by the source host",
    LAYER_EXTRACTED_TEXT: "DERIVATIVE — text extracted from the fetched document by a DOM selector",
    LAYER_FEED_SUMMARY: "DERIVATIVE — the publisher's own feed summary, not the article body",
    LAYER_PLATFORM_FIELD: "DERIVATIVE — a text field returned by a platform API",
    LAYER_MODEL_EXCERPT: "DERIVATIVE — the range of a derivative that was supplied to a model",
}


def describe_layer(layer: str) -> str:
    return _LAYER_DESCRIPTIONS.get(layer, f"UNDECLARED LAYER ({layer})")


# --- Identity ---------------------------------------------------------------

def sha256_hex(payload) -> str:
    if isinstance(payload, str):
        payload = payload.encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def normalize_url(url: str) -> str:
    """Normalize for source identity only. Never used to alter stored bytes."""
    if not url:
        return ""
    parts = urlsplit(url.strip())
    scheme = parts.scheme.lower() or "https"
    netloc = parts.netloc.lower()
    if netloc.startswith("www."):
        netloc = netloc[4:]
    path = parts.path.rstrip("/") or "/"
    return urlunsplit((scheme, netloc, path, parts.query, ""))


def source_url_id(url: str) -> str:
    """Stable id for a source location. Shared by every revision of it."""
    return sha256_hex(normalize_url(url))[:16]


def content_version_id(item: dict) -> str:
    """
    Identity of *this version* of the content, over the complete captured
    material: the normalized url, the digest of the raw original if one was
    obtained, and the full derivative text. No prefix, no truncation.
    """
    raw = item.get("raw_original")
    raw_digest = sha256_hex(raw) if raw is not None else "-"
    basis = "\n".join([
        normalize_url(item.get("url", "")),
        raw_digest,
        item.get("text", "") or "",
    ])
    return sha256_hex(basis)[:16]


def legacy_item_hash(item: dict) -> str:
    """
    The superseded key: url + the first 200 characters of text.

    Retained only so that a pre-existing seen-file can still suppress items
    that were already emitted under it. It must not be used to establish that
    two captures are the same content — that is the defect it carries.
    """
    key = item.get("url", "") + (item.get("text", "") or "")[:200]
    return hashlib.sha256(key.encode()).hexdigest()[:16]


# --- Coverage ---------------------------------------------------------------

@dataclass
class Segment:
    start: int
    end: int

    @property
    def length(self) -> int:
        return self.end - self.start

    def as_tuple(self) -> tuple:
        return (self.start, self.end)


@dataclass
class Coverage:
    """What of a text was supplied downstream, and what was withheld."""
    total_chars: int
    supplied: list = field(default_factory=list)   # list[Segment]
    omitted: list = field(default_factory=list)    # list[Segment]
    segment_count: int = 1
    segment_index: int = 1
    budget_chars: int = 0

    @property
    def complete(self) -> bool:
        return not self.omitted

    @property
    def supplied_chars(self) -> int:
        return sum(s.length for s in self.supplied)

    @property
    def omitted_chars(self) -> int:
        return sum(s.length for s in self.omitted)

    def to_dict(self) -> dict:
        return {
            "total_chars": self.total_chars,
            "supplied_ranges": [s.as_tuple() for s in self.supplied],
            "omitted_ranges": [s.as_tuple() for s in self.omitted],
            "supplied_chars": self.supplied_chars,
            "omitted_chars": self.omitted_chars,
            "segment_index": self.segment_index,
            "segment_count": self.segment_count,
            "budget_chars": self.budget_chars,
            "complete": self.complete,
        }

    def describe(self) -> str:
        """A line the downstream record can carry verbatim."""
        if self.complete:
            return (
                f"COMPLETE — all {self.total_chars} characters of the captured "
                f"text were supplied (ranges: "
                f"{'; '.join(f'{s.start}-{s.end}' for s in self.supplied)})."
            )
        omitted = "; ".join(f"{s.start}-{s.end}" for s in self.omitted)
        supplied = "; ".join(f"{s.start}-{s.end}" for s in self.supplied)
        return (
            f"PARTIAL — segment {self.segment_index} of {self.segment_count}. "
            f"Supplied character ranges: {supplied}. "
            f"OMITTED FROM THIS REQUEST: {omitted} "
            f"({self.omitted_chars} of {self.total_chars} characters). "
            f"The omitted ranges are preserved in the capture record and were "
            f"NOT read by the analyst producing this draft. Any claim about "
            f"the omitted ranges is unsupported."
        )


DEFAULT_EXCERPT_BUDGET = 24000


def plan_segments(text: str, budget: int = DEFAULT_EXCERPT_BUDGET) -> list:
    """Ordered segments covering the whole text. Never drops a tail."""
    if budget <= 0:
        raise ValueError("budget must be positive")
    if not text:
        return [Segment(0, 0)]
    return [Segment(i, min(i + budget, len(text))) for i in range(0, len(text), budget)]


def excerpt_with_coverage(text: str, budget: int = DEFAULT_EXCERPT_BUDGET,
                          segment_index: int = 1) -> tuple:
    """
    Return (supplied_text, Coverage) for one segment of `text`.

    Under the default budget an ordinary article is supplied whole and Coverage
    reports COMPLETE. When the text exceeds the budget the omitted ranges are
    named rather than dropped, and every character remains addressable by
    segment index against the preserved capture record.
    """
    text = text or ""
    segments = plan_segments(text, budget)
    idx = max(1, min(segment_index, len(segments)))
    chosen = segments[idx - 1]
    omitted = [s for i, s in enumerate(segments, start=1) if i != idx and s.length]
    coverage = Coverage(
        total_chars=len(text),
        supplied=[chosen],
        omitted=omitted,
        segment_count=len(segments),
        segment_index=idx,
        budget_chars=budget,
    )
    return text[chosen.start:chosen.end], coverage


# --- Capture records --------------------------------------------------------

_SAFE_ID = re.compile(r"[^A-Za-z0-9._-]+")


def _slug(value: str, limit: int = 60) -> str:
    return _SAFE_ID.sub("-", (value or "item")).strip("-")[:limit] or "item"


def build_capture_record(item: dict) -> dict:
    """
    The evidence record for one captured item. Analysis is never stored here.

    `custody_state` is deliberately null. An automated collector hashes bytes;
    it does not adjudicate custody. Bands (LOCATOR-VERIFIED /
    HASHED-PENDING-BACKUP / VERIFIED) are assigned by the case-level custody
    process against docs/custody-status-2026-07-02.md.
    """
    text = item.get("text", "") or ""
    raw = item.get("raw_original")
    cvid = content_version_id(item)
    url_id = source_url_id(item.get("url", ""))
    gaps = list(item.get("capture_gaps", []))

    record = {
        "schema": "veriticide.capture/1",
        "item_id": f"{url_id}-{cvid}",
        "content_version_id": cvid,
        "source_url_id": url_id,
        "source_url": item.get("url", ""),
        "source_name": item.get("source_name", ""),
        "title": item.get("title", ""),
        "captured_at": item.get("captured_at") or datetime.now(timezone.utc).isoformat(),
        "captured_by": "scraper/scraper.py (automated collection)",
        "capture_method": item.get("capture_method", ""),
        "analysis_text_layer": item.get("text_layer", LAYER_EXTRACTED_TEXT),
        "analysis_text_layer_note": describe_layer(item.get("text_layer", LAYER_EXTRACTED_TEXT)),
        "analysis_text_chars": len(text),
        "sha256_analysis_text": sha256_hex(text) if text else None,
        "raw_original_held": raw is not None,
        "raw_original_bytes": len(raw) if raw is not None else 0,
        "sha256_raw_original": sha256_hex(raw) if raw is not None else None,
        "raw_original_content_type": item.get("raw_original_content_type"),
        "raw_original_url": item.get("raw_original_url") or item.get("url", ""),
        "capture_complete": bool(item.get("capture_complete", raw is not None)),
        "capture_gaps": gaps,
        "custody_state": None,
        "custody_state_note": (
            "NOT ASSIGNED. Automated collection hashes what it received; it does "
            "not adjudicate custody. Assign a band only through the case-level "
            "custody process (docs/custody-status-2026-07-02.md)."
        ),
        "custodians": ["devinendorphin/veriticide-general-ledger (git)"],
    }
    if item.get("tweet_meta"):
        record["platform_meta"] = item["tweet_meta"]
    return record


def write_capture(store_root: Path, item: dict) -> dict:
    """
    Write one capture to the store and return its record.

    Layout, mirroring the case evidence stores:

        <store_root>/<url_id>/<content_version_id>/
            capture.json          the record (tracked)
            extracted.txt         the derivative text supplied for analysis
            original/manifest.json, original/sha256sums.txt  (tracked)
            original/<file>       raw bytes (git-ignored, as in cases/*/evidence)
    """
    record = build_capture_record(item)
    item_dir = Path(store_root) / record["source_url_id"] / record["content_version_id"]
    (item_dir / "original").mkdir(parents=True, exist_ok=True)

    text = item.get("text", "") or ""
    (item_dir / "extracted.txt").write_text(text, encoding="utf-8")

    raw = item.get("raw_original")
    manifest = {
        "item": record["item_id"],
        "captured_at": record["captured_at"],
        "artifact_count": 0,
        "artifacts": {},
        "capture_complete": record["capture_complete"],
        "capture_gaps": record["capture_gaps"],
    }
    if raw is not None:
        name = f"{_slug(normalize_url(record['source_url']))}.original"
        (item_dir / "original" / name).write_bytes(
            raw if isinstance(raw, bytes) else raw.encode("utf-8")
        )
        digest = record["sha256_raw_original"]
        manifest["artifacts"][name] = {"sha256": digest, "bytes": record["raw_original_bytes"]}
        manifest["artifact_count"] = 1
        (item_dir / "original" / "sha256sums.txt").write_text(
            f"{digest}  {name}\n", encoding="utf-8"
        )
    else:
        manifest["note"] = (
            "NO RAW ORIGINAL HELD. The original-form bytes were not obtained for "
            "this capture; see capture_gaps. This absence is a gap in the record, "
            "not evidence about the source."
        )
        (item_dir / "original" / "sha256sums.txt").write_text("", encoding="utf-8")

    (item_dir / "original" / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    record["store_path"] = str(item_dir)
    (item_dir / "capture.json").write_text(
        json.dumps(record, indent=2) + "\n", encoding="utf-8"
    )
    return record
