#!/usr/bin/env python3
"""Render the Veriticide General Ledger film, ICC cut (silent-text, 1080p30).

First half: identical to media/ledger-film/render.py (branch ccr-9ccea43f-ymg1wk).
Second half: the ninth case file, cases/rubio-icc-dismantlement/.

Every figure on screen is read from this repository or from a cited public
record; see SOURCES.md beside this script. Usage:
    python3 render.py <out.mp4>
"""
import math, subprocess, sys, textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
W, H, FPS = 1920, 1080, 30
BG, FG, DIM, GOLD, RED = (11, 13, 16), (232, 230, 225), (128, 134, 144), (200, 162, 74), (181, 72, 59)
F = "/usr/share/fonts/opentype/inter/"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
_fc = {}
def font(name, size):
    k = (name, size)
    if k not in _fc:
        _fc[k] = ImageFont.truetype(MONO if name == "mono" else F + name + ".otf", size)
    return _fc[k]

def ease(x): x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3
def mix(c, a): return tuple(int(BG[i] + (c[i] - BG[i]) * a) for i in range(3))

# ---- element helpers: (start, text, xy, font, color, anchor) ----------------
def T(t, s, xy, f=("Inter-Regular", 40), c=FG, anchor="la"):
    return dict(t=t, s=s, xy=xy, f=f, c=c, a=anchor)

def draw_elems(d, elems, lt, dur):
    out = ease((dur - lt) / 0.45)
    for e in elems:
        a = ease((lt - e["t"]) / 0.55) * out
        if a <= 0: continue
        x, y = e["xy"]; y += (1 - a) * 16
        if e["s"] == "__rule__":
            d.line([(x, y), (x + e["f"] * a, y)], fill=mix(e["c"], a), width=2); continue
        d.text((x, y), e["s"], font=font(*e["f"]), fill=mix(e["c"], a), anchor=e["a"])

# ---- the ledger scroll texture (real lines from ledger/ledger.md) ------------
def ledger_texture():
    lines = (ROOT / "ledger/ledger.md").read_text().splitlines()[150:260]
    wrapped = []
    for ln in lines:
        wrapped += textwrap.wrap(ln, 92) or [""]
    f = font("mono", 22); lh = 32
    img = Image.new("RGB", (1500, lh * len(wrapped) + 40), BG)
    d = ImageDraw.Draw(img)
    for i, ln in enumerate(wrapped):
        hot = any(k in ln for k in ("CLASSIFICATION", "BOUNDARY", "ADVERSARIAL CHECK"))
        d.text((0, 20 + i * lh), ln, font=f, fill=GOLD if hot else (150, 154, 160))
    return img
LEDGER = ledger_texture()

def hashes():
    out = []
    for p in sorted(p for p in (ROOT / "cases").glob("*/evidence/*/sha256.txt")
                    if "rubio-icc-dismantlement" not in p.parts)[:26]:
        h = p.read_text().split()[0]
        out.append(f"{h[:24]}…  {p.parts[-4]}/{p.parts[-2]}"[:70])
    return out
HASHES = hashes()

# ---- scenes: (duration, elements, optional background painter) --------------
L = 160
def H1(t, s, y, c=FG, size=76): return T(t, s, (L, y), ("InterDisplay-Bold", size), c)
def P(t, s, y, c=FG, size=40): return T(t, s, (L, y), ("Inter-Regular", size), c)
def K(t, s, y): return T(t, s.upper(), (L, y), ("Inter-SemiBold", 24), GOLD)
def RULE(t, y, w=220, c=GOLD): return dict(t=t, s="__rule__", xy=(L, y), f=w, c=c, a=None)

def bg_ledger(img, d, lt, dur):
    off = int(lt * 70)
    crop = LEDGER.crop((0, off, 1500, off + H))
    fade = ease(lt / 0.8) * ease((dur - lt) / 0.5) * 0.55
    layer = Image.blend(Image.new("RGB", crop.size, BG), crop, fade)
    # soft left edge so the scroll recedes behind the headline column
    mask = Image.linear_gradient("L").rotate(90, expand=True).resize(crop.size).transpose(Image.FLIP_LEFT_RIGHT)
    img.paste(layer, (1060, 0), mask.point(lambda v: min(255, v * 3)))

def bg_hashes(img, d, lt, dur):
    fade = ease(lt / 0.8) * ease((dur - lt) / 0.5)
    f = font("mono", 19)
    for i, h in enumerate(HASHES):
        a = fade * ease((lt - 1.2 - i * 0.07) / 0.3) * 0.75
        if a > 0: d.text((1060, 150 + i * 31), h, font=f, fill=mix((150, 154, 160), a))

S = []
S.append((5.5, [H1(0.3, "Institutions can be dismantled.", 420, size=88),
                 H1(2.3, "A record is harder to dismantle.", 540, GOLD, 88)], None))
S.append((6.5, [K(0.2, "Track A · Standing Protocol", 360), RULE(0.3, 410),
                 H1(0.6, "The Veriticide General Ledger", 440, size=96),
                 P(1.6, "Automated capture and protocol-grade analysis", 590, DIM, 44),
                 P(1.9, "of institutional harm laundering.", 650, DIM, 44)], None))
S.append((8.0, [K(0.2, "01 · The ledger", 300), RULE(0.3, 350),
                 H1(0.6, "A source-of-record archive.", 380, size=64),
                 P(1.6, "7,993 lines in ledger/ledger.md", 520),
                 P(2.2, "188 commits — every change versioned", 590),
                 P(2.8, "Public — anyone can clone, diff, and mirror it", 660, DIM),
                 P(3.4, "Nothing is asserted past what it bears.", 760, GOLD)], bg_ledger))
S.append((8.0, [K(0.2, "02 · Capture", 300), RULE(0.3, 350),
                 H1(0.6, "Hash what was served.", 380, size=64),
                 P(1.6, "The collector stores raw bytes + SHA-256.", 520),
                 P(2.2, "Evidence and analysis are kept apart:", 590),
                 P(2.6, "neither store writes to the other.", 650),
                 P(3.4, "65 hashed evidence items across 8 cases.", 750, GOLD)], bg_hashes))
S.append((9.5, [K(0.2, "03 · Classify", 200), RULE(0.3, 250),
                 H1(0.6, "One scheme. Applied the same way every time.", 280, size=60),
                 T(1.5, "FIVE CLASSIFICATIONS", (L, 420), ("Inter-SemiBold", 24), DIM),
                 T(1.7, "SPECIMEN · CONTROL · NULL · SINCERE-UNBOUNDED · INSTRUMENT", (L, 460), ("mono", 30), FG),
                 T(2.6, "SIX LAUNDERING MOVES", (L, 560), ("Inter-SemiBold", 24), DIM),
                 T(2.8, "concealment · denial · fragmentation · reframing as benefit", (L, 600), ("mono", 30), FG),
                 T(3.0, "attribution to the victim · discrediting testimony", (L, 645), ("mono", 30), FG),
                 T(3.9, "SIX TIERS", (L, 745), ("Inter-SemiBold", 24), DIM),
                 T(4.1, "constraint harm → conscription → subgraph erasure", (L, 785), ("mono", 30), FG),
                 T(4.3, "→ veriticide → mundicide → worldcide", (L, 830), ("mono", 30), FG)], None))
S.append((8.0, [K(0.2, "04 · Check", 300), RULE(0.3, 350),
                 H1(0.6, "Every entry argues against itself.", 380, size=64),
                 P(1.6, "ADVERSARIAL CHECK — the strongest innocent reading,", 520),
                 P(2.0, "and why it fails, or why it holds.", 580),
                 P(2.8, "BOUNDARY — what the item establishes,", 670),
                 P(3.2, "and what it does not establish alone.", 730),
                 P(4.2, "A single item is an instance. Pattern is the proof.", 830, GOLD)], None))
S.append((9.0, [K(0.2, "05 · Cut", 220), RULE(0.3, 270),
                 H1(0.6, "Eight case files, cut from the ledger.", 300, size=64),
                 P(1.5, "Each: one population · one instrument · one authorization chain · one harm pathway.", 420, DIM, 34),
                 T(2.3, "00 charge theory    01 evidence matrix    02 source bundle", (L, 520), ("mono", 30), FG),
                 T(2.5, "03 adversarial check    04 falsification memo    05 custody manifest", (L, 565), ("mono", 30), FG),
                 P(3.4, "Graded by evidence band, strongest first.", 670),
                 P(3.9, "Custody graded separately: 19 of 65 items VERIFIED", 740),
                 P(4.3, "(hashed original + off-platform second custodian).", 795, DIM)], None))
S.append((8.0, [K(0.2, "06 · Use", 300), RULE(0.3, 350),
                 H1(0.6, "Step one. Never step two.", 380, size=76),
                 P(1.7, "A case file asserts a basis to demand", 530),
                 P(2.1, "preservation · disclosure · audit · inquiry.", 595, GOLD),
                 P(3.2, "A finding of guilt is for a tribunal.", 700),
                 P(4.0, "Structural identity is claimed. Coordination is not.", 780, DIM)], None))
S.append((11.0, [K(0.2, "07 · Time", 170), RULE(0.3, 220),
                  H1(0.6, "Mandate to readiness.", 250, size=64),
                  T(1.6, "UN Independent Investigative Mechanism for Myanmar", (L, 380), ("Inter-SemiBold", 34), DIM),
                  T(1.9, "mandated 27 Sep 2018  →  operational 30 Aug 2019", (L, 430), ("mono", 30), FG),
                  T(2.3, "337 days", (L + 1200, 410), ("InterDisplay-Bold", 64), FG),
                  T(3.2, "Veriticide General Ledger", (L, 540), ("Inter-SemiBold", 34), DIM),
                  T(3.5, "first commit 21 Jun 2026  →  eight case files 30 Jun 2026", (L, 590), ("mono", 30), FG),
                  T(3.9, "9 days", (L + 1200, 570), ("InterDisplay-Bold", 64), GOLD),
                  P(5.4, "Not an equivalence. The Mechanism investigates in the field, protects witnesses,", 720, DIM, 32),
                  P(5.8, "and holds tribunal-grade custody. The ledger is the step-one layer that can", 765, DIM, 32),
                  P(6.2, "exist before a mandate does, and outlast one that is withdrawn.", 810, DIM, 32)], None))
S.append((8.0, [K(0.2, "Why it exists", 330), RULE(0.3, 380),
                 H1(0.6, "Not a condemnation.", 410, size=88),
                 H1(1.8, "A record.", 520, GOLD, 88),
                 P(3.2, "Jurisdiction can be contested. A hashed, versioned, public record", 680, FG, 38),
                 P(3.6, "remains for whichever forum is still standing.", 735, FG, 38)], None))
S.append((7.0, [H1(0.3, "veriticide-general-ledger", 430, size=72),
                 T(0.9, "github.com/devinendorphin/veriticide-general-ledger", (L, 540), ("mono", 34), GOLD),
                 P(1.6, "Start with cases/  ·  reader's map: docs/readers-map.md", 620, DIM, 34),
                 P(2.4, "Copy it. Mirror it. Audit it.", 740, FG, 44)], None))

# ---- second half: the ninth case file, opened (cases/rubio-icc-dismantlement/) ----
def M(t, s, y, c=FG, size=30, x=L): return T(t, s, (x, y), ("mono", size), c)
def R2(t, s, y, c=FG, size=32): return T(t, s, (1000, y), ("Inter-Regular", size), c)
RB = "cases/rubio-icc-dismantlement/"
S.append((7.0, [K(0.2, "Example · the ninth case file", 230), RULE(0.3, 280),
                 H1(0.6, "Rubio / ICC dismantlement", 310, size=88),
                 P(1.5, "Band 2 · Tier 4 — correction-environment form · single named respondent", 440, DIM, 36),
                 M(2.2, RB, 560, GOLD, 28),
                 M(2.5, "  00-charge-theory.md      03-adversarial-check.md", 610, FG, 28),
                 M(2.7, "  01-evidence-matrix.md    04-falsification-memo.md", 655, FG, 28),
                 M(2.9, "  02-source-bundle.md      05-custody-manifest.md", 700, FG, 28),
                 M(3.1, "  06-timeline.md           evidence/  (15 items, hashed, indexed)", 745, FG, 28)], None))
S.append((10.5, [K(0.2, "00 · Charge theory — the act", 170), RULE(0.3, 220),
                  H1(0.6, "Three forms. One direction.", 250, size=60),
                  M(1.5, "1  Judges — designated \"for ruling to authorize\"", 380, FG, 30),
                  M(2.0, "2  A UN rapporteur — for recommendations and letters", 435, FG, 30),
                  M(2.5, "2  Palestinian rights NGOs — \"punish entities that are complicit\"", 490, FG, 30),
                  M(3.0, "3  The Court itself — \"crippling its ability to operate\"", 545, GOLD, 30),
                  M(1.5, "Aug 2025", 382, DIM, 26, 1600), M(2.0, "Jul 2025", 437, DIM, 26, 1600),
                  M(2.5, "Sep 2025", 492, DIM, 26, 1600), M(3.0, "Oct 2026", 547, DIM, 26, 1600),
                  P(4.4, "Apex: the affected population's own documenters, penalized for testimony.", 660, DIM, 34),
                  P(5.4, "Neutral check: \"Albanese has done nothing more than speak.\" — Judge Leon", 735, GOLD, 34)], None))
S.append((9.5, [K(0.2, "The disconfirming test — run first", 170), RULE(0.3, 220),
                 H1(0.6, "It began by trying to talk itself out of existence.", 250, size=56),
                 M(1.5, "Opposing the ICC's jurisdiction    PROTECTED — NOT CHARGED", 390, GOLD, 30),
                 M(2.0, "Denying the predicate              REMOVED — warrant standard only", 445, FG, 30),
                 M(2.5, "Benefit inversion                  NOT PRESENT", 500, FG, 30),
                 M(3.0, "Concealment                        NOT PRESENT — it was announced", 555, FG, 30),
                 M(3.7, "Penalty on rulings · testimony · the Court   STANDS", 630, FG, 30),
                 P(4.8, "Arguing about jurisdiction is protected. Penalizing the judge is not.", 750, GOLD, 36)], None))
S.append((9.0, [K(0.2, "00 · Charge theory — the elements", 200), RULE(0.3, 250),
                 H1(0.6, "Each element graded, not assumed.", 280, size=60),
                 M(1.5, "Instrument       MET — CONTESTED", 410, GOLD, 32),
                 P(1.7, "one sanctions listing, executed by every bank's compliance screen", 455, DIM, 30),
                 M(2.4, "Legibility       MET — STRONG", 530, FG, 32),
                 P(2.6, "effects reported 17 months before; the aim stated outright", 575, DIM, 30),
                 M(3.3, "Mental element   MET as to the Court · INFERRED as to reach", 650, FG, 32),
                 P(3.5, "\"crippling its ability to operate\" — in the Secretary's own statement", 695, DIM, 30),
                 M(4.2, "Conscription     N/A", 770, DIM, 32)], None))
S.append((10.5, [K(0.2, "03 · Adversarial check  ·  04 · Falsification memo", 170), RULE(0.3, 220),
                  H1(0.6, "The case argues against itself, in advance.", 250, size=56),
                  T(1.4, "STRONGEST DEFENSES, STEEL-MANNED", (L, 370), ("Inter-SemiBold", 24), DIM),
                  P(1.7, "Non-consent is lawful policy — conceded", 410, FG, 32),
                  P(2.0, "Its Prosecutor was removed for misconduct", 460, FG, 32),
                  P(2.3, "It is staged: a 180-day licence", 510, FG, 32),
                  P(2.6, "A sanctions list is not an instrument", 560, FG, 32),
                  P(2.9, "The analyst is not neutral", 610, FG, 32),
                  T(3.6, "WHAT WOULD PROVE IT WRONG", (1000, 370), ("Inter-SemiBold", 24), DIM),
                  R2(3.9, "Judges designated for misconduct, not rulings", 410),
                  R2(4.2, "Non-speech conduct by the NGOs, on evidence", 460),
                  R2(4.5, "Every non-U.S. proceeding freed by licence", 510),
                  R2(4.8, "A statement engaging the rulings on the merits", 560),
                  P(6.0, "Counter-evidence kept on the record, including what cuts against the Court.", 720, GOLD, 34)], None))
S.append((8.0, [K(0.2, "Boundary", 260), RULE(0.3, 310),
                 H1(0.6, "What this case does not establish.", 340, size=60),
                 P(1.5, "That any crime before the Court occurred, or did not.", 470),
                 P(2.0, "That the Court has jurisdiction over Americans or Israelis.", 535),
                 P(2.5, "That any withdrawal from the Court was caused by the campaign.", 600),
                 P(3.0, "That any proceeding is yet impaired — a 180-day licence defers it.", 665),
                 P(4.0, "The target is penalty on adjudication and testimony — never the disagreement.", 765, GOLD, 36)], None))
S.append((10.0, [K(0.2, "Forum-Now  ·  Custody", 170), RULE(0.3, 220),
                  H1(0.6, "Soft vehicles live. Hard vehicles dormant.", 250, size=56),
                  T(1.4, "ACTIVE — STEP ONE", (L, 370), ("Inter-SemiBold", 24), GOLD),
                  P(1.7, "Preservation demand to State · OFAC", 410, FG, 32),
                  P(2.0, "FOIA: the record behind each designation", 460, FG, 32),
                  P(2.3, "Congress: questions for the record", 510, FG, 32),
                  P(2.6, "State OIG · GAO", 560, FG, 32),
                  T(3.2, "DORMANT — STEP TWO", (1000, 370), ("Inter-SemiBold", 24), DIM),
                  R2(3.5, "Rome Statute Art. 70 communication: OFF", 410, DIM),
                  R2(3.8, "jurisdiction doubtful — not asserted", 460, DIM),
                  R2(4.1, "litigation: only by those with standing", 510, DIM),
                  T(5.0, "EVIDENCE · 15 ITEMS · WARC + BODY · HASHED-PENDING-BACKUP · 0 VERIFIED · NOT YET REVIEWED", (L, 660), ("Inter-SemiBold", 24), DIM),
                  M(5.4, "666096c38ba4c7ed5abba216590b91e372483335d62b7be50dce169b417b402a  state-icc-institution-designation", 705, FG, 22),
                  M(5.6, "ef3797f44ede8ac50b064b6e0113822a2436fb6371ea665bef03e45be0de6a5a  state-icc-designation-chain", 740, FG, 22),
                  M(5.8, "a67076facef1c33a4693ad5586db0146c2aaef30741a077a2831ce0552096f94  state-palestinian-ngo-designations", 775, FG, 22)], None))

# The climax: the same mandate-to-readiness measure as scene 07, one rung further down.
CLOCK_T0, CLOCK_DUR, CLOCK_SECS = 5.0, 3.0, 20 * 60 + 35   # 05:42:12Z -> 06:02:47Z
def bg_clock(img, d, lt, dur):
    a = ease((lt - CLOCK_T0) / 0.4) * ease((dur - lt) / 0.45)
    if a <= 0: return
    s = round(ease((lt - CLOCK_T0) / CLOCK_DUR) * CLOCK_SECS)
    d.text((L + 1160, 588), f"{s // 3600:02d}:{s % 3600 // 60:02d}:{s % 60:02d}",
           font=font("InterDisplay-Bold", 80), fill=mix(GOLD, a))
S.append((15.0, [K(0.2, "07 · Time — again", 150), RULE(0.3, 200),
                  H1(0.6, "Mandate to readiness.", 230, size=64),
                  T(1.4, "UN Independent Investigative Mechanism for Myanmar", (L, 350), ("Inter-SemiBold", 34), DIM),
                  T(1.7, "mandated 27 Sep 2018  →  operational 30 Aug 2019", (L, 400), ("mono", 30), FG),
                  T(2.0, "337 days", (L + 1160, 370), ("InterDisplay-Bold", 64), FG),
                  T(2.8, "Veriticide General Ledger — the first eight case files", (L, 480), ("Inter-SemiBold", 34), DIM),
                  T(3.1, "first commit 21 Jun 2026  →  eight case files 30 Jun 2026", (L, 530), ("mono", 30), FG),
                  T(3.4, "9 days", (L + 1160, 500), ("InterDisplay-Bold", 64), FG),
                  T(4.2, "This case file", (L, 610), ("Inter-SemiBold", 34), GOLD),
                  T(4.5, "requested 05:42:12 UTC  →  pushed 06:02:47 UTC · 10 Oct 2026", (L, 660), ("mono", 30), FG),
                  P(8.6, "The designation it charges was announced the day before.", 760, FG, 34),
                  P(9.6, "Not an equivalence. Speed is not proof: not yet independently reviewed,", 830, DIM, 32),
                  P(10.0, "custody not yet tribunal-grade. Twenty minutes stands on 111 days of protocol.", 875, DIM, 32)],
                 bg_clock))
S.append((6.0, [H1(0.3, "A basis to demand.", 430, size=80),
                 H1(1.3, "The verdict is for a tribunal.", 540, GOLD, 80),
                 T(2.4, "github.com/devinendorphin/veriticide-general-ledger  ·  cases/rubio-icc-dismantlement", (L, 680), ("mono", 26), DIM)], None))

def main(out):
    total = sum(s[0] for s in S)
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
        "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
        "-f", "lavfi", "-i", f"aevalsrc=0.05*sin(2*PI*55*t)*(0.6+0.4*sin(2*PI*0.07*t))+0.03*sin(2*PI*82.5*t)+0.015*sin(2*PI*110*t):s=48000:d={total}",
        "-af", f"afade=t=in:d=2,afade=t=out:st={total-2.5}:d=2.5",
        "-c:v", "libx264", "-preset", "slow", "-crf", "20", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
    n = 0
    for dur, elems, painter in S:
        for k in range(int(dur * FPS)):
            lt = k / FPS
            img = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(img)
            if painter: painter(img, d, lt, dur)
            draw_elems(d, elems, lt, dur)
            # progress hairline + running mark
            d.line([(0, H - 3), (int(W * n / (total * FPS)), H - 3)], fill=(40, 44, 50), width=3)
            d.text((W - 60, 50), "VGL", font=font("Inter-SemiBold", 20), fill=(70, 74, 82), anchor="ra")
            ff.stdin.write(img.tobytes()); n += 1
    ff.stdin.close(); ff.wait()
    print(f"{out}: {total:.1f}s, {n} frames")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "veriticide-ledger-icc.mp4")
