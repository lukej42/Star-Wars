#!/usr/bin/env python3
"""Generate stylized cartoon SVG portraits for directory entries."""

from __future__ import annotations

import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Data"
OUT = ROOT / "wwwroot" / "images"
SCRIPTS = Path(__file__).resolve().parent

import sys
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from directory_art import ship_svg_for
from jedi_sith_art import portrait_svg as jedi_sith_portrait_svg

SLUG_ARCHETYPE: dict[str, str] = {
    "admiral-ackbar": "alien_fish",
    "bb-8": "droid",
    "boba-fett": "mando",
    "c-3po": "droid",
    "captain-phasma": "trooper",
    "chewbacca": "wookiee",
    "darth-vader": "masked_sith",
    "darth-malak": "masked_sith",
    "darth-nihilus": "masked_sith",
    "darth-sidious": "hooded_sith",
    "darth-vitiate": "hooded_sith",
    "darth-maul": "horned",
    "din-djarin": "mando",
    "general-grievous": "cyborg",
    "grogu": "small_green",
    "han-solo": "human",
    "hera-syndulla": "twilek",
    "hk-47": "droid",
    "ig-11": "droid",
    "jabba-the-hutt": "hutt",
    "jango-fett": "mando",
    "k-2so": "droid",
    "kuiil": "wookiee",
    "moff-gideon": "human",
    "r2-d2": "droid",
    "t3-m4": "droid",
    "thrawn": "alien_blue",
    "yoda": "small_green",
    "yaddle": "small_green",
}


def starfield() -> str:
    coords = [
        (42, 38, 1.2, 0.7), (118, 92, 1.5, 0.5), (380, 54, 1, 0.65), (460, 120, 1.8, 0.45),
        (88, 180, 1, 0.55), (430, 210, 1.2, 0.75), (250, 44, 1.6, 0.6), (310, 150, 1, 0.4),
        (170, 420, 1.3, 0.5), (480, 380, 1, 0.55), (60, 340, 1.7, 0.35), (400, 460, 1.2, 0.65),
        (200, 480, 1, 0.5), (340, 40, 1.4, 0.7), (28, 260, 1.1, 0.45), (490, 260, 1.5, 0.6),
    ]
    return "\n".join(
        f'  <circle cx="{x}" cy="{y}" r="{r}" fill="#ffffff" opacity="{o}"/>'
        for x, y, r, o in coords
    )

STYLE = """
<style>
  .bg {{ fill: url(#bgGrad); }}
  .outline {{ fill: none; stroke: #1a1a2e; stroke-width: 3; stroke-linecap: round; stroke-linejoin: round; }}
  .skin {{ fill: #f4c99b; stroke: #1a1a2e; stroke-width: 3; }}
  .hair {{ fill: #4a3728; stroke: #1a1a2e; stroke-width: 3; }}
  .gear {{ fill: {accent}; stroke: #1a1a2e; stroke-width: 3; }}
  .metal {{ fill: #b8c4d0; stroke: #1a1a2e; stroke-width: 3; }}
  .dark {{ fill: #2d2d3a; stroke: #1a1a2e; stroke-width: 3; }}
  .eye-white {{ fill: #fff; stroke: #1a1a2e; stroke-width: 2; }}
  .pupil {{ fill: #1a1a2e; }}
  .highlight {{ fill: rgba(255,255,255,0.45); }}
  .robe {{ fill: {accent}; stroke: #1a1a2e; stroke-width: 3; }}
  .sith {{ fill: #111; stroke: #8b0000; stroke-width: 3; }}
  .fur {{ fill: #6b4423; stroke: #1a1a2e; stroke-width: 3; }}
  .green {{ fill: #7ec850; stroke: #1a1a2e; stroke-width: 3; }}
  .red {{ fill: #dc2626; stroke: #1a1a2e; stroke-width: 3; }}
</style>
"""


def parse_entries(path: Path, role_field: str) -> list[dict]:
    text = path.read_text()
    entries = []
    for block in re.findall(r"new\(\)\s*\{(.*?)\}", text, re.DOTALL):
        name = re.search(r'Name = "(.*?)"', block)
        slug = re.search(r'Slug = "(.*?)"', block)
        role = re.search(rf'{role_field} = "(.*?)"', block)
        desc = re.search(r'Description = "(.*?)"', block)
        color = re.search(r'Color = "(.*?)"', block)
        if name and slug:
            entries.append(
                {
                    "name": name.group(1),
                    "slug": slug.group(1),
                    "role": role.group(1) if role else "",
                    "desc": desc.group(1) if desc else "",
                    "color": color.group(1) if color else "#7eb8ff",
                }
            )
    return entries


def parse_ship_entries(path: Path) -> list[dict]:
    text = path.read_text()
    entries = []
    for block in re.findall(r"new\(\)\s*\{(.*?)\}", text, re.DOTALL):
        name = re.search(r'Name = "(.*?)"', block)
        slug = re.search(r'Slug = "(.*?)"', block)
        ship_class = re.search(r'Class = "(.*?)"', block)
        desc = re.search(r'Description = "(.*?)"', block)
        color = re.search(r'Color = "(.*?)"', block)
        if name and slug:
            entries.append(
                {
                    "name": name.group(1),
                    "slug": slug.group(1),
                    "role": ship_class.group(1) if ship_class else "",
                    "desc": desc.group(1) if desc else "",
                    "color": color.group(1) if color else "#7eb8ff",
                }
            )
    return entries


def archetype(entry: dict, folder: str) -> str:
    if entry["slug"] in SLUG_ARCHETYPE:
        return SLUG_ARCHETYPE[entry["slug"]]
    blob = f"{entry['name']} {entry['role']} {entry['desc']}".lower()
    if folder == "sith" or "sith" in entry["role"].lower() or "inquisitor" in blob:
        if "droid" in blob or entry["slug"] in {"hk-47", "ig-11", "k-2so", "c-3po", "r2-d2", "bb-8", "t3-m4"}:
            return "droid"
        if "hood" in blob or "emperor" in blob or "palpatine" in blob or "vitiate" in blob:
            return "hooded_sith"
        if "mask" in blob or "vader" in blob or "malak" in blob or "nihilus" in blob:
            return "masked_sith"
        if "zabrak" in blob or "maul" in blob or "talzin" in blob:
            return "horned"
        return "sith"
    if any(k in blob for k in ("droid", "astromech", "protocol droid", "assassin droid", "utility droid", "security droid")):
        return "droid"
    if any(k in blob for k in ("wookiee", "chewbacca", "kuiil", "ugnaught")):
        return "wookiee"
    if any(k in blob for k in ("twi'lek", "twilek", "hera", "aayla", "mission vao", "tiplee", "tiplar")):
        return "twilek"
    if any(k in blob for k in ("mon calamari", "ackbar", "nahdar", "fisto", "nautolan")):
        return "alien_fish"
    if any(k in blob for k in ("hutt", "jabba")):
        return "hutt"
    if any(k in blob for k in ("mandalorian", "boba", "jango", "din djarin", "bo-katan", "sabine", "canderous")):
        return "mando"
    if any(k in blob for k in ("stormtrooper", "clone", "phasma", "trooper")) and "jedi" not in blob:
        return "trooper"
    if any(k in blob for k in ("yoda", "grogu", "yaddle")):
        return "small_green"
    if folder == "jedi" or "jedi" in entry["role"].lower():
        return "jedi"
    if any(k in blob for k in ("grievous", "cyborg")):
        return "cyborg"
    if any(k in blob for k in ("admira", "thrawn", "chiss")):
        return "alien_blue"
    return "human"


def body_for(kind: str) -> str:
    templates = {
        "human": """
  <ellipse class="skin" cx="256" cy="290" rx="95" ry="110"/>
  <path class="hair" d="M165 250 Q256 150 347 250 Q330 210 256 195 Q182 210 165 250"/>
  <circle class="eye-white" cx="220" cy="275" r="16"/>
  <circle class="eye-white" cx="292" cy="275" r="16"/>
  <circle class="pupil" cx="225" cy="277" r="7"/>
  <circle class="pupil" cx="297" cy="277" r="7"/>
  <path class="outline" d="M230 330 Q256 355 282 330"/>
  <rect class="gear" x="190" y="360" width="132" height="90" rx="18"/>
""",
        "jedi": """
  <path class="robe" d="M130 420 Q256 300 382 420 L360 512 H152 Z"/>
  <ellipse class="skin" cx="256" cy="265" rx="78" ry="88"/>
  <path class="hair" d="M185 245 Q256 170 327 245 Q310 215 256 205 Q202 215 185 245"/>
  <circle class="eye-white" cx="228" cy="260" r="14"/>
  <circle class="eye-white" cx="284" cy="260" r="14"/>
  <circle class="pupil" cx="232" cy="262" r="6"/>
  <circle class="pupil" cx="288" cy="262" r="6"/>
  <rect class="gear" x="360" y="300" width="18" height="140" rx="8" transform="rotate(18 360 300)"/>
  <circle class="highlight" cx="368" cy="292" r="8"/>
""",
        "sith": """
  <path class="sith" d="M140 420 Q256 290 372 420 L350 512 H162 Z"/>
  <ellipse class="skin" cx="256" cy="265" rx="78" ry="88"/>
  <circle class="eye-white" cx="228" cy="258" r="14"/>
  <circle class="eye-white" cx="284" cy="258" r="14"/>
  <circle class="pupil" cx="232" cy="260" r="6"/>
  <circle class="pupil" cx="288" cy="260" r="6"/>
  <path class="red" d="M220 320 Q256 340 292 320" fill="none" stroke="#dc2626" stroke-width="4"/>
  <rect class="dark" x="360" y="300" width="18" height="140" rx="8" transform="rotate(18 360 300)"/>
""",
        "hooded_sith": """
  <path class="sith" d="M110 430 Q256 120 402 430 L380 512 H132 Z"/>
  <ellipse class="skin" cx="256" cy="285" rx="62" ry="70"/>
  <circle class="eye-white" cx="232" cy="278" r="12"/>
  <circle class="eye-white" cx="280" cy="278" r="12"/>
  <circle class="pupil" cx="236" cy="280" r="5"/>
  <circle class="pupil" cx="284" cy="280" r="5"/>
  <path class="red" d="M235 315 Q256 330 277 315" fill="none" stroke="#ff4444" stroke-width="3"/>
""",
        "masked_sith": """
  <path class="dark" d="M150 420 Q256 180 362 420 L340 512 H172 Z"/>
  <rect class="dark" x="190" y="250" width="132" height="120" rx="24"/>
  <rect class="metal" x="210" y="270" width="92" height="28" rx="8"/>
  <circle class="eye-white" cx="228" cy="330" r="10"/>
  <circle class="eye-white" cx="284" cy="330" r="10"/>
  <circle class="red" cx="232" cy="332" r="4"/>
  <circle class="red" cx="288" cy="332" r="4"/>
  <rect class="metal" x="230" y="360" width="52" height="36" rx="10"/>
""",
        "horned": """
  <path class="red" d="M200 180 L185 120 L215 170 Z"/>
  <path class="red" d="M312 180 L327 120 L297 170 Z"/>
  <ellipse class="skin" cx="256" cy="285" rx="82" ry="92"/>
  <path class="red" d="M170 250 Q256 140 342 250" fill="#8b0000"/>
  <circle class="eye-white" cx="224" cy="275" r="14"/>
  <circle class="eye-white" cx="288" cy="275" r="14"/>
  <circle class="pupil" cx="228" cy="277" r="6"/>
  <circle class="pupil" cx="292" cy="277" r="6"/>
  <path class="dark" d="M150 420 Q256 320 362 420 L340 512 H172 Z"/>
""",
        "droid": """
  <rect class="metal" x="170" y="170" width="172" height="190" rx="36"/>
  <rect class="dark" x="200" y="210" width="112" height="70" rx="14"/>
  <circle class="gear" cx="228" cy="245" r="14"/>
  <circle class="gear" cx="284" cy="245" r="14"/>
  <rect class="metal" x="210" y="360" width="92" height="110" rx="16"/>
  <line class="outline" x1="256" y1="360" x2="256" y2="470"/>
""",
        "wookiee": """
  <ellipse class="fur" cx="256" cy="285" rx="105" ry="115"/>
  <circle class="eye-white" cx="215" cy="265" r="16"/>
  <circle class="eye-white" cx="297" cy="265" r="16"/>
  <circle class="pupil" cx="220" cy="267" r="7"/>
  <circle class="pupil" cx="302" cy="267" r="7"/>
  <path class="outline" d="M220 330 Q256 360 292 330"/>
  <path class="fur" d="M170 300 Q130 340 150 390"/>
  <path class="fur" d="M342 300 Q382 340 362 390"/>
  <rect class="gear" x="185" y="380" width="142" height="90" rx="20"/>
""",
        "twilek": """
  <ellipse class="skin" cx="256" cy="265" rx="78" ry="88"/>
  <path class="gear" d="M178 250 Q120 320 130 420"/>
  <path class="gear" d="M334 250 Q392 320 382 420"/>
  <circle class="eye-white" cx="228" cy="258" r="14"/>
  <circle class="eye-white" cx="284" cy="258" r="14"/>
  <circle class="pupil" cx="232" cy="260" r="6"/>
  <circle class="pupil" cx="288" cy="260" r="6"/>
  <rect class="gear" x="190" y="360" width="132" height="90" rx="18"/>
""",
        "alien_fish": """
  <ellipse class="skin" cx="256" cy="275" rx="88" ry="98"/>
  <circle class="eye-white" cx="256" cy="255" r="28"/>
  <circle class="pupil" cx="262" cy="258" r="12"/>
  <path class="gear" d="M190 320 Q256 360 322 320"/>
  <rect class="gear" x="185" y="370" width="142" height="95" rx="20"/>
""",
        "alien_blue": """
  <ellipse class="gear" cx="256" cy="275" rx="88" ry="98"/>
  <circle class="eye-white" cx="228" cy="258" r="14"/>
  <circle class="eye-white" cx="284" cy="258" r="14"/>
  <circle class="pupil" cx="232" cy="260" r="6"/>
  <circle class="pupil" cx="288" cy="260" r="6"/>
  <path class="dark" d="M210 300 Q256 330 302 300"/>
  <rect class="dark" x="190" y="360" width="132" height="90" rx="18"/>
""",
        "hutt": """
  <ellipse class="green" cx="256" cy="320" rx="130" ry="95"/>
  <ellipse class="green" cx="256" cy="250" rx="85" ry="70"/>
  <circle class="eye-white" cx="220" cy="235" r="16"/>
  <circle class="eye-white" cx="292" cy="235" r="16"/>
  <circle class="pupil" cx="225" cy="237" r="7"/>
  <circle class="pupil" cx="297" cy="237" r="7"/>
  <path class="outline" d="M220 275 Q256 300 292 275"/>
""",
        "mando": """
  <ellipse class="metal" cx="256" cy="270" rx="95" ry="105"/>
  <rect class="dark" x="205" y="230" width="102" height="36" rx="8"/>
  <circle class="gear" cx="228" cy="285" r="10"/>
  <circle class="gear" cx="284" cy="285" r="10"/>
  <path class="gear" d="M170 260 Q256 160 342 260 L330 420 Q256 450 182 420 Z"/>
  <rect class="gear" x="190" y="380" width="132" height="85" rx="16"/>
""",
        "trooper": """
  <ellipse class="metal" cx="256" cy="265" rx="92" ry="102"/>
  <rect class="dark" x="205" y="220" width="102" height="40" rx="8"/>
  <circle class="dark" cx="228" cy="285" r="8"/>
  <circle class="dark" cx="284" cy="285" r="8"/>
  <rect class="metal" x="185" y="360" width="142" height="95" rx="20"/>
""",
        "small_green": """
  <ellipse class="green" cx="256" cy="300" rx="78" ry="88"/>
  <ellipse class="green" cx="256" cy="230" rx="68" ry="62"/>
  <circle class="eye-white" cx="232" cy="225" r="16"/>
  <circle class="eye-white" cx="280" cy="225" r="16"/>
  <circle class="pupil" cx="236" cy="227" r="7"/>
  <circle class="pupil" cx="284" cy="227" r="7"/>
  <path class="gear" d="M190 360 Q256 390 322 360 L310 470 H202 Z"/>
""",
        "cyborg": """
  <ellipse class="metal" cx="256" cy="270" rx="92" ry="102"/>
  <rect class="dark" x="205" y="220" width="102" height="40" rx="8"/>
  <circle class="gear" cx="228" cy="285" r="10"/>
  <circle class="gear" cx="284" cy="285" r="10"/>
  <path class="metal" d="M150 350 L120 420 M362 350 L392 420"/>
  <rect class="dark" x="185" y="360" width="142" height="95" rx="20"/>
""",
    }
    return templates.get(kind, templates["human"])


def svg_for(entry: dict, folder: str) -> str:
    accent = entry["color"]
    kind = archetype(entry, folder)
    body = body_for(kind)
    style = STYLE.format(accent=accent)
    return textwrap.dedent(
        f"""\
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" role="img" aria-label="{entry['name']}">
          <defs>
            <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="{accent}" stop-opacity="0.55"/>
              <stop offset="100%" stop-color="#050814" stop-opacity="0.95"/>
            </linearGradient>
          </defs>
          {style}
          <rect class="bg" width="512" height="512" rx="24"/>
          {starfield()}
          {body}
        </svg>
        """
    )


def main() -> None:
    datasets = [
        ("characters", DATA / "CharacterData.cs", "Role"),
        ("jedi", DATA / "JediData.cs", "Rank"),
        ("sith", DATA / "SithData.cs", "Title"),
    ]
    total = 0
    for folder, path, role_field in datasets:
        out_dir = OUT / folder
        out_dir.mkdir(parents=True, exist_ok=True)
        for entry in parse_entries(path, role_field):
            svg_path = out_dir / f"{entry['slug']}.svg"
            if folder in ("jedi", "sith"):
                svg_path.write_text(jedi_sith_portrait_svg(entry, folder))
            else:
                svg_path.write_text(svg_for(entry, folder))
            total += 1

    ship_dir = OUT / "ships"
    ship_dir.mkdir(parents=True, exist_ok=True)
    for entry in parse_ship_entries(DATA / "ShipData.cs"):
        svg_path = ship_dir / f"{entry['slug']}.svg"
        svg_path.write_text(ship_svg_for(entry))
        total += 1

    print(f"Generated {total} cartoon portrait SVGs.")


if __name__ == "__main__":
    main()
