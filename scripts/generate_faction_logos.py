#!/usr/bin/env python3
"""Generate stylized cartoon SVG faction logos."""

from __future__ import annotations

import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Data"
OUT = ROOT / "wwwroot" / "images" / "factions"

STYLE = """
<style>
  .bg {{ fill: url(#bgGrad); }}
  .ring {{ fill: none; stroke: #1a1a2e; stroke-width: 5; }}
  .fill-primary {{ fill: {accent}; stroke: #1a1a2e; stroke-width: 4; }}
  .fill-secondary {{ fill: #f8fafc; stroke: #1a1a2e; stroke-width: 3; }}
  .fill-dark {{ fill: #1a1a2e; stroke: #1a1a2e; stroke-width: 3; }}
  .fill-metal {{ fill: #cbd5e1; stroke: #1a1a2e; stroke-width: 3; }}
  .stroke-only {{ fill: none; stroke: #1a1a2e; stroke-width: 4; stroke-linecap: round; stroke-linejoin: round; }}
  .accent-stroke {{ fill: none; stroke: {accent}; stroke-width: 5; stroke-linecap: round; stroke-linejoin: round; }}
</style>
"""


def parse_factions(path: Path) -> list[dict]:
    text = path.read_text()
    entries = []
    for block in re.findall(r"new\(\)\s*\{(.*?)\}", text, re.DOTALL):
        name = re.search(r'Name = "(.*?)"', block)
        slug = re.search(r'Slug = "(.*?)"', block)
        color = re.search(r'Color = "(.*?)"', block)
        if name and slug:
            entries.append(
                {
                    "name": name.group(1),
                    "slug": slug.group(1),
                    "color": color.group(1) if color else "#7eb8ff",
                }
            )
    return entries


def starfield() -> str:
    coords = [
        (42, 38, 1.2, 0.7), (118, 92, 1.5, 0.5), (380, 54, 1, 0.65), (460, 120, 1.8, 0.45),
        (88, 180, 1, 0.55), (430, 210, 1.2, 0.75), (250, 44, 1.6, 0.6), (310, 150, 1, 0.4),
        (170, 420, 1.3, 0.5), (480, 380, 1, 0.55), (60, 340, 1.7, 0.35), (400, 460, 1.2, 0.65),
    ]
    return "\n".join(
        f'  <circle cx="{x}" cy="{y}" r="{r}" fill="#ffffff" opacity="{o}"/>'
        for x, y, r, o in coords
    )


def logo_for(slug: str) -> str:
    logos = {
        "republic": """
  <circle class="fill-secondary" cx="256" cy="256" r="148"/>
  <circle class="ring" cx="256" cy="256" r="148"/>
  <circle class="fill-primary" cx="256" cy="256" r="108"/>
  <g transform="translate(256 256)">
    <line class="stroke-only" x1="0" y1="-92" x2="0" y2="92"/>
    <line class="stroke-only" x1="-92" y1="0" x2="92" y2="0"/>
    <line class="stroke-only" x1="-65" y1="-65" x2="65" y2="65"/>
    <line class="stroke-only" x1="65" y1="-65" x2="-65" y2="65"/>
    <circle class="fill-secondary" cx="0" cy="0" r="24"/>
  </g>
""",
        "confederacy": """
  <polygon class="fill-secondary" points="256,88 404,174 404,338 256,424 108,338 108,174"/>
  <polygon class="ring" points="256,88 404,174 404,338 256,424 108,338 108,174"/>
  <circle class="fill-primary" cx="256" cy="256" r="78"/>
  <circle class="fill-secondary" cx="256" cy="178" r="16"/>
  <circle class="fill-secondary" cx="224" cy="302" r="16"/>
  <circle class="fill-secondary" cx="288" cy="302" r="16"/>
  <circle class="fill-secondary" cx="194" cy="222" r="16"/>
  <circle class="fill-secondary" cx="318" cy="222" r="16"/>
  <circle class="fill-secondary" cx="194" cy="290" r="16"/>
  <circle class="fill-secondary" cx="318" cy="290" r="16"/>
  <circle class="fill-dark" cx="256" cy="256" r="18"/>
""",
        "empire": """
  <circle class="fill-secondary" cx="256" cy="256" r="148"/>
  <circle class="ring" cx="256" cy="256" r="148"/>
  <circle class="fill-dark" cx="256" cy="256" r="108"/>
  <g transform="translate(256 256)">
    <line class="accent-stroke" x1="0" y1="-88" x2="0" y2="88"/>
    <line class="accent-stroke" x1="-76" y1="-44" x2="76" y2="44"/>
    <line class="accent-stroke" x1="-76" y1="44" x2="76" y2="-44"/>
    <line class="accent-stroke" x1="-88" y1="0" x2="88" y2="0"/>
    <line class="accent-stroke" x1="-44" y1="-76" x2="44" y2="76"/>
    <line class="accent-stroke" x1="44" y1="-76" x2="-44" y2="76"/>
    <circle class="fill-metal" cx="0" cy="0" r="28"/>
  </g>
""",
        "rebel-alliance": """
  <circle class="fill-secondary" cx="256" cy="256" r="148"/>
  <circle class="ring" cx="256" cy="256" r="148"/>
  <path class="fill-primary" d="M256 110 L300 190 L390 205 L325 265 L340 355 L256 315 L172 355 L187 265 L122 205 L212 190 Z"/>
  <path class="fill-secondary" d="M256 145 L275 205 L340 215 L295 255 L305 315 L256 285 L207 315 L217 255 L172 215 L237 205 Z"/>
  <circle class="fill-dark" cx="256" cy="250" r="14"/>
""",
        "new-republic": """
  <circle class="fill-secondary" cx="256" cy="256" r="148"/>
  <circle class="ring" cx="256" cy="256" r="148"/>
  <circle class="fill-primary" cx="256" cy="256" r="98"/>
  <path class="fill-secondary" d="M256 138 L292 210 L370 222 L315 275 L330 352 L256 312 L182 352 L197 275 L142 222 L220 210 Z"/>
  <rect class="fill-dark" x="236" y="236" width="40" height="40" rx="6" transform="rotate(45 256 256)"/>
""",
        "hutts": """
  <circle class="fill-secondary" cx="256" cy="256" r="148"/>
  <circle class="ring" cx="256" cy="256" r="148"/>
  <ellipse class="fill-primary" cx="256" cy="290" rx="92" ry="62"/>
  <ellipse class="fill-primary" cx="256" cy="220" rx="72" ry="52"/>
  <circle class="fill-dark" cx="228" cy="210" r="10"/>
  <circle class="fill-dark" cx="284" cy="210" r="10"/>
  <path class="stroke-only" d="M230 248 Q256 270 282 248"/>
  <path class="fill-secondary" d="M180 250 Q150 280 165 320"/>
  <path class="fill-secondary" d="M332 250 Q362 280 347 320"/>
""",
        "sith-empire": """
  <polygon class="fill-secondary" points="256,92 420,256 256,420 92,256"/>
  <polygon class="ring" points="256,92 420,256 256,420 92,256"/>
  <polygon class="fill-primary" points="256,130 370,256 256,382 142,256"/>
  <path class="fill-dark" d="M256 170 L276 250 L360 250 L292 300 L318 380 L256 335 L194 380 L220 300 L152 250 L236 250 Z"/>
  <circle class="fill-secondary" cx="256" cy="256" r="22"/>
""",
    }
    return logos.get(slug, logos["republic"])


def svg_for(entry: dict) -> str:
    accent = entry["color"]
    style = STYLE.format(accent=accent)
    body = logo_for(entry["slug"])
    return textwrap.dedent(
        f"""\
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" role="img" aria-label="{entry['name']} emblem">
          <defs>
            <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="{accent}" stop-opacity="0.45"/>
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
    OUT.mkdir(parents=True, exist_ok=True)
    factions = parse_factions(DATA / "FactionData.cs")
    for entry in factions:
        (OUT / f"{entry['slug']}.svg").write_text(svg_for(entry))
    print(f"Generated {len(factions)} faction logo SVGs.")


if __name__ == "__main__":
    main()
