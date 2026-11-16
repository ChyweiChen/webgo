"""Generate the illustrative SVG artwork used by the Ume Nail Studio website.

These are stylised vector illustrations, NOT photographs of the real salon or
real client nails. Replace the .svg files with real photography before launch.

Run:  python generate_visuals.py
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent

CREAM = "#FBF8F3"
IVORY = "#F4EDE2"
SAND = "#E8DCCB"
GOLD = "#B99A6B"
GOLD_LIGHT = "#D9C39B"
NAVY = "#1B2A47"
NAVY_DEEP = "#12203A"
NUDE = "#E9C6B6"
NUDE_LIGHT = "#F6DED0"
SKIN = "#E4BBA0"
SKIN_DARK = "#CE9F82"
WHITE = "#FFFFFF"


def svg(w, h, body, extra_defs=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{CREAM}"/><stop offset="1" stop-color="{IVORY}"/>
  </linearGradient>
  <radialGradient id="glow" cx="50%" cy="35%" r="65%">
    <stop offset="0" stop-color="#FFFFFF" stop-opacity=".85"/>
    <stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="skin" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{SKIN_DARK}"/><stop offset=".42" stop-color="{SKIN}"/>
    <stop offset=".78" stop-color="#F0CFB6"/><stop offset="1" stop-color="{SKIN_DARK}"/>
  </linearGradient>
  <linearGradient id="navy" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#2B3E63"/><stop offset=".55" stop-color="{NAVY}"/>
    <stop offset="1" stop-color="{NAVY_DEEP}"/>
  </linearGradient>
  <linearGradient id="nude" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#FBEAE0"/><stop offset=".55" stop-color="{NUDE_LIGHT}"/>
    <stop offset="1" stop-color="{NUDE}"/>
  </linearGradient>
  <linearGradient id="milky" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#FFFFFF"/><stop offset=".6" stop-color="#F8F1E9"/>
    <stop offset="1" stop-color="#E9DAC9"/>
  </linearGradient>
  <pattern id="dots" width="27" height="27" patternUnits="userSpaceOnUse">
    <circle cx="8" cy="8" r="4.3" fill="{WHITE}" opacity=".95"/>
    <circle cx="21" cy="20" r="3.1" fill="{WHITE}" opacity=".88"/>
    <circle cx="24" cy="3" r="1.7" fill="{WHITE}" opacity=".7"/>
  </pattern>
  <pattern id="dotsFine" width="19" height="19" patternUnits="userSpaceOnUse">
    <circle cx="6" cy="6" r="3" fill="{WHITE}" opacity=".95"/>
    <circle cx="15" cy="15" r="2.2" fill="{WHITE}" opacity=".85"/>
  </pattern>
  <filter id="soft" x="-40%" y="-40%" width="180%" height="180%">
    <feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="#4A3B2A" flood-opacity=".16"/>
  </filter>
  <filter id="softSmall" x="-40%" y="-40%" width="180%" height="180%">
    <feDropShadow dx="0" dy="7" stdDeviation="8" flood-color="#4A3B2A" flood-opacity=".14"/>
  </filter>
  <filter id="grain" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency=".8" numOctaves="3" stitchTiles="stitch"/>
    <feColorMatrix type="saturate" values="0"/>
  </filter>
  {extra_defs}
</defs>
{body}
</svg>
'''


# One almond-shaped nail with a finger underneath.
# style: "navy" (navy + white polka dots), "french" (nude + white tip),
#        "milky" (milky white + gold line), "dotfrench" (nude + dotted tip)
def nail(cx, cy, rot, scale, style, uid, length=170):
    w = 100
    plate = ("M50 0 C21 26 1 68 1 108 C1 145 20 166 50 166 "
             "C80 166 99 145 99 108 C99 68 79 26 50 0 Z")
    tip = ("M50 0 C22 25 2 66 2 96 C18 78 33 72 50 72 "
           "C67 72 82 78 98 96 C98 66 78 25 50 0 Z")

    if style == "navy":
        fill = f'<path d="{plate}" fill="url(#navy)"/>' \
               f'<path d="{plate}" fill="url(#dots)" clip-path="url(#clip{uid})"/>'
        tip_mark = f'<path d="{tip}" fill="{WHITE}" opacity=".95"/>'
    elif style == "french":
        fill = f'<path d="{plate}" fill="url(#nude)"/>'
        tip_mark = (f'<path d="{tip}" fill="{WHITE}" opacity=".96"/>'
                    f'<path d="M6 99 C24 80 34 76 50 76 C66 76 79 80 94 99" '
                    f'fill="none" stroke="{GOLD}" stroke-width="1.6" opacity=".85"/>')
    elif style == "milky":
        fill = f'<path d="{plate}" fill="url(#milky)"/>'
        tip_mark = (f'<path d="{tip}" fill="{WHITE}" opacity=".5"/>'
                    f'<path d="M12 106 C30 88 38 84 50 84 C62 84 72 88 88 106" '
                    f'fill="none" stroke="{GOLD}" stroke-width="2.2"/>'
                    f'<circle cx="50" cy="112" r="3.2" fill="{GOLD}"/>')
    else:  # dotfrench — nude base with a navy dotted smile line
        fill = f'<path d="{plate}" fill="url(#nude)"/>'
        tip_mark = (f'<path d="{tip}" fill="url(#navy)"/>'
                    f'<path d="{tip}" fill="url(#dotsFine)"/>'
                    f'<path d="M50 0 C22 25 2 66 2 96 C18 78 33 72 50 72 '
                    f'C67 72 82 78 98 96 C98 66 78 25 50 0 Z" fill="none" '
                    f'stroke="{WHITE}" stroke-width="2" opacity=".7"/>')

    shine = ('<path d="M22 44 C14 66 10 88 11 112" fill="none" stroke="#FFFFFF" '
             'stroke-width="7" stroke-linecap="round" opacity=".22"/>')

    return f'''<g transform="translate({cx} {cy}) rotate({rot}) scale({scale})">
  <defs><clipPath id="clip{uid}"><path d="{plate}"/></clipPath></defs>
  <rect x="3" y="138" width="94" height="{length}" rx="46" fill="url(#skin)"/>
  <g filter="url(#softSmall)">
    {fill}
    {tip_mark}
    <path d="{plate}" fill="none" stroke="#FFFFFF" stroke-width="1.4" opacity=".5"/>
    {shine}
  </g>
</g>'''


def hero():
    w, h = 760, 980
    nails = [
        nail(120, 392, -17, 1.02, "navy", "h1", 300),
        nail(228, 318, -9, 1.10, "french", "h2", 340),
        nail(348, 286, -1, 1.16, "navy", "h3", 360),
        nail(472, 316, 9, 1.10, "dotfrench", "h4", 340),
        nail(582, 388, 17, 1.02, "french", "h5", 300),
    ]
    body = f'''
<rect width="{w}" height="{h}" fill="url(#bg)"/>
<circle cx="380" cy="400" r="330" fill="{WHITE}" opacity=".38"/>
<circle cx="380" cy="400" r="286" fill="none" stroke="{GOLD_LIGHT}" stroke-width="1.4" opacity=".8"/>
<circle cx="380" cy="400" r="304" fill="none" stroke="{GOLD_LIGHT}" stroke-width=".8" opacity=".5"/>
<ellipse cx="380" cy="905" rx="300" ry="42" fill="#B99A6B" opacity=".10"/>
{''.join(nails)}
<g fill="{GOLD}" opacity=".75">
  <path d="M108 208 l4 12 12 4 -12 4 -4 12 -4 -12 -12 -4 12 -4 z"/>
  <path d="M650 250 l3 9 9 3 -9 3 -3 9 -3 -9 -9 -3 9 -3 z"/>
  <circle cx="86" cy="520" r="3"/><circle cx="676" cy="578" r="3"/>
</g>
<rect width="{w}" height="{h}" filter="url(#grain)" opacity=".045"/>
'''
    (OUT / "hero-art.svg").write_text(svg(w, h, body), encoding="utf-8")


def work(filename, styles, title):
    w = h = 800
    parts = []
    positions = [(160, 250, -13, 1.18), (400, 190, 0, 1.30), (630, 260, 13, 1.18)]
    for i, st in enumerate(styles):
        x, y, r, s = positions[i]
        parts.append(nail(x, y, r, s, st, f"{filename}{i}", 330))
    body = f'''
<rect width="{w}" height="{h}" fill="url(#bg)"/>
<circle cx="400" cy="360" r="290" fill="{WHITE}" opacity=".45"/>
<circle cx="400" cy="360" r="250" fill="none" stroke="{GOLD_LIGHT}" stroke-width="1.2" opacity=".7"/>
<ellipse cx="400" cy="760" rx="290" ry="36" fill="#B99A6B" opacity=".10"/>
{''.join(parts)}
<rect width="{w}" height="{h}" filter="url(#grain)" opacity=".045"/>
'''
    (OUT / f"{filename}.svg").write_text(svg(w, h, body), encoding="utf-8")


def studio():
    w, h = 1200, 860
    # shelves of polish bottles inside an arched niche
    bottles = []
    palette = [NAVY, "#3A4E75", NUDE, "#F2E4D6", GOLD, "#8C9BB8"]
    for row in range(3):
        y = 268 + row * 96
        bottles.append(f'<rect x="176" y="{y+44}" width="196" height="9" rx="4" fill="#C4AE8F"/>')
        for col in range(9):
            x = 182 + col * 21
            c = palette[(row * 3 + col) % len(palette)]
            bottles.append(
                f'<rect x="{x}" y="{y+10}" width="13" height="34" rx="3" fill="{c}" opacity=".92"/>'
                f'<rect x="{x+3}" y="{y+5}" width="7" height="7" rx="2" fill="{GOLD}" opacity=".8"/>'
            )
    bottles = "".join(bottles)

    # wood grain lines on the floor
    grain_lines = "".join(
        f'<line x1="0" y1="{640 + i*34}" x2="1200" y2="{640 + i*34}" '
        f'stroke="#C4A985" stroke-width="1" opacity=".35"/>' for i in range(7)
    )
    planks = "".join(
        f'<line x1="{x}" y1="630" x2="{x-90}" y2="860" stroke="#C4A985" '
        f'stroke-width="1" opacity=".25"/>' for x in range(120, 1300, 210)
    )

    body = f'''
<rect width="{w}" height="{h}" fill="#EFE6D8"/>
<rect width="{w}" height="630" fill="#F3EBDF"/>
<circle cx="880" cy="90" r="230" fill="url(#glow)" opacity=".55"/>
<path d="M0 630 H1200 V860 H0 Z" fill="#DCC6A7"/>
{grain_lines}{planks}
<!-- arched niche -->
<path d="M140 470 V250 A134 134 0 0 1 408 250 V470 Z" fill="#E7D8C2"/>
<path d="M140 470 V250 A134 134 0 0 1 408 250 V470" fill="none" stroke="#C9B493" stroke-width="3"/>
{bottles}
<!-- floating shelves on the right -->
<rect x="880" y="250" width="230" height="10" rx="5" fill="#C9AE87"/>
<rect x="880" y="360" width="230" height="10" rx="5" fill="#C9AE87"/>
<g>
  <rect x="906" y="216" width="15" height="34" rx="3" fill="{NAVY}"/>
  <rect x="930" y="222" width="15" height="28" rx="3" fill="{NUDE}"/>
  <rect x="954" y="212" width="15" height="38" rx="3" fill="{GOLD}"/>
  <rect x="1000" y="220" width="15" height="30" rx="3" fill="#8C9BB8"/>
  <rect x="906" y="326" width="15" height="34" rx="3" fill="{GOLD}"/>
  <rect x="930" y="332" width="15" height="28" rx="3" fill="{NAVY}"/>
  <rect x="954" y="322" width="15" height="38" rx="3" fill="{NUDE}"/>
</g>
<!-- manicure table -->
<g filter="url(#soft)">
  <rect x="470" y="470" width="330" height="26" rx="12" fill="#FFFFFF"/>
  <rect x="492" y="496" width="22" height="150" rx="8" fill="#EFEFEF"/>
  <rect x="756" y="496" width="22" height="150" rx="8" fill="#EFEFEF"/>
</g>
<rect x="566" y="446" width="94" height="26" rx="7" fill="#F7F4EE"/>
<rect x="596" y="432" width="18" height="16" rx="5" fill="{NAVY}"/>
<circle cx="690" cy="458" r="9" fill="{GOLD}" opacity=".7"/>
<!-- chair -->
<g filter="url(#softSmall)">
  <path d="M820 500 q70 -40 140 0 l-8 96 q-62 -22 -124 0 z" fill="#F7F5F0"/>
  <rect x="818" y="592" width="144" height="20" rx="10" fill="#FFFFFF"/>
  <rect x="882" y="610" width="14" height="66" rx="6" fill="#DEDBD4"/>
  <path d="M845 676 h90 M889 676 v-64" stroke="#DEDBD4" stroke-width="9" stroke-linecap="round"/>
</g>
<!-- warm ceiling light -->
<circle cx="620" cy="70" r="13" fill="#FFF6E4"/>
<circle cx="620" cy="70" r="42" fill="#FFF3DC" opacity=".35"/>
<rect width="{w}" height="{h}" filter="url(#grain)" opacity=".05"/>
'''
    (OUT / "studio-art.svg").write_text(svg(w, h, body), encoding="utf-8")


if __name__ == "__main__":
    hero()
    work("work-navy", ["navy", "french", "navy"], "MIDNIGHT POLKA")
    work("work-french", ["french", "french", "french"], "SOFT FRENCH")
    work("work-milky", ["milky", "navy", "milky"], "MILKY & GOLD")
    studio()
    print("Generated:", ", ".join(sorted(p.name for p in OUT.glob("*.svg"))))
