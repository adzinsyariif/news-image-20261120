#!/usr/bin/env python3
"""Compose the 20 November 2026 front page.

One broadsheet page, top to bottom: the nameplate, a black dateline
strip, the market-crash artwork, a crimson headline band carrying the
day's lead story, and a dark 4-by-2 grid of the other stories. All
lettering is drawn with PIL so it stays sharp; the plunging-chart
scene is the only generated art.

The lead is the global sell-off: Wall Street fell for a fifth straight
session on Thursday and Tokyo's Nikkei dropped 4.8% on Friday as the
AI trade shuddered a day after Anthropic's record debut. Around it:
the Shenzhen summit's symbolism-rich, breakthrough-free aftermath,
overnight strikes on Kyiv's bridges, Russian objects in Polish
airspace, another Houthi barrage intercepted over Riyadh, Italy's
EUR 805 million fine on Meta, the FAA ground stop, President Prabowo's
return with nearly Rp1,600 trillion in investment pledges, and Kenya
discharging its last Ebola patient.
"""
import os

from PIL import Image, ImageDraw, ImageFont, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
MARKET_ART = (
    "/home/hatch/workspace/makefun/news-art-20/"
    "media-generation-news-hero-markets-20-0-8546d180-0fe0-4d7f-b145-999ff4a1a710.webp"
)
OUT_PATH = os.path.join(HERE, "entry.png")
SIZE_CAP = 1_048_576

FONTS = "/usr/share/fonts/truetype/liberation"
SERIF_BOLD = os.path.join(FONTS, "LiberationSerif-Bold.ttf")
SANS_BOLD = os.path.join(FONTS, "LiberationSans-Bold.ttf")
SANS = os.path.join(FONTS, "LiberationSans-Regular.ttf")

SIDE = 1024
PAPER = (246, 241, 233)
INK = (16, 16, 16)
GRID_BG = (15, 18, 23)
BAND = (146, 20, 20)
BAND_SUB = (255, 224, 166)
PAPER_WHITE = (255, 255, 255)
BODY_GREY = (203, 209, 217)
DIVIDER = (62, 68, 76)

HEADLINE = "MARKETS PLUNGE AS AI SELL-OFF DEEPENS"
SUBHEAD = "WALL ST FALLS A FIFTH DAY - NIKKEI OFF 4.8%"

# (headline, one-line summary, accent bar colour), in reading order.
PANELS = [
    ("SUMMIT OF SYMBOLS",
     "Trump, Xi, Putin: big symbolism, no breakthrough",
     (255, 196, 110)),
    ("KYIV BRIDGES STRUCK",
     "8 killed as missiles target the capital overnight",
     (255, 96, 96)),
    ("NATO AIRSPACE BREACHED",
     "Poland: 2 Russian missiles and a drone crossed in",
     (196, 164, 255)),
    ("RIYADH INTERCEPTS AGAIN",
     "Saudi defences down Houthi missile and 5 drones",
     (110, 186, 255)),
    ("ITALY FINES META EUR 805M",
     "Regulator: Android photo access broke the rules",
     (168, 232, 150)),
    ("FAA GROUNDS US FLIGHTS",
     "Ground stop strands 1.5 million travellers",
     (255, 170, 96)),
    ("PRABOWO'S RP1,600T HAUL",
     "President back with near Rp1,600 trillion in pledges",
     (255, 142, 196)),
    ("KENYA BEATS EBOLA",
     "Last patient discharged, 37 days after first case",
     (140, 224, 240)),
]


def load(size_path, size):
    return ImageFont.truetype(size_path, size)


def shrink_to_fit(draw, text, path, start_size, limit):
    """Biggest size at or under start_size that fits inside limit."""
    size = start_size
    while size > 10 and draw.textlength(text, font=load(path, size)) > limit:
        size -= 1
    return load(path, size)


def wrap(draw, text, face, limit):
    """Greedy word wrap, measured with real glyph widths."""
    lines, current = [], ""
    for word in text.split():
        trial = f"{current} {word}".strip()
        if draw.textlength(trial, font=face) <= limit:
            current = trial
        elif current:
            lines.append(current)
            current = word
        else:
            current = word
    if current:
        lines.append(current)
    return lines


def draw_panel(pen, index, grid_top, cell_w, cell_h):
    head, body, accent = PANELS[index]
    row, col = divmod(index, 4)
    left = col * cell_w
    top = grid_top + row * cell_h
    pen.rectangle([left + 10, top + 10, left + cell_w - 10, top + 16],
                  fill=accent)
    if col:
        pen.line([left, top + 8, left, top + cell_h - 8], fill=DIVIDER)
    if row:
        pen.line([left + 8, top, left + cell_w - 8, top], fill=DIVIDER)
    head_face = load(SANS_BOLD, 20)
    body_face = load(SANS, 18)
    y = top + 24
    for line in wrap(pen, head, head_face, cell_w - 24)[:3]:
        pen.text((left + 12, y), line, font=head_face, fill=PAPER_WHITE)
        y += 24
    for line in wrap(pen, body, body_face, cell_w - 24)[:3]:
        pen.text((left + 12, y), line, font=body_face, fill=BODY_GREY)
        y += 22


def build():
    page = Image.new("RGB", (SIDE, SIDE), PAPER)
    pen = ImageDraw.Draw(page)

    # Nameplate and dateline.
    pen.text((SIDE / 2, 10), "THE WORLD IN ONE DAY",
             font=load(SERIF_BOLD, 60), fill=INK, anchor="ma")
    pen.rectangle([30, 78, SIDE - 30, 82], fill=INK)
    pen.rectangle([30, 85, SIDE - 30, 86], fill=INK)
    pen.rectangle([0, 92, SIDE, 122], fill=INK)
    pen.text((SIDE / 2, 107),
             "FRIDAY  \u2022  20 NOVEMBER 2026  \u2022  WORLD NEWS IN ONE IMAGE",
             font=load(SANS_BOLD, 20), fill=PAPER_WHITE, anchor="mm")

    # Crash artwork, centred on the plunging chart line.
    art_top, art_h = 122, 500
    art = Image.open(MARKET_ART).convert("RGB")
    art = ImageOps.fit(art, (SIDE, art_h), method=Image.LANCZOS,
                       centering=(0.5, 0.42))
    page.paste(art, (0, art_top))
    pen = ImageDraw.Draw(page)

    # Crimson headline band: the sell-off.
    band_top = art_top + art_h
    band_h = 100
    pen.rectangle([0, band_top, SIDE, band_top + band_h], fill=BAND)
    pen.text((SIDE / 2, band_top + 12), HEADLINE,
             font=shrink_to_fit(pen, HEADLINE, SERIF_BOLD, 40, SIDE - 40),
             fill=PAPER_WHITE, anchor="ma")
    pen.text((SIDE / 2, band_top + 62), SUBHEAD,
             font=load(SANS_BOLD, 25), fill=BAND_SUB, anchor="ma")

    # The eight other stories.
    grid_top = band_top + band_h
    pen.rectangle([0, grid_top, SIDE, SIDE], fill=GRID_BG)
    cell_w = SIDE // 4
    cell_h = (SIDE - grid_top) // 2
    for index in range(len(PANELS)):
        draw_panel(pen, index, grid_top, cell_w, cell_h)

    page.save(OUT_PATH, format="PNG", optimize=True)
    if os.path.getsize(OUT_PATH) > SIZE_CAP:
        # Same pixels, JPEG at q88: stays crisp and lands under the cap.
        page.save(OUT_PATH, format="JPEG", quality=88, optimize=True)
    print(f"wrote {OUT_PATH}: {page.size}, {os.path.getsize(OUT_PATH)} bytes")


if __name__ == "__main__":
    build()
