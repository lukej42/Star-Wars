#!/usr/bin/env python3
"""Generate Force Power SVG illustrations and detailed profile JSON."""

from __future__ import annotations

import hashlib
import json
import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Data" / "ForcePowerData.cs"
IMAGES = ROOT / "wwwroot" / "images" / "force-powers"
PROFILES = ROOT / "wwwroot" / "data" / "profiles" / "force-powers"

ERAS = [
    "Ancient Era",
    "Old Republic",
    "High Republic",
    "Clone Wars",
    "Imperial Era",
    "Galactic Civil War",
    "New Republic",
    "Sequel Era",
]

CATEGORY_ARCHETYPE = {
    "Telekinesis": "telekinesis",
    "Protection": "shield",
    "Healing": "healing",
    "Support": "aura",
    "Mind": "mind",
    "Sense": "sense",
    "Physical": "speed",
    "Nature": "nature",
    "Purification": "light",
    "Connection": "bond",
    "Transcendence": "spirit",
    "Energy": "energy",
    "Drain": "drain",
    "Enhancement": "rage",
    "Offensive": "strike",
    "Illusion": "illusion",
    "Ritual": "ritual",
}


def parse_powers(path: Path) -> list[dict]:
    text = path.read_text()
    entries = []
    for block in re.findall(r"new\(\)\s*\{(.*?)\}", text, re.DOTALL):
        name = re.search(r'Name = "(.*?)"', block)
        slug = re.search(r'Slug = "(.*?)"', block)
        side = re.search(r"Side = ForceSide\.(\w+)", block)
        category = re.search(r'Category = "(.*?)"', block)
        difficulty = re.search(r'Difficulty = "(.*?)"', block)
        desc = re.search(r'Description = "(.*?)"', block)
        color = re.search(r'Color = "(.*?)"', block)
        sources = re.search(r'Sources = "(.*?)"', block)
        if name and slug:
            entries.append(
                {
                    "name": name.group(1),
                    "slug": slug.group(1),
                    "side": side.group(1).lower() if side else "light",
                    "category": category.group(1) if category else "",
                    "difficulty": difficulty.group(1) if difficulty else "",
                    "desc": desc.group(1) if desc else "",
                    "color": color.group(1) if color else "#7eb8ff",
                    "sources": sources.group(1) if sources else "",
                }
            )
    return entries


def svg_wrap(title: str, accent: str, body: str) -> str:
    return textwrap.dedent(
        f"""
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" role="img" aria-label="{title}">
          <defs>
            <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="{accent}" stop-opacity="0.55"/>
              <stop offset="100%" stop-color="#050814" stop-opacity="0.95"/>
            </linearGradient>
            <radialGradient id="glowGrad" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="{accent}" stop-opacity="0.85"/>
              <stop offset="100%" stop-color="{accent}" stop-opacity="0"/>
            </radialGradient>
            <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
              <feGaussianBlur stdDeviation="8" result="blur"/>
              <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
            </filter>
          </defs>
          <style>
            .bg {{ fill: url(#bgGrad); }}
            .outline {{ fill: none; stroke: #1a1a2e; stroke-width: 3; stroke-linecap: round; stroke-linejoin: round; }}
            .fill-accent {{ fill: {accent}; stroke: #1a1a2e; stroke-width: 3; }}
            .fill-light {{ fill: #e2e8f0; stroke: #1a1a2e; stroke-width: 3; }}
            .fill-dark {{ fill: #1a1a2e; stroke: #1a1a2e; stroke-width: 3; }}
            .fill-mid {{ fill: {accent}; opacity: 0.65; stroke: #1a1a2e; stroke-width: 2; }}
            .glow {{ fill: url(#glowGrad); filter: url(#glow); }}
          </style>
          <rect class="bg" width="512" height="512" rx="24"/>
          {starfield()}
          {body}
        </svg>
        """
    ).strip() + "\n"


def starfield() -> str:
    coords = [
        (42, 38, 1.2, 0.7), (118, 92, 1.5, 0.5), (380, 54, 1, 0.65), (460, 120, 1.8, 0.45),
        (88, 180, 1, 0.55), (430, 210, 1.2, 0.75), (250, 44, 1.6, 0.6), (310, 150, 1, 0.4),
    ]
    return "\n".join(
        f'  <circle cx="{x}" cy="{y}" r="{r}" fill="#ffffff" opacity="{o}"/>'
        for x, y, r, o in coords
    )


def body_for(entry: dict, scene: bool = False) -> str:
    archetype = CATEGORY_ARCHETYPE.get(entry["category"], "energy")
    side = entry["side"]
    scale = 1.15 if scene else 1.0
    cx, cy = 256, 270

    bodies = {
        "telekinesis": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="90"/>
          <path class="fill-accent" d="M{cx} {cy-70} L{cx+50} {cy} L{cx} {cy+70} L{cx-50} {cy} Z"/>
          <circle class="fill-light" cx="{cx}" cy="{cy}" r="28"/>
          <path class="outline" d="M{cx-120} {cy+20} Q{cx-60} {cy-40} {cx} {cy+10}" fill="none"/>
          <path class="outline" d="M{cx+120} {cy+20} Q{cx+60} {cy-40} {cx} {cy+10}" fill="none"/>
        """,
        "shield": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="100"/>
          <path class="fill-accent" d="M{cx} {cy-95} Q{cx+85} {cy-30} {cx+75} {cy+60} L{cx} {cy+110} L{cx-75} {cy+60} Q{cx-85} {cy-30} {cx} {cy-95} Z" opacity="0.85"/>
          <path class="fill-light" d="M{cx} {cy-70} Q{cx+55} {cy-20} {cx+48} {cy+45} L{cx} {cy+80} L{cx-48} {cy+45} Q{cx-55} {cy-20} {cx} {cy-70} Z"/>
        """,
        "healing": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="95"/>
          <rect class="fill-accent" x="{cx-22}" y="{cy-80}" width="44" height="160" rx="8"/>
          <rect class="fill-accent" x="{cx-80}" y="{cy-22}" width="160" height="44" rx="8"/>
          <circle class="fill-light" cx="{cx}" cy="{cy}" r="36"/>
        """,
        "aura": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="110"/>
          <circle class="fill-accent" cx="{cx}" cy="{cy}" r="70" opacity="0.5"/>
          <circle class="outline" cx="{cx}" cy="{cy}" r="95" fill="none"/>
          <circle class="outline" cx="{cx}" cy="{cy}" r="55" fill="none"/>
          <circle class="fill-light" cx="{cx}" cy="{cy}" r="20"/>
        """,
        "mind": f"""
          <circle class="glow" cx="{cx}" cy="{cy-10}" r="85"/>
          <ellipse class="fill-accent" cx="{cx}" cy="{cy-10}" rx="75" ry="60"/>
          <path class="fill-light" d="M{cx-40} {cy-30} Q{cx} {cy-70} {cx+40} {cy-30} Q{cx} {cy+10} {cx-40} {cy-30}"/>
          <circle class="fill-dark" cx="{cx-20}" cy="{cy-15}" r="8"/>
          <circle class="fill-dark" cx="{cx+20}" cy="{cy-15}" r="8"/>
          <path class="outline" d="M{cx-30} {cy+80} Q{cx} {cy+50} {cx+30} {cy+80}" fill="none"/>
        """,
        "sense": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="90"/>
          <ellipse class="fill-light" cx="{cx-30}" cy="{cy-5}" rx="28" ry="18"/>
          <ellipse class="fill-light" cx="{cx+30}" cy="{cy-5}" rx="28" ry="18"/>
          <circle class="fill-accent" cx="{cx-30}" cy="{cy-5}" r="10"/>
          <circle class="fill-accent" cx="{cx+30}" cy="{cy-5}" r="10"/>
          <path class="fill-accent" d="M{cx} {cy-90} L{cx+15} {cy-50} L{cx+55} {cy-50} L{cx+22} {cy-25} L{cx+35} {cy+15} L{cx} {cy-5} L{cx-35} {cy+15} L{cx-22} {cy-25} L{cx-55} {cy-50} L{cx-15} {cy-50} Z" opacity="0.7"/>
        """,
        "speed": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="80"/>
          <path class="fill-accent" d="M{cx-100} {cy} L{cx-20} {cy-40} L{cx-20} {cy+40} Z"/>
          <path class="fill-light" d="M{cx-20} {cy-35} L{cx+90} {cy-35} L{cx+70} {cy} L{cx+90} {cy+35} L{cx-20} {cy+35} Z"/>
          <line class="outline" x1="{cx+95}" y1="{cy-60}" x2="{cx+130}" y2="{cy-60}"/>
          <line class="outline" x1="{cx+105}" y1="{cy}" x2="{cx+145}" y2="{cy}"/>
          <line class="outline" x1="{cx+95}" y1="{cy+60}" x2="{cx+130}" y2="{cy+60}"/>
        """,
        "nature": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="95"/>
          <path class="fill-accent" d="M{cx} {cy+90} L{cx-8} {cy-20} Q{cx} {cy-90} {cx+8} {cy-20} Z"/>
          <path class="fill-light" d="M{cx-50} {cy+30} Q{cx-90} {cy-10} {cx-55} {cy-40} Q{cx-20} {cy} {cx-50} {cy+30}"/>
          <path class="fill-light" d="M{cx+50} {cy+30} Q{cx+90} {cy-10} {cx+55} {cy-40} Q{cx+20} {cy} {cx+50} {cy+30}"/>
          <line class="outline" x1="{cx-60}" y1="{cy+90}" x2="{cx+60}" y2="{cy+90}"/>
        """,
        "light": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="105"/>
          <circle class="fill-accent" cx="{cx}" cy="{cy}" r="55"/>
          <line class="fill-light" x1="{cx}" y1="{cy-120}" x2="{cx}" y2="{cy-70}" stroke-width="6"/>
          <line class="fill-light" x1="{cx}" y1="{cy+70}" x2="{cx}" y2="{cy+120}" stroke-width="6"/>
          <line class="fill-light" x1="{cx-120}" y1="{cy}" x2="{cx-70}" y2="{cy}" stroke-width="6"/>
          <line class="fill-light" x1="{cx+70}" y1="{cy}" x2="{cx+120}" y2="{cy}" stroke-width="6"/>
        """,
        "bond": f"""
          <circle class="glow" cx="{cx-55}" cy="{cy}" r="55"/>
          <circle class="glow" cx="{cx+55}" cy="{cy}" r="55"/>
          <circle class="fill-accent" cx="{cx-55}" cy="{cy}" r="38"/>
          <circle class="fill-accent" cx="{cx+55}" cy="{cy}" r="38"/>
          <path class="fill-light" d="M{cx-17} {cy} Q{cx} {cy-40} {cx+17} {cy} Q{cx} {cy+40} {cx-17} {cy}" opacity="0.8"/>
        """,
        "spirit": f"""
          <circle class="glow" cx="{cx}" cy="{cy+20}" r="100"/>
          <path class="fill-accent" d="M{cx} {cy-80} Q{cx+60} {cy-20} {cx+50} {cy+40} Q{cx+20} {cy+100} {cx} {cy+130} Q{cx-20} {cy+100} {cx-50} {cy+40} Q{cx-60} {cy-20} {cx} {cy-80} Z" opacity="0.75"/>
          <ellipse class="fill-light" cx="{cx}" cy="{cy-30}" rx="35" ry="42"/>
        """,
        "energy": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="95"/>
          <path class="fill-accent" d="M{cx-15} {cy-90} L{cx+25} {cy-20} L{cx-5} {cy-20} L{cx+15} {cy+90} L{cx-25} {cy+20} L{cx-5} {cy+20} Z"/>
          <path class="fill-light" d="M{cx-50} {cy-40} L{cx-30} {cy} L{cx-55} {cy+10} Z" opacity="0.8"/>
          <path class="fill-light" d="M{cx+50} {cy-40} L{cx+30} {cy} L{cx+55} {cy+10} Z" opacity="0.8"/>
        """,
        "drain": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="90"/>
          <path class="fill-accent" d="M{cx} {cy-80} Q{cx+70} {cy} {cx} {cy+80} Q{cx-70} {cy} {cx} {cy-80} Z" opacity="0.7"/>
          <path class="fill-dark" d="M{cx} {cy+80} L{cx+30} {cy+30} L{cx-30} {cy+30} Z"/>
          <circle class="fill-light" cx="{cx}" cy="{cy-20}" r="22"/>
        """,
        "rage": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="95"/>
          <path class="fill-accent" d="M{cx-70} {cy+60} L{cx-40} {cy-30} L{cx} {cy+10} L{cx+40} {cy-30} L{cx+70} {cy+60} Z"/>
          <circle class="fill-light" cx="{cx-25}" cy="{cy-10}" r="14"/>
          <circle class="fill-light" cx="{cx+25}" cy="{cy-10}" r="14"/>
        """,
        "strike": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="85"/>
          <polygon class="fill-accent" points="{cx},{cy-80} {cx+35},{cy+20} {cx+10},{cy+20} {cx+20},{cy+80} {cx-20},{cy+80} {cx-10},{cy+20} {cx-35},{cy+20}"/>
        """,
        "illusion": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="95"/>
          <path class="fill-accent" d="M{cx-80} {cy+40} L{cx} {cy-70} L{cx+80} {cy+40} Z" opacity="0.55"/>
          <path class="fill-light" d="M{cx-55} {cy+30} L{cx} {cy-40} L{cx+55} {cy+30} Z" opacity="0.75"/>
          <circle class="fill-accent" cx="{cx}" cy="{cy+50}" r="18"/>
        """,
        "ritual": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="100"/>
          <circle class="outline" cx="{cx}" cy="{cy}" r="80" fill="none"/>
          <circle class="outline" cx="{cx}" cy="{cy}" r="55" fill="none"/>
          <polygon class="fill-accent" points="{cx},{cy-45} {cx+39},{cy+22} {cx-39},{cy+22}" opacity="0.85"/>
          <circle class="fill-light" cx="{cx}" cy="{cy+55}" r="12"/>
        """,
    }

    body = bodies.get(archetype, bodies["energy"])
    if scene:
        body += f"""
          <text x="48" y="480" fill="{entry['color']}" font-family="system-ui,sans-serif" font-size="22" font-weight="600">{entry['name'][:28]}</text>
          <text x="48" y="48" fill="#e2e8f0" font-family="system-ui,sans-serif" font-size="16" opacity="0.8">{'Light Side' if side == 'light' else 'Dark Side'} · {entry['category']}</text>
        """
    return body


def practitioners_for(entry: dict) -> list[str]:
    side = entry["side"]
    category = entry["category"]
    name = entry["name"].lower()
    base = ["Jedi Order", "Sith Order"] if side == "dark" else ["Jedi Order", "Force-sensitive traditions"]
    if "lightning" in name or "drain" in name:
        base = ["Sith Lords", "Emperor Palpatine", "Darth Sidious", "Sith Inquisitors"]
    elif "heal" in name or "barrier" in name:
        base = ["Jedi healers", "Rey", "Obi-Wan Kenobi", "Luke Skywalker"]
    elif "mind trick" in name or "persuasion" in name:
        base = ["Jedi Knights", "Obi-Wan Kenobi", "Rey", "Jedi Temple instructors"]
    elif "meditation" in name:
        base = ["Jedi Masters", "Oppo Rancisis", "Satele Shan", "Jedi Battlemasters"]
    elif "choke" in name or "grip" in name:
        base = ["Darth Vader", "Emperor Palpatine", "Sith Lords", "Dark-side adepts"]
    elif "kotor" in entry["sources"].lower() or "old republic" in entry["sources"].lower():
        base.append("Old Republic Force-users")
    if category == "Ritual":
        base = ["Ancient Sith", "Sith Emperor Vitiate", "Sith alchemists", "Nightsisters"]
    return list(dict.fromkeys(base))[:6]


def build_profile(entry: dict) -> dict:
    side_label = "light side" if entry["side"] == "light" else "dark side"
    side_doctrine = (
        "The Jedi teach that this ability must serve life, consent, and the greater good — never domination or fear."
        if entry["side"] == "light"
        else "The dark side amplifies this power through passion, anger, and the will to dominate — at the cost of corruption and suffering."
    )
    practitioners = practitioners_for(entry)

    overview = (
        f"{entry['name']} is a {entry['difficulty'].lower()}-level {side_label} technique classified under {entry['category']}. "
        f"{entry['desc']}"
    )

    history = (
        f"Force scholars trace {entry['name']} across eras recorded in holocrons, Jedi Archives data-tapes, and Sith tombs on Korriban and Dromund Kaas. "
        f"Practitioners documented in {entry['sources']} established the modern understanding of how this ability manifests in combat, meditation, and ritual.\n\n"
        f"During the Old Republic and Sith Empire conflicts, masters drilled {entry['name']} into initiates as part of the standard curriculum for {entry['category'].lower()} specialisation. "
        f"Surviving battle logs from the Clone Wars and Galactic Civil War show the technique adapted to blaster-era warfare, starfighter engagements, and close-quarters lightsaber duels.\n\n"
        f"In the sequel era, surviving texts and oral traditions kept knowledge of {entry['name']} alive even as the Jedi Temple fell and the Sith assumed new forms. "
        f"Each generation reinterpreted the power through its own doctrine while the underlying Force mechanism — channelled midi-chlorian symbiosis and focused will — remained constant.\n\n"
        f"{side_doctrine}"
    )

    significance = (
        f"{entry['name']} exemplifies how {entry['category'].lower()} abilities shape Force doctrine on the {side_label}. "
        f"At {entry['difficulty'].lower()} mastery, users balance raw potential against discipline, emotional control, and the moral weight of their choices.\n\n"
        f"Historians note that armies and orders rose or fell partly on how widely and wisely this technique was taught. "
        f"A single master of {entry['name']} could turn a skirmish, break a siege, or unravel an enemy's will before blades crossed.\n\n"
        f"For students today — in academies, hidden enclaves, or alone with ancient texts — {entry['name']} remains a benchmark of {entry['category'].lower()} proficiency across the Star Wars saga."
    )

    seed = int(hashlib.md5(entry["slug"].encode()).hexdigest()[:8], 16)
    events = [
        f"First major documented use of {entry['name']} in {ERAS[seed % len(ERAS)]} conflicts",
        f"Standardised in {entry['category']} curricula of the {'Jedi' if entry['side'] == 'light' else 'Sith'} academies",
        f"Featured prominently in media: {entry['sources'][:60]}{'…' if len(entry['sources']) > 60 else ''}",
        f"Requires {entry['difficulty']} training minimum before field deployment",
        f"Countermeasures developed by rival Force traditions and ysalamiri research",
    ]
    if entry["difficulty"] == "Master":
        events.append(f"Grand Master–level demonstrations of {entry['name']} altered galactic history")

    timeline = [
        {"era": ERAS[(seed + i) % len(ERAS)], "event": evt}
        for i, evt in enumerate(events[:5])
    ]

    return {
        "overview": overview,
        "history": history,
        "significance": significance,
        "notableEvents": events,
        "affiliations": practitioners,
        "timeline": timeline,
        "gallery": [
            {"path": f"/images/force-powers/{entry['slug']}.svg", "caption": f"Emblem — {entry['name']}"},
            {"path": f"/images/force-powers/{entry['slug']}-scene.svg", "caption": f"Scene illustration — {entry['name']}"},
        ],
    }


def main() -> None:
    entries = parse_powers(DATA)
    IMAGES.mkdir(parents=True, exist_ok=True)
    PROFILES.mkdir(parents=True, exist_ok=True)

    for entry in entries:
        slug = entry["slug"]
        accent = entry["color"]

        icon_path = IMAGES / f"{slug}.svg"
        scene_path = IMAGES / f"{slug}-scene.svg"
        profile_path = PROFILES / f"{slug}.json"

        icon_path.write_text(svg_wrap(entry["name"], accent, body_for(entry, scene=False)))
        scene_path.write_text(svg_wrap(f"{entry['name']} — scene", accent, body_for(entry, scene=True)))
        profile_path.write_text(json.dumps(build_profile(entry), indent=2, ensure_ascii=False) + "\n")

    light = sum(1 for e in entries if e["side"] == "light")
    dark = sum(1 for e in entries if e["side"] == "dark")
    print(f"Generated {len(entries)} force powers ({light} light, {dark} dark)")
    print(f"  SVG icons:  {len(entries)}")
    print(f"  SVG scenes: {len(entries)}")
    print(f"  Profiles:   {len(entries)}")


if __name__ == "__main__":
    main()
