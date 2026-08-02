#!/usr/bin/env python3
"""Banner profil GitHub — bahasa visual sama dengan cover blog dan banner repo.

Kanvas 1200x300: lebih pendek dari cover blog karena README profil menampilkan
gambar apa adanya tanpa crop, jadi tidak perlu ruang aman untuk object-fit.
Semua elemen tetap di dalam kanvas.
"""
import random
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 300
PAPER = (244, 243, 239)
INK = (17, 17, 17)
GREY = (105, 105, 105)
RED = (214, 32, 28)

IMPACT = "/System/Library/Fonts/Supplemental/Impact.ttf"
DIN = "/System/Library/Fonts/Supplemental/DIN Condensed Bold.ttf"
MONO = "/System/Library/Fonts/Menlo.ttc"


def F(p, s, i=0):
    return ImageFont.truetype(p, s, index=i)


def fig_phone(a, cx, cy):
    """Ponsel dengan glyph terbuka di layar — subjek kerjanya, bukan avatar."""
    w, h = 150, 250
    a.rounded_rectangle([cx - w // 2, cy - h // 2, cx + w // 2, cy + h // 2], radius=26, fill=0)
    a.rounded_rectangle([cx - w // 2 + 12, cy - h // 2 + 22, cx + w // 2 - 12, cy + h // 2 - 26],
                        radius=12, fill=255)
    a.rounded_rectangle([cx - 22, cy - h // 2 + 9, cx + 22, cy - h // 2 + 17], radius=4, fill=255)
    # gembok terbuka di layar
    bx, by = cx, cy + 26
    a.rounded_rectangle([bx - 34, by - 6, bx + 34, by + 52], radius=8, fill=0)
    a.arc([bx - 30, by - 62, bx + 18, by - 14], start=180, end=360, fill=0, width=11)
    a.rectangle([bx - 30, by - 44, bx - 19, by - 4], fill=0)
    a.ellipse([bx - 8, by + 12, bx + 8, by + 28], fill=255)
    # Baris kode di atas gembok. Harus berhenti sebelum puncak shackle (by-62),
    # kalau tidak keduanya menyatu jadi satu gumpalan hitam.
    for i in range(3):
        y = cy - 78 + i * 14
        a.rectangle([cx - 44, y, cx + 44 - (i % 2) * 30, y + 5], fill=0)


def arrow(d, x, y, colour=INK, length=40):
    d.line([(x, y), (x + length - 12, y)], fill=colour, width=4)
    d.polygon([(x + length - 12, y - 6), (x + length - 12, y + 6), (x + length, y)], fill=colour)


def make(out, seed=7):
    random.seed(seed)
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    art = Image.new("L", (W, H), 255)
    fig_phone(ImageDraw.Draw(art), 1050, 138)
    art = art.convert("1", dither=Image.FLOYDSTEINBERG).convert("L")
    img.paste(Image.new("RGB", (W, H), INK), (0, 0), Image.eval(art, lambda v: 255 - v))

    d.text((40, 18), "ALVINHAYY", font=F(IMPACT, 96), fill=INK)

    tag = "OFFENSIVE SECURITY"
    tw = d.textlength(tag, font=F(DIN, 24))
    d.rectangle([42, 122, 64 + tw, 152], fill=INK)
    d.text((53, 125), tag, font=F(DIN, 22), fill=PAPER)

    d.text((44, 160), "MOBILE RE  ·  ANDROID  ·  RED TEAM AUTOMATION",
           font=F(DIN, 30), fill=INK)
    d.text((46, 196), "YOGYAKARTA, INDONESIA", font=F(DIN, 20), fill=GREY)
    d.line([(46, 220), (470, 220)], fill=INK, width=2)

    # Dua baris, dua sisi kerja: perkakas mobile dan orkestrator red team.
    for i, ln in enumerate([
        "$ ./create-avd.sh --api 36 --full   + SM-S921B  uid=0(root)",
        "$ reddelta run --target <scope>     + 22 agents  6 MCP",
    ]):
        d.text((46, 230 + i * 15), ln, font=F(MONO, 10), fill=GREY)

    for i, ln in enumerate([
        "$ getprop ro.product.model",
        "- sdk_gphone64_arm64",
        "+ SM-S921B",
    ]):
        col = RED if ln[:1] == "-" else INK if ln[:1] == "+" else GREY
        d.text((640, 40 + i * 16), ln, font=F(MONO, 11), fill=col)

    d.text((640, 118), "DETECTED", font=F(DIN, 38), fill=INK)
    aw = d.textlength("DETECTED", font=F(DIN, 38))
    arrow(d, 654 + aw, 138, length=34)
    d.text((700 + aw, 118), "BYPASSED", font=F(DIN, 38), fill=RED)
    d.text((642, 160), "EMULATOR DETECTION", font=F(MONO, 10), fill=RED)

    band, cell = 272, 7
    for y in range(band, H, cell):
        dens = ((y - band) / (H - band)) ** 1.3 * 0.8
        for x in range(0, W, cell):
            if random.random() < dens:
                d.rectangle([x, y, x + cell - 1, y + cell - 1],
                            fill=RED if random.random() < 0.35 else INK)
    for _ in range(55):
        x, y = random.randint(0, W), random.randint(258, band)
        if random.random() < (y - 258) / (band - 258):
            s = random.choice([4, 6])
            d.rectangle([x, y, x + s, y + s], fill=RED if random.random() < 0.4 else INK)

    img.save(out)
    print("  ", out, img.size)


if __name__ == "__main__":
    make(sys.argv[1])
