# CANONICAL CUSTODY INDEX — @yacineMTB corpus packet

*Mechanically derived from `evidence/*/capture.json` by `build-custody-index.py` — regenerate, do not hand-edit.*

> **This index governs** custody state. **ACCOUNT-LEVEL VERDICT: DECLINED** (high-variance account).
> This packet records *acts* (specimens), not the account. See `../00-charge-theory.md`.

**Generated:** 2026-06-29 · **Items:** 6 · **States:** SCREENSHOT-HELD 6

| Item | Class | Register | Reach | Custody | sha256(transcript) |
|---|---|---|---|---|---|
| `agp-breakcore-narrow` | SPECIMEN-narrow | medical-pathologizing (vocab-normalization; affirmative frame) | 3.1K views | SCREENSHOT-HELD | `eb583391132c…` |
| `eating-children-conspiracy` | SPECIMEN | Satanic-panic/conspiracy | 252K views (highest in corpus) | SCREENSHOT-HELD | `32219e284690…` |
| `epidemic-homely-girls` | SPECIMEN | medical-pathologizing | 12.8K views | SCREENSHOT-HELD | `34762d2d5fbb…` |
| `grooming-vindication` | SPECIMEN | grooming/conspiracy | 60.6K views | SCREENSHOT-HELD | `d5ea287a825b…` |
| `shoujo-maxx-chemical-castration` | SPECIMEN | medical-pathologizing | engagement not captured | SCREENSHOT-HELD | `727dc7b4c387…` |
| `trans-muslims-death-threats` | SPECIMEN | negative-equivalence | 414 views | SCREENSHOT-HELD | `decfcf309d0d…` |

## Custody states

- **SCREENSHOT-HELD** — verbatim text preserved as a hashed transcript from an operator-supplied screenshot; **no canonical URL and no original-form web bytes**. This corpus cannot reach VERIFIED without locating canonical tweet URLs (deliberately not pursued — private individual; corpus deprioritized/not load-bearing in the ledger).
- **LOCATOR-VERIFIED / VERIFIED** — not applicable to this packet (no URLs captured).

## Not in this evidence store

Counter-evidence (5), the NULL/SINCERE-UNBOUNDED entries, the algorithm meta-post, and the
`@glubose` companion counter-speech are tabulated in `../02-source-bundle.md`, not as separate
evidence dirs — they are part of the same high-variance record and are preserved there.

## Regenerate

```bash
# from cases/yacinemtb-corpus/evidence/
python3 build-custody-index.py
for d in */; do (cd "$d" && sha256sum -c sha256.txt); done
```

