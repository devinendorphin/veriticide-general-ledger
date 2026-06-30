# 05 — CUSTODY MANIFEST

*Track F for the CTF-1 packet. Convention Art. VI(6); Protocol §6. This is the weakest-custody
packet in the repo, by the nature of its sources — and it says so.*

> **Authoritative source:** `evidence/custody-index.md` governs. **ACCOUNT-LEVEL VERDICT: DECLINED.**

---

## Custody state — SCREENSHOT-HELD (the whole packet)

| State | Meaning |
|---|---|
| `SCREENSHOT-HELD` | Verbatim text preserved as a hashed `transcript.md`, derived from an **operator-supplied screenshot**. **No canonical tweet URL** and **no original-form web bytes** are held. |
| `LOCATOR-VERIFIED` / `VERIFIED` | **Not applicable.** This corpus has no captured URLs; it cannot reach VERIFIED without first locating canonical tweet URLs. |

## Items (all SCREENSHOT-HELD)

| Specimen | Date | Reach | Screenshot provenance |
|---|---|---|---|
| `epidemic-homely-girls` | 02 Oct 25 | 12.8K | `/mnt/data/1000026306.jpg` |
| `shoujo-maxx-chemical-castration` | 28 Oct 25 | n/c | `/mnt/data/1000026306.jpg` |
| `agp-breakcore-narrow` | 28 Oct 25 | 3.1K | `/mnt/data/1000026306.jpg` |
| `grooming-vindication` | 04 Jan 26 | 60.6K | `/mnt/data/1000026302.jpg` |
| `trans-muslims-death-threats` | 26 Jan 26 | 414 | `/mnt/data/1000026302.jpg` |
| `eating-children-conspiracy` | 08 Feb 26 | 252K | `/root/.claude/uploads/…/742bb7d9-1000027101.jpg` |

Integrity: `for d in evidence/*/; do (cd "$d" && sha256sum -c sha256.txt); done` (all `OK`). The
hashed verbatim transcript is the preserved artifact; the screenshots themselves are operator-held
and are **not** in this repo.

## Honest-custody notes (limitations recorded, not cured)

1. **No original-form capture, by design.** Upgrading to VERIFIED would require locating each post's
   canonical URL, then running web capture. This is **deliberately not pursued**: the subject is a
   private individual, the corpus is deprioritized and not load-bearing in the ledger, and hunting an
   individual's posts to build a dossier is itself an escalation the packet declines. Recorded as an
   accepted limitation.
2. **Operator-curated selection.** The screenshots are the operator's selection; the operator is a
   participant in the corpus (`04-falsification-memo.md` §Reflexivity). Selection effect is the
   packet's gravest, uncured caveat.
3. **Screenshot integrity is the single point of failure.** With no canonical URL, the corpus rests on
   the hashed transcripts of operator screenshots; one demonstrated manipulation would impeach it.

## What this packet does not claim

It does not hold canonical URLs or original-form bytes; it does not assert an account-level verdict;
it does not treat the operator's counter-speech as above scrutiny; and it does not pretend custody
discipline can substitute for the independent, complete capture that an account-level inference would
require (which is absent). It preserves and hashes the verbatim record, declares its limits, and
stops there.
