"""Process user-supplied Google Maps photos into optimized WebP assets.
Usage: C:/Python311/python.exe assets/process_photos.py
"""
import os
from PIL import Image, ImageEnhance, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "photos")
OUT = os.path.join(HERE, "img")
os.makedirs(OUT, exist_ok=True)


def enhance(im, contrast=1.08, color=1.08, bright=1.0, sharp=80):
    im = ImageEnhance.Contrast(im).enhance(contrast)
    im = ImageEnhance.Color(im).enhance(color)
    if bright != 1.0:
        im = ImageEnhance.Brightness(im).enhance(bright)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=sharp, threshold=3))
    return im


def save(im, name, quality=88):
    path = os.path.join(OUT, name)
    im.save(path, "WEBP", quality=quality, method=6)
    print(name, im.size, str(round(os.path.getsize(path) / 1024)) + "KB")


# hero: beer taps + fiddle on the wall — the soul of this pub
hero = Image.open(os.path.join(SRC, "unnamed (3).jpg")).convert("RGB")
save(enhance(hero, contrast=1.1, color=1.08, bright=1.02), "hero-taps.webp")

# the pub: real interior with a pint and corkboard
pub = Image.open(os.path.join(SRC, "unnamed (1).jpg")).convert("RGB")
save(enhance(pub, contrast=1.08, color=1.06), "pub-bar.webp")

# live section background: four craft cans with warm string lights
amb = Image.open(os.path.join(SRC, "unnamed.jpg")).convert("RGB")
save(enhance(amb, contrast=1.05, color=1.05), "live-ambience.webp")

# find-us strip: hand-drawn PIPERS CORNER sign with a treble clef
sign = Image.open(os.path.join(SRC, "unnamed (4).jpg")).convert("RGB")
save(enhance(sign, contrast=1.1, color=1.05), "pub-sign.webp")

# find-us strip: pouring a Kinnegar craft beer
pour = Image.open(os.path.join(SRC, "unnamed (2).jpg")).convert("RGB")
save(enhance(pour, contrast=1.06, color=1.06), "pouring.webp")

print("done")
