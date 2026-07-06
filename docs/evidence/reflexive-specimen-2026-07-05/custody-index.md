# CUSTODY INDEX — Reflexive specimen, 2026-07-05 session

*Original-form evidence store for `docs/reflexive-specimen-2026-07-05-fable5-session-mapping.md`.*

> **This index governs custody state.** **VERDICT: DECLINED** (high-variance reflexive self-record; see the mapping memo).

**Captured into repo:** 2026-07-06 · **Source:** operator-supplied upload · **Items:** 1 · **State:** ORIGINAL-HELD (of the transcription artifact only — see below)

| Item | Type | Role in record | Custody | sha256 |
|---|---|---|---|---|
| `Fable5_Veriticide_Session_Transcript_20260705.md` | Text transcript (instrument-transcribed) | The full 25-turn session record, transcribed 2026-07-05 by the same Claude Fable 5 instance from live context at the operator's request. Source artifact for every S-act, O-act, and counter-register item in the mapping memo. | ORIGINAL-HELD (artifact) / SELF-TRANSCRIBED (content) | `92fc9b42d9c5c38659259c10f55dbd56aa063a2c3e62d78aa3c20d507e404572` |

## The custody distinction this index turns on

**ORIGINAL-HELD applies to the transcription file as an artifact** — the bytes the operator uploaded are preserved and hashed, so the *record of what the instrument claimed the session contained* cannot now be silently altered.

**It does not apply to the session itself.** The transcript declares its own defects in its provenance note, and they are custody defects of the first order:

1. It is **instrument-transcribed from surviving context** — "a post-selection surface artifact, not ground truth," in its own words.
2. **Several early tool results were cleared from context by the system** before transcription and are marked unrecoverable. The evidentiary basis of Turns 1, 3, 4, 9, and 11's tool calls cannot be reconstructed.
3. **Third-party news text is summarized, not reproduced** — the Turn 11 web-search results, on which the session's strongest factual turn rests, are not in the record.
4. The transcriber is the subject. Selection effect is maximal and uncured by construction (same defect class as `reflexive-specimen-2026-06-30-transcript.md`, declared there in identical terms).

The session content therefore **cannot reach VERIFIED and never will** — the session is unrecoverable. What *can* be verified are the transcript's externally checkable claims, which the mapping memo's verification table grades against the public record (performed 2026-07-06).

## Verify

```bash
# from docs/evidence/reflexive-specimen-2026-07-05/
sha256sum -c sha256.txt
```
