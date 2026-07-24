#!/usr/bin/env python3
"""Generate Bounty Hunter C# data, SVG assets, and profile JSON."""

from __future__ import annotations

import json
import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HUNTER_CS = ROOT / "Data" / "BountyHunterData.cs"
HUNTER_IMAGES = ROOT / "wwwroot" / "images" / "bounty-hunters"
HUNTER_PROFILES = ROOT / "wwwroot" / "data" / "profiles" / "bounty-hunters"


def cs_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def slugify(name: str) -> str:
    s = name.lower().replace("'", "")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def xml_escape(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )


def join_sentences(*parts: str) -> str:
    return " ".join(p.strip() for p in parts if p and p.strip())


def join_paragraphs(*parts: str) -> str:
    return "\n\n".join(p.strip() for p in parts if p and p.strip())


def _tl(*pairs: tuple[str, str]) -> list[tuple[str, str]]:
    return list(pairs)


def _ev(*items: str) -> list[str]:
    return list(items)


def _aff(*items: str) -> list[str]:
    return list(items)


def build_bounty_hunter_lore(
    name: str,
    specialty: str,
    homeworld: str,
    *,
    origin_detail: str,
    ancient_detail: str,
    modern_detail: str,
    conflict_detail: str,
    methods_detail: str,
    reputation_detail: str,
    impact_detail: str,
    events: list[str],
    affiliations: list[str],
    timeline: list[tuple[str, str]],
) -> dict:
    origins = join_sentences(
        f"{name} rose from {homeworld} to become a {specialty.lower()} whose name appears on guild boards from the Core to the Outer Rim.",
        origin_detail,
        f"Bounty puck archives, Imperial warrant logs, and Hutt contract registries all document {name} as a contractor who shaped wars without wearing a uniform.",
        f"Coverage spans all nine saga films, Clone Wars, Rebels, Mandalorian, Book of Boba Fett, Andor, KOTOR, KOTOR II, SWTOR, and Sith Empire-era mercenary markets.",
    )
    ancient = join_sentences(
        f"Even before {name}'s career, {homeworld} produced hunters, soldiers, and syndicate enforcers whose traditions fed the modern guild system.",
        ancient_detail,
        f"Old Republic bounty charters and Sith Empire mercenary rolls show how {specialty.lower()} contractors were hired to bypass political treaties.",
        f"Mandalorian foundling laws and Hutt kajidic codes both influenced how hunters like {name} negotiate payment and honor.",
    )
    modern = join_sentences(
        f"In the modern era, {name} competed on postings issued by the Empire, the Rebellion, the Hutt Cartel, and independent monarchs alike.",
        modern_detail,
        f"Post-Endor guild restructuring and New Republic amnesty debates still reference contracts linked to {name}.",
        f"Mandalorian-era postings on Nevarro and Mos Espa show {specialty.lower()} specialists remain essential to galactic order—and chaos.",
    )
    conflicts = join_sentences(
        f"{name} operated in war zones where capture alive paid more than kill, and both paid more than failure.",
        conflict_detail,
        f"KOTOR-era Nar Shaddaa boards and TOR-era Great Galactic War contracts show earlier generations of {specialty.lower()} hunters in the same blood-stained market.",
        f"Jedi, Sith, and clone troopers alike learned to respect or fear {name}'s approach to pursuit and extraction.",
    )
    methods = join_sentences(
        f"Operational profiles classify {name} as a {specialty.lower()} relying on specific tactics—tracking, intimidation, sniper overwatch, or starship interception.",
        methods_detail,
        f"Guild instructors use redacted mission logs from {name}'s career to teach negotiation, trap-setting, and when to walk away from a bounty.",
        f"Imperial Security Bureau analysts note that hunters like {name} often know smuggler routes better than naval patrols.",
    )
    reputation = join_sentences(
        f"Among peers, {name} earned a reputation that outlived individual contracts—feared, respected, or mocked, but rarely ignored.",
        reputation_detail,
        f"Hunter cantinas on Nar Shaddaa, Ord Mantell, and Tatooine still tell stories about {name} that may be half true and fully instructive.",
        f"Whether {name} followed the Bounty Hunter Code or broke it defines how guild historians judge their legacy.",
    )
    impact = join_sentences(
        f"The galactic impact of {name} exceeds credit totals: key captures, assassinations, and rescues altered the timeline.",
        impact_detail,
        f"Without contractors like {name}, governments would need armies ten times larger to enforce law across the Rim.",
        f"New Republic reformers cite {name} when arguing for guild regulation versus outright prohibition of bounty hunting.",
    )
    return {
        "origins": origins,
        "ancient": ancient,
        "modern": modern,
        "conflicts": conflicts,
        "methods": methods,
        "reputation": reputation,
        "impact": impact,
        "events": events,
        "affiliations": affiliations,
        "timeline": [{"era": era, "event": event} for era, event in timeline],
    }


def bp(
    name: str,
    specialty: str,
    homeworld: str,
    description: str,
    color: str,
    sources: str,
    silhouette: str,
    lore_kwargs: dict,
) -> dict:
    slug = slugify(name)
    lore = build_bounty_hunter_lore(name, specialty, homeworld, **lore_kwargs)
    return {
        "name": name,
        "slug": slug,
        "specialty": specialty,
        "homeworld": homeworld,
        "description": description,
        "color": color,
        "sources": sources,
        "silhouette": silhouette,
        "lore": lore,
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


def scene_backdrop(accent: str, scene: bool) -> str:
    if not scene:
        return ""
    return f"""
          <rect x="0" y="360" width="512" height="152" fill="#0a0f1a" opacity="0.85"/>
          <rect x="0" y="360" width="512" height="4" fill="{accent}" opacity="0.45"/>
          <ellipse cx="420" cy="88" rx="48" ry="48" fill="{accent}" opacity="0.12"/>
          <ellipse cx="460" cy="72" rx="28" ry="28" fill="#cbd5e1" opacity="0.18"/>
          <circle cx="72" cy="92" r="22" fill="{accent}" opacity="0.55"/>
          <circle cx="98" cy="78" r="14" fill="#e2e8f0" opacity="0.35"/>
        """


def bounty_puck(accent: str, scene: bool) -> str:
    if not scene:
        return ""
    return f"""
          <circle cx="448" cy="448" r="28" fill="#111827" stroke="{accent}" stroke-width="3"/>
          <circle cx="448" cy="448" r="14" fill="{accent}" opacity="0.85"/>
          <text x="448" y="454" text-anchor="middle" fill="#fff" font-family="system-ui,sans-serif" font-size="14" font-weight="700">₵</text>
        """


def svg_wrap(title: str, accent: str, body: str, slug: str) -> str:
    sid = re.sub(r"[^a-z0-9]", "", slug) or "hunter"
    safe_title = xml_escape(title)
    return textwrap.dedent(
        f"""
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" role="img" aria-label="{safe_title}">
          <defs>
            <linearGradient id="bgGrad-{sid}" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="{accent}" stop-opacity="0.55"/>
              <stop offset="100%" stop-color="#050814" stop-opacity="0.95"/>
            </linearGradient>
            <radialGradient id="glowGrad-{sid}" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="{accent}" stop-opacity="0.85"/>
              <stop offset="100%" stop-color="{accent}" stop-opacity="0"/>
            </radialGradient>
            <filter id="glow-{sid}" x="-50%" y="-50%" width="200%" height="200%">
              <feGaussianBlur stdDeviation="8" result="blur"/>
              <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
            </filter>
          </defs>
          <style>
            .bg {{ fill: url(#bgGrad-{sid}); }}
            .outline {{ fill: none; stroke: #1a1a2e; stroke-width: 3; stroke-linecap: round; stroke-linejoin: round; }}
            .fill-accent {{ fill: {accent}; stroke: #1a1a2e; stroke-width: 3; }}
            .fill-light {{ fill: #e2e8f0; stroke: #1a1a2e; stroke-width: 3; }}
            .fill-dark {{ fill: #1a1a2e; stroke: #1a1a2e; stroke-width: 3; }}
            .fill-skin {{ fill: #f4c99b; stroke: #1a1a2e; stroke-width: 3; }}
            .fill-metal {{ fill: #b8c4d0; stroke: #1a1a2e; stroke-width: 3; }}
            .fill-mid {{ fill: {accent}; opacity: 0.65; stroke: #1a1a2e; stroke-width: 2; }}
            .glow {{ fill: url(#glowGrad-{sid}); filter: url(#glow-{sid}); }}
          </style>
          <rect class="bg" width="512" height="512" rx="24"/>
          {starfield()}
          {body}
        </svg>
        """
    ).strip() + "\n"


def hunter_body(kind: str, scene: bool, name: str, accent: str, specialty: str) -> str:
    cx, cy = 256, 270
    safe_name = xml_escape(name[:32])
    safe_specialty = xml_escape(specialty[:40])
    bodies = {
        "mando": f"""
          {scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="105"/>
          <rect class="fill-metal" x="{cx-48}" y="{cy+55}" width="96" height="28" rx="8" opacity="0.9"/>
          <path class="fill-accent" d="M{cx-48} {cy-88} Q{cx} {cy-122} {cx+48} {cy-88} L{cx+52} {cy-38} Q{cx} {cy-18} {cx-52} {cy-38} Z"/>
          <rect class="fill-light" x="{cx-14}" y="{cy-58}" width="28" height="20" rx="4"/>
          <line class="outline" x1="{cx+20}" y1="{cy-72}" x2="{cx+34}" y2="{cy-95}"/>
          <circle class="fill-dark" cx="{cx+34}" cy="{cy-95}" r="5"/>
          <rect class="fill-accent" x="{cx-42}" y="{cy-2}" width="84" height="98" rx="16"/>
          <rect class="fill-metal" x="{cx-18}" y="{cy+18}" width="36" height="42" rx="6"/>
          <rect class="fill-dark" x="{cx-72}" y="{cy+35}" width="28" height="14" rx="4" transform="rotate(-12 {cx-72} {cy+35})"/>
          <rect class="fill-dark" x="{cx+44}" y="{cy+35}" width="28" height="14" rx="4" transform="rotate(12 {cx+44} {cy+35})"/>
          <path class="fill-metal" d="M{cx-8} {cy+58} L{cx} {cy+95} L{cx+8} {cy+58} Z"/>
          <line class="outline" x1="{cx-42}" y1="{cy+28}" x2="{cx-78}" y2="{cy+58}"/>
          <line class="outline" x1="{cx+42}" y1="{cy+28}" x2="{cx+78}" y2="{cy+58}"/>
        """,
        "human": f"""
          {scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="98"/>
          <circle class="fill-skin" cx="{cx}" cy="{cy-58}" r="38"/>
          <path class="fill-dark" d="M{cx-38} {cy-78} Q{cx} {cy-98} {cx+38} {cy-78} Q{cx} {cy-62} {cx-38} {cy-78}"/>
          <circle class="fill-light" cx="{cx-14}" cy="{cy-62}" r="7"/>
          <circle class="fill-light" cx="{cx+14}" cy="{cy-62}" r="7"/>
          <circle class="fill-dark" cx="{cx-12}" cy="{cy-60}" r="3"/>
          <circle class="fill-dark" cx="{cx+16}" cy="{cy-60}" r="3"/>
          <path class="outline" d="M{cx-12} {cy-42} Q{cx} {cy-34} {cx+12} {cy-42}"/>
          <rect class="fill-accent" x="{cx-44}" y="{cy-8}" width="88" height="102" rx="16"/>
          <rect class="fill-dark" x="{cx-68}" y="{cy+18}" width="34" height="16" rx="4"/>
          <line class="outline" x1="{cx-44}" y1="{cy+22}" x2="{cx-82}" y2="{cy+52}"/>
          <line class="outline" x1="{cx+44}" y1="{cy+22}" x2="{cx+82}" y2="{cy+52}"/>
          <line class="outline" x1="{cx-44}" y1="{cy+55}" x2="{cx-72}" y2="{cy+95}"/>
          <line class="outline" x1="{cx+44}" y1="{cy+55}" x2="{cx+72}" y2="{cy+95}"/>
        """,
        "rodian": f"""
          {scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="98"/>
          <ellipse class="fill-accent" cx="{cx}" cy="{cy-54}" rx="46" ry="36"/>
          <ellipse class="fill-skin" cx="{cx}" cy="{cy-54}" rx="34" ry="28"/>
          <ellipse class="fill-accent" cx="{cx+38}" cy="{cy-48}" rx="20" ry="14"/>
          <circle class="fill-light" cx="{cx-12}" cy="{cy-58}" r="8"/>
          <circle class="fill-dark" cx="{cx-10}" cy="{cy-56}" r="3"/>
          <rect class="fill-accent" x="{cx-36}" y="{cy-2}" width="72" height="98" rx="14"/>
          <rect class="fill-dark" x="{cx-62}" y="{cy+20}" width="36" height="14" rx="4"/>
        """,
        "trandoshan": f"""
          {scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="102"/>
          <ellipse class="fill-accent" cx="{cx}" cy="{cy-50}" rx="48" ry="42"/>
          <circle class="fill-light" cx="{cx-16}" cy="{cy-58}" r="9"/>
          <circle class="fill-light" cx="{cx+16}" cy="{cy-58}" r="9"/>
          <circle class="fill-dark" cx="{cx-14}" cy="{cy-56}" r="4"/>
          <circle class="fill-dark" cx="{cx+18}" cy="{cy-56}" r="4"/>
          <path class="outline" d="M{cx-18} {cy-34} L{cx-8} {cy-28} M{cx+18} {cy-34} L{cx+8} {cy-28}"/>
          <rect class="fill-accent" x="{cx-42}" y="{cy-2}" width="84" height="102" rx="16"/>
          <line class="outline" x1="{cx-42}" y1="{cy+30}" x2="{cx-78}" y2="{cy+62}"/>
        """,
        "droid": f"""
          {scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="98"/>
          <rect class="fill-metal" x="{cx-32}" y="{cy-82}" width="64" height="46" rx="10"/>
          <rect class="fill-light" x="{cx-24}" y="{cy-72}" width="48" height="24" rx="6"/>
          <rect class="fill-accent" x="{cx-36}" y="{cy-22}" width="72" height="118" rx="14"/>
          <circle class="fill-dark" cx="{cx-14}" cy="{cy-66}" r="8"/>
          <circle class="fill-dark" cx="{cx+14}" cy="{cy-66}" r="8"/>
          <circle class="fill-light" cx="{cx-14}" cy="{cy-66}" r="3"/>
          <circle class="fill-light" cx="{cx+14}" cy="{cy-66}" r="3"/>
          <rect class="fill-dark" x="{cx-48}" y="{cy+10}" width="24" height="52" rx="6"/>
          <rect class="fill-dark" x="{cx+24}" y="{cy+10}" width="24" height="52" rx="6"/>
          <line class="outline" x1="{cx}" y1="{cy+96}" x2="{cx}" y2="{cy+118}"/>
        """,
        "twilek": f"""
          {scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="98"/>
          <circle class="fill-skin" cx="{cx}" cy="{cy-54}" r="36"/>
          <circle class="fill-light" cx="{cx-12}" cy="{cy-58}" r="7"/>
          <circle class="fill-light" cx="{cx+12}" cy="{cy-58}" r="7"/>
          <path class="fill-accent" d="M{cx-34} {cy-54} Q{cx-92} {cy-8} {cx-74} {cy+38} Q{cx-52} {cy+10} {cx-34} {cy-18}"/>
          <path class="fill-accent" d="M{cx+34} {cy-54} Q{cx+92} {cy-8} {cx+74} {cy+38} Q{cx+52} {cy+10} {cx+34} {cy-18}"/>
          <rect class="fill-accent" x="{cx-36}" y="{cy-2}" width="72" height="98" rx="14"/>
          <rect class="fill-dark" x="{cx-58}" y="{cy+18}" width="30" height="14" rx="4"/>
        """,
        "wookiee": f"""
          {scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="108"/>
          <ellipse class="fill-accent" cx="{cx}" cy="{cy-46}" rx="52" ry="46"/>
          <circle class="fill-light" cx="{cx-18}" cy="{cy-52}" r="10"/>
          <circle class="fill-light" cx="{cx+18}" cy="{cy-52}" r="10"/>
          <rect class="fill-accent" x="{cx-50}" y="{cy+2}" width="100" height="92" rx="20"/>
          <path class="fill-accent" d="M{cx-50} {cy+28} Q{cx-88} {cy+58} {cx-72} {cy+98}"/>
          <line class="outline" x1="{cx-50}" y1="{cy+28}" x2="{cx-88}" y2="{cy+58}"/>
        """,
        "chiss": f"""
          {scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="98"/>
          <circle class="fill-accent" cx="{cx}" cy="{cy-54}" r="36" opacity="0.92"/>
          <circle class="fill-light" cx="{cx-14}" cy="{cy-58}" r="8"/>
          <circle class="fill-light" cx="{cx+14}" cy="{cy-58}" r="8"/>
          <circle class="fill-dark" cx="{cx-12}" cy="{cy-56}" r="3"/>
          <circle class="fill-dark" cx="{cx+16}" cy="{cy-56}" r="3"/>
          <rect class="fill-accent" x="{cx-38}" y="{cy-2}" width="76" height="98" rx="14"/>
          <rect class="fill-dark" x="{cx-62}" y="{cy+18}" width="32" height="14" rx="4"/>
        """,
        "zabrak": f"""
          {scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="98"/>
          <circle class="fill-skin" cx="{cx}" cy="{cy-54}" r="36"/>
          <path class="fill-accent" d="M{cx-22} {cy-92} L{cx-32} {cy-58} L{cx-8} {cy-68} Z"/>
          <path class="fill-accent" d="M{cx+22} {cy-92} L{cx+32} {cy-58} L{cx+8} {cy-68} Z"/>
          <circle class="fill-light" cx="{cx-12}" cy="{cy-58}" r="7"/>
          <circle class="fill-light" cx="{cx+12}" cy="{cy-58}" r="7"/>
          <rect class="fill-accent" x="{cx-36}" y="{cy-2}" width="72" height="98" rx="14"/>
        """,
        "clawdite": f"""
          {scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="95"/>
          <ellipse class="fill-accent" cx="{cx}" cy="{cy-46}" rx="42" ry="38" opacity="0.88"/>
          <ellipse class="fill-skin" cx="{cx}" cy="{cy-46}" rx="30" ry="28" opacity="0.75"/>
          <circle class="fill-light" cx="{cx-12}" cy="{cy-50}" r="7"/>
          <circle class="fill-light" cx="{cx+12}" cy="{cy-50}" r="7"/>
          <rect class="fill-light" x="{cx-34}" y="{cy-2}" width="68" height="98" rx="14" opacity="0.92"/>
          <path class="fill-accent" d="M{cx-34} {cy+20} Q{cx} {cy+38} {cx+34} {cy+20}" fill="none" stroke-width="4"/>
        """,
        "cyborg": f"""
          {scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="102"/>
          <circle class="fill-skin" cx="{cx}" cy="{cy-54}" r="34"/>
          <circle class="fill-light" cx="{cx-12}" cy="{cy-58}" r="7"/>
          <circle class="fill-light" cx="{cx+12}" cy="{cy-58}" r="7"/>
          <rect class="fill-accent" x="{cx-40}" y="{cy-2}" width="80" height="102" rx="14"/>
          <rect class="fill-dark" x="{cx+16}" y="{cy+8}" width="26" height="58" rx="5"/>
          <rect class="fill-metal" x="{cx+20}" y="{cy+14}" width="18" height="10" rx="2"/>
          <line class="outline" x1="{cx-40}" y1="{cy+28}" x2="{cx-78}" y2="{cy+58}"/>
        """,
        "helmet": f"""
          {scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="102"/>
          <path class="fill-accent" d="M{cx-44} {cy-82} Q{cx} {cy-114} {cx+44} {cy-82} L{cx+48} {cy-28} L{cx-48} {cy-28} Z"/>
          <rect class="fill-light" x="{cx-20}" y="{cy-52}" width="40" height="16" rx="4"/>
          <rect class="fill-accent" x="{cx-38}" y="{cy-2}" width="76" height="98" rx="14"/>
          <rect class="fill-dark" x="{cx-64}" y="{cy+18}" width="32" height="14" rx="4"/>
        """,
        "alien": f"""
          {scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="96"/>
          <ellipse class="fill-accent" cx="{cx}" cy="{cy-50}" rx="40" ry="42"/>
          <ellipse class="fill-light" cx="{cx-18}" cy="{cy-54}" rx="11" ry="15"/>
          <ellipse class="fill-light" cx="{cx+18}" cy="{cy-54}" rx="11" ry="15"/>
          <circle class="fill-dark" cx="{cx-16}" cy="{cy-52}" r="4"/>
          <circle class="fill-dark" cx="{cx+20}" cy="{cy-52}" r="4"/>
          <rect class="fill-accent" x="{cx-36}" y="{cy-2}" width="72" height="98" rx="14"/>
        """,
        "nautolan": f"""
          {scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="98"/>
          <circle class="fill-accent" cx="{cx}" cy="{cy-52}" r="36"/>
          <circle class="fill-light" cx="{cx-12}" cy="{cy-56}" r="7"/>
          <circle class="fill-light" cx="{cx+12}" cy="{cy-56}" r="7"/>
          <path class="outline" d="M{cx-32} {cy-58} Q{cx-58} {cy+8} {cx-42} {cy+52}" stroke="{accent}" stroke-width="7"/>
          <path class="outline" d="M{cx+32} {cy-58} Q{cx+58} {cy+8} {cx+42} {cy+52}" stroke="{accent}" stroke-width="7"/>
          <rect class="fill-accent" x="{cx-36}" y="{cy-2}" width="72" height="98" rx="14"/>
        """,
        "weequay": f"""
          {scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="96"/>
          <ellipse class="fill-skin" cx="{cx}" cy="{cy-50}" rx="38" ry="40"/>
          <path class="fill-dark" d="M{cx-28} {cy-72} Q{cx} {cy-94} {cx+28} {cy-72} L{cx+22} {cy-46} L{cx-22} {cy-46} Z"/>
          <circle class="fill-light" cx="{cx-12}" cy="{cy-54}" r="6"/>
          <circle class="fill-light" cx="{cx+12}" cy="{cy-54}" r="6"/>
          <rect class="fill-accent" x="{cx-36}" y="{cy-2}" width="72" height="98" rx="14"/>
        """,
        "hutt": f"""
          {scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy+10}" r="98"/>
          <ellipse class="fill-accent" cx="{cx}" cy="{cy+28}" rx="118" ry="82"/>
          <ellipse class="fill-accent" cx="{cx}" cy="{cy-18}" rx="78" ry="62"/>
          <circle class="fill-light" cx="{cx-22}" cy="{cy-28}" r="14"/>
          <circle class="fill-light" cx="{cx+22}" cy="{cy-28}" r="14"/>
          <circle class="fill-dark" cx="{cx-18}" cy="{cy-26}" r="5"/>
          <circle class="fill-dark" cx="{cx+26}" cy="{cy-26}" r="5"/>
        """,
    }
    body = bodies.get(kind, bodies["human"])
    body += bounty_puck(accent, scene)
    if scene:
        body += f"""
          <text x="48" y="480" fill="{accent}" font-family="system-ui,sans-serif" font-size="20" font-weight="600">{safe_name}</text>
          <text x="48" y="48" fill="#e2e8f0" font-family="system-ui,sans-serif" font-size="15" opacity="0.85">{safe_specialty}</text>
        """
    return body


def build_hunter_profile(entry: dict) -> dict:
    lore = entry["lore"]
    overview = join_sentences(
        f"{entry['name']} is a {entry['specialty'].lower()} from {entry['homeworld']}, documented across {entry['sources']}.",
        entry["description"],
    )
    history = join_paragraphs(lore["origins"], lore["ancient"], lore["modern"], lore["conflicts"])
    significance = join_paragraphs(lore["methods"], lore["reputation"], lore["impact"])
    return {
        "overview": overview,
        "history": history,
        "significance": significance,
        "notableEvents": lore["events"],
        "affiliations": lore["affiliations"],
        "timeline": lore["timeline"],
        "gallery": [
            {"path": f"/images/bounty-hunters/{entry['slug']}.svg", "caption": f"Emblem — {entry['name']}"},
            {"path": f"/images/bounty-hunters/{entry['slug']}-scene.svg", "caption": f"Scene illustration — {entry['name']}"},
        ],
    }


def write_hunter_cs(entries: list[dict]) -> None:
    lines = [
        "using StarWars.Models;",
        "",
        "namespace StarWars.Data;",
        "",
        "public static class BountyHunterData",
        "{",
        "    public static IReadOnlyList<BountyHunter> BountyHunters { get; } =",
        "    [",
    ]
    for e in entries:
        lines.extend([
            "        new()",
            "        {",
            f'            Name = "{cs_escape(e["name"])}",',
            f'            Slug = "{cs_escape(e["slug"])}",',
            f'            Route = "bounty-hunters/{cs_escape(e["slug"])}",',
            f'            Specialty = "{cs_escape(e["specialty"])}",',
            f'            Homeworld = "{cs_escape(e["homeworld"])}",',
            f'            Description = "{cs_escape(e["description"])}",',
            f'            Color = "{cs_escape(e["color"])}",',
            f'            Sources = "{cs_escape(e["sources"])}",',
            "        },",
        ])
    lines.extend([
        "    ];",
        "",
        "    public static BountyHunter? GetBySlug(string slug) =>",
        "        BountyHunters.FirstOrDefault(h => h.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));",
        "}",
        "",
    ])
    HUNTER_CS.write_text("\n".join(lines))


def main() -> None:
    from bounty_hunter_catalog_data import BOUNTY_HUNTERS

    try:
        from bounty_hunter_catalog_additions import ADDITIONAL_BOUNTY_HUNTERS
    except ImportError:
        ADDITIONAL_BOUNTY_HUNTERS = []

    seen: set[str] = set()
    all_hunters: list[dict] = []
    for entry in BOUNTY_HUNTERS + ADDITIONAL_BOUNTY_HUNTERS:
        if entry["slug"] in seen:
            continue
        seen.add(entry["slug"])
        all_hunters.append(entry)

    HUNTER_IMAGES.mkdir(parents=True, exist_ok=True)
    HUNTER_PROFILES.mkdir(parents=True, exist_ok=True)

    write_hunter_cs(all_hunters)

    for entry in all_hunters:
        slug = entry["slug"]
        accent = entry["color"]
        kind = entry["silhouette"]
        (HUNTER_IMAGES / f"{slug}.svg").write_text(
            svg_wrap(entry["name"], accent, hunter_body(kind, False, entry["name"], accent, entry["specialty"]), slug)
        )
        (HUNTER_IMAGES / f"{slug}-scene.svg").write_text(
            svg_wrap(
                f"{entry['name']} — scene",
                accent,
                hunter_body(kind, True, entry["name"], accent, entry["specialty"]),
                f"{slug}-scene",
            )
        )
        (HUNTER_PROFILES / f"{slug}.json").write_text(
            json.dumps(build_hunter_profile(entry), indent=2, ensure_ascii=False) + "\n"
        )

    print(f"Generated {len(all_hunters)} bounty hunters")
    print("  BountyHunterData.cs")
    print(f"  Bounty hunter assets: {len(all_hunters)} icons, {len(all_hunters)} scenes, {len(all_hunters)} profiles")
    print(f"  Total files: {1 + len(all_hunters) * 3}")


if __name__ == "__main__":
    main()
