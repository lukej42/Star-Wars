#!/usr/bin/env python3
"""Generate full-bleed space background SVGs for planets without PNG heroes."""

from __future__ import annotations

import hashlib
import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Data" / "GalaxyData.cs"
OUT = ROOT / "wwwroot" / "images" / "planets"


def parse_planets(path: Path) -> list[dict]:
    text = path.read_text()
    entries = []
    for block in re.findall(r"new\(\)\s*\{(.*?)\}", text, re.DOTALL):
        name = re.search(r'Name = "(.*?)"', block)
        slug = re.search(r'Slug = "(.*?)"', block)
        desc = re.search(r'Description = "(.*?)"', block)
        color = re.search(r'Color = "(.*?)"', block)
        image = re.search(r'ImagePath = "(.*?)"', block)
        if name and slug:
            entries.append(
                {
                    "name": name.group(1),
                    "slug": slug.group(1),
                    "desc": desc.group(1) if desc else "",
                    "color": color.group(1) if color else "#7eb8ff",
                    "has_png": bool(image and image.group(1).lower().endswith(".webp")),
                }
            )
    return entries


def slug_seed(slug: str) -> int:
    return int(hashlib.md5(slug.encode()).hexdigest(), 16)


def starfield(width: int, height: int, seed: int, count: int = 120) -> str:
    lines = []
    for i in range(count):
        x = (seed * (i + 17) * 37) % width
        y = (seed * (i + 23) * 53) % height
        r = 1 + ((seed + i) % 3)
        opacity = 0.25 + ((seed + i * 3) % 60) / 100
        lines.append(f'  <circle cx="{x}" cy="{y}" r="{r}" fill="#ffffff" opacity="{opacity:.2f}"/>')
    return "\n".join(lines)


def space_svg(entry: dict) -> str:
    accent = entry["color"]
    seed = slug_seed(entry["slug"])
    blob = entry["desc"].lower()

    if any(k in blob for k in ("gas", "cloud", "tibanna")):
        planet_body = """
          <ellipse cx="960" cy="920" rx="780" ry="420" fill="url(#planetGrad)" opacity="0.95"/>
          <ellipse cx="760" cy="760" rx="520" ry="180" fill="#ffffff" opacity="0.12"/>
          <ellipse cx="1180" cy="800" rx="380" ry="120" fill="#ffffff" opacity="0.08"/>
        """
    elif any(k in blob for k in ("ice", "snow", "frozen")):
        planet_body = """
          <circle cx="980" cy="780" r="520" fill="url(#planetGrad)"/>
          <ellipse cx="760" cy="620" rx="280" ry="120" fill="#ffffff" opacity="0.35"/>
          <ellipse cx="1120" cy="860" rx="220" ry="90" fill="#ffffff" opacity="0.18"/>
        """
    else:
        planet_body = """
          <circle cx="960" cy="820" r="560" fill="url(#planetGrad)"/>
          <ellipse cx="720" cy="620" rx="320" ry="140" fill="#ffffff" opacity="0.18"/>
          <ellipse cx="1180" cy="760" rx="240" ry="100" fill="#ffffff" opacity="0.1"/>
          <path d="M420 820 Q960 660 1500 820" fill="none" stroke="#ffffff" stroke-width="6" opacity="0.08"/>
        """

    stars = starfield(1920, 1080, seed)
    return textwrap.dedent(
        f"""\
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" role="img" aria-label="{entry['name']} from space">
          <defs>
            <radialGradient id="spaceGrad" cx="50%" cy="40%" r="70%">
              <stop offset="0%" stop-color="{accent}" stop-opacity="0.35"/>
              <stop offset="45%" stop-color="#0b1020" stop-opacity="1"/>
              <stop offset="100%" stop-color="#02040a" stop-opacity="1"/>
            </radialGradient>
            <radialGradient id="planetGrad" cx="35%" cy="30%" r="70%">
              <stop offset="0%" stop-color="#ffffff" stop-opacity="0.55"/>
              <stop offset="35%" stop-color="{accent}" stop-opacity="0.95"/>
              <stop offset="100%" stop-color="#050814" stop-opacity="1"/>
            </radialGradient>
          </defs>
          <rect width="1920" height="1080" fill="url(#spaceGrad)"/>
          {stars}
          <ellipse cx="1500" cy="180" rx="280" ry="120" fill="{accent}" opacity="0.08"/>
          <ellipse cx="300" cy="260" rx="220" ry="90" fill="#7eb8ff" opacity="0.06"/>
          {planet_body}
        </svg>
        """
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    created = 0
    skipped = 0
    for entry in parse_planets(DATA):
        if entry["has_png"]:
            skipped += 1
            continue
        path = OUT / f"{entry['slug']}-space.svg"
        path.write_text(space_svg(entry))
        created += 1
    print(f"Generated {created} planet space backgrounds ({skipped} PNG heroes kept).")


if __name__ == "__main__":
    main()
