#!/usr/bin/env python3
"""Draft image for make.fun news-image-20261118 (DRAFT - not submitted).
Renders a 1024x1024 front-page-style collage summing up Wednesday 18 Nov 2026.
Headlines grounded in web research 19 Nov 2026 (see NEWS-BRIEF.md).
Run: python3 make_news_image.py  -> writes entry.png next to this script.
"""
from PIL import Image, ImageDraw, ImageFont
import textwrap

W, H = 1024, 1024
PAPER = (245, 239, 227)
INK = (22, 19, 14)
RED = (179, 39, 30)
NAVY = (29, 45, 80)
TEAL = (14, 107, 107)
GOLD = (200, 155, 60)
CARD = (255, 253, 246)
GREY = (90, 84, 72)

FD = "/usr/share/fonts/truetype/dejavu/"
def font(name, size):
    return ImageFont.truetype(FD + name, size)

F_TITLE = font("DejaVuSerif-Bold.ttf", 56)
F_KICK = font("DejaVuSans-Bold.ttf", 19)
F_HEAD = font("DejaVuSerif-Bold.ttf", 30)
F_HEAD_S = font("DejaVuSerif-Bold.ttf", 27)
F_DECK = font("DejaVuSans.ttf", 20)
F_DECK_S = font("DejaVuSans.ttf", 18)
F_FOOT = font("DejaVuSans.ttf", 17)
F_SUB = font("DejaVuSans-Bold.ttf", 20)
F_BIG = font("DejaVuSerif-Bold.ttf", 38)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def wrap(draw, text, fnt, width):
    words = text.split()
    lines, cur = [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if draw.textlength(t, font=fnt) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines

def panel(x, y, w, h, accent):
    d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=CARD,
                        outline=INK, width=2)
    d.rectangle([x, y, x + w, y + 8], fill=accent)

def kicker(x, y, text, color):
    d.text((x, y), text, font=F_KICK, fill=color)

def headline(x, y, text, fnt, width):
    lines = wrap(d, text, fnt, width)
    yy = y
    for ln in lines:
        d.text((x, yy), ln, font=fnt, fill=INK)
        yy += fnt.size + 4
    return yy

def deck(x, y, text, width, fnt=F_DECK):
    lines = wrap(d, text, fnt, width)
    yy = y
    for ln in lines:
        d.text((x, yy), ln, font=fnt, fill=(60, 54, 44))
        yy += fnt.size + 5
    return yy

# ---------- masthead ----------
d.text((36, 26), "THE WORLD IN ONE IMAGE", font=F_TITLE, fill=INK)
d.text((36, 100), "WEDNESDAY,  18  NOVEMBER  2026", font=F_SUB, fill=RED)
d.text((36, 128), "Six stories that defined the day", font=F_DECK, fill=GREY)
d.line([36, 158, 988, 158], fill=INK, width=3)
d.line([36, 164, 988, 164], fill=INK, width=1)

# ---------- lead: Shenzhen summit ----------
LX, LY, LW, LH = 36, 178, 952, 252
panel(LX, LY, LW, LH, RED)
kicker(LX + 24, LY + 22, "LEAD  ·  SHENZHEN", RED)
# flag trio, right side (3 small flags, 64x42, inside the panel)
fx, fy, fw, fh = 756, LY + 26, 64, 42
d.rectangle([fx, fy, fx + fw, fy + fh], fill=(222, 41, 16))          # China
d.text((fx + 9, fy + 7), "\u2605", font=font("DejaVuSans-Bold.ttf", 24), fill=(255, 222, 0))
d.rectangle([fx + 74, fy, fx + 74 + fw, fy + fh], fill=(255, 255, 255), outline=INK)  # Russia
d.rectangle([fx + 74, fy + 14, fx + 74 + fw, fy + 28], fill=(0, 57, 166))
d.rectangle([fx + 74, fy + 28, fx + 74 + fw, fy + 42], fill=(213, 0, 50))
d.rectangle([fx + 148, fy, fx + 148 + fw, fy + fh], fill=(255, 255, 255), outline=INK)  # USA
for i in range(5):
    d.rectangle([fx + 148, fy + i * 9, fx + 148 + fw, fy + i * 9 + 4], fill=(178, 34, 52))
d.rectangle([fx + 148, fy, fx + 148 + 30, fy + 23], fill=(60, 59, 110))
d.text((fx + 2, fy + 50), "CN  ·  RU  ·  US", font=font("DejaVuSans-Bold.ttf", 15), fill=GREY)
yy = headline(LX + 24, LY + 52, "XI, PUTIN AND TRUMP TO MEET IN SHENZHEN", F_BIG, 680)
deck(LX + 24, LY + 158,
     "First-ever trilateral summit set for Thursday as Xi and Putin open talks "
     "on the eve of APEC \u2014 with Ukraine, Iran and trade on the table.",
     900, F_DECK_S)
d.text((LX + 24, LY + LH - 34), "APEC OPENS IN SHENZHEN  ·  QUAD MEETS IN MANILA",
       font=font("DejaVuSans-Bold.ttf", 15), fill=NAVY)

# ---------- row 1 ----------
RY, RH = 448, 248
# Gulf panel
GX, GW = 36, 466
panel(GX, RY, GW, RH, NAVY)
kicker(GX + 20, RY + 20, "THE GULF", NAVY)
yy = headline(GX + 20, RY + 48, "U.S. SINKS FIVE IRANIAN TANKERS", F_HEAD_S, GW - 40)
deck(GX + 20, yy + 4,
     "Tehran hits back at ships and a Jordan base; oil nears $93 as "
     "Hormuz shipping reels.", GW - 40, F_DECK_S)
# tanker pictogram
bx, by = GX + 20, RY + RH - 62
d.polygon([(bx, by + 18), (bx + 150, by + 18), (bx + 138, by + 40),
           (bx + 12, by + 40)], fill=(40, 40, 40))
d.rectangle([bx + 18, by, bx + 58, by + 18], fill=RED)
d.rectangle([bx + 64, by, bx + 104, by + 18], fill=NAVY)
d.polygon([(bx + 168, by + 18), (bx + 178, by - 14), (bx + 188, by + 18)],
          fill=(230, 120, 20))
d.polygon([(bx + 196, by + 18), (bx + 204, by - 6), (bx + 212, by + 18)],
          fill=(240, 170, 30))
d.line([bx, by + 48, bx + 220, by + 48], fill=(70, 130, 180), width=3)
# Kerch panel
KX, KW = 522, 466
panel(KX, RY, KW, RH, RED)
kicker(KX + 20, RY + 20, "UKRAINE", RED)
yy = headline(KX + 20, RY + 48, "KERCH BRIDGE HIT \u2014 SECOND NIGHT", F_HEAD_S, KW - 40)
deck(KX + 20, yy + 4,
     "Blasts shut the Crimea link as Russia strikes bridges of its own "
     "before Thursday's summit.", KW - 40, F_DECK_S)
# bridge pictogram
bx, by = KX + 20, RY + RH - 62
d.line([bx, by + 34, bx + 220, by + 34], fill=INK, width=5)
for px in (bx + 30, bx + 110, bx + 190):
    d.line([px, by + 34, px, by - 6], fill=INK, width=4)
    d.line([px, by - 6, px + 26, by + 34], fill=INK, width=2)
    d.line([px, by - 6, px - 26, by + 34], fill=INK, width=2)
d.polygon([(bx + 236, by + 10), (bx + 244, by - 16), (bx + 252, by + 10),
           (bx + 260, by - 16), (bx + 268, by + 10), (bx + 276, by - 16),
           (bx + 284, by + 10), (bx + 276, by + 30), (bx + 268, by + 10),
           (bx + 260, by + 30), (bx + 252, by + 10), (bx + 244, by + 30)],
          fill=(240, 160, 20))

# ---------- row 2 ----------
RY2, RH2 = 714, 222
# Senate panel
SX, SW = 36, 466
panel(SX, RY2, SW, RH2, TEAL)
kicker(SX + 20, RY2 + 20, "WASHINGTON", TEAL)
yy = headline(SX + 20, RY2 + 48, "PELTOLA FLIPS ALASKA", F_HEAD_S, SW - 40)
deck(SX + 20, yy + 4,
     "Democrat unseats Sullivan \u2014 the Senate is now 56\u201344 blue.",
     SW - 40, F_DECK_S)
# ballot box pictogram
bx, by = SX + 20, RY2 + RH2 - 56
d.rectangle([bx, by, bx + 90, by + 44], fill=TEAL, outline=INK, width=2)
d.rectangle([bx + 28, by + 8, bx + 62, by + 14], fill=PAPER)
d.line([bx + 100, by + 34, bx + 116, by + 46], fill=RED, width=6)
d.line([bx + 116, by + 46, bx + 142, by + 6], fill=RED, width=6)
d.text((bx + 160, by + 8), "56\u201344", font=font("DejaVuSans-Bold.ttf", 30), fill=INK)
# Cyclone panel
CX, CW = 522, 466
panel(CX, RY2, CW, RH2, NAVY)
kicker(CX + 20, RY2 + 20, "INDIA", NAVY)
yy = headline(CX + 20, RY2 + 48, "CYCLONE AKVAN BEARS DOWN", F_HEAD_S, CW - 40)
deck(CX + 20, yy + 4,
     "Severe storm heads for India's east coast; evacuations under way.",
     CW - 150, F_DECK_S)
# spiral pictogram (bottom-right corner, clear of the text)
cx, cy = CX + CW - 58, RY2 + RH2 - 52
for r, a0 in ((34, 0), (25, 60), (16, 120), (8, 180)):
    d.arc([cx - r, cy - r, cx + r, cy + r], a0, a0 + 300, fill=NAVY, width=5)

# ---------- footer ticker ----------
d.line([36, 952, 988, 952], fill=INK, width=2)
ticker = ("ALSO ON THE DAY:  COP31 enters its decisive phase  \u00b7  UN warns of Gaza cold deaths  "
          "\u00b7  Jesse Jackson dies at 84  \u00b7  Huang out at Nvidia  \u00b7  Dhoni retires  \u00b7  "
          "Pattinson is the new Bond")
lines = wrap(d, ticker, F_FOOT, 952)
yy = 964
for ln in lines:
    d.text((36, yy), ln, font=F_FOOT, fill=INK)
    yy += 22

img.save("entry.png")
print("saved entry.png", img.size)
