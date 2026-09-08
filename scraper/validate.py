"""
Draft validation.

A draft analysis is not a finished entry. This module decides whether a model
return may even be labelled a complete *draft* — that is, whether it is whole,
structurally conformant, and free of citations the record cannot support.

The three failures it is built to catch:

- INTERRUPTION. An output cut off at the token limit ends mid-analysis but
  still looks like an entry. It is marked incomplete here.
- UNVERIFIABLE CITATION. An entry reference the collector never retrieved is
  not counter-evidence accounting; it is an assertion about a record nobody
  read.
- EMPTY-SEARCH SUBSTITUTION. "NONE ON RECORD" asserts that a search was
  performed and returned nothing. When no prior-record set was supplied, that
  assertion is unsupported, and the draft must say RETRIEVAL NOT PERFORMED
  instead. This is the distinction the collector previously could not make.

BOUNDARY. Passing validation establishes that a draft is structurally complete
and cites only records that were supplied to it. It does not establish that the
analysis is correct, that the classification is right, or that the adversarial
check was performed in good faith. Validation is a floor, not a review.
"""

import re

STATUS_COMPLETE = "DRAFT — COMPLETE, UNREVIEWED"
STATUS_INCOMPLETE = "DRAFT — INCOMPLETE, DO NOT READ AS AN ENTRY"
STATUS_NO_ANALYSIS = "RAW CAPTURE — NO ANALYSIS PERFORMED"

RETRIEVAL_NOT_PERFORMED = "RETRIEVAL NOT PERFORMED"
NONE_ON_RECORD = "NONE ON RECORD"

_STANDARD_SECTIONS = [
    "TRACK A ENTRY",
    "LAUNDERING MOVE FLAG",
    "DISCRIMINATORS",
    "CLASSIFICATION",
    "ADVERSARIAL CHECK",
    "COUNTER-EVIDENCE STATUS",
    "BOUNDARY",
]

_INSTRUMENT_SECTIONS = [
    "INSTRUMENT ENTRY",
    "CONVENTION ELEMENTS",
    "CLASSIFICATION",
    "ADVERSARIAL CHECK",
    "COUNTER-EVIDENCE STATUS",
    "BOUNDARY",
]

# Entry references used across the ledger: "Entry 3.5", "Entry 15",
# "TD-001", "TE-002", "TF-004", "CTF-1".
_REFERENCE = re.compile(r"\b(?:Entry\s+\d+(?:\.\d+)*|T[A-F]-\d{2,4})\b")


class DraftValidation:
    def __init__(self, status, problems=None, references=None):
        self.status = status
        self.problems = list(problems or [])
        self.references = list(references or [])

    @property
    def complete(self) -> bool:
        return self.status == STATUS_COMPLETE

    def to_dict(self) -> dict:
        return {
            "status": self.status,
            "problems": self.problems,
            "cited_references": self.references,
        }


def _section(text: str, heading: str) -> str:
    """Text from `heading` to the next all-caps heading, for scoped checks."""
    idx = text.find(heading)
    if idx == -1:
        return ""
    rest = text[idx + len(heading):]
    nxt = re.search(r"\n(?=[A-Z][A-Z \-/]{6,}\n)", rest)
    return rest[:nxt.start()] if nxt else rest


def find_references(text: str) -> list:
    seen, out = set(), []
    for m in _REFERENCE.finditer(text or ""):
        ref = re.sub(r"\s+", " ", m.group(0))
        if ref not in seen:
            seen.add(ref)
            out.append(ref)
    return out


def validate_draft(text: str, response=None, retrieval_performed: bool = False,
                   available_references=None) -> DraftValidation:
    """
    Validate a model draft.

    `retrieval_performed` says whether a prior-record set was actually supplied
    with the request. `available_references` is that set. When retrieval was not
    performed, any entry reference in the counter-evidence section is
    unverifiable and an assertion of NONE ON RECORD is unsupported.
    """
    text = (text or "").strip()
    problems = []
    available = set(available_references or [])

    if not text:
        return DraftValidation(STATUS_INCOMPLETE, ["model returned no text"])

    if response is not None:
        if not response.available:
            return DraftValidation(STATUS_INCOMPLETE,
                                   [f"provider error: {response.error}"])
        if response.truncated:
            problems.append(
                f"output interrupted (stop_reason={response.stop_reason!r}); "
                "the analysis is cut off, not concluded"
            )
        elif response.stop_reason != "end_turn":
            problems.append(
                f"unrecognized stop_reason {response.stop_reason!r}; completion not established"
            )

    required = _INSTRUMENT_SECTIONS if "INSTRUMENT ENTRY" in text else _STANDARD_SECTIONS
    for heading in required:
        if heading not in text:
            problems.append(f"required section missing: {heading}")

    if required is _STANDARD_SECTIONS:
        for n in range(1, 7):
            if not re.search(rf"^\s*{n}\.\s", text, re.MULTILINE):
                problems.append(f"required numbered field missing: {n}.")

    counter = _section(text, "COUNTER-EVIDENCE STATUS")
    references = find_references(counter)

    if retrieval_performed:
        for ref in references:
            if ref not in available:
                problems.append(
                    f"unverifiable citation {ref!r}: not present in the prior-record "
                    "set supplied with this request"
                )
    else:
        if references:
            problems.append(
                "counter-evidence section cites prior entries "
                f"({', '.join(references)}) although no prior-record set was "
                "supplied; these citations are unverifiable"
            )
        if NONE_ON_RECORD in counter:
            problems.append(
                "counter-evidence section asserts NONE ON RECORD although no "
                "cross-record search was performed; an unperformed search is not "
                f"an empty result. Required: {RETRIEVAL_NOT_PERFORMED}"
            )
        elif RETRIEVAL_NOT_PERFORMED not in counter:
            problems.append(
                "counter-evidence section does not record the retrieval state; "
                f"it must state {RETRIEVAL_NOT_PERFORMED}"
            )

    status = STATUS_INCOMPLETE if problems else STATUS_COMPLETE
    return DraftValidation(status, problems, references)
