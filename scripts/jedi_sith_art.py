#!/usr/bin/env python3
"""Rich SVG artwork for Jedi and Sith directory entries."""

from __future__ import annotations

import re
import textwrap

OUTLINE = "#1a1a2e"

SLUG_ARCHETYPE: dict[str, str] = {
    "yoda": "small_green",
    "yaddle": "small_green",
    "grogu": "small_green",
    "aayla-secura": "twilek",
    "tiplee": "twilek",
    "tiplar": "twilek",
    "kit-fisto": "alien_fish",
    "plo-koon": "masked_jedi",
    "nahdar-vebb": "alien_fish",
    "gungi": "wookiee",
    "katooni": "small_green",
    "petro": "small_green",
    "darth-vader": "masked_sith",
    "darth-malak": "masked_sith",
    "darth-nihilus": "void_sith",
    "darth-sion": "scarred_sith",
    "darth-sidious": "hooded_sith",
    "darth-vitiate": "hooded_sith",
    "darth-plagueis": "hooded_sith",
    "darth-maul": "horned",
    "savage-opress": "horned",
    "darth-revan": "masked_sith",
    "darth-traya": "hooded_sith",
    "asajj-ventress": "zabrak",
    "grand-inquisitor": "inquisitor",
    "second-sister": "inquisitor",
    "fifth-brother": "inquisitor",
    "sixth-brother": "inquisitor",
    "seventh-sister": "inquisitor",
    "eighth-brother": "inquisitor",
    "ninth-sister": "inquisitor",
    "bastila-shan": "jedi_master",
    "jolee-bindo": "jedi_master",
    "meetra-surik": "jedi_master",
    "revan": "masked_jedi",
    "satele-shan": "jedi_master",
    "mace-windu": "jedi_master",
    "shaak-ti": "togruta",
    "ahsoka-tano": "togruta",
}


def xml_escape(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )


def slug_id(slug: str, suffix: str = "") -> str:
    sid = re.sub(r"[^a-z0-9]", "", slug) or "force"
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


def svg_wrap(title: str, accent: str, body: str, slug: str, *, extra_style: str = "", blade: str = "blue") -> str:
    sid = slug_id(slug)
    safe_title = xml_escape(title)
    blade_glow = "#38bdf8" if blade == "blue" else "#ef4444"
    style = textwrap.dedent(
        f"""
        <style>
          .bg {{ fill: url(#bgGrad-{sid}); }}
          .outline {{ fill: none; stroke: {OUTLINE}; stroke-width: 3; stroke-linecap: round; stroke-linejoin: round; }}
          .fill-accent {{ fill: {accent}; stroke: {OUTLINE}; stroke-width: 3; }}
          .fill-dark {{ fill: #1a1a2e; stroke: {OUTLINE}; stroke-width: 3; }}
          .fill-light {{ fill: #f8fafc; stroke: {OUTLINE}; stroke-width: 3; }}
          .fill-mid {{ fill: #94a3b8; stroke: {OUTLINE}; stroke-width: 3; }}
          .fill-red {{ fill: #dc2626; stroke: {OUTLINE}; stroke-width: 3; }}
          .fill-skin {{ fill: #f4c99b; stroke: {OUTLINE}; stroke-width: 3; }}
          .fill-robe {{ fill: {accent}; stroke: {OUTLINE}; stroke-width: 3; }}
          .fill-inner {{ fill: #e2e8f0; stroke: {OUTLINE}; stroke-width: 2; }}
          .fill-sith {{ fill: #111827; stroke: #7f1d1d; stroke-width: 3; }}
          .fill-metal {{ fill: #b8c4d0; stroke: {OUTLINE}; stroke-width: 3; }}
          .fill-green {{ fill: #7ec850; stroke: {OUTLINE}; stroke-width: 3; }}
          .stroke-red {{ fill: none; stroke: #ef4444; stroke-width: 4; stroke-linecap: round; }}
          .stroke-blue {{ fill: none; stroke: {blade_glow}; stroke-width: 5; stroke-linecap: round; filter: url(#softGlow-{sid}); }}
          .glow {{ fill: url(#glowGrad-{sid}); filter: url(#softGlow-{sid}); }}
          {extra_style}
        </style>
        """
    )
    return textwrap.dedent(
        f"""\
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" role="img" aria-label="{safe_title}">
          <defs>
            <linearGradient id="bgGrad-{sid}" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="{accent}" stop-opacity="0.58"/>
              <stop offset="100%" stop-color="#050814" stop-opacity="0.96"/>
            </linearGradient>
            <radialGradient id="glowGrad-{sid}" cx="50%" cy="45%" r="50%">
              <stop offset="0%" stop-color="{blade_glow}" stop-opacity="0.55"/>
              <stop offset="100%" stop-color="{blade_glow}" stop-opacity="0"/>
            </radialGradient>
            <filter id="softGlow-{sid}" x="-50%" y="-50%" width="200%" height="200%">
              <feGaussianBlur stdDeviation="6" result="blur"/>
              <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
            </filter>
          </defs>
          {style}
          <rect class="bg" width="512" height="512" rx="24"/>
          {starfield()}
          {body}
        </svg>
        """
    )


def lightsaber(accent: str, cx: int, cy: int, angle: int, blade: str = "blue") -> str:
    color = "#38bdf8" if blade == "blue" else "#ef4444"
    core = "#ffffff" if blade == "blue" else "#fecaca"
    return f"""
          <g transform="rotate({angle} {cx} {cy})">
            <rect fill="#64748b" stroke="{OUTLINE}" stroke-width="2" x="{cx-8}" y="{cy}" width="16" height="48" rx="4"/>
            <rect fill="{accent}" x="{cx-5}" y="{cy+8}" width="10" height="8" rx="2"/>
            <rect fill="{core}" x="{cx-3}" y="{cy-72}" width="6" height="74" rx="3" opacity="0.95"/>
            <rect fill="{color}" x="{cx-5}" y="{cy-78}" width="10" height="80" rx="4" opacity="0.85"/>
          </g>
        """


def archetype(entry: dict, folder: str) -> str:
    slug = entry["slug"]
    if slug in SLUG_ARCHETYPE:
        return SLUG_ARCHETYPE[slug]
    blob = f"{entry['name']} {entry.get('role', '')} {entry.get('desc', '')}".lower()
    if folder == "sith" or "sith" in entry.get("role", "").lower() or "inquisitor" in blob:
        if "zabrak" in blob or "ventress" in blob:
            return "zabrak"
        if "hood" in blob or "emperor" in blob or "palpatine" in blob:
            return "hooded_sith"
        if "nihilus" in blob:
            return "void_sith"
        if "sion" in blob:
            return "scarred_sith"
        if "mask" in blob or "vader" in blob or "malak" in blob or "revan" in blob:
            return "masked_sith"
        if "maul" in blob or "opress" in blob:
            return "horned"
        if "inquisitor" in blob or "brother" in blob or "sister" in blob:
            return "inquisitor"
        return "sith"
    if "twi'lek" in blob or "twilek" in blob or "secura" in blob:
        return "twilek"
    if "togruta" in blob or "shaak" in blob or "ahsoka" in blob:
        return "togruta"
    if "nautolan" in blob or "fisto" in blob:
        return "alien_fish"
    if "kel dor" in blob or "plo koon" in blob:
        return "masked_jedi"
    if any(k in blob for k in ("yoda", "grogu", "yaddle")):
        return "small_green"
    if "wookiee" in blob or "gungi" in blob:
        return "wookiee"
    if "windu" in blob:
        return "jedi_master"
    if folder == "jedi" or "jedi" in entry.get("role", "").lower():
        return "jedi"
    return "jedi"


def portrait_body(kind: str, accent: str, blade: str = "blue") -> str:
    cx, cy = 256, 268
    saber = lightsaber(accent, 368, 300, -18, blade)
    bodies = {
        "jedi": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="108"/>
          <path class="fill-robe" d="M118 430 Q256 290 394 430 L372 512 H140 Z"/>
          <path class="fill-inner" d="M152 420 Q256 330 360 420 L344 512 H168 Z" opacity="0.85"/>
          <ellipse class="fill-skin" cx="{cx}" cy="{cy-58}" rx="76" ry="86"/>
          <path class="fill-dark" d="M186 228 Q256 168 326 228 Q308 198 256 188 Q204 198 186 228"/>
          <circle fill="#fff" stroke="{OUTLINE}" stroke-width="2" cx="{cx-28}" cy="{cy-62}" r="13"/>
          <circle fill="#fff" stroke="{OUTLINE}" stroke-width="2" cx="{cx+28}" cy="{cy-62}" r="13"/>
          <circle fill="{OUTLINE}" cx="{cx-24}" cy="{cy-60}" r="5"/>
          <circle fill="{OUTLINE}" cx="{cx+32}" cy="{cy-60}" r="5"/>
          <rect class="fill-metal" x="{cx-42}" y="{cy+8}" width="84" height="14" rx="4"/>
          <rect class="fill-accent" x="{cx-12}" y="{cy+8}" width="24" height="14" rx="3"/>
          {saber}
        """,
        "jedi_master": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="110"/>
          <path class="fill-robe" d="M110 432 Q256 280 402 432 L378 512 H134 Z"/>
          <path fill="#4c1d95" stroke="{OUTLINE}" stroke-width="3" d="M138 418 Q256 318 374 418 L358 512 H154 Z" opacity="0.9"/>
          <ellipse class="fill-skin" cx="{cx}" cy="{cy-56}" rx="78" ry="88"/>
          <path class="fill-dark" d="M184 220 Q256 155 328 220 Q310 188 256 178 Q202 188 184 220"/>
          <circle fill="#fff" stroke="{OUTLINE}" stroke-width="2" cx="{cx-28}" cy="{cy-60}" r="13"/>
          <circle fill="#fff" stroke="{OUTLINE}" stroke-width="2" cx="{cx+28}" cy="{cy-60}" r="13"/>
          <circle fill="{OUTLINE}" cx="{cx-24}" cy="{cy-58}" r="5"/>
          <circle fill="{OUTLINE}" cx="{cx+32}" cy="{cy-58}" r="5"/>
          <rect class="fill-metal" x="{cx-44}" y="{cy+10}" width="88" height="16" rx="4"/>
          {lightsaber("#7c3aed", 372, 298, -16, blade)}
        """,
        "small_green": f"""
          <circle class="glow" cx="{cx}" cy="{cy+8}" r="98"/>
          <path class="fill-robe" d="M156 400 Q256 320 356 400 L342 512 H170 Z"/>
          <ellipse class="fill-green" cx="{cx}" cy="{cy-18}" rx="72" ry="68"/>
          <ellipse class="fill-green" cx="{cx}" cy="{cy+48}" rx="68" ry="78"/>
          <circle fill="#fff" stroke="{OUTLINE}" stroke-width="2" cx="{cx-22}" cy="{cy-22}" r="14"/>
          <circle fill="#fff" stroke="{OUTLINE}" stroke-width="2" cx="{cx+22}" cy="{cy-22}" r="14"/>
          <circle fill="{OUTLINE}" cx="{cx-18}" cy="{cy-20}" r="6"/>
          <circle fill="{OUTLINE}" cx="{cx+26}" cy="{cy-20}" r="6"/>
          {lightsaber(accent, 350, 310, -22, blade)}
        """,
        "twilek": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="104"/>
          <path class="fill-robe" d="M124 428 Q256 300 388 428 L368 512 H144 Z"/>
          <ellipse class="fill-skin" cx="{cx}" cy="{cy-54}" rx="72" ry="82"/>
          <path class="fill-accent" d="M{cx-34} {cy-54} Q{cx-98} {cy+8} {cx-78} {cy+58} Q{cx-52} {cy+18} {cx-34} {cy-18}"/>
          <path class="fill-accent" d="M{cx+34} {cy-54} Q{cx+98} {cy+8} {cx+78} {cy+58} Q{cx+52} {cy+18} {cx+34} {cy-18}"/>
          <circle fill="#fff" stroke="{OUTLINE}" stroke-width="2" cx="{cx-24}" cy="{cy-58}" r="12"/>
          <circle fill="#fff" stroke="{OUTLINE}" stroke-width="2" cx="{cx+24}" cy="{cy-58}" r="12"/>
          {saber}
        """,
        "togruta": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="106"/>
          <path class="fill-robe" d="M120 430 Q256 292 392 430 L372 512 H140 Z"/>
          <ellipse class="fill-skin" cx="{cx}" cy="{cy-52}" rx="74" ry="84"/>
          <path class="fill-accent" d="M{cx-36} {cy-70} L{cx-88} {cy-40} L{cx-72} {cy-10} Z"/>
          <path class="fill-accent" d="M{cx+36} {cy-70} L{cx+88} {cy-40} L{cx+72} {cy-10} Z"/>
          <circle fill="#fff" stroke="{OUTLINE}" stroke-width="2" cx="{cx-26}" cy="{cy-56}" r="12"/>
          <circle fill="#fff" stroke="{OUTLINE}" stroke-width="2" cx="{cx+26}" cy="{cy-56}" r="12"/>
          {saber}
        """,
        "alien_fish": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="104"/>
          <path class="fill-robe" d="M124 428 Q256 300 388 428 L368 512 H144 Z"/>
          <ellipse class="fill-accent" cx="{cx}" cy="{cy-48}" rx="82" ry="88"/>
          <circle fill="#fff" stroke="{OUTLINE}" stroke-width="2" cx="{cx}" cy="{cy-52}" r="24"/>
          <circle fill="{OUTLINE}" cx="{cx+4}" cy="{cy-50}" r="10"/>
          {saber}
        """,
        "masked_jedi": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="106"/>
          <path class="fill-robe" d="M118 430 Q256 290 394 430 L372 512 H140 Z"/>
          <rect class="fill-metal" x="{cx-52}" y="{cy-88}" width="104" height="88" rx="22"/>
          <rect class="fill-dark" x="{cx-38}" y="{cy-68}" width="76" height="22" rx="8"/>
          <rect class="fill-accent" x="{cx-44}" y="{cy+8}" width="88" height="72" rx="14"/>
          {saber}
        """,
        "wookiee": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="112"/>
          <path class="fill-robe" d="M108 432 Q256 300 404 432 L382 512 H130 Z"/>
          <ellipse fill="#6b4423" stroke="{OUTLINE}" stroke-width="3" cx="{cx}" cy="{cy-38}" rx="88" ry="82"/>
          <circle fill="#fff" stroke="{OUTLINE}" stroke-width="2" cx="{cx-28}" cy="{cy-44}" r="14"/>
          <circle fill="#fff" stroke="{OUTLINE}" stroke-width="2" cx="{cx+28}" cy="{cy-44}" r="14"/>
          {saber}
        """,
        "sith": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="108"/>
          <path class="fill-sith" d="M132 430 Q256 288 380 430 L358 512 H154 Z"/>
          <path fill="#7f1d1d" stroke="{OUTLINE}" stroke-width="2" d="M156 418 Q256 322 356 418 L340 512 H172 Z" opacity="0.85"/>
          <ellipse class="fill-skin" cx="{cx}" cy="{cy-56}" rx="76" ry="86"/>
          <circle fill="#fef08a" stroke="{OUTLINE}" stroke-width="2" cx="{cx-26}" cy="{cy-60}" r="12"/>
          <circle fill="#fef08a" stroke="{OUTLINE}" stroke-width="2" cx="{cx+26}" cy="{cy-60}" r="12"/>
          <circle fill="#dc2626" cx="{cx-22}" cy="{cy-58}" r="4"/>
          <circle fill="#dc2626" cx="{cx+30}" cy="{cy-58}" r="4"/>
          {lightsaber(accent, 370, 298, -16, "red")}
        """,
        "hooded_sith": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="112"/>
          <path class="fill-sith" d="M96 438 Q256 98 416 438 L392 512 H120 Z"/>
          <ellipse class="fill-skin" cx="{cx}" cy="{cy-42}" rx="64" ry="72"/>
          <circle fill="#fef08a" stroke="{OUTLINE}" stroke-width="2" cx="{cx-22}" cy="{cy-46}" r="10"/>
          <circle fill="#fef08a" stroke="{OUTLINE}" stroke-width="2" cx="{cx+22}" cy="{cy-46}" r="10"/>
          <circle fill="#dc2626" cx="{cx-18}" cy="{cy-44}" r="3"/>
          <circle fill="#dc2626" cx="{cx+26}" cy="{cy-44}" r="3"/>
          <path class="stroke-red" d="M{cx-40} {cy+20} Q{cx} {cy+48} {cx+40} {cy+20}"/>
          {lightsaber(accent, 372, 300, -14, "red")}
        """,
        "masked_sith": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="110"/>
          <path class="fill-sith" d="M128 432 Q256 180 384 432 L362 512 H150 Z"/>
          <rect class="fill-dark" x="{cx-58}" y="{cy-72}" width="116" height="98" rx="24"/>
          <rect class="fill-metal" x="{cx-42}" y="{cy-52}" width="84" height="24" rx="8"/>
          <circle fill="#ef4444" cx="{cx-20}" cy="{cy-8}" r="9"/>
          <circle fill="#ef4444" cx="{cx+20}" cy="{cy-8}" r="9"/>
          <rect class="fill-metal" x="{cx-28}" y="{cy+18}" width="56" height="38" rx="10"/>
          {lightsaber(accent, 374, 296, -12, "red")}
        """,
        "void_sith": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="114"/>
          <path class="fill-sith" d="M108 434 Q256 160 404 434 L382 512 H130 Z"/>
          <ellipse fill="#0f172a" stroke="#ef4444" stroke-width="4" cx="{cx}" cy="{cy-48}" rx="78" ry="84"/>
          <circle fill="#111" cx="{cx-22}" cy="{cy-52}" r="16"/>
          <circle fill="#111" cx="{cx+22}" cy="{cy-52}" r="16"/>
          <circle fill="#ef4444" cx="{cx-22}" cy="{cy-52}" r="6"/>
          <circle fill="#ef4444" cx="{cx+22}" cy="{cy-52}" r="6"/>
          {lightsaber("#111", 372, 298, -14, "red")}
        """,
        "scarred_sith": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="108"/>
          <path class="fill-sith" d="M124 432 Q256 280 388 432 L368 512 H144 Z"/>
          <ellipse class="fill-skin" cx="{cx}" cy="{cy-52}" rx="78" ry="88"/>
          <path fill="none" stroke="#ef4444" stroke-width="4" d="M{cx-40} {cy-78} L{cx+10} {cy-28}"/>
          <path fill="none" stroke="#ef4444" stroke-width="3" d="M{cx+30} {cy-72} L{cx-8} {cy-34}"/>
          <circle fill="#fef08a" cx="{cx-24}" cy="{cy-56}" r="10"/>
          <circle fill="#111" cx="{cx+24}" cy="{cy-56}" r="10"/>
          {lightsaber(accent, 370, 300, -16, "red")}
        """,
        "horned": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="110"/>
          <path fill="#7f1d1d" stroke="{OUTLINE}" stroke-width="3" d="M{cx-28} {cy-98} L{cx-38} {cy-58} L{cx-12} {cy-68} Z"/>
          <path fill="#7f1d1d" stroke="{OUTLINE}" stroke-width="3" d="M{cx+28} {cy-98} L{cx+38} {cy-58} L{cx+12} {cy-68} Z"/>
          <path class="fill-sith" d="M132 430 Q256 288 380 430 L358 512 H154 Z"/>
          <ellipse class="fill-skin" cx="{cx}" cy="{cy-50}" rx="80" ry="90"/>
          <path fill="#8b0000" d="M172 228 Q256 148 340 228"/>
          <circle fill="#fef08a" cx="{cx-24}" cy="{cy-54}" r="12"/>
          <circle fill="#fef08a" cx="{cx+24}" cy="{cy-54}" r="12"/>
          {lightsaber(accent, 372, 298, -14, "red")}
        """,
        "zabrak": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="108"/>
          <path fill="#7f1d1d" stroke="{OUTLINE}" stroke-width="3" d="M{cx-24} {cy-92} L{cx-32} {cy-58} L{cx-8} {cy-66} Z"/>
          <path fill="#7f1d1d" stroke="{OUTLINE}" stroke-width="3" d="M{cx+24} {cy-92} L{cx+32} {cy-58} L{cx+8} {cy-66} Z"/>
          <path class="fill-sith" d="M128 430 Q256 292 384 430 L362 512 H150 Z"/>
          <ellipse class="fill-skin" cx="{cx}" cy="{cy-52}" rx="76" ry="86"/>
          <circle fill="#fef08a" cx="{cx-24}" cy="{cy-56}" r="11"/>
          <circle fill="#fef08a" cx="{cx+24}" cy="{cy-56}" r="11"/>
          {lightsaber(accent, 370, 300, -16, "red")}
        """,
        "inquisitor": f"""
          <circle class="glow" cx="{cx}" cy="{cy}" r="108"/>
          <path class="fill-sith" d="M120 432 Q256 260 392 432 L370 512 H142 Z"/>
          <ellipse fill="#374151" stroke="{OUTLINE}" stroke-width="3" cx="{cx}" cy="{cy-54}" rx="78" ry="88"/>
          <rect class="fill-metal" x="{cx-34}" y="{cy-72}" width="68" height="18" rx="6"/>
          <circle fill="#ef4444" cx="{cx-22}" cy="{cy-48}" r="10"/>
          <circle fill="#ef4444" cx="{cx+22}" cy="{cy-48}" r="10"/>
          <path class="stroke-red" d="M{cx-52} {cy+10} L{cx-78} {cy+48}"/>
          <path class="stroke-red" d="M{cx+52} {cy+10} L{cx+78} {cy+48}"/>
          {lightsaber(accent, 372, 298, -12, "red")}
        """,
    }
    return bodies.get(kind, bodies["jedi" if blade == "blue" else "sith"])


def portrait_svg(entry: dict, folder: str) -> str:
    accent = entry["color"]
    kind = archetype(entry, folder)
    blade = "red" if folder == "sith" else "blue"
    body = portrait_body(kind, accent, blade)
    return svg_wrap(entry["name"], accent, body, entry["slug"], blade=blade)


def scene_figure(accent: str, blade: str) -> str:
    cx, cy = 256, 292
    saber_color = "#38bdf8" if blade == "blue" else "#ef4444"
    robe = accent if blade == "blue" else "#111827"
    skin = "#f4c99b" if blade == "blue" else "#d4a574"
    return f"""
          <path fill="{robe}" stroke="{OUTLINE}" stroke-width="3" d="M186 392 Q256 288 326 392 L312 438 H200 Z"/>
          <circle fill="{skin}" stroke="{OUTLINE}" stroke-width="3" cx="{cx}" cy="{cy-42}" r="34"/>
          <rect fill="#64748b" stroke="{OUTLINE}" stroke-width="2" x="{cx+18}" y="{cy-8}" width="12" height="36" rx="3"/>
          <line stroke="{saber_color}" stroke-width="7" stroke-linecap="round" x1="{cx+24}" y1="{cy-12}" x2="{cx+82}" y2="{cy-72}"/>
          <line stroke="#ffffff" stroke-width="3" stroke-linecap="round" x1="{cx+24}" y1="{cy-12}" x2="{cx+82}" y2="{cy-72}" opacity="0.65"/>
        """


def jedi_scene_svg(entry: dict) -> str:
    accent = entry["color"]
    entry = {**entry, "role": entry.get("role", entry.get("rank", "Jedi"))}
    name = xml_escape(entry["name"])
    role = xml_escape(entry.get("role", "Jedi"))
    body = textwrap.dedent(
        f"""
          <rect fill="#0f172a" x="0" y="352" width="512" height="160" opacity="0.88"/>
          <rect fill="{accent}" x="0" y="352" width="512" height="4" opacity="0.55"/>
          <path class="fill-light" d="M64 352 L112 148 L168 352 Z" opacity="0.92"/>
          <path class="fill-light" d="M196 352 L248 118 L300 352 Z" opacity="0.95"/>
          <path class="fill-light" d="M344 352 L404 132 L464 352 Z" opacity="0.92"/>
          <rect class="fill-light" x="228" y="96" width="56" height="256" rx="6" opacity="0.88"/>
          <path class="fill-accent" d="M256 62 L286 118 L226 118 Z"/>
          <rect class="fill-mid" x="188" y="318" width="136" height="34" rx="8"/>
          <circle class="fill-accent" cx="128" cy="388" r="16" opacity="0.75"/>
          <circle class="fill-accent" cx="384" cy="396" r="12" opacity="0.75"/>
          <line class="stroke-blue" x1="128" y1="388" x2="188" y2="332"/>
          <line class="stroke-blue" x1="384" y1="396" x2="324" y2="336"/>
          <circle fill="#38bdf8" cx="96" cy="280" r="4" opacity="0.7"/>
          <circle fill="#38bdf8" cx="420" cy="260" r="5" opacity="0.65"/>
          <circle fill="#38bdf8" cx="360" cy="220" r="3" opacity="0.55"/>
          <rect class="fill-accent" x="438" y="368" width="48" height="48" rx="8" opacity="0.85"/>
          <polygon fill="#7dd3fc" points="462,382 452,408 472,408"/>
          {scene_figure(accent, "blue")}
          <text x="48" y="480" fill="{accent}" font-family="system-ui,sans-serif" font-size="20" font-weight="600">{name[:28]}</text>
          <text x="48" y="48" fill="#e2e8f0" font-family="system-ui,sans-serif" font-size="15" opacity="0.88">{role[:36]}</text>
        """
    )
    return svg_wrap(f"{entry['name']} Jedi scene", accent, body, f"{entry['slug']}-scene", blade="blue")


def sith_scene_svg(entry: dict) -> str:
    accent = entry["color"]
    entry = {**entry, "role": entry.get("role", entry.get("title", "Sith"))}
    name = xml_escape(entry["name"])
    role = xml_escape(entry.get("role", "Sith"))
    lava = entry["slug"] in {"darth-vader", "darth-sidious", "darth-tyranus"} or "mustafar" in entry.get("desc", "").lower()
    lava_block = ""
    if lava:
        lava_block = """
          <rect fill="#991b1b" x="0" y="380" width="512" height="132" opacity="0.75"/>
          <path fill="#ef4444" d="M0 420 Q128 390 256 430 T512 410 L512 512 H0 Z" opacity="0.55"/>
        """
    body = textwrap.dedent(
        f"""
          <path class="fill-dark" d="M48 420 Q256 250 464 420 L440 512 H72 Z"/>
          <path class="fill-dark" d="M168 420 L256 168 L344 420 Z"/>
          {lava_block}
          <path class="stroke-red" d="M256 72 L214 196"/>
          <path class="stroke-red" d="M256 72 L298 196"/>
          <path class="stroke-red" d="M256 72 L256 228"/>
          <path class="stroke-red" d="M148 108 Q256 148 364 108"/>
          <path class="stroke-red" d="M108 188 Q256 220 404 188"/>
          <circle class="fill-red" cx="256" cy="248" r="30" opacity="0.9"/>
          <rect class="fill-dark" x="228" y="308" width="56" height="88" rx="10"/>
          <circle fill="#ef4444" cx="180" cy="320" r="5" opacity="0.8"/>
          <circle fill="#ef4444" cx="332" cy="340" r="4" opacity="0.75"/>
          <circle fill="#ef4444" cx="400" cy="280" r="6" opacity="0.7"/>
          <rect fill="#111827" stroke="{accent}" stroke-width="3" x="438" y="368" width="48" height="48" rx="8"/>
          <polygon fill="#ef4444" points="462,382 452,408 472,408"/>
          {scene_figure(accent, "red")}
          <text x="48" y="480" fill="{accent}" font-family="system-ui,sans-serif" font-size="20" font-weight="600">{name[:28]}</text>
          <text x="48" y="48" fill="#fecaca" font-family="system-ui,sans-serif" font-size="15" opacity="0.88">{role[:36]}</text>
        """
    )
    return svg_wrap(f"{entry['name']} Sith scene", accent, body, f"{entry['slug']}-scene", blade="red")


def jedi_emblem_svg(entry: dict) -> str:
    accent = entry["color"]
    body = textwrap.dedent(
        f"""
          <circle class="fill-light" cx="256" cy="256" r="152"/>
          <circle class="outline" cx="256" cy="256" r="152"/>
          <circle fill="none" stroke="{accent}" stroke-width="6" cx="256" cy="256" r="128" opacity="0.85"/>
          <path class="fill-accent" d="M256 92 L292 228 L438 228 L318 312 L362 448 L256 362 L150 448 L194 312 L74 228 L220 228 Z"/>
          <circle class="fill-light" cx="256" cy="256" r="42"/>
          <circle fill="{accent}" cx="256" cy="256" r="18" opacity="0.9"/>
          <rect class="fill-metal" x="248" y="168" width="16" height="52" rx="4"/>
          <rect class="fill-metal" x="248" y="292" width="16" height="52" rx="4"/>
          <rect class="fill-metal" x="168" y="248" width="52" height="16" rx="4"/>
          <rect class="fill-metal" x="292" y="248" width="52" height="16" rx="4"/>
        """
    )
    return svg_wrap(f"Jedi emblem — {entry['name']}", accent, body, f"{entry['slug']}-emblem", blade="blue")


def sith_emblem_svg(entry: dict) -> str:
    accent = entry["color"]
    body = textwrap.dedent(
        f"""
          <circle class="fill-dark" cx="256" cy="256" r="152"/>
          <circle class="outline" cx="256" cy="256" r="152"/>
          <circle fill="none" stroke="#ef4444" stroke-width="5" cx="256" cy="256" r="128" opacity="0.75"/>
          <polygon class="fill-red" points="256,88 372,176 336,312 176,312 140,176"/>
          <polygon fill="#111827" points="256,128 336,192 312,288 200,288 176,192"/>
          <circle class="fill-light" cx="256" cy="220" r="24"/>
          <rect class="fill-red" x="244" y="242" width="24" height="62" rx="6"/>
          <path class="stroke-red" d="M196 168 L176 128"/>
          <path class="stroke-red" d="M316 168 L336 128"/>
          <path class="stroke-red" d="M256 88 L256 58"/>
        """
    )
    return svg_wrap(f"Sith emblem — {entry['name']}", accent, body, f"{entry['slug']}-emblem", blade="red")
