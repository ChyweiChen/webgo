"""
Process high-resolution Google Maps photos into optimized WebP for the site.
Source: ../_hair_hi/ (downloaded from Google Maps photo CDN at 1200px).
Run: /c/Python311/python.exe assets/process_photos.py
"""
import os
from PIL import Image, ImageEnhance, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(os.path.dirname(ROOT), "_hair_hi")
DST = os.path.join(ROOT, "assets", "img")
os.makedirs(DST, exist_ok=True)

# (source, output, target_width, target_height or None, quality, crop)
# crop 'cover' -> center-crop to exact target aspect; 'fit' -> resize keeping aspect
JOBS = [
    ("h_00.jpg", "hero-storefront.webp", 1100, 1400, 85, "cover"),   # pink storefront -> hero
    ("h_01.jpg", "salon-interior.webp", 1200, 800, 84, "cover"),     # interior chairs+floral wall
    ("h_02.jpg", "colour-detail.webp", 900, 1200, 85, "cover"),      # foils/hair detail
    ("h_05.jpg", "wash-area.webp", 900, 1200, 84, "cover"),          # pink wall + basins
    ("h_06.jpg", "front-window.webp", 1200, 800, 84, "cover"),       # bright window seating
]

def cover(im, tw, th):
    w, h = im.size
    scale = max(tw / w, th / h)
    nw, nh = round(w * scale), round(h * scale)
    im = im.resize((nw, nh), Image.LANCZOS)
    x = (nw - tw) // 2; y = (nh - th) // 2
    return im.crop((x, y, x + tw, y + th))

for src, out, tw, th, q, mode in JOBS:
    p = os.path.join(SRC, src)
    if not os.path.exists(p):
        print("SKIP missing", src); continue
    im = Image.open(p).convert("RGB")
    if mode == "cover" and th:
        im = cover(im, tw, th)
    else:
        nh = round(im.height * tw / im.width)
        im = im.resize((tw, nh), Image.LANCZOS)
    im = ImageEnhance.Color(im).enhance(1.06)
    im = ImageEnhance.Contrast(im).enhance(1.04)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.1, percent=85, threshold=3))
    op = os.path.join(DST, out)
    im.save(op, "WEBP", quality=q, method=6)
    print(f"{out:24s} {im.size}  {round(os.path.getsize(op)/1024)}KB")
