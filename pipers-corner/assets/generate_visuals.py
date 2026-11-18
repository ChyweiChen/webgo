"""Generate local SVG illustrations for the Pipers Corner site.
Theme: traditional Irish live music + a proper pint. No external images.
Run: C:/Python311/python.exe assets/generate_visuals.py
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "img")
os.makedirs(OUT, exist_ok=True)


def write(name, svg):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(svg.strip())
    print("wrote", name)


# ---------------------------------------------------------------- clover logo
clover = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <g fill="none" stroke="#C8A45C" stroke-width="2.4" stroke-linejoin="round">
    <path d="M32 30c-3-7-12-9-16-3-4 6 1 12 8 11 3 0 5-2 8-4Z"/>
    <path d="M32 30c7-3 9-12 3-16-6-4-12 1-11 8 0 3 2 5 4 8Z"/>
    <path d="M32 30c3 7 12 9 16 3 4-6-1-12-8-11-3 0-5 2-8 4Z"/>
    <path d="M32 30c-7 3-9 12-3 16 6 4 12-1 11-8 0-3-2-5-4-8Z"/>
    <path d="M32 30c1 6 2 12 0 20-1 4-4 6-6 8"/>
  </g>
</svg>
"""
write("clover.svg", clover)

# ---------------------------------------------------------------- hero (desktop): fiddle + notes + pint
hero = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 800" width="620" height="800">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#163B2B"/>
      <stop offset="1" stop-color="#0A1C15"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="30%" r="60%">
      <stop offset="0" stop-color="#E7C888" stop-opacity=".42"/>
      <stop offset="1" stop-color="#E7C888" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="gold" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F0DCA6"/>
      <stop offset=".5" stop-color="#C8A45C"/>
      <stop offset="1" stop-color="#A97F38"/>
    </linearGradient>
    <linearGradient id="stout" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#3A2012"/>
      <stop offset=".45" stop-color="#1C0E07"/>
      <stop offset="1" stop-color="#0B0503"/>
    </linearGradient>
    <linearGradient id="glass" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#ffffff" stop-opacity=".28"/>
      <stop offset=".15" stop-color="#ffffff" stop-opacity=".05"/>
      <stop offset=".85" stop-color="#ffffff" stop-opacity=".05"/>
      <stop offset="1" stop-color="#ffffff" stop-opacity=".22"/>
    </linearGradient>
    <linearGradient id="head" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#FFF6E2"/>
      <stop offset="1" stop-color="#E4D2AC"/>
    </linearGradient>
  </defs>

  <rect width="620" height="800" rx="6" fill="url(#bg)"/>
  <rect width="620" height="800" rx="6" fill="url(#glow)"/>
  <rect x="14" y="14" width="592" height="772" rx="3" fill="none" stroke="#C8A45C" stroke-opacity=".5" stroke-width="1.5"/>

  <!-- floating notes -->
  <g fill="url(#gold)" opacity=".92">
    <g transform="translate(150 150) rotate(-12)"><ellipse cx="0" cy="34" rx="13" ry="9"/><rect x="10" y="-4" width="4" height="40"/><path d="M14 -4c18 4 26 14 22 30 2-14-6-22-22-24Z"/></g>
    <g transform="translate(470 110) rotate(10)"><ellipse cx="0" cy="34" rx="11" ry="8"/><rect x="8" y="0" width="3.5" height="36"/><path d="M11.5 0c15 3 22 12 18 26 2-12-5-19-18-21Z"/></g>
    <g transform="translate(505 250) rotate(-8)"><ellipse cx="0" cy="24" rx="9" ry="6.5"/><rect x="6.5" y="-8" width="3" height="34"/></g>
    <g transform="translate(112 268) rotate(15)"><ellipse cx="0" cy="24" rx="8" ry="6"/><rect x="5.5" y="-6" width="2.8" height="32"/></g>
  </g>

  <!-- fiddle: elegant gold line-art, tilted -->
  <g transform="translate(310 250) rotate(-16)">
    <g fill="none" stroke="url(#gold)" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
      <!-- upper & lower bouts -->
      <path d="M0 -40c-30 -4 -46 12 -44 36 1 18 14 28 30 33 -22 10 -34 28 -32 52 2 30 26 52 46 52s44 -22 46 -52c2 -24 -10 -42 -32 -52 16 -5 29 -15 30 -33 2 -24 -14 -40 -44 -36Z"/>
      <!-- neck -->
      <path d="M-9 -40 L-9 -128 M9 -40 L9 -128"/>
      <!-- scroll / pegbox -->
      <path d="M-11 -128 L-13 -160 Q0 -176 13 -160 L11 -128"/>
      <circle cx="-13" cy="-150" r="3.5" fill="#C8A45C"/>
      <circle cx="13" cy="-150" r="3.5" fill="#C8A45C"/>
      <circle cx="-11" cy="-138" r="3.5" fill="#C8A45C"/>
      <circle cx="11" cy="-138" r="3.5" fill="#C8A45C"/>
      <!-- f holes -->
      <path d="M-22 4 q-8 12 0 24 M-22 4 l6 -3 M-22 28 l6 3" stroke-width="3"/>
      <path d="M22 4 q8 12 0 24 M22 4 l-6 -3 M22 28 l-6 3" stroke-width="3"/>
      <!-- strings -->
      <path d="M-5 -160 L-5 70 M-1.5 -160 L-1.5 70 M1.5 -160 L1.5 70 M5 -160 L5 70" stroke-width="1.3" opacity=".8"/>
      <!-- bridge -->
      <path d="M-20 60 q20 -10 40 0" stroke-width="3"/>
    </g>
    <!-- bow -->
    <g transform="translate(0 66) rotate(-9)">
      <path d="M-120 0 L130 0" stroke="url(#gold)" stroke-width="5" stroke-linecap="round"/>
      <path d="M-118 4 L128 4" stroke="#EFE3C4" stroke-width="2" stroke-linecap="round" opacity=".85"/>
      <rect x="-126" y="-6" width="12" height="18" rx="2" fill="#3A2416" stroke="#C8A45C" stroke-width="1.5"/>
    </g>
  </g>

  <!-- pint of stout -->
  <g transform="translate(310 610)">
    <!-- glass body -->
    <path d="M-92 -70 L92 -70 L74 128 Q0 140 -74 128 Z" fill="url(#glass)"/>
    <!-- stout -->
    <path d="M-86 -46 L86 -46 L70 122 Q0 133 -70 122 Z" fill="url(#stout)"/>
    <!-- creamy head -->
    <path d="M-88 -46 q10 -16 24 -8 q12 -14 28 -4 q14 -16 30 -3 q16 -13 30 2 q14 -8 26 6 q-4 10 -18 8 q-16 6 -30 -2 q-16 8 -32 0 q-16 8 -32 -1 q-14 7 -26 -2 Z" fill="url(#head)"/>
    <!-- harp mark -->
    <g transform="translate(0 30) scale(.9)" fill="#E7C888" opacity=".9">
      <path d="M-22 -26 h7 v44 h-7 Z"/>
      <path d="M-8 -30 h5 v48 h-5 Z"/>
      <path d="M6 -28 h5 v46 h-5 Z"/>
      <path d="M18 -24 h6 v42 h-6 Z"/>
      <path d="M-26 -28 h52 v6 h-52 Z"/>
      <path d="M-4 -30 q10 -10 20 0 q-10 -4 -20 2 Z"/>
    </g>
    <!-- glass highlights -->
    <path d="M-74 -40 L-60 112" stroke="#ffffff" stroke-opacity=".3" stroke-width="7" stroke-linecap="round" fill="none"/>
    <path d="M62 -40 L52 108" stroke="#ffffff" stroke-opacity=".16" stroke-width="4" stroke-linecap="round" fill="none"/>
    <ellipse cx="0" cy="132" rx="86" ry="10" fill="#000" opacity=".35"/>
  </g>

  <!-- base rule + caption -->
  <path d="M150 760 H470" stroke="#C8A45C" stroke-width="1" opacity=".6"/>
  <text x="310" y="784" text-anchor="middle" font-family="Georgia,serif" font-size="15" letter-spacing="5" fill="#E7C888" opacity=".85">LIVE TRAD · DUBLIN 1</text>
</svg>
"""
write("hero-music.svg", hero)

# ---------------------------------------------------------------- hero mobile: pint + notes, tighter crop
hero_mobile = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 640" width="520" height="640">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#163B2B"/>
      <stop offset="1" stop-color="#0A1C15"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="28%" r="62%">
      <stop offset="0" stop-color="#E7C888" stop-opacity=".4"/>
      <stop offset="1" stop-color="#E7C888" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="gold" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F0DCA6"/><stop offset=".5" stop-color="#C8A45C"/><stop offset="1" stop-color="#A97F38"/>
    </linearGradient>
    <linearGradient id="stout" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#3A2012"/><stop offset=".45" stop-color="#1C0E07"/><stop offset="1" stop-color="#0B0503"/>
    </linearGradient>
    <linearGradient id="glass" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#fff" stop-opacity=".28"/><stop offset=".15" stop-color="#fff" stop-opacity=".05"/>
      <stop offset=".85" stop-color="#fff" stop-opacity=".05"/><stop offset="1" stop-color="#fff" stop-opacity=".22"/>
    </linearGradient>
    <linearGradient id="head" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#FFF6E2"/><stop offset="1" stop-color="#E4D2AC"/>
    </linearGradient>
  </defs>
  <rect width="520" height="640" rx="6" fill="url(#bg)"/>
  <rect width="520" height="640" rx="6" fill="url(#glow)"/>
  <g fill="url(#gold)" opacity=".92">
    <g transform="translate(96 120) rotate(-12)"><ellipse cx="0" cy="30" rx="12" ry="8"/><rect x="9" y="-6" width="4" height="38"/><path d="M13 -6c16 4 24 13 20 28 2-13-6-20-20-22Z"/></g>
    <g transform="translate(420 96) rotate(10)"><ellipse cx="0" cy="30" rx="11" ry="7.5"/><rect x="8" y="-2" width="3.5" height="34"/><path d="M11.5 -2c14 3 21 11 17 25 2-11-5-18-17-20Z"/></g>
    <g transform="translate(438 232) rotate(-8)"><ellipse cx="0" cy="22" rx="8" ry="6"/><rect x="6" y="-8" width="2.8" height="32"/></g>
  </g>
  <!-- small fiddle behind -->
  <g transform="translate(260 210) rotate(-16)" opacity=".9">
    <g fill="none" stroke="url(#gold)" stroke-width="3.4" stroke-linejoin="round">
      <path d="M0 -30c-24 -3 -37 10 -35 29 1 14 11 22 24 26 -18 8 -27 22 -25 41 1 24 21 42 36 42s35 -18 36 -42c2 -19 -7 -33 -25 -41 13 -4 23 -12 24 -26 2 -19 -11 -32 -35 -29Z"/>
      <path d="M-7 -30 L-7 -104 M7 -30 L7 -104"/><path d="M-9 -104 L-10 -132 Q0 -146 10 -132 L9 -104"/>
    </g>
  </g>
  <!-- pint -->
  <g transform="translate(260 458)">
    <path d="M-104 -78 L104 -78 L86 142 Q0 156 -86 142 Z" fill="url(#glass)"/>
    <path d="M-98 -52 L98 -52 L82 136 Q0 148 -82 136 Z" fill="url(#stout)"/>
    <path d="M-100 -52 q11 -18 27 -9 q13 -16 31 -5 q16 -18 33 -3 q18 -15 33 2 q16 -9 29 7 q-5 11 -20 9 q-18 7 -33 -2 q-18 9 -35 0 q-18 9 -35 -1 q-16 8 -29 -2 Z" fill="url(#head)"/>
    <g transform="translate(0 34) scale(1.02)" fill="#E7C888" opacity=".9">
      <path d="M-24 -28 h7 v46 h-7 Z"/><path d="M-9 -32 h5 v50 h-5 Z"/><path d="M6 -30 h5 v48 h-5 Z"/><path d="M19 -26 h6 v44 h-6 Z"/>
      <path d="M-28 -30 h54 v6 h-54 Z"/><path d="M-5 -32 q10 -10 20 0 q-10 -4 -20 2 Z"/>
    </g>
    <path d="M-82 -44 L-68 124" stroke="#fff" stroke-opacity=".3" stroke-width="8" stroke-linecap="round" fill="none"/>
    <path d="M66 -44 L56 118" stroke="#fff" stroke-opacity=".16" stroke-width="4" stroke-linecap="round" fill="none"/>
    <ellipse cx="0" cy="148" rx="96" ry="11" fill="#000" opacity=".35"/>
  </g>
  <path d="M120 592 H400" stroke="#C8A45C" stroke-width="1" opacity=".6"/>
  <text x="260" y="618" text-anchor="middle" font-family="Georgia,serif" font-size="14" letter-spacing="5" fill="#E7C888" opacity=".85">LIVE TRAD · DUBLIN 1</text>
</svg>
"""
write("hero-music-mobile.svg", hero_mobile)

# ---------------------------------------------------------------- interior scene
interior = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 600" width="900" height="600">
  <defs>
    <linearGradient id="wall" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#2A1B12"/><stop offset="1" stop-color="#4A2E1B"/>
    </linearGradient>
    <radialGradient id="lamp" cx="50%" cy="0%" r="90%">
      <stop offset="0" stop-color="#F0C877" stop-opacity=".55"/><stop offset="1" stop-color="#F0C877" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="wood" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#6B452A"/><stop offset="1" stop-color="#3A2416"/>
    </linearGradient>
  </defs>
  <rect width="900" height="600" fill="url(#wall)"/>
  <rect width="900" height="600" fill="url(#lamp)"/>

  <!-- ceiling lamps -->
  <g stroke="#C8A45C" stroke-width="2" fill="none" opacity=".8">
    <path d="M200 0 v70"/><path d="M450 0 v50"/><path d="M700 0 v70"/>
  </g>
  <g fill="#E7C888">
    <path d="M176 70 h48 l-10 22 h-28 Z" opacity=".9"/>
    <path d="M426 50 h48 l-10 22 h-28 Z" opacity=".9"/>
    <path d="M676 70 h48 l-10 22 h-28 Z" opacity=".9"/>
  </g>
  <g fill="#F6D98A" opacity=".28">
    <ellipse cx="200" cy="100" rx="70" ry="90"/><ellipse cx="450" cy="80" rx="70" ry="90"/><ellipse cx="700" cy="100" rx="70" ry="90"/>
  </g>

  <!-- framed pictures -->
  <g stroke="#C8A45C" stroke-width="3" fill="#3A2416" opacity=".85">
    <rect x="70" y="150" width="120" height="90"/><rect x="710" y="150" width="120" height="90"/>
  </g>
  <g fill="#C8A45C" opacity=".5">
    <circle cx="130" cy="195" r="26"/><path d="M770 225 l30 -40 l30 40 Z"/>
  </g>

  <!-- little stage with musicians -->
  <rect x="300" y="330" width="300" height="110" rx="4" fill="#2A160C" stroke="#C8A45C" stroke-width="2" stroke-opacity=".6"/>
  <g fill="#1C0F08">
    <!-- fiddle player -->
    <circle cx="360" cy="300" r="20"/>
    <path d="M336 330 q24 -18 48 0 l8 78 h-64 Z"/>
    <path d="M352 300 q24 -14 44 4 l-6 10 q-18 -12 -38 -4 Z" fill="#3A2416"/>
    <!-- piper -->
    <circle cx="450" cy="296" r="21"/>
    <path d="M424 330 q26 -20 52 0 l8 78 h-68 Z"/>
    <!-- drummer -->
    <circle cx="540" cy="304" r="19"/>
    <path d="M516 334 q24 -18 48 0 l8 74 h-64 Z"/>
  </g>
  <!-- fiddle in arms -->
  <path d="M372 318 q-16 8 -8 26 q10 -10 8 -26Z" fill="none" stroke="#C8A45C" stroke-width="3"/>
  <!-- tin whistle -->
  <path d="M446 312 l0 34" stroke="#C8A45C" stroke-width="3"/>
  <!-- notes in air -->
  <g fill="#E7C888" opacity=".85">
    <g transform="translate(330 250)"><ellipse cx="0" cy="12" rx="7" ry="5"/><rect x="5" y="-16" width="2.5" height="30"/></g>
    <g transform="translate(480 236)"><ellipse cx="0" cy="12" rx="7" ry="5"/><rect x="5" y="-16" width="2.5" height="30"/></g>
    <g transform="translate(560 268)"><ellipse cx="0" cy="10" rx="6" ry="4.5"/><rect x="4.5" y="-14" width="2.3" height="26"/></g>
  </g>

  <!-- wooden bar counter -->
  <rect x="0" y="470" width="900" height="130" fill="url(#wood)"/>
  <rect x="0" y="470" width="900" height="10" fill="#8A5C38"/>
  <!-- beer taps -->
  <g fill="#C8A45C">
    <rect x="120" y="430" width="10" height="42"/><rect x="150" y="430" width="10" height="42"/><rect x="180" y="430" width="10" height="42"/>
  </g>
  <g fill="#0A1C15">
    <rect x="112" y="424" width="26" height="10" rx="2"/><rect x="142" y="424" width="26" height="10" rx="2"/><rect x="172" y="424" width="26" height="10" rx="2"/>
  </g>
  <!-- pints on the bar -->
  <g>
    <g transform="translate(560 442)"><path d="M-22 0 h44 l-5 40 h-34 Z" fill="#140B06"/><path d="M-23 0 q6 -9 12 -3 q8 -8 14 -1 q9 -4 13 4Z" fill="#F3E6C8"/></g>
    <g transform="translate(620 442)"><path d="M-22 0 h44 l-5 40 h-34 Z" fill="#140B06"/><path d="M-23 0 q6 -9 12 -3 q8 -8 14 -1 q9 -4 13 4Z" fill="#F3E6C8"/></g>
  </g>
</svg>
"""
write("pub-interior.svg", interior)

print("done")
