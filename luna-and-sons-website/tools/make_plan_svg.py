#!/usr/bin/env python3
"""
Draws the illustrative 2D landscape plan used in the "Design & Planning" step of the
homepage, in English and Spanish:  images/process/plan-en.svg  /  plan-es.svg
This is an original drawing (not a photo, not a real client's property) — it shows what a
Luna & Sons concept plan looks like. To use a real plan instead, export it to images/process/
and point build_home.py's PROCESS_PHOTOS at it.
Run: python3 tools/make_plan_svg.py
"""
import os
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "images", "process")

TEXT = {
    "en": dict(title="LANDSCAPE PLAN · CONCEPT", home="HOME", brand="Luna & Sons Landscaping",
               legend=["Paver patio", "Pergola", "Planting bed", "Retaining wall", "Lawn", "Stepping stones"]),
    "es": dict(title="PLANO DE PAISAJE · CONCEPTO", home="CASA", brand="Luna & Sons Landscaping",
               legend=["Patio de adoquines", "Pérgola", "Jardinera", "Muro de contención", "Césped", "Piedras de paso"]),
}

INK, PLUM, WOOD, GREEN, GREEN_BG, STONE = "#3A2A44", "#4B1D63", "#7A5230", "#4F7A47", "#DCE8D2", "#8D8296"


def marker(n, x, y, r=11, size=12):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{PLUM}" stroke="#fff" stroke-width="1.5"/>'
            f'<text x="{x}" y="{y + size * 0.35:.1f}" text-anchor="middle" font-size="{size}" font-weight="700" fill="#fff">{n}</text>')


def plant(x, y, r):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#C3DAB5" stroke="{GREEN}" stroke-width="1.3"/>'
            f'<circle cx="{x}" cy="{y}" r="2" fill="{GREEN}"/>')


def tree(x, y, r):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#CFE0C4" stroke="{GREEN}" stroke-width="1.6"/>'
            f'<circle cx="{x}" cy="{y}" r="{r * 0.5:.1f}" fill="none" stroke="{GREEN}" stroke-width="1" stroke-dasharray="3 3"/>'
            f'<circle cx="{x}" cy="{y}" r="2.5" fill="{GREEN}"/>')


def build(lang):
    t = TEXT[lang]
    rafters = "".join(f'<line x1="{x}" y1="186" x2="{x}" y2="294" stroke="{WOOD}" stroke-width="1.4" opacity=".75"/>' for x in range(297, 508, 12))
    posts = "".join(f'<rect x="{x}" y="{y}" width="9" height="9" fill="{WOOD}"/>' for x, y in ((281, 182), (506, 182), (281, 289), (506, 289)))
    chairs = "".join(f'<circle cx="{x}" cy="{y}" r="8" fill="#fff" stroke="{INK}" stroke-width="1.2"/>' for x, y in ((400, 202), (400, 278), (362, 240), (438, 240)))
    stones = "".join(f'<rect x="{x - 17}" y="{y - 9}" width="34" height="18" rx="4" fill="#E8E1EE" stroke="{PLUM}" stroke-width="1.2"/>' for x, y in ((396, 338), (410, 362), (394, 388), (408, 412)))
    left_plants = "".join(plant(*p) for p in ((95, 185, 16), (150, 212, 12), (98, 262, 14), (155, 290, 17), (108, 328, 12), (146, 166, 10)))
    right_plants = "".join(plant(*p) for p in ((665, 138, 14), (712, 122, 17), (702, 178, 13), (656, 186, 10), (737, 168, 11)))
    low_plants = "".join(plant(*p) for p in ((608, 452, 12), (645, 446, 15), (682, 456, 11)))
    cols = [60, 250, 440]
    legend = ""
    for i, label in enumerate(t["legend"]):
        x, y = cols[i % 3], 568 + (i // 3) * 28
        legend += (f'<circle cx="{x}" cy="{y}" r="9" fill="{PLUM}"/>'
                   f'<text x="{x}" y="{y + 4}" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">{i + 1}</text>'
                   f'<text x="{x + 18}" y="{y + 4.5}" font-size="13" fill="{INK}">{escape(label)}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 640" role="img" aria-label="{escape(t["title"])}" font-family="Helvetica, Arial, sans-serif">
<defs>
  <pattern id="pav" width="30" height="20" patternUnits="userSpaceOnUse"><rect width="30" height="20" fill="#EDE6F1"/><path d="M0 0H30M0 10H30M0 0V10M15 10V20" stroke="#B7A6C4" stroke-width=".9" fill="none"/></pattern>
  <pattern id="lawn" width="14" height="14" patternUnits="userSpaceOnUse"><rect width="14" height="14" fill="#F1F6EB"/><circle cx="3" cy="3" r="1" fill="#9DB98F"/><circle cx="10" cy="10" r="1" fill="#9DB98F"/></pattern>
  <pattern id="hatch" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="9" height="9" fill="#F3EEF6"/><path d="M0 0V9" stroke="#9C8EA6" stroke-width="1"/></pattern>
</defs>
<rect width="800" height="640" fill="#FAF7F1"/>
<rect x="14" y="14" width="772" height="612" fill="none" stroke="{INK}" stroke-width="1.5"/>
<text x="40" y="46" font-size="15" font-weight="700" letter-spacing="3" fill="{PLUM}">{escape(t["title"])}</text>
<text x="760" y="46" text-anchor="end" font-size="12" fill="#6B5B73">{escape(t["brand"])}</text>

<rect x="40" y="64" width="720" height="470" fill="#fff" stroke="#6B5B73" stroke-width="1.4" stroke-dasharray="8 5"/>

<rect x="60" y="380" width="680" height="135" rx="40" fill="url(#lawn)" stroke="#9DB98F" stroke-width="1.2"/>
<ellipse cx="125" cy="250" rx="70" ry="105" fill="{GREEN_BG}" stroke="#7A9A6B" stroke-width="1.8"/>{left_plants}
<ellipse cx="690" cy="160" rx="62" ry="72" fill="{GREEN_BG}" stroke="#7A9A6B" stroke-width="1.2"/>{right_plants}
<path d="M628 160 A62 72 0 0 0 752 160" fill="none" stroke="{STONE}" stroke-width="10" stroke-linecap="round"/>
<path d="M628 160 A62 72 0 0 0 752 160" fill="none" stroke="#CFC6D6" stroke-width="3.5" stroke-linecap="round"/>
<ellipse cx="645" cy="455" rx="80" ry="38" fill="{GREEN_BG}" stroke="#7A9A6B" stroke-width="1.6"/>{low_plants}
{tree(110, 450, 30)}{tree(260, 466, 24)}

<rect x="240" y="64" width="320" height="96" fill="url(#hatch)" stroke="{INK}" stroke-width="2.5"/>
<rect x="352" y="100" width="96" height="28" rx="3" fill="#fff" opacity=".92"/>
<text x="400" y="119" text-anchor="middle" font-size="14" font-weight="700" letter-spacing="2" fill="{INK}">{escape(t["home"])}</text>
<rect x="230" y="160" width="340" height="160" fill="url(#pav)" stroke="{PLUM}" stroke-width="2"/>
<rect x="380" y="160" width="40" height="14" fill="#fff" stroke="{INK}" stroke-width="1.5"/>

<rect x="285" y="186" width="230" height="108" fill="none" stroke="{WOOD}" stroke-width="3"/>{rafters}{posts}
<circle cx="400" cy="240" r="26" fill="#fff" stroke="{INK}" stroke-width="1.5"/>{chairs}
{stones}

{marker(1, 252, 300)}{marker(2, 542, 182)}{marker(3, 125, 236)}{marker(4, 690, 232)}{marker(5, 200, 420)}{marker(6, 452, 376)}

<rect x="40" y="548" width="720" height="70" fill="#fff" stroke="{INK}" stroke-width="1.2"/>
{legend}
<circle cx="722" cy="587" r="19" fill="none" stroke="{INK}" stroke-width="1.3"/>
<polygon points="722,570 730,592 722,587 714,592" fill="{PLUM}"/>
<text x="722" y="565" text-anchor="middle" font-size="11" font-weight="700" fill="{INK}">N</text>
</svg>
'''


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for lang in ("en", "es"):
        path = os.path.join(OUT, f"plan-{lang}.svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write(build(lang))
        print("wrote", os.path.relpath(path, ROOT))
