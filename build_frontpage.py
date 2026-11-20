#!/usr/bin/env python3
"""
One Day - 20 November 2026: compose the front page.

The page is a single 1024x1024 broadsheet. From the top: a serif
nameplate, a dateline strip, the day's artwork (a red chart diving
across a wall of trading screens while two skylines watch), a crimson
band with the lead headline, a grid of eight further stories, and a
black ticker along the foot with four more. Every letter is rendered
here with PIL; the artwork is the only picture element.

Lead story: the sell-off. US shares closed lower for a fifth session
running on Thursday and Tokyo's Nikkei shed 4.8% on Friday, as the AI
trade wobbled a day after Anthropic's record-breaking market debut.
"""

import os

from PIL import Image, ImageDraw, ImageFont, ImageOps

BASE = os.path.dirname(os.path.abspath(__file__))
ARTWORK = os.path.join(
    "/home/hatch/workspace/makefun/news-art-20",
    "media-generation-news-hero-markets-20-0-8546d180-0fe0-4d7f-b145-999ff4a1a710.webp",
)
TARGET = os.path.join(BASE, "entry.png")
BYTE_LIMIT = 1024 * 1024

FONT_DIR = "/usr/share/fonts/truetype/liberation"
SERIF = os.path.join(FONT_DIR, "LiberationSerif-Bold.ttf")
SANS = os.path.join(FONT_DIR, "LiberationSans-Regular.ttf")
SANS_B = os.path.join(FONT_DIR, "LiberationSans-Bold.ttf")

W = 1024
CREAM = (247, 242, 234)
BLACK = (18, 18, 18)
CRIMSON = (148, 22, 22)
GOLD = (255, 225, 170)
WHITE = (255, 255, 255)
GRID = (14, 17, 22)
MIST = (200, 206, 214)
RULE = (60, 66, 74)

LEAD = "MARKETS PLUNGE AS AI SELL-OFF DEEPENS"
LEAD_SUB = "WALL ST FALLS A FIFTH DAY - NIKKEI OFF 4.8%"
DATELINE = "FRIDAY  \u2022  20 NOVEMBER 2026  \u2022  WORLD NEWS IN ONE IMAGE"

# Eight stories under the fold: (title, standfirst, tab colour).
STORIES = [
    ("SUMMIT OF SYMBOLS",
     "Trump, Xi, Putin: big symbolism, no breakthrough",
     (255, 199, 110)),
    ("KYIV BRIDGES STRUCK",
     "8 killed as missiles target the capital overnight",
     (255, 97, 97)),
    ("NATO AIRSPACE BREACHED",
     "Warsaw: 2 missiles and a drone crossed overnight",
     (199, 166, 255)),
    ("RIYADH INTERCEPTS AGAIN",
     "Saudi defences down Houthi missile and 5 drones",
     (110, 187, 255)),
    ("ITALY FINES META EUR 805M",
     "Regulator: Android photo access broke the rules",
     (170, 233, 150)),
    ("FAA GROUNDS US FLIGHTS",
     "Ground stop strands 1.5 million travellers",
     (255, 171, 97)),
    ("PRABOWO'S RP1,600T HAUL",
     "President back with near Rp1,600 trillion in pledges",
     (255, 143, 197)),
    ("KENYA BEATS EBOLA",
     "Last patient discharged, 37 days after first case",
     (140, 225, 241)),
]

TICKER = [
    "IMF: GLOBAL DEBT NEARS 100% OF WORLD GDP",
    "ESTONIA TO SHUT RUSSIAN BORDER FOR SIX MONTHS",
    "GTA VI SALES TOP $2.3 BILLION",
    "JAKARTA MINIMUM WAGE UP 7.1% TO RP6.1M",
]


def face(path, size):
    return ImageFont.truetype(path, size)


def fit_face(canvas, text, path, size, max_width):
    """Shrink from `size` until `text` fits `max_width`."""
    while size > 10:
        f = face(path, size)
        if canvas.textlength(text, font=f) <= max_width:
            return f
        size -= 1
    return face(path, size)


def fold_lines(canvas, text, fnt, max_width):
    """Split `text` into lines that fit `max_width`."""
    out, line = [], ""
    for word in text.split():
        trial = (line + " " + word).strip()
        if canvas.textlength(trial, font=fnt) <= max_width:
            line = trial
        elif line:
            out.append(line)
            line = word
        else:
            line = word
    if line:
        out.append(line)
    return out


def story_cell(canvas, slot, grid_y, cw, ch):
    title, standfirst, tab = STORIES[slot]
    r, c = divmod(slot, 4)
    x0 = c * cw
    y0 = grid_y + r * ch
    canvas.rectangle([x0 + 10, y0 + 10, x0 + cw - 10, y0 + 16], fill=tab)
    if c > 0:
        canvas.line([x0, y0 + 8, x0, y0 + ch - 8], fill=RULE)
    if r > 0:
        canvas.line([x0 + 8, y0, x0 + cw - 8, y0], fill=RULE)
    title_f = face(SANS_B, 20)
    body_f = face(SANS, 18)
    y = y0 + 24
    for ln in fold_lines(canvas, title, title_f, cw - 24)[:3]:
        canvas.text((x0 + 12, y), ln, font=title_f, fill=WHITE)
        y += 24
    for ln in fold_lines(canvas, standfirst, body_f, cw - 24)[:3]:
        canvas.text((x0 + 12, y), ln, font=body_f, fill=MIST)
        y += 22


def compose():
    page = Image.new("RGB", (W, W), CREAM)
    pen = ImageDraw.Draw(page)

    # Nameplate with its double rule, then the black dateline strip.
    pen.text((W // 2, 10), "THE WORLD IN ONE DAY",
             font=face(SERIF, 60), fill=BLACK, anchor="ma")
    pen.rectangle([30, 78, W - 30, 82], fill=BLACK)
    pen.rectangle([30, 85, W - 30, 86], fill=BLACK)
    pen.rectangle([0, 92, W, 122], fill=BLACK)
    pen.text((W // 2, 107), DATELINE,
             font=face(SANS_B, 20), fill=WHITE, anchor="mm")

    # The artwork: 480 px tall, cropped a little high so the chart's
    # final dive stays in frame.
    art = Image.open(ARTWORK).convert("RGB")
    art = ImageOps.fit(art, (W, 480), method=Image.LANCZOS,
                       centering=(0.5, 0.40))
    page.paste(art, (0, 122))
    pen = ImageDraw.Draw(page)

    # Crimson lead band.
    band_y = 122 + 480
    pen.rectangle([0, band_y, W, band_y + 90], fill=CRIMSON)
    pen.text((W // 2, band_y + 10), LEAD,
             font=fit_face(pen, LEAD, SERIF, 40, W - 40),
             fill=WHITE, anchor="ma")
    pen.text((W // 2, band_y + 58), LEAD_SUB,
             font=face(SANS_B, 24), fill=GOLD, anchor="ma")

    # Eight stories in a 4x2 grid.
    grid_y = band_y + 90
    grid_h = 972 - grid_y
    pen.rectangle([0, grid_y, W, 972], fill=GRID)
    for slot in range(len(STORIES)):
        story_cell(pen, slot, grid_y, W // 4, grid_h // 2)

    # Foot ticker: four more headlines on black, diamond-separated.
    pen.rectangle([0, 972, W, W], fill=BLACK)
    ticker_text = "  \u25c6  ".join(TICKER)
    pen.text((W // 2, 998), ticker_text,
             font=fit_face(pen, ticker_text, SANS_B, 19, W - 24),
             fill=GOLD, anchor="mm")

    page.save(TARGET, format="PNG", optimize=True)
    if os.path.getsize(TARGET) > BYTE_LIMIT:
        page.save(TARGET, format="JPEG", quality=88, optimize=True)
    print("entry.png:", page.size, os.path.getsize(TARGET), "bytes")


if __name__ == "__main__":
    compose()
