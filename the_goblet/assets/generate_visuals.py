# -*- coding: utf-8 -*-
"""Generate local SVG artwork for The Goblet website.

No external image service and no photography required. All artwork is vector,
so it stays sharp on phones and desktops and adds almost no page weight.
Run: python generate_visuals.py
"""

from pathlib import Path

OUT = Path(__file__).resolve().parent / "img"
OUT.mkdir(parents=True, exist_ok=True)

# Traditional Irish pub palette.
GREEN_DEEP = "#0A1C15"
GREEN = "#123326"
GREEN_LIGHT = "#1B4A35"
WOOD_DARK = "#3A2416"
WOOD = "#6B452A"
WOOD_LIGHT = "#9A6C42"
BRASS = "#C8A45C"
BRASS_LIGHT = "#E7C888"
CREAM = "#F6EBD6"
STOUT = "#140E0A"
FOAM = "#F3E7CE"


def defs_common():
    return f"""
  <linearGradient id="wood" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{WOOD_DARK}"/>
    <stop offset=".5" stop-color="{WOOD}"/>
    <stop offset="1" stop-color="#2B1A10"/>
  </linearGradient>
  <linearGradient id="stout" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#0A0706"/>
    <stop offset=".28" stop-color="#241812"/>
    <stop offset=".62" stop-color="#1B120D"/>
    <stop offset="1" stop-color="#080504"/>
  </linearGradient>
  <linearGradient id="foam" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#FFF9EC"/>
    <stop offset=".6" stop-color="{FOAM}"/>
    <stop offset="1" stop-color="#DBC7A4"/>
  </linearGradient>
  <linearGradient id="brass" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#8A6A31"/>
    <stop offset=".35" stop-color="{BRASS_LIGHT}"/>
    <stop offset=".7" stop-color="{BRASS}"/>
    <stop offset="1" stop-color="#6E5226"/>
  </linearGradient>
  <radialGradient id="glow" cx=".5" cy=".42" r=".62">
    <stop offset="0" stop-color="#F0C77A" stop-opacity=".42"/>
    <stop offset=".55" stop-color="#C88F45" stop-opacity=".16"/>
    <stop offset="1" stop-color="#C88F45" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="glass" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#FFFFFF" stop-opacity=".30"/>
    <stop offset=".18" stop-color="#FFFFFF" stop-opacity=".06"/>
    <stop offset=".8" stop-color="#FFFFFF" stop-opacity="0"/>
    <stop offset="1" stop-color="#FFFFFF" stop-opacity=".18"/>
  </linearGradient>
  <filter id="grain">
    <feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="3" stitchTiles="stitch"/>
    <feColorMatrix type="saturate" values="0"/>
  </filter>
  <filter id="soft"><feGaussianBlur stdDeviation="18"/></filter>
"""


def clover(x, y, s, fill=BRASS, opacity=".9"):
    """A small three-leaf clover made of circles and paths."""
    return f"""
  <g transform="translate({x} {y}) scale({s})" opacity="{opacity}" fill="{fill}">
    <circle cx="-9" cy="-6" r="9"/><circle cx="9" cy="-6" r="9"/>
    <circle cx="0" cy="8" r="9"/>
    <path d="M0 12 C1 24 5 30 9 34" fill="none" stroke="{fill}" stroke-width="3" stroke-linecap="round"/>
  </g>"""


def wood_planks(x, y, w, h, count=13):
    parts = []
    for i in range(count):
        px = x + (w / count) * i
        op = 0.05 + (i % 4) * 0.025
        parts.append(
            f'<rect x="{px:.1f}" y="{y}" width="1.6" height="{h}" fill="#000" opacity="{op:.2f}"/>'
        )
    return "".join(parts)


def pint_art():
    w, h = 620, 780
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Illustration of a pint of stout on a wooden bar">
<defs>{defs_common()}
  <clipPath id="arch"><path d="M42 770 V262 C42 128 148 34 310 34 C472 34 578 128 578 262 V770 Z"/></clipPath>
</defs>

<rect width="{w}" height="{h}" fill="{GREEN_DEEP}"/>
<rect x="16" y="16" width="{w-32}" height="{h-32}" rx="8" fill="none" stroke="{BRASS}" stroke-opacity=".35" stroke-width="1.5"/>

<g clip-path="url(#arch)">
  <rect x="42" y="34" width="536" height="736" fill="url(#wood)"/>
  {wood_planks(42, 34, 536, 700)}
  <ellipse cx="310" cy="300" rx="300" ry="290" fill="url(#glow)"/>

  <!-- suggestion of a back bar with shelves and bottles -->
  <g opacity=".45">
    <rect x="70" y="150" width="480" height="7" fill="{WOOD_LIGHT}"/>
    <rect x="70" y="232" width="480" height="7" fill="{WOOD_LIGHT}"/>
  </g>
  <g fill="#1A1009" opacity=".6">
    <rect x="96" y="96" width="18" height="54" rx="5"/><rect x="126" y="108" width="16" height="42" rx="4"/>
    <rect x="466" y="96" width="18" height="54" rx="5"/><rect x="496" y="110" width="15" height="40" rx="4"/>
    <rect x="150" y="180" width="17" height="52" rx="5"/><rect x="446" y="184" width="17" height="48" rx="5"/>
  </g>

  <!-- hanging glasses -->
  <g stroke="{CREAM}" stroke-opacity=".32" stroke-width="2" fill="none">
    <path d="M210 106 v56 c0 22 12 34 24 34 s24-12 24-34 v-56"/>
    <path d="M362 106 v56 c0 22 12 34 24 34 s24-12 24-34 v-56"/>
  </g>

  <!-- warm lamp -->
  <circle cx="310" cy="118" r="9" fill="{BRASS_LIGHT}"/>
  <path d="M268 128 h84 l-16-28 h-52 Z" fill="url(#brass)"/>
  <ellipse cx="310" cy="150" rx="120" ry="70" fill="#FFD58A" opacity=".10" filter="url(#soft)"/>

  <!-- bar counter in perspective -->
  <path d="M42 592 H578 V770 H42 Z" fill="url(#wood)"/>
  <path d="M42 592 H578 V606 H42 Z" fill="{WOOD_LIGHT}" opacity=".75"/>
  {wood_planks(42, 606, 536, 164, 9)}

  <!-- the pint -->
  <g>
    <ellipse cx="310" cy="694" rx="128" ry="24" fill="#000" opacity=".45"/>
    <path d="M214 356 L226 660 Q228 684 254 686 H366 Q392 684 394 660 L406 356 Z" fill="url(#stout)"/>
    <path d="M214 356 L226 660 Q228 684 254 686 H366 Q392 684 394 660 L406 356 Z" fill="url(#glass)"/>
    <!-- cream head, slightly domed and overflowing -->
    <path d="M210 356 C210 330 230 316 258 322 C274 302 300 300 314 314 C334 296 364 306 370 326 C392 322 408 336 406 358 C404 376 380 382 310 382 C240 382 212 374 210 356 Z" fill="url(#foam)"/>
    <path d="M226 350 C246 340 268 348 286 342 C310 334 330 348 352 342 C370 338 384 344 392 352" fill="none" stroke="#FFFDF6" stroke-opacity=".7" stroke-width="3" stroke-linecap="round"/>
    <!-- glass highlights -->
    <path d="M232 392 L242 646" stroke="#FFF" stroke-opacity=".20" stroke-width="10" stroke-linecap="round"/>
    <path d="M386 400 L380 620" stroke="#FFF" stroke-opacity=".10" stroke-width="6" stroke-linecap="round"/>
    <ellipse cx="310" cy="686" rx="84" ry="11" fill="#000" opacity=".3"/>
  </g>
</g>

<!-- brass arch outline -->
<path d="M42 770 V262 C42 128 148 34 310 34 C472 34 578 128 578 262 V770" fill="none" stroke="url(#brass)" stroke-width="5"/>
<path d="M58 770 V262 C58 138 156 50 310 50 C464 50 562 138 562 262 V770" fill="none" stroke="{BRASS}" stroke-opacity=".35" stroke-width="1.2"/>
{clover(310, 740, .72, BRASS, .85)}
<rect width="{w}" height="{h}" filter="url(#grain)" opacity=".045"/>
</svg>"""
    return svg


def pub_scene():
    w, h = 900, 600
    bottles = []
    for i in range(16):
        bx = 596 + (i % 8) * 31
        by = 208 if i < 8 else 320
        bh = 44 + (i % 3) * 9
        bottles.append(
            f'<rect x="{bx}" y="{by-bh}" width="15" height="{bh}" rx="4" fill="#160D08" opacity=".85"/>'
        )
    glasses = []
    for i in range(6):
        gx = 150 + i * 42
        glasses.append(
            f'<path d="M{gx} 88 v42 c0 17 8 26 16 26 s16-9 16-26 V88" fill="none" stroke="{CREAM}" stroke-opacity=".35" stroke-width="2"/>'
        )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Illustration of a traditional Irish pub interior with a fireplace and brass bar">
<defs>{defs_common()}
  <linearGradient id="fire" x1="0" y1="1" x2="0" y2="0">
    <stop offset="0" stop-color="#E06A1F"/><stop offset=".5" stop-color="#F2A53C"/><stop offset="1" stop-color="#F6D98A"/>
  </linearGradient>
</defs>

<rect width="{w}" height="{h}" fill="{GREEN_DEEP}"/>
<rect x="0" y="0" width="{w}" height="474" fill="url(#wood)"/>
{wood_planks(0, 0, w, 474, 20)}
<ellipse cx="450" cy="240" rx="420" ry="250" fill="url(#glow)"/>

<!-- fireplace -->
<path d="M62 474 V212 C62 130 126 70 206 70 C286 70 350 130 350 212 V474 Z" fill="#241610"/>
<path d="M84 474 V216 C84 144 138 94 206 94 C274 94 328 144 328 216 V474 Z" fill="#120B07"/>
<path d="M120 474 V300 C120 252 158 226 206 226 C254 226 292 252 292 300 V474 Z" fill="#0A0604"/>
<path d="M150 474 C146 424 178 404 190 370 C198 402 224 402 226 440 C240 410 258 402 262 376 C282 412 268 452 260 474 Z" fill="url(#fire)" opacity=".92"/>
<ellipse cx="206" cy="420" rx="90" ry="80" fill="#F4A33C" opacity=".18" filter="url(#soft)"/>
<rect x="46" y="466" width="320" height="18" rx="4" fill="url(#brass)"/>

<!-- shelves and bottles -->
<g opacity=".7"><rect x="566" y="224" width="310" height="8" fill="{WOOD_LIGHT}"/><rect x="566" y="336" width="310" height="8" fill="{WOOD_LIGHT}"/></g>
{''.join(bottles)}
{''.join(glasses)}

<!-- hanging lamps -->
<g>
  <path d="M424 0 v58"/><path d="M604 0 v92"/>
  <path d="M392 58 h64 l-12-24 h-40 Z" fill="url(#brass)"/>
  <path d="M572 92 h64 l-12-24 h-40 Z" fill="url(#brass)"/>
  <ellipse cx="424" cy="82" rx="76" ry="58" fill="#FFD88F" opacity=".12" filter="url(#soft)"/>
  <ellipse cx="604" cy="116" rx="76" ry="58" fill="#FFD88F" opacity=".12" filter="url(#soft)"/>
</g>

<!-- brass beer taps -->
<g transform="translate(470 300)">
  <rect x="0" y="0" width="10" height="96" fill="url(#brass)"/>
  <rect x="60" y="0" width="10" height="96" fill="url(#brass)"/>
  <rect x="-12" y="-16" width="34" height="18" rx="4" fill="url(#brass)"/>
  <rect x="48" y="-16" width="34" height="18" rx="4" fill="url(#brass)"/>
  <path d="M-28 -8 h10 v26 h18" fill="none" stroke="url(#brass)" stroke-width="6" stroke-linejoin="round"/>
  <path d="M92 -8 h-10 v26 h-18" fill="none" stroke="url(#brass)" stroke-width="6" stroke-linejoin="round"/>
</g>

<!-- bar counter -->
<path d="M0 474 H900 V600 H0 Z" fill="url(#wood)"/>
<rect x="0" y="470" width="900" height="16" fill="{WOOD_LIGHT}"/>
<rect x="0" y="486" width="900" height="4" fill="#000" opacity=".3"/>
{wood_planks(0, 490, w, 110, 12)}

<rect width="{w}" height="{h}" filter="url(#grain)" opacity=".05"/>
</svg>"""
    return svg


def clover_mark():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 80" width="80" height="80" role="img" aria-label="Three leaf clover">
{clover(40, 28, 1.55, BRASS, 1)}
</svg>"""
    return svg


def pint_mobile():
    """Tight crop around the glass itself for small phone screens."""
    svg = pint_art()
    svg = svg.replace('viewBox="0 0 620 780" width="620" height="780"',
                      'viewBox="150 268 320 452" width="320" height="452"')
    return svg


if __name__ == "__main__":
    for name, content in {
        "pint.svg": pint_art(),
        "pint-mobile.svg": pint_mobile(),
        "pub-interior.svg": pub_scene(),
        "clover.svg": clover_mark(),
    }.items():
        p = OUT / name
        p.write_text(content.strip(), encoding="utf-8")
        print("wrote", p.relative_to(OUT.parent.parent), len(content), "bytes")
