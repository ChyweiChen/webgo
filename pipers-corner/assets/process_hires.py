"""
Process high-resolution Google Maps photos into optimized WebP for the site.
Source: _gmapshi/ (downloaded from Google Maps photo CDN at large sizes).
Run with: /c/Python311/python.exe assets/process_hires.py
"""
import os
from PIL import Image, ImageEnhance, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # project root
SRC = os.path.join(os.path.dirname(ROOT), "_gmapshi")               # sibling _gmapshi
DST = os.path.join(ROOT, "assets", "img")
os.makedirs(DST, exist_ok=True)

# (source file, output name, target width, height cap 0=auto, quality, crop mode)
# crop mode: 'contain' -> keep full frame resized; 'portrait' -> center-crop to portrait for hero
JOBS = [
    ("gp_2.jpg",  "hero-session.webp",  900,  None, 84),   # vertical live session -> hero
    ("hi_3.jpg",  "pub-sign-hd.webp",   768,  None, 84),    # PIPERS mural + sign (door/front)
    ("gp_3.jpg",  "live-session.webp",  1400, None, 82),    # wide trad session w/ xmas lights
    ("hi_5.jpg",  "blackboard-hd.webp", 900,  None, 84),    # hand-drawn blackboard menu
    ("gp_0.jpg",  "musician-hd.webp",   1200, None, 83),    # fiddle/tin whistle player close-up
    ("gp_1.jpg",  "session-row.webp",   1200, None, 83),    # row of musicians
    ("hi_4.jpg",  "session-portrait.webp", 900, None, 83),  # vertical session
    ("hi_2.jpg",  "food-pizza.webp",    1100, None, 82),    # pizza (food offering)
]

for src, out, tw, th, q in JOBS:
    p = os.path.join(SRC, src)
    if not os.path.exists(p):
        print("SKIP (missing)", src); continue
    im = Image.open(p).convert("RGB")
    w, h = im.size
    if th:
        im.thumbnail((tw, th), Image.LANCZOS)
    else:
        nh = round(h * tw / w)
        im = im.resize((tw, nh), Image.LANCZOS)
    # gentle enhancement for MDPI photos
    im = ImageEnhance.Contrast(im).enhance(1.05)
    im = ImageEnhance.Color(im).enhance(1.08)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=90, threshold=3))
    op = os.path.join(DST, out)
    im.save(op, "WEBP", quality=q, method=6)
    print(f"{out:24s} {im.size}  {round(os.path.getsize(op)/1024)}KB  (from {w}x{h})")
