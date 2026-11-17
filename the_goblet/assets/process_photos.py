"""Process the user-supplied Google Maps photos into optimized WebP assets.

Usage:  C:/Python311/python.exe assets/process_photos.py
"""
import os
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "photos")
OUT = os.path.join(HERE, "img")
os.makedirs(OUT, exist_ok=True)


def enhance(im, contrast=1.08, color=1.1, sharp=90):
    im = ImageEnhance.Contrast(im).enhance(contrast)
    im = ImageEnhance.Color(im).enhance(color)
    im = ImageEnhance.Sharpness(im).enhance(1.15)
    if sharp:
        im = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=sharp, threshold=3))
    return im


def save(im, name, quality=88):
    path = os.path.join(OUT, name)
    im.save(path, "WEBP", quality=quality, method=6)
    print(name, im.size, str(round(os.path.getsize(path) / 1024)) + "KB")


# 1) Guinness three-pint hero — keep full portrait, gentle enhancement.
guinness = Image.open(os.path.join(SRC, "unnamed (2).jpg")).convert("RGB")
save(enhance(guinness), "hero-guinness.webp")

# 2) Beer glasses — gentle enhancement.
beer = Image.open(os.path.join(SRC, "unnamed (3).jpg")).convert("RGB")
save(enhance(beer), "beer-pints.webp")

# 3) Pub front — crop off the translucent "Google" watermark in the sky (top ~100px of 298)
front = Image.open(os.path.join(SRC, "thumbnail.jpg")).convert("RGB")
w, h = front.size
front = front.crop((0, int(h * 0.34), w, h))  # remove watermarked sky
save(enhance(front, contrast=1.05, color=1.08), "pub-front.webp")

print("done")
