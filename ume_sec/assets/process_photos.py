"""Prepare the real salon photos for the website.

Originals stay in assets/photos/; optimised WebP derivatives go to assets/img/.
Two sources are deliberately excluded from prominent slots:
  * 890612267 carries a third-party Xiaohongshu watermark, not the studio's work.
  * 892017411 is a moving-in snapshot: empty shelves, a clipped "GOOD LUCK"
    balloon, a ring-light stand and a pastry box. It is kept in assets/photos/
    for a future reshoot, but the site is work-led instead.

Run:  python process_photos.py
"""
from pathlib import Path

from PIL import Image, ImageOps

BASE = Path(__file__).resolve().parent
SRC = BASE / "photos"
OUT = BASE / "img"
OUT.mkdir(exist_ok=True)


def original(prefix):
    matches = sorted(SRC.glob(prefix + "*"))
    if not matches:
        raise FileNotFoundError(f"No photo starting with {prefix}")
    return ImageOps.exif_transpose(Image.open(matches[0])).convert("RGB")


def emit(im, name, quality=86):
    path = OUT / name
    im.save(path, "WEBP", quality=quality, method=6)
    print(f"  {name:24s} {im.width}x{im.height}  {path.stat().st_size // 1024} KB")


def square(prefix, name, size=1100):
    im = original(prefix)
    emit(ImageOps.fit(im, (size, size), Image.LANCZOS, centering=(0.5, 0.5)), name)


def portrait(prefix, name, width, height, centering=(0.5, 0.5)):
    im = original(prefix)
    emit(ImageOps.fit(im, (width, height), Image.LANCZOS, centering=centering), name)


def custom(prefix, name, box, size, quality=84):
    im = original(prefix).crop(box)
    emit(im.resize(size, Image.LANCZOS), name, quality)


if __name__ == "__main__":
    print("Generating optimised images in", OUT)
    # Hero: the signature navy polka set on white fabric, cropped tall.
    portrait("658930229", "hero-main.webp", 900, 1120, (0.5, 0.48))
    # Hero accent: the sheer nude / silver linework set.
    square("657400623", "hero-accent.webp", 560)

    # Gallery: three distinct sets.
    square("660845997", "work-01.webp")
    square("658522961", "work-02.webp")
    square("670572148", "work-03.webp")

    # Studio section: a work-led composition (large portrait + detail accent).
    portrait("658930229", "studio-feature.webp", 900, 1125, (0.62, 0.60))
    custom("657400623", "studio-accent.webp", (360, 300, 1080, 1020), (560, 560))

    # Gallery wide tile: a clean horizontal band of the signature set instead
    # of the old thin strip of empty wall.
    emit(ImageOps.fit(original("658930229"), (1800, 820), Image.LANCZOS,
                      centering=(0.5, 0.58)), "work-banner.webp")

    # Social sharing preview.
    im = original("658930229")
    emit(ImageOps.fit(im, (1200, 630), Image.LANCZOS, centering=(0.5, 0.5)), "og-image.webp", 84)
    print("Done.")
