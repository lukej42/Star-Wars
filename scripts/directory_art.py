#!/usr/bin/env python3
"""Rich SVG artwork for Ships, Species, and Droids directory entries."""

from __future__ import annotations

import re
import textwrap

OUTLINE = "#1a1a2e"


def xml_escape(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )


def slug_id(slug: str, suffix: str = "") -> str:
    sid = re.sub(r"[^a-z0-9]", "", slug) or "asset"
    return sid + suffix


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


def svg_wrap(title: str, accent: str, body: str, slug: str = "asset") -> str:
    sid = slug_id(slug)
    safe_title = xml_escape(title)
    return textwrap.dedent(
        f"""
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" role="img" aria-label="{safe_title}">
          <defs>
            <linearGradient id="bgGrad-{sid}" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="{accent}" stop-opacity="0.58"/>
              <stop offset="100%" stop-color="#050814" stop-opacity="0.96"/>
            </linearGradient>
            <radialGradient id="glowGrad-{sid}" cx="50%" cy="45%" r="50%">
              <stop offset="0%" stop-color="{accent}" stop-opacity="0.75"/>
              <stop offset="100%" stop-color="{accent}" stop-opacity="0"/>
            </radialGradient>
            <filter id="softGlow-{sid}" x="-50%" y="-50%" width="200%" height="200%">
              <feGaussianBlur stdDeviation="7" result="blur"/>
              <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
            </filter>
          </defs>
          <style>
            .bg {{ fill: url(#bgGrad-{sid}); }}
            .outline {{ fill: none; stroke: {OUTLINE}; stroke-width: 3; stroke-linecap: round; stroke-linejoin: round; }}
            .fill-accent {{ fill: {accent}; stroke: {OUTLINE}; stroke-width: 3; }}
            .fill-light {{ fill: #e2e8f0; stroke: {OUTLINE}; stroke-width: 3; }}
            .fill-dark {{ fill: #1a1a2e; stroke: {OUTLINE}; stroke-width: 3; }}
            .fill-mid {{ fill: #94a3b8; stroke: {OUTLINE}; stroke-width: 3; }}
            .fill-skin {{ fill: #f4c99b; stroke: {OUTLINE}; stroke-width: 3; }}
            .fill-metal {{ fill: #b8c4d0; stroke: {OUTLINE}; stroke-width: 3; }}
            .fill-panel {{ fill: {accent}; opacity: 0.45; stroke: {OUTLINE}; stroke-width: 2; }}
            .glow {{ fill: url(#glowGrad-{sid}); filter: url(#softGlow-{sid}); }}
            .stroke-accent {{ fill: none; stroke: {accent}; stroke-width: 2; stroke-linecap: round; opacity: 0.7; }}
          </style>
          <rect class="bg" width="512" height="512" rx="24"/>
          {starfield()}
          {body}
        </svg>
        """
    ).strip() + "\n"


def species_scene_backdrop(accent: str, scene: bool) -> str:
    if not scene:
        return ""
    return f"""
          <rect x="0" y="358" width="512" height="154" fill="#0a0f1a" opacity="0.82"/>
          <rect x="0" y="358" width="512" height="4" fill="{accent}" opacity="0.5"/>
          <ellipse cx="420" cy="88" rx="46" ry="46" fill="{accent}" opacity="0.14"/>
          <ellipse cx="448" cy="72" rx="24" ry="24" fill="#e2e8f0" opacity="0.18"/>
          <path fill="{accent}" opacity="0.25" d="M0 390 Q128 360 256 380 T512 370 L512 512 H0 Z"/>
        """


def droid_scene_backdrop(accent: str, scene: bool) -> str:
    if not scene:
        return ""
    return f"""
          <rect x="0" y="340" width="512" height="172" fill="#111827" opacity="0.88"/>
          <rect x="0" y="340" width="512" height="4" fill="{accent}" opacity="0.55"/>
          <line class="stroke-accent" x1="48" y1="380" x2="464" y2="380"/>
          <line class="stroke-accent" x1="48" y1="420" x2="464" y2="420"/>
          <rect x="72" y="360" width="48" height="12" rx="3" fill="{accent}" opacity="0.35"/>
          <rect x="392" y="360" width="48" height="12" rx="3" fill="{accent}" opacity="0.35"/>
          <circle cx="128" cy="400" r="6" fill="#22c55e" opacity="0.85"/>
          <circle cx="384" cy="400" r="6" fill="#ef4444" opacity="0.75"/>
        """


def scene_labels(name: str, subtitle: str, accent: str) -> str:
    safe_name = xml_escape(name[:32])
    safe_sub = xml_escape(subtitle[:40])
    return f"""
          <text x="48" y="480" fill="{accent}" font-family="system-ui,sans-serif" font-size="20" font-weight="600">{safe_name}</text>
          <text x="48" y="48" fill="#e2e8f0" font-family="system-ui,sans-serif" font-size="15" opacity="0.88">{safe_sub}</text>
        """


def ship_kind(entry: dict) -> str:
    blob = f"{entry['name']} {entry.get('role', '')} {entry.get('desc', '')}".lower()
    if "battle station" in blob or "death star" in blob:
        return "station"
    if any(k in blob for k in ("destroyer", "cruiser", "dreadnought", "battleship", "frigate", "corvette", "carrier")):
        return "capital"
    if any(k in blob for k in ("freighter", "transport", "yacht")):
        return "freighter"
    if any(k in blob for k in ("bomber", "gunship", "lander")):
        return "bomber"
    if "shuttle" in blob:
        return "shuttle"
    if "droid" in blob:
        return "droid"
    if any(k in blob for k in ("speeder", "airspeeder")):
        return "speeder"
    return "fighter"


def ship_portrait_body(kind: str, accent: str) -> str:
    cx, cy = 256, 268
    engines = f"""
          <ellipse fill="#38bdf8" cx="118" cy="348" rx="18" ry="10" opacity="0.55"/>
          <ellipse fill="#38bdf8" cx="394" cy="348" rx="18" ry="10" opacity="0.55"/>
        """
    bodies = {
        "capital": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="108"/>
          <path class="fill-accent" d="M52 310 L228 130 L460 310 L418 392 L98 392 Z"/>
          <rect class="fill-light" x="198" y="168" width="116" height="52" rx="8"/>
          <rect class="fill-metal" x="168" y="318" width="176" height="38" rx="6"/>
          <rect class="fill-panel" x="188" y="200" width="36" height="18" rx="3"/>
          <rect class="fill-panel" x="288" y="200" width="36" height="18" rx="3"/>
          <line class="outline" x1="256" y1="130" x2="256" y2="168"/>
          {engines}
        """,
        "station": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="112"/>
          <circle class="fill-accent" cx="{cx}" cy="{cy}" r="118"/>
          <circle class="fill-dark" cx="{cx}" cy="{cy}" r="68"/>
          <rect class="fill-light" x="232" y="88" width="48" height="76" rx="6"/>
          <rect class="fill-light" x="232" y="372" width="48" height="76" rx="6"/>
          <rect class="fill-light" x="88" y="232" width="76" height="48" rx="6"/>
          <rect class="fill-light" x="348" y="232" width="76" height="48" rx="6"/>
          <circle class="fill-metal" cx="{cx}" cy="{cy}" r="22"/>
        """,
        "freighter": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="102"/>
          <ellipse class="fill-accent" cx="{cx}" cy="292" rx="158" ry="72"/>
          <rect class="fill-light" x="178" y="198" width="156" height="82" rx="16"/>
          <rect class="fill-metal" x="208" y="218" width="96" height="36" rx="6"/>
          <circle class="fill-dark" cx="118" cy="302" r="24"/>
          <circle class="fill-dark" cx="394" cy="302" r="24"/>
          <rect class="fill-panel" x="188" y="268" width="28" height="14" rx="3"/>
          <rect class="fill-panel" x="296" y="268" width="28" height="14" rx="3"/>
        """,
        "bomber": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="100"/>
          <path class="fill-accent" d="M78 308 L208 228 L328 308 L288 348 L118 348 Z"/>
          <rect class="fill-light" x="214" y="262" width="84" height="50" rx="10"/>
          <circle class="fill-dark" cx="152" cy="318" r="20"/>
          <circle class="fill-dark" cx="360" cy="318" r="20"/>
          <path class="fill-metal" d="M238 348 L270 392 L238 432 L206 392 Z"/>
        """,
        "shuttle": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="98"/>
          <rect class="fill-accent" x="148" y="228" width="216" height="84" rx="14"/>
          <path class="fill-light" d="M148 268 L68 328 L148 308 Z"/>
          <path class="fill-light" d="M364 268 L444 328 L364 308 Z"/>
          <rect class="fill-metal" x="214" y="248" width="84" height="44" rx="8"/>
          <rect class="fill-panel" x="232" y="292" width="48" height="12" rx="3"/>
        """,
        "droid": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="92"/>
          <circle class="fill-accent" cx="{cx}" cy="268" r="78"/>
          <rect class="fill-light" x="214" y="188" width="84" height="42" rx="10"/>
          <line class="outline" x1="{cx}" y1="346" x2="{cx}" y2="408"/>
          <circle class="fill-dark" cx="208" cy="228" r="14"/>
          <circle class="fill-dark" cx="304" cy="228" r="14"/>
        """,
        "speeder": f"""
          <circle class="glow" cx="{cx}" cy="{cy+20}" r="88"/>
          <path class="fill-accent" d="M128 320 Q256 260 384 320 L352 360 H160 Z"/>
          <rect class="fill-light" x="214" y="288" width="84" height="28" rx="8"/>
          <circle class="fill-dark" cx="168" cy="360" r="18"/>
          <circle class="fill-dark" cx="344" cy="360" r="18"/>
        """,
        "fighter": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="100"/>
          <path class="fill-accent" d="M118 308 L256 178 L394 308 L342 348 H170 Z"/>
          <rect class="fill-light" x="226" y="218" width="60" height="58" rx="8"/>
          <path class="fill-metal" d="M256 178 L274 136 L238 136 Z"/>
          <circle class="fill-dark" cx="154" cy="318" r="16"/>
          <circle class="fill-dark" cx="358" cy="318" r="16"/>
          <ellipse fill="#38bdf8" cx="256" cy="348" rx="12" ry="22" opacity="0.65"/>
        """,
    }
    return bodies.get(kind, bodies["fighter"])


def ship_svg_for(entry: dict) -> str:
    accent = entry["color"]
    kind = ship_kind(entry)
    body = ship_portrait_body(kind, accent)
    return svg_wrap(entry["name"], accent, body, entry["slug"])


def ship_scene_svg(entry: dict) -> str:
    accent = entry["color"]
    kind = ship_kind(entry)
    name = xml_escape(entry["name"])
    ship_class = xml_escape(entry.get("role", "Starship")[:36])
    hull = ship_portrait_body(kind, accent)
    body = textwrap.dedent(
        f"""
          <rect x="0" y="0" width="512" height="512" fill="#020617" opacity="0.35"/>
          <ellipse cx="400" cy="120" rx="120" ry="40" fill="{accent}" opacity="0.12"/>
          <line stroke="#ef4444" stroke-width="3" opacity="0.65" x1="48" y1="180" x2="120" y2="160"/>
          <line stroke="#38bdf8" stroke-width="2" opacity="0.55" x1="420" y1="200" x2="480" y2="170"/>
          <circle cx="380" cy="280" r="3" fill="#fbbf24" opacity="0.8"/>
          <circle cx="140" cy="240" r="2" fill="#fbbf24" opacity="0.7"/>
          <g transform="translate(256 280) scale(0.92) translate(-256 -268)">
            {hull}
          </g>
          <text x="48" y="480" fill="{accent}" font-family="system-ui,sans-serif" font-size="20" font-weight="600">{name[:28]}</text>
          <text x="48" y="48" fill="#e2e8f0" font-family="system-ui,sans-serif" font-size="15" opacity="0.88">{ship_class}</text>
        """
    )
    return svg_wrap(f"{entry['name']} in combat", accent, body, f"{entry['slug']}-scene")


def ship_blueprint_svg(entry: dict) -> str:
    accent = entry["color"]
    kind = ship_kind(entry)
    name = xml_escape(entry["name"][:24])
    production = xml_escape(entry.get("production", "")[:28])
    sid = slug_id(entry["slug"], "-bp")
    grid = "\n".join(
        f'  <line stroke="{accent}" stroke-width="1" opacity="0.15" x1="{x}" y1="48" x2="{x}" y2="464"/>'
        for x in range(48, 465, 32)
    )
    grid += "\n" + "\n".join(
        f'  <line stroke="{accent}" stroke-width="1" opacity="0.15" x1="48" y1="{y}" x2="464" y2="{y}"/>'
        for y in range(48, 465, 32)
    )
    body = textwrap.dedent(
        f"""
          <rect fill="#0f172a" x="48" y="48" width="416" height="416" rx="16" opacity="0.92"/>
          {grid}
          <path class="outline" d="M96 320 L256 152 L416 320" fill="none" stroke-width="4"/>
          <line class="outline" x1="256" y1="152" x2="256" y2="392" stroke-width="3"/>
          <line class="outline" x1="152" y1="256" x2="360" y2="256" stroke-width="2" stroke-dasharray="8 6"/>
          <rect class="outline" x="214" y="188" width="84" height="52" fill="none"/>
          <line stroke="{accent}" x1="96" y1="320" x2="72" y2="336" stroke-width="2"/>
          <text x="68" y="342" fill="{accent}" font-family="monospace" font-size="12">BOW</text>
          <text x="72" y="96" fill="#f8fafc" font-family="monospace" font-size="18">{name}</text>
          <text x="72" y="430" fill="{accent}" font-family="monospace" font-size="14">{production}</text>
          <text x="72" y="452" fill="#94a3b8" font-family="monospace" font-size="12">{kind.upper()} CLASS</text>
        """
    )
    return svg_wrap(f"Blueprint — {entry['name']}", accent, body, f"{entry['slug']}-blueprint")


def species_body(kind: str, scene: bool, name: str, accent: str, classification: str) -> str:
    cx, cy = 256, 268
    bodies = {
        "humanoid": f"""
          {species_scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="102"/>
          <circle class="fill-skin" cx="{cx}" cy="{cy-58}" r="40"/>
          <path class="fill-dark" d="M{cx-40} {cy-78} Q{cx} {cy-98} {cx+40} {cy-78} Q{cx} {cy-62} {cx-40} {cy-78}"/>
          <circle fill="#fff" stroke="{OUTLINE}" stroke-width="2" cx="{cx-14}" cy="{cy-62}" r="7"/>
          <circle fill="#fff" stroke="{OUTLINE}" stroke-width="2" cx="{cx+14}" cy="{cy-62}" r="7"/>
          <circle fill="{OUTLINE}" cx="{cx-12}" cy="{cy-60}" r="3"/>
          <circle fill="{OUTLINE}" cx="{cx+16}" cy="{cy-60}" r="3"/>
          <rect class="fill-accent" x="{cx-44}" y="{cy-12}" width="88" height="112" rx="18"/>
          <rect class="fill-light" x="{cx-32}" y="{cy+2}" width="64" height="28" rx="6" opacity="0.85"/>
          <line class="outline" x1="{cx-44}" y1="{cy+22}" x2="{cx-72}" y2="{cy+72}"/>
          <line class="outline" x1="{cx+44}" y1="{cy+22}" x2="{cx+72}" y2="{cy+72}"/>
          <line class="outline" x1="{cx-18}" y1="{cy+100}" x2="{cx-28}" y2="{cy+152}"/>
          <line class="outline" x1="{cx+18}" y1="{cy+100}" x2="{cx+28}" y2="{cy+152}"/>
        """,
        "twilek": f"""
          {species_scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="100"/>
          <circle class="fill-skin" cx="{cx}" cy="{cy-56}" r="36"/>
          <path class="fill-accent" d="M{cx-36} {cy-56} Q{cx-92} {cy-8} {cx-76} {cy+42} Q{cx-54} {cy+8} {cx-36} {cy-18}"/>
          <path class="fill-accent" d="M{cx+36} {cy-56} Q{cx+92} {cy-8} {cx+76} {cy+42} Q{cx+54} {cy+8} {cx+36} {cy-18}"/>
          <rect class="fill-accent" x="{cx-40}" y="{cy-8}" width="80" height="108" rx="16"/>
        """,
        "togruta": f"""
          {species_scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="102"/>
          <circle class="fill-skin" cx="{cx}" cy="{cy-54}" r="36"/>
          <path class="fill-accent" d="M{cx-32} {cy-72} L{cx-98} {cy-22} L{cx-72} {cy+32} L{cx-34} {cy-8} Z"/>
          <path class="fill-accent" d="M{cx+32} {cy-72} L{cx+98} {cy-22} L{cx+72} {cy+32} L{cx+34} {cy-8} Z"/>
          <rect class="fill-accent" x="{cx-38}" y="{cy-6}" width="76" height="102" rx="14"/>
        """,
        "wookiee": f"""
          {species_scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="108"/>
          <ellipse class="fill-accent" cx="{cx}" cy="{cy-44}" rx="52" ry="46"/>
          <path class="fill-light" d="M{cx-50} {cy-54} L{cx-68} {cy-86} L{cx-34} {cy-70} Z"/>
          <path class="fill-light" d="M{cx+50} {cy-54} L{cx+68} {cy-86} L{cx+34} {cy-70} Z"/>
          <circle fill="#fff" cx="{cx-18}" cy="{cy-48}" r="8"/>
          <circle fill="#fff" cx="{cx+18}" cy="{cy-48}" r="8"/>
          <rect class="fill-accent" x="{cx-52}" y="{cy+2}" width="104" height="98" rx="22"/>
          <line class="outline" x1="{cx-52}" y1="{cy+32}" x2="{cx-88}" y2="{cy+62}"/>
        """,
        "insectoid": f"""
          {species_scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="96"/>
          <ellipse class="fill-accent" cx="{cx}" cy="{cy-40}" rx="58" ry="42"/>
          <circle class="fill-light" cx="{cx-24}" cy="{cy-44}" r="15"/>
          <circle class="fill-light" cx="{cx+24}" cy="{cy-44}" r="15"/>
          <path class="fill-accent" d="M{cx-42} {cy+2} L{cx-78} {cy+62} L{cx-58} {cy+82} L{cx-26} {cy+32} Z"/>
          <path class="fill-accent" d="M{cx+42} {cy+2} L{cx+78} {cy+62} L{cx+58} {cy+82} L{cx+26} {cy+32} Z"/>
          <rect class="fill-mid" x="{cx-32}" y="{cy-2}" width="64" height="72" rx="10"/>
        """,
        "amphibian": f"""
          {species_scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="98"/>
          <ellipse class="fill-skin" cx="{cx}" cy="{cy-50}" rx="42" ry="38"/>
          <ellipse class="fill-accent" cx="{cx-20}" cy="{cy-58}" rx="13" ry="17"/>
          <ellipse class="fill-accent" cx="{cx+20}" cy="{cy-58}" rx="13" ry="17"/>
          <path class="fill-accent" d="M{cx-38} {cy-8} Q{cx} {cy+32} {cx+38} {cy-8} L{cx+32} {cy+82} Q{cx} {cy+112} {cx-32} {cy+82} Z"/>
        """,
        "reptilian": f"""
          {species_scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="96"/>
          <ellipse class="fill-accent" cx="{cx}" cy="{cy-48}" rx="44" ry="40"/>
          <path class="fill-light" d="M{cx-44} {cy-55} L{cx-62} {cy-25} L{cx-36} {cy-30} Z"/>
          <path class="fill-light" d="M{cx+44} {cy-55} L{cx+62} {cy-25} L{cx+36} {cy-30} Z"/>
          <rect class="fill-accent" x="{cx-42}" y="{cy+6}" width="84" height="98" rx="14"/>
        """,
        "cephalopod": f"""
          {species_scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy-18}" r="94"/>
          <ellipse class="fill-accent" cx="{cx}" cy="{cy-28}" rx="52" ry="58"/>
          <path class="outline" d="M{cx-42} {cy+18} Q{cx-58} {cy+78} {cx-38} {cy+128}" stroke="{accent}" stroke-width="7"/>
          <path class="outline" d="M{cx-14} {cy+22} Q{cx-8} {cy+88} {cx-4} {cy+138}" stroke="{accent}" stroke-width="7"/>
          <path class="outline" d="M{cx+14} {cy+22} Q{cx+8} {cy+88} {cx+4} {cy+138}" stroke="{accent}" stroke-width="7"/>
          <path class="outline" d="M{cx+42} {cy+18} Q{cx+58} {cy+78} {cx+38} {cy+128}" stroke="{accent}" stroke-width="7"/>
        """,
        "hutt": f"""
          {species_scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy+12}" r="108"/>
          <ellipse class="fill-accent" cx="{cx}" cy="{cy+22}" rx="98" ry="72"/>
          <ellipse class="fill-light" cx="{cx}" cy="{cy-28}" rx="48" ry="42"/>
          <circle class="fill-dark" cx="{cx-16}" cy="{cy-32}" r="8"/>
          <circle class="fill-dark" cx="{cx+16}" cy="{cy-32}" r="8"/>
        """,
        "small": f"""
          {species_scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy+18}" r="78"/>
          <circle class="fill-light" cx="{cx}" cy="{cy-28}" r="30"/>
          <rect class="fill-accent" x="{cx-28}" y="{cy+2}" width="56" height="58" rx="12"/>
        """,
        "feline": f"""
          {species_scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="96"/>
          <circle class="fill-skin" cx="{cx}" cy="{cy-50}" r="36"/>
          <path class="fill-accent" d="M{cx-32} {cy-78} L{cx-42} {cy-48} L{cx-16} {cy-58} Z"/>
          <path class="fill-accent" d="M{cx+32} {cy-78} L{cx+42} {cy-48} L{cx+16} {cy-58} Z"/>
          <rect class="fill-accent" x="{cx-38}" y="{cy-2}" width="76" height="98" rx="16"/>
        """,
        "horned": f"""
          {species_scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="96"/>
          <circle class="fill-skin" cx="{cx}" cy="{cy-50}" r="36"/>
          <path class="fill-accent" d="M{cx-24} {cy-88} L{cx-32} {cy-58} L{cx-8} {cy-66} Z"/>
          <path class="fill-accent" d="M{cx+24} {cy-88} L{cx+32} {cy-58} L{cx+8} {cy-66} Z"/>
          <rect class="fill-accent" x="{cx-36}" y="{cy-2}" width="72" height="98" rx="14"/>
        """,
    }
    # Fallback merge: import extended kinds from inline minimal set
    for fallback_kind, template in {
        "masked": f'<circle class="glow" cx="{cx}" cy="{cy}" r="98"/><circle class="fill-skin" cx="{cx}" cy="{cy-50}" r="36"/><rect class="fill-accent" x="{cx-56}" y="{cy-66}" width="112" height="38" rx="8"/><rect class="fill-accent" x="{cx-40}" y="{cy-8}" width="80" height="100" rx="14"/>',
        "energy": f'<circle class="glow" cx="{cx}" cy="{cy}" r="104"/><path class="fill-accent" d="M{cx} {cy-88} Q{cx+62} {cy-18} {cx+42} {cy+52} Q{cx} {cy+102} {cx-42} {cy+52} Q{cx-62} {cy-18} {cx} {cy-88} Z" opacity="0.85"/><circle class="fill-light" cx="{cx}" cy="{cy}" r="32"/>',
        "mollusk": f'<circle class="glow" cx="{cx}" cy="{cy}" r="98"/><ellipse class="fill-accent" cx="{cx}" cy="{cy-18}" rx="62" ry="48"/><path class="fill-mid" d="M{cx-58} {cy+12} Q{cx} {cy+102} {cx+58} {cy+12} L{cx+42} {cy+62} Q{cx} {cy+82} {cx-42} {cy+62} Z"/>',
        "avian": f'<circle class="glow" cx="{cx}" cy="{cy}" r="92"/><ellipse class="fill-light" cx="{cx}" cy="{cy-40}" rx="32" ry="30"/><path class="fill-accent" d="M{cx-32} {cy-18} L{cx-102} {cy+12} L{cx-40} {cy+22} Z"/><path class="fill-accent" d="M{cx+32} {cy-18} L{cx+102} {cy+12} L{cx+40} {cy+22} Z"/>',
        "tall": f'<circle class="glow" cx="{cx}" cy="{cy-8}" r="98"/><ellipse class="fill-skin" cx="{cx}" cy="{cy-72}" rx="34" ry="38"/><rect class="fill-accent" x="{cx-32}" y="{cy-28}" width="64" height="132" rx="14"/>',
        "multi": f'<circle class="glow" cx="{cx}" cy="{cy}" r="98"/><circle class="fill-skin" cx="{cx}" cy="{cy-52}" r="34"/><rect class="fill-accent" x="{cx-36}" y="{cy-8}" width="72" height="92" rx="14"/>',
        "serpentine": f'<circle class="glow" cx="{cx}" cy="{cy+8}" r="98"/><ellipse class="fill-skin" cx="{cx}" cy="{cy-62}" rx="40" ry="36"/><path class="fill-accent" d="M{cx-32} {cy-28} Q{cx-52} {cy+42} {cx-42} {cy+122} Q{cx} {cy+152} {cx+42} {cy+122} Q{cx+52} {cy+42} {cx+32} {cy-28}"/>',
        "tall_neck": f'<circle class="glow" cx="{cx}" cy="{cy-18}" r="98"/><rect class="fill-skin" x="{cx-14}" y="{cy-98}" width="28" height="58" rx="8"/><circle class="fill-skin" cx="{cx}" cy="{cy-118}" r="32"/><rect class="fill-accent" x="{cx-34}" y="{cy-32}" width="68" height="88" rx="14"/>',
    }.items():
        if fallback_kind not in bodies:
            bodies[fallback_kind] = species_scene_backdrop(accent, scene) + template

    body = bodies.get(kind, bodies["humanoid"])
    if scene:
        body += scene_labels(name, classification, accent)
    return body


def droid_body(kind: str, scene: bool, name: str, accent: str, dtype: str) -> str:
    cx, cy = 256, 268
    panel = f'<rect class="fill-panel" x="{cx-18}" y="{cy+18}" width="36" height="14" rx="3"/>'
    leds = f"""
          <circle cx="{cx-24}" cy="{cy-48}" r="4" fill="#22c55e"/>
          <circle cx="{cx+24}" cy="{cy-48}" r="4" fill="#ef4444"/>
        """
    bodies = {
        "astromech": f"""
          {droid_scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="98"/>
          <rect class="fill-accent" x="{cx-58}" y="{cy-18}" width="116" height="98" rx="18"/>
          <circle class="fill-light" cx="{cx}" cy="{cy-58}" r="44"/>
          <circle class="fill-dark" cx="{cx-14}" cy="{cy-60}" r="9"/>
          <circle class="fill-dark" cx="{cx+14}" cy="{cy-60}" r="9"/>
          <rect class="fill-metal" x="{cx-22}" y="{cy+42}" width="44" height="30" rx="6"/>
          {panel}
        """,
        "protocol": f"""
          {droid_scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="98"/>
          <rect class="fill-light" x="{cx-40}" y="{cy-72}" width="80" height="58" rx="14"/>
          <rect class="fill-accent" x="{cx-44}" y="{cy-2}" width="88" height="108" rx="16"/>
          {leds}
          <rect class="fill-metal" x="{cx-8}" y="{cy-52}" width="16" height="10" rx="2"/>
        """,
        "battle": f"""
          {droid_scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="96"/>
          <rect class="fill-accent" x="{cx-34}" y="{cy-62}" width="68" height="52" rx="10"/>
          <rect class="fill-light" x="{cx-30}" y="{cy+2}" width="60" height="88" rx="8"/>
          <line class="outline" x1="{cx-30}" y1="{cy+22}" x2="{cx-62}" y2="{cy+48}"/>
          <line class="outline" x1="{cx+30}" y1="{cy+22}" x2="{cx+62}" y2="{cy+48}"/>
          <rect class="fill-dark" x="{cx-58}" y="{cy+8}" width="22" height="12" rx="3"/>
        """,
        "super_battle": f"""
          {droid_scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="100"/>
          <rect class="fill-accent" x="{cx-48}" y="{cy-58}" width="96" height="58" rx="12"/>
          <rect class="fill-light" x="{cx-40}" y="{cy+2}" width="80" height="98" rx="10"/>
          <rect class="fill-dark" x="{cx-58}" y="{cy+18}" width="30" height="18" rx="4"/>
          <rect class="fill-dark" x="{cx+28}" y="{cy+18}" width="30" height="18" rx="4"/>
        """,
        "droideka": f"""
          {droid_scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="98"/>
          <circle class="fill-accent" cx="{cx}" cy="{cy-8}" r="58"/>
          <circle class="fill-light" cx="{cx}" cy="{cy-8}" r="30" opacity="0.85"/>
          <line class="outline" x1="{cx-58}" y1="{cy+28}" x2="{cx-88}" y2="{cy+72}"/>
          <line class="outline" x1="{cx+58}" y1="{cy+28}" x2="{cx+88}" y2="{cy+72}"/>
        """,
        "assassin": f"""
          {droid_scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="98"/>
          <rect class="fill-metal" x="{cx-30}" y="{cy-88}" width="60" height="44" rx="8"/>
          <rect class="fill-light" x="{cx-34}" y="{cy-32}" width="68" height="114" rx="12"/>
          {leds}
          <rect class="fill-dark" x="{cx-48}" y="{cy+8}" width="26" height="52" rx="6"/>
          <rect class="fill-dark" x="{cx+22}" y="{cy+8}" width="26" height="52" rx="6"/>
        """,
        "gonk": f"""
          {droid_scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="84"/>
          <rect class="fill-accent" x="{cx-42}" y="{cy-42}" width="84" height="94" rx="10"/>
          <rect class="fill-light" x="{cx-32}" y="{cy-28}" width="64" height="28" rx="4"/>
          <text x="{cx}" y="{cy+8}" text-anchor="middle" fill="{accent}" font-family="monospace" font-size="14">GONK</text>
          <line class="outline" x1="{cx-22}" y1="{cy+52}" x2="{cx-22}" y2="{cy+88}"/>
          <line class="outline" x1="{cx+22}" y1="{cy+52}" x2="{cx+22}" y2="{cy+88}"/>
        """,
        "medical": f"""
          {droid_scene_backdrop(accent, scene)}
          <circle class="glow" cx="{cx}" cy="{cy}" r="96"/>
          <rect class="fill-light" x="{cx-36}" y="{cy-72}" width="72" height="48" rx="12"/>
          <rect class="fill-accent" x="{cx-32}" y="{cy-12}" width="64" height="104" rx="14"/>
          <path class="fill-dark" d="M{cx} {cy-58} L{cx+14} {cy-36} L{cx} {cy-26} L{cx-14} {cy-36} Z"/>
        """,
    }
    for fallback_kind, template in {
        "magnaguard": f'<circle class="glow" cx="{cx}" cy="{cy}" r="96"/><rect class="fill-accent" x="{cx-36}" y="{cy-76}" width="72" height="52" rx="8"/><rect class="fill-light" x="{cx-32}" y="{cy-12}" width="64" height="98" rx="10"/>',
        "probe": f'<circle class="glow" cx="{cx}" cy="{cy-18}" r="92"/><circle class="fill-accent" cx="{cx}" cy="{cy-28}" r="48"/><line class="outline" x1="{cx}" y1="{cy+18}" x2="{cx}" y2="{cy+92}"/>',
        "mouse": f'<circle class="glow" cx="{cx}" cy="{cy+10}" r="78"/><rect class="fill-accent" x="{cx-36}" y="{cy-14}" width="72" height="48" rx="8"/>',
        "tactical": f'<circle class="glow" cx="{cx}" cy="{cy}" r="94"/><ellipse class="fill-accent" cx="{cx}" cy="{cy-56}" rx="40" ry="46"/><rect class="fill-light" x="{cx-32}" y="{cy-2}" width="64" height="96" rx="10"/>',
        "labor": f'<circle class="glow" cx="{cx}" cy="{cy}" r="90"/><rect class="fill-accent" x="{cx-40}" y="{cy-52}" width="80" height="58" rx="10"/><rect class="fill-light" x="{cx-34}" y="{cy+4}" width="68" height="92" rx="8"/>',
        "pit": f'<circle class="glow" cx="{cx}" cy="{cy+6}" r="80"/><rect class="fill-accent" x="{cx-32}" y="{cy-28}" width="64" height="58" rx="8"/>',
        "interrogator": f'<circle class="glow" cx="{cx}" cy="{cy-8}" r="92"/><circle class="fill-accent" cx="{cx}" cy="{cy-26}" r="42"/><line class="outline" x1="{cx-16}" y1="{cy+14}" x2="{cx-16}" y2="{cy+82}"/>',
        "gatekeeper": f'<rect class="fill-dark" x="{cx-82}" y="{cy-82}" width="164" height="124" rx="8"/><rect class="fill-accent" x="{cx-26}" y="{cy-62}" width="52" height="38" rx="6"/>',
        "dark_trooper": f'<circle class="glow" cx="{cx}" cy="{cy}" r="100"/><rect class="fill-accent" x="{cx-42}" y="{cy-78}" width="84" height="58" rx="10"/><rect class="fill-light" x="{cx-36}" y="{cy-8}" width="72" height="104" rx="12"/>',
        "bd": f'<circle class="glow" cx="{cx}" cy="{cy}" r="88"/><circle class="fill-accent" cx="{cx}" cy="{cy-8}" r="40"/><rect class="fill-light" x="{cx-24}" y="{cy+28}" width="48" height="58" rx="10"/>',
        "artillery": f'<circle class="glow" cx="{cx}" cy="{cy}" r="94"/><rect class="fill-accent" x="{cx-52}" y="{cy-28}" width="104" height="48" rx="8"/><rect class="fill-dark" x="{cx-12}" y="{cy-58}" width="24" height="32" rx="4"/>',
        "biped": f'<circle class="glow" cx="{cx}" cy="{cy}" r="92"/><circle class="fill-light" cx="{cx}" cy="{cy-62}" r="34"/><rect class="fill-accent" x="{cx-32}" y="{cy-18}" width="64" height="98" rx="12"/>',
        "droid_starfighter": f'<circle class="glow" cx="{cx}" cy="{cy}" r="92"/><path class="fill-accent" d="M{cx-82} {cy+18} L{cx} {cy-72} L{cx+82} {cy+18} L{cx+42} {cy+38} L{cx-42} {cy+38} Z"/>',
        "security": f'<circle class="glow" cx="{cx}" cy="{cy-4}" r="96"/><rect class="fill-accent" x="{cx-36}" y="{cy-82}" width="72" height="50" rx="8"/><rect class="fill-light" x="{cx-34}" y="{cy-22}" width="68" height="108" rx="10"/>',
    }.items():
        if fallback_kind not in bodies:
            bodies[fallback_kind] = droid_scene_backdrop(accent, scene) + template

    body = bodies.get(kind, bodies.get("biped", bodies["astromech"]))
    if scene:
        body += scene_labels(name, dtype, accent)
    return body
