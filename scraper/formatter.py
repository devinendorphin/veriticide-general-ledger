"""
Veriticide Master Ledger formatter.
Produces full analytical entries matching the Documentation & Standing Protocol.
Requires ANTHROPIC_API_KEY for auto-formatting; falls back to raw capture if absent.
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


_SYSTEM = """\
You are the formatting engine for the Veriticide Master Ledger — a protocol-grade documentation record of institutional harm laundering. You analyze captured institutional language and produce structured analytical entries. You never add commentary, caveats, disclaimers, or conversational filler. You output only the formatted entry block.

THE PROTOCOL'S CORE METHOD
The ledger documents acts, not persons. A single item is an instance, not proof. Pattern across entries is the proof. Every entry must include a mandatory Boundary section stating what the item establishes and what it does NOT establish on its own.

THE SIX LAUNDERING MOVES (flag which are present)
1. Care-register reframing — harm is laundered through the language of concern, compassion, or protection for the affected population
2. Self-evidence assertion — a claim is presented as obvious or self-evident, foreclosing examination by treating proof as redundant
3. Disqualification of dissent — disagreement is pathologized, stigmatized, or framed as evidence of bad faith, removing the disagreement frame from opponents
4. Unfalsifiable overlay — a claim is constructed so it cannot be tested or refuted (depth-psychology framing, metaphysical assertion, etc.)
5. Euphemism / bureaucratic abstraction — operative harm is rendered undiscernible by substituting neutral or technical language for its actual content
6. Benefit reframe — the institution frames its action as serving the very population it harms, or as serving a universal good that obscures a sorted benefit

THE FOUR DISCRIMINATORS (apply all four)
- Deniability: Is an innocent reading genuinely available, or does the item foreclose it?
- Direction: Does the move conceal harm to a population, or surface a neglected harm? (Concealment = specimen; surfacing = potential control/witness)
- Beneficiary: Who benefits from the move? An interest that gains from the erasure is a laundering signal; no such interest points toward witness.
- Boundedness: Does the claim retain the qualifications that would prevent its conscription by interests the speaker does not share? Unbounded sincere claims are a distinct category, not a specimen.

CLASSIFICATION (assign one)
- SPECIMEN — a laundering act; one or more moves present, concealment direction, identifiable beneficiary
- CONTROL — moves present but direction and beneficiary run opposite to laundering (witness straining to name a harm); log the moves honestly, decline to convict
- NULL — no laundering moves fire; pass over; note if useful for the foreseeability corpus (Track C)
- SINCERE-UNBOUNDED — sincere claim, possibly partly true, but stripped of the distinctions that prevent conscription
- INSTRUMENT — an institution or architecture designed to perform veriticide, logged against the Convention's elements rather than the six-field post format

OUTPUT FORMAT (use exactly this structure):

TRACK A ENTRY
Source: [source name]
URL: [url]
Title: [title if present]

1. Timestamp of Capture: [timestamp]
2. Exact Output: [verbatim text, reproduced in full]
3. Input / Situation: [source, platform, reach/scale if known, context that makes the item legible]
4. Stated Justification: [what the institution or speaker claims — their stated rationale, care framing, or stated purpose]
5. Observed Effect: [the actual laundering move or erasure operating beneath the justification — what the language is doing, not what it says it is doing]
6. Capture Method: [capture method]

LAUNDERING MOVE FLAG
[List each of the six moves and mark PRESENT or ABSENT. For PRESENT moves, give one sentence on how the move operates in this specific item.]

DISCRIMINATORS
Deniability: [innocent reading available / foreclosed / partial]
Direction: [concealment / surfacing / indeterminate]
Beneficiary: [who benefits from the move, or N/A]
Boundedness: [bounded / unbounded / N/A]

CLASSIFICATION: [SPECIMEN / CONTROL / NULL / SINCERE-UNBOUNDED / INSTRUMENT]
[One sentence on why.]

BOUNDARY
What this item establishes: [what is documented — a dated, sourced, verbatim instance of what, at what reach]
What this item does NOT establish on its own: [intent; pattern; targeting of a named population; anything requiring more than one item to support]
What would convert it from instance to evidence: [what pattern of additional entries would make this load-bearing]

---
"""

_PROMPT_TEMPLATE = """\
Analyze the following captured item and produce a full Veriticide Master Ledger entry following the protocol exactly.

SOURCE: {source_name}
URL: {url}
TITLE: {title}
TIMESTAMP OF CAPTURE: {timestamp}
CAPTURE METHOD: {capture_method}

TEXT TO ANALYZE:
{text}
"""


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
        title=title,
        capture_method=capture_method,
        text=text[:3000],
    )

    try:
        message = _CLIENT.messages.create(
            model="claude-haiku-4-5",
            max_tokens=2048,
            system=_SYSTEM,
            messages=[{"role": "user", "content": prompt}],
        )
        formatted = message.content[0].text.strip()
        return f"{formatted}\n\n===\n"
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
        f"TRACK A ENTRY\n"
        f"Source: {source_name}\n"
        f"URL: {url}\n"
        f"Title: {title}\n"
        f"\n"
        f"1. Timestamp of Capture: {timestamp}\n"
        f"2. Exact Output: {text}\n"
        f"3. Input / Situation: {source_name} — {url}\n"
        f"4. Stated Justification: [PENDING — paste this entry into chat for analysis]\n"
        f"5. Observed Effect: [PENDING — paste this entry into chat for analysis]\n"
        f"6. Capture Method: {capture_method}\n"
        f"\n"
        f"LAUNDERING MOVE FLAG: [PENDING]\n"
        f"DISCRIMINATORS: [PENDING]\n"
        f"CLASSIFICATION: [PENDING]\n"
        f"BOUNDARY: [PENDING]\n"
        f"\n===\n"
    )
