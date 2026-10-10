#!/usr/bin/env python3
"""Render the Veriticide General Ledger explainer film (silent-text, 1080p30).

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
    for p in sorted((ROOT / "cases").glob("*/evidence/*/sha256.txt"))[:26]:
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

# ---- appendix: one case file, opened (cases/rubio-usaid-denial/) -------------
def M(t, s, y, c=FG, size=30, x=L): return T(t, s, (x, y), ("mono", size), c)
def R2(t, s, y, c=FG, size=36): return T(t, s, (1000, y), ("Inter-Regular", size), c)
RB = "cases/rubio-usaid-denial/"
S.append((7.0, [K(0.2, "Example · what a case file contains", 230), RULE(0.3, 280),
                 H1(0.6, "Rubio / USAID denial", 310, size=88),
                 P(1.5, "Band 2 · Tier 4 — veriticide proper · single named respondent", 440, DIM, 36),
                 M(2.2, RB, 560, GOLD, 28),
                 M(2.5, "  00-charge-theory.md      03-adversarial-check.md", 610, FG, 28),
                 M(2.7, "  01-evidence-matrix.md    04-falsification-memo.md", 655, FG, 28),
                 M(2.9, "  02-source-bundle.md      05-custody-manifest.md", 700, FG, 28),
                 M(3.1, "  06-timeline.md           evidence/  (hashed, indexed)", 745, FG, 28)], None))
S.append((10.0, [K(0.2, "00 · Charge theory — the act", 170), RULE(0.3, 220),
                  H1(0.6, "An escalation ladder, each rung sourced.", 250, size=56),
                  M(1.5, "1  \"No one has died because of USAID cuts\"", 380, FG, 30),
                  M(2.0, "2  \"No children are dying on my watch\"", 435, FG, 30),
                  M(2.5, "3  Of the mortality modeling: \"false, that's fake\"", 490, FG, 30),
                  M(3.0, "4  The truthful testimony itself branded \"a lie\"", 545, GOLD, 30),
                  M(3.5, "5  Non-response to two congressional demands", 600, FG, 30),
                  P(4.6, "Rung 4 is the apex: not denial but inversion — the witness recoded as liar.", 700, DIM, 34),
                  P(5.4, "Charged: the defeat of recognition. Not charged: causing any death.", 770, GOLD, 34)], None))
S.append((9.0, [K(0.2, "00 · Charge theory — the elements", 200), RULE(0.3, 250),
                 H1(0.6, "Each element graded, not assumed.", 280, size=60),
                 M(1.5, "Instrument       MET — CONTESTED", 410, GOLD, 32),
                 P(1.7, "the office and its megaphone, not one voice", 455, DIM, 30),
                 M(2.4, "Legibility       MET — STRONG", 530, FG, 32),
                 P(2.6, "named deaths, internal cable and memos, all before the denial", 575, DIM, 30),
                 M(3.3, "Mental element   MET — STRONGEST", 650, FG, 32),
                 P(3.5, "he was Acting Administrator of USAID; the warnings were his agency's", 695, DIM, 30),
                 M(4.2, "Conscription     N/A", 770, DIM, 32)], None))
S.append((10.0, [K(0.2, "03 · Adversarial check  ·  04 · Falsification memo", 170), RULE(0.3, 220),
                  H1(0.6, "The case argues against itself, in advance.", 250, size=56),
                  T(1.4, "STRONGEST DEFENSES, STEEL-MANNED", (L, 370), ("Inter-SemiBold", 24), DIM),
                  P(1.7, "Protected political speech", 410, FG, 32),
                  P(2.0, "One official is not an instrument", 460, FG, 32),
                  P(2.3, "He never read the cable", 510, FG, 32),
                  P(2.6, "They were only projections", 560, FG, 32),
                  P(2.9, "A fact-check is just opinion", 610, FG, 32),
                  T(3.6, "WHAT WOULD PROVE IT WRONG", (1000, 370), ("Inter-SemiBold", 24), DIM),
                  R2(3.9, "He engaged the evidence on stated grounds", 410, FG, 32),
                  R2(4.2, "The quotes are inaccurate or out of context", 460, FG, 32),
                  R2(4.5, "A genuine firewall kept the warnings from him", 510, FG, 32),
                  R2(4.8, "The record was still genuinely open on May 21", 560, FG, 32),
                  P(6.0, "If the denial was actually argued, it is protected — and this is not the case.", 720, GOLD, 34)], None))
S.append((8.0, [K(0.2, "Boundary", 260), RULE(0.3, 310),
                 H1(0.6, "What this case does not establish.", 340, size=60),
                 P(1.5, "That he caused any death.", 470),
                 P(2.0, "Specific intent to deceive.", 535),
                 P(2.5, "That a court will accept the instrument characterization.", 600),
                 P(3.0, "That honest political disagreement is criminal. It is not.", 665),
                 P(4.0, "The target is the official denial against a closed internal record.", 765, GOLD, 36)], None))
S.append((10.0, [K(0.2, "Forum-Now  ·  Custody", 170), RULE(0.3, 220),
                  H1(0.6, "Soft vehicles live. Hard vehicles dormant.", 250, size=56),
                  T(1.4, "ACTIVE — STEP ONE", (L, 370), ("Inter-SemiBold", 24), GOLD),
                  P(1.7, "Preservation demand to State / USAID", 410, FG, 32),
                  P(2.0, "FOIA for the basis of \"no one has died\"", 460, FG, 32),
                  P(2.3, "HFAC: correct the record", 510, FG, 32),
                  P(2.6, "State OIG · GAO", 560, FG, 32),
                  T(3.2, "DORMANT — STEP TWO", (1000, 370), ("Inter-SemiBold", 24), DIM),
                  R2(3.5, "False-statement referral: OFF", 410, DIM, 32),
                  R2(3.8, "until knowing falsity is shown", 460, DIM, 32),
                  R2(4.1, "and a committee will act", 510, DIM, 32),
                  T(5.0, "EVIDENCE · 2 ITEMS · HASHED-PENDING-BACKUP · NOT YET TRIBUNAL-GRADE", (L, 660), ("Inter-SemiBold", 24), DIM),
                  M(5.4, "43347d81d0f5bd8d394d99a7e2688ffed14348590a2d0cb02d25b0544ecc8888  rubio-acting-administrator", 705, FG, 22),
                  M(5.7, "93cc853e9ad2e4c4d532e33d88465a913953485def543e80382c0d3c0eb0334a  wapo-factchecker-four-pinocchios", 740, FG, 22)], None))
S.append((6.0, [H1(0.3, "A basis to demand.", 430, size=80),
                 H1(1.3, "The verdict is for a tribunal.", 540, GOLD, 80),
                 T(2.4, "github.com/devinendorphin/veriticide-general-ledger/tree/main/cases/rubio-usaid-denial", (L, 680), ("mono", 26), DIM)], None))

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
    main(sys.argv[1] if len(sys.argv) > 1 else "veriticide-ledger.mp4")
