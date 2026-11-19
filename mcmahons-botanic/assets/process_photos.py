"""Process McMahon's Google Maps photos -> optimized WebP.
Source: ../_mc_hi/ (temporary, deleted after processing).
"""
from PIL import Image, ImageEnhance, ImageFilter
import os

SRC = r"C:/Users/chenyuwe/WorkBuddy/2026-11-12-13-49-18/_mc_hi"
OUT = os.path.join(os.path.dirname(__file__), "img")
os.makedirs(OUT, exist_ok=True)

# (source, output, target size, crop mode)  crop: 'cover' or 'none'
JOBS = [
    ("m_01.jpg", "hero-storefront.webp", (900, 1150), "cover"),   # green storefront - hero
    ("m_02.jpg", "food-bakes.webp",      (1200, 780), "cover"),   # icing pastries
    ("m_07.jpg", "coffee-iced.webp",     (900, 1050), "cover"),   # iced latte
    ("m_03.jpg", "courtyard.webp",       (900, 1100), "cover"),   # garden seating
    ("m_04.jpg", "coffee-outdoor.webp",  (900, 1100), "cover"),   # coffee cup outdoor
    ("m_00.jpg", "street-view.webp",     (1000, 700), "cover"),   # street corner storefront
]


def cover(im, size):
    w, h = im.size
    tw, th = size
    scale = max(tw / w, th / h)
    nw, nh = round(w * scale), round(h * scale)
    im = im.resize((nw, nh), Image.LANCZOS)
    x = (nw - tw) // 2
    y = (nh - th) // 2
    return im.crop((x, y, x + tw, y + th))


for src, out, size, mode in JOBS:
    p = os.path.join(SRC, src)
    im = Image.open(p).convert("RGB")
    if mode == "cover":
        im = cover(im, size)
    else:
        im = im.resize(size, Image.LANCZOS)
    im = ImageEnhance.Color(im).enhance(1.06)
    im = ImageEnhance.Contrast(im).enhance(1.04)
    im = ImageEnhance.Sharpness(im).enhance(1.1)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.0, percent=75, threshold=3))
    dest = os.path.join(OUT, out)
    im.save(dest, "WEBP", quality=84, method=6)
    print(out, im.size, str(round(os.path.getsize(dest) / 1024)) + "KB")
