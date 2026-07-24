#!/usr/bin/env python3
"""Character-specific rich SVG artwork for Droid Directory entries."""

from __future__ import annotations

import hashlib
import math
from typing import Callable

from directory_art import droid_scene_backdrop, scene_labels, svg_wrap

OUTLINE = "#1a1a2e"
CX, CY = 256, 268


def _glow() -> str:
    return f'<circle class="glow" cx="{CX}" cy="{CY}" r="100"/>'


def _scene_wrap(body: str, scene: bool, accent: str, name: str, subtitle: str) -> str:
    if scene:
        body += scene_labels(name, subtitle, accent)
    return body


# ---------------------------------------------------------------------------
# Character design renderers
# ---------------------------------------------------------------------------


def _r2_series(
    scene: bool,
    *,
    dome: str = "#f8fafc",
    body: str = "#2563eb",
    stripe: str = "#dc2626",
    accent_panel: str = "#38bdf8",
    leg_stripe: bool = True,
) -> str:
    leg = (
        f'<rect fill="{stripe}" x="{CX-6}" y="{CY+58}" width="12" height="38" rx="3"/>'
        if leg_stripe
        else f'<rect class="fill-metal" x="{CX-6}" y="{CY+58}" width="12" height="38" rx="3"/>'
    )
    return f"""
          {droid_scene_backdrop(body if scene else "#64748b", scene)}
          {_glow()}
          <circle fill="{dome}" stroke="{OUTLINE}" stroke-width="3" cx="{CX}" cy="{CY-58}" r="46"/>
          <rect fill="{body}" stroke="{OUTLINE}" stroke-width="3" x="{CX-44}" y="{CY-18}" width="88" height="78" rx="14"/>
          <rect fill="{accent_panel}" stroke="{OUTLINE}" stroke-width="2" x="{CX-28}" y="{CY-2}" width="56" height="18" rx="4"/>
          <rect fill="{accent_panel}" stroke="{OUTLINE}" stroke-width="2" x="{CX-22}" y="{CY+22}" width="44" height="14" rx="3"/>
          <circle fill="{stripe}" cx="{CX+18}" cy="{CY-52}" r="7"/>
          <circle fill="#111827" cx="{CX-16}" cy="{CY-62}" r="5"/>
          <circle fill="#111827" cx="{CX+16}" cy="{CY-62}" r="5"/>
          <rect class="fill-metal" x="{CX-52}" y="{CY+8}" width="18" height="34" rx="6"/>
          <rect class="fill-metal" x="{CX+34}" y="{CY+8}" width="18" height="34" rx="6"/>
          {leg}
          <line class="outline" x1="{CX-44}" y1="{CY+18}" x2="{CX-58}" y2="{CY+42}"/>
          <line class="outline" x1="{CX+44}" y1="{CY+18}" x2="{CX+58}" y2="{CY+42}"/>
        """


def _c3po_series(scene: bool, *, gold: str = "#eab308", wire: bool = True) -> str:
    wires = (
        f"""
          <rect fill="#dc2626" x="{CX-18}" y="{CY+12}" width="36" height="28" rx="4" opacity="0.85"/>
          <line stroke="#64748b" stroke-width="2" x1="{CX-10}" y1="{CY+16}" x2="{CX+10}" y2="{CY+34}"/>
          <line stroke="#64748b" stroke-width="2" x1="{CX+10}" y1="{CY+16}" x2="{CX-10}" y2="{CY+34}"/>
        """
        if wire
        else ""
    )
    return f"""
          {droid_scene_backdrop(gold, scene)}
          {_glow()}
          <rect fill="{gold}" stroke="{OUTLINE}" stroke-width="3" x="{CX-38}" y="{CY-78}" width="76" height="52" rx="14"/>
          <circle fill="#111827" cx="{CX-14}" cy="{CY-62}" r="6"/>
          <circle fill="#111827" cx="{CX+14}" cy="{CY-62}" r="6"/>
          <rect fill="{gold}" stroke="{OUTLINE}" stroke-width="3" x="{CX-42}" y="{CY-12}" width="84" height="98" rx="16"/>
          <rect fill="#fef3c7" stroke="{OUTLINE}" stroke-width="2" x="{CX-28}" y="{CY+2}" width="56" height="22" rx="4"/>
          {wires}
          <line class="outline" x1="{CX-42}" y1="{CY+18}" x2="{CX-72}" y2="{CY+48}"/>
          <line class="outline" x1="{CX+42}" y1="{CY+18}" x2="{CX+72}" y2="{CY+48}"/>
          <line class="outline" x1="{CX-14}" y1="{CY+86}" x2="{CX-18}" y2="{CY+128}"/>
          <line class="outline" x1="{CX+14}" y1="{CY+86}" x2="{CX+18}" y2="{CY+128}"/>
        """


def _bb8(scene: bool) -> str:
    return f"""
          {droid_scene_backdrop("#f97316", scene)}
          {_glow()}
          <circle fill="#f8fafc" stroke="{OUTLINE}" stroke-width="3" cx="{CX}" cy="{CY+18}" r="62"/>
          <circle fill="#f97316" stroke="{OUTLINE}" stroke-width="3" cx="{CX-28}" cy="{CY+8}" r="14"/>
          <circle fill="#f97316" stroke="{OUTLINE}" stroke-width="3" cx="{CX+22}" cy="{CY+28}" r="10"/>
          <circle fill="#f97316" stroke="{OUTLINE}" stroke-width="3" cx="{CX+8}" cy="{CY-8}" r="8"/>
          <circle fill="#111827" stroke="{OUTLINE}" stroke-width="2" cx="{CX}" cy="{CY-48}" r="28"/>
          <circle fill="#38bdf8" cx="{CX-8}" cy="{CY-52}" r="6"/>
          <rect fill="#f97316" stroke="{OUTLINE}" stroke-width="2" x="{CX-4}" y="{CY-78}" width="8" height="18" rx="2"/>
        """


def _k2so(scene: bool) -> str:
    return f"""
          {droid_scene_backdrop("#111827", scene)}
          {_glow()}
          <rect fill="#111827" stroke="{OUTLINE}" stroke-width="3" x="{CX-34}" y="{CY-88}" width="68" height="48" rx="10"/>
          <rect fill="#374151" stroke="{OUTLINE}" stroke-width="3" x="{CX-38}" y="{CY-28}" width="76" height="108" rx="12"/>
          <rect fill="#1f2937" x="{CX-12}" y="{CY-72}" width="24" height="14" rx="3"/>
          <circle fill="#22c55e" cx="{CX-18}" cy="{CY-58}" r="5"/>
          <circle fill="#ef4444" cx="{CX+18}" cy="{CY-58}" r="5"/>
          <rect fill="#111827" x="{CX-58}" y="{CY+8}" width="28" height="58" rx="6"/>
          <rect fill="#111827" x="{CX+30}" y="{CY+8}" width="28" height="58" rx="6"/>
          <line class="outline" x1="{CX}" y1="{CY+80}" x2="{CX}" y2="{CY+118}"/>
        """


def _chopper(scene: bool) -> str:
    return f"""
          {droid_scene_backdrop("#e11d48", scene)}
          {_glow()}
          <rect fill="#64748b" stroke="{OUTLINE}" stroke-width="3" x="{CX-48}" y="{CY-8}" width="96" height="72" rx="18"/>
          <circle fill="#f8fafc" stroke="{OUTLINE}" stroke-width="3" cx="{CX}" cy="{CY-52}" r="34"/>
          <rect fill="#dc2626" x="{CX-18}" y="{CY-68}" width="36" height="12" rx="3"/>
          <rect fill="#2563eb" x="{CX-52}" y="{CY+12}" width="22" height="28" rx="4"/>
          <rect fill="#eab308" x="{CX+30}" y="{CY+18}" width="18" height="22" rx="4"/>
          <line class="outline" x1="{CX-48}" y1="{CY+22}" x2="{CX-78}" y2="{CY+52}"/>
          <rect class="fill-metal" x="{CX-8}" y="{CY+64}" width="16" height="34" rx="4"/>
        """


def _hk_series(scene: bool, *, label: str = "HK") -> str:
    return f"""
          {droid_scene_backdrop("#991b1b", scene)}
          {_glow()}
          <rect fill="#7f1d1d" stroke="{OUTLINE}" stroke-width="3" x="{CX-28}" y="{CY-82}" width="56" height="38" rx="8"/>
          <circle fill="#dc2626" cx="{CX-10}" cy="{CY-68}" r="5"/>
          <circle fill="#dc2626" cx="{CX+10}" cy="{CY-68}" r="5"/>
          <rect fill="#991b1b" stroke="{OUTLINE}" stroke-width="3" x="{CX-32}" y="{CY-32}" width="64" height="88" rx="8"/>
          <rect fill="#450a0a" x="{CX-48}" y="{CY+4}" width="22" height="48" rx="4"/>
          <rect fill="#450a0a" x="{CX+26}" y="{CY+4}" width="22" height="48" rx="4"/>
          <line class="outline" x1="{CX-32}" y1="{CY+8}" x2="{CX-68}" y2="{CY+38}"/>
          <line class="outline" x1="{CX+32}" y1="{CY+8}" x2="{CX+68}" y2="{CY+38}"/>
          <text x="{CX}" y="{CY+58}" text-anchor="middle" fill="#fecaca" font-family="monospace" font-size="12">{label}</text>
        """


def _ig_series(scene: bool, *, dark: bool = True) -> str:
    body = "#111827" if dark else "#64748b"
    return f"""
          {droid_scene_backdrop(body, scene)}
          {_glow()}
          <rect fill="{body}" stroke="{OUTLINE}" stroke-width="3" x="{CX-24}" y="{CY-88}" width="48" height="36" rx="6"/>
          <rect fill="{body}" stroke="{OUTLINE}" stroke-width="3" x="{CX-28}" y="{CY-38}" width="56" height="96" rx="8"/>
          <circle fill="#ef4444" cx="{CX-10}" cy="{CY-74}" r="5"/>
          <circle fill="#ef4444" cx="{CX+10}" cy="{CY-74}" r="5"/>
          <line class="outline" x1="{CX-28}" y1="{CY+8}" x2="{CX-62}" y2="{CY+38}"/>
          <line class="outline" x1="{CX+28}" y1="{CY+8}" x2="{CX+62}" y2="{CY+38}"/>
          <line class="outline" x1="{CX-12}" y1="{CY+58}" x2="{CX-18}" y2="{CY+118}"/>
          <line class="outline" x1="{CX+12}" y1="{CY+58}" x2="{CX+18}" y2="{CY+118}"/>
        """


def _bd1(scene: bool) -> str:
    return f"""
          {droid_scene_backdrop("#38bdf8", scene)}
          {_glow()}
          <circle fill="#64748b" stroke="{OUTLINE}" stroke-width="3" cx="{CX}" cy="{CY-18}" r="36"/>
          <circle fill="#38bdf8" cx="{CX-10}" cy="{CY-22}" r="6"/>
          <rect fill="#475569" stroke="{OUTLINE}" stroke-width="3" x="{CX-22}" y="{CY+18}" width="44" height="48" rx="10"/>
          <line class="outline" x1="{CX-28}" y1="{CY+66}" x2="{CX-38}" y2="{CY+98}"/>
          <line class="outline" x1="{CX+28}" y1="{CY+66}" x2="{CX+38}" y2="{CY+98}"/>
          <path fill="#38bdf8" opacity="0.7" d="M{CX+18} {CY-8} L{CX+48} {CY+18} L{CX+38} {CY+28} L{CX+12} {CY+2} Z"/>
        """


def _b1(scene: bool, *, command: bool = False, rocket: bool = False, firefighter: bool = False) -> str:
    head = "#1f2937" if command else "#64748b"
    accent = "#eab308" if command else "#94a3b8"
    pack = (
        f'<rect fill="#475569" x="{CX+28}" y="{CY+8}" width="22" height="38" rx="4"/>'
        if rocket
        else ""
    )
    nozzle = (
        f'<rect fill="#dc2626" x="{CX-32}" y="{CY+18}" width="14" height="22" rx="3"/>'
        if firefighter
        else ""
    )
    return f"""
          {droid_scene_backdrop("#94a3b8", scene)}
          {_glow()}
          <ellipse fill="{head}" stroke="{OUTLINE}" stroke-width="3" cx="{CX}" cy="{CY-62}" rx="22" ry="18"/>
          <circle fill="#111827" cx="{CX-8}" cy="{CY-64}" r="4"/>
          <circle fill="#111827" cx="{CX+8}" cy="{CY-64}" r="4"/>
          <rect fill="{accent}" stroke="{OUTLINE}" stroke-width="3" x="{CX-18}" y="{CY-38}" width="36" height="52" rx="6"/>
          <line class="outline" x1="{CX-18}" y1="{CY-18}" x2="{CX-48}" y2="{CY+8}"/>
          <line class="outline" x1="{CX+18}" y1="{CY-18}" x2="{CX+48}" y2="{CY+8}"/>
          <line class="outline" x1="{CX-10}" y1="{CY+14}" x2="{CX-14}" y2="{CY+88}"/>
          <line class="outline" x1="{CX+10}" y1="{CY+14}" x2="{CX+14}" y2="{CY+88}"/>
          {pack}
          {nozzle}
        """


def _b2(scene: bool, *, ultra: bool = False) -> str:
    w = 52 if ultra else 44
    return f"""
          {droid_scene_backdrop("#64748b", scene)}
          {_glow()}
          <rect fill="#475569" stroke="{OUTLINE}" stroke-width="3" x="{CX-38}" y="{CY-72}" width="76" height="48" rx="10"/>
          <circle fill="#dc2626" cx="{CX-14}" cy="{CY-58}" r="5"/>
          <circle fill="#dc2626" cx="{CX+14}" cy="{CY-58}" r="5"/>
          <rect fill="#64748b" stroke="{OUTLINE}" stroke-width="3" x="{CX-w//2}" y="{CY-12}" width="{w}" height="92" rx="8"/>
          <rect fill="#1f2937" x="{CX-58}" y="{CY+8}" width="28" height="18" rx="4"/>
          <rect fill="#1f2937" x="{CX+30}" y="{CY+8}" width="28" height="18" rx="4"/>
          <rect fill="#334155" x="{CX-12}" y="{CY+72}" width="24" height="28" rx="4"/>
        """


def _droideka(scene: bool, *, scorpenek: bool = False) -> str:
    r = 64 if scorpenek else 54
    return f"""
          {droid_scene_backdrop("#94a3b8", scene)}
          {_glow()}
          <circle fill="#64748b" stroke="{OUTLINE}" stroke-width="3" cx="{CX}" cy="{CY-8}" r="{r}"/>
          <circle fill="#cbd5e1" cx="{CX}" cy="{CY-8}" r="{r//2}"/>
          <line class="outline" stroke-width="6" x1="{CX-58}" y1="{CY+28}" x2="{CX-92}" y2="{CY+72}"/>
          <line class="outline" stroke-width="6" x1="{CX+58}" y1="{CY+28}" x2="{CX+92}" y2="{CY+72}"/>
          <circle fill="#dc2626" cx="{CX-88}" cy="{CY+76}" r="8"/>
          <circle fill="#dc2626" cx="{CX+88}" cy="{CY+76}" r="8"/>
        """


def _magnaguard(scene: bool) -> str:
    return f"""
          {droid_scene_backdrop("#64748b", scene)}
          {_glow()}
          <rect fill="#475569" stroke="{OUTLINE}" stroke-width="3" x="{CX-32}" y="{CY-82}" width="64" height="44" rx="8"/>
          <rect fill="#94a3b8" stroke="{OUTLINE}" stroke-width="3" x="{CX-28}" y="{CY-22}" width="56" height="92" rx="8"/>
          <line class="outline" x1="{CX-28}" y1="{CY+8}" x2="{CX-78}" y2="{CY-42}"/>
          <line class="outline" x1="{CX+28}" y1="{CY+8}" x2="{CX+78}" y2="{CY-42}"/>
          <rect fill="#1f2937" x="{CX-8}" y="{CY-72}" width="16" height="18" rx="3"/>
        """


def _tactical(scene: bool, *, super_droid: bool = False) -> str:
    h = 58 if super_droid else 48
    return f"""
          {droid_scene_backdrop("#64748b", scene)}
          {_glow()}
          <ellipse fill="#475569" stroke="{OUTLINE}" stroke-width="3" cx="{CX}" cy="{CY-58}" rx="38" ry="{h//2 + 8}"/>
          <rect fill="#64748b" stroke="{OUTLINE}" stroke-width="3" x="{CX-30}" y="{CY-8}" width="60" height="88" rx="8"/>
          <rect fill="#eab308" x="{CX-18}" y="{CY-48}" width="36" height="12" rx="3"/>
          <rect fill="#111827" x="{CX-22}" y="{CY+12}" width="44" height="28" rx="4"/>
        """


def _vulture(scene: bool) -> str:
    return f"""
          {droid_scene_backdrop("#64748b", scene)}
          {_glow()}
          <path fill="#475569" stroke="{OUTLINE}" stroke-width="3" d="M{CX-88} {CY+18} L{CX} {CY-78} L{CX+88} {CY+18} L{CX+42} {CY+38} L{CX-42} {CY+38} Z"/>
          <circle fill="#dc2626" cx="{CX}" cy="{CY-8}" r="12"/>
          <line class="outline" x1="{CX-42}" y1="{CY+38}" x2="{CX-72}" y2="{CY+72}"/>
          <line class="outline" x1="{CX+42}" y1="{CY+38}" x2="{CX+72}" y2="{CY+72}"/>
        """


def _probe(scene: bool, *, seeker: bool = False) -> str:
    eye = "#ef4444" if seeker else "#38bdf8"
    return f"""
          {droid_scene_backdrop("#64748b", scene)}
          {_glow()}
          <circle fill="#475569" stroke="{OUTLINE}" stroke-width="3" cx="{CX}" cy="{CY-28}" r="46"/>
          <circle fill="{eye}" cx="{CX}" cy="{CY-28}" r="14"/>
          <line class="outline" x1="{CX}" y1="{CY+18}" x2="{CX}" y2="{CY+92}"/>
          <line class="outline" x1="{CX-28}" y1="{CY+92}" x2="{CX+28}" y2="{CY+92}"/>
          <line class="outline" x1="{CX-18}" y1="{CY+48}" x2="{CX-48}" y2="{CY+78}"/>
          <line class="outline" x1="{CX+18}" y1="{CY+48}" x2="{CX+48}" y2="{CY+78}"/>
        """


def _ito(scene: bool) -> str:
    return f"""
          {droid_scene_backdrop("#111827", scene)}
          {_glow()}
          <circle fill="#1f2937" stroke="{OUTLINE}" stroke-width="3" cx="{CX}" cy="{CY-18}" r="42"/>
          <circle fill="#dc2626" cx="{CX}" cy="{CY-18}" r="10"/>
          <line stroke="#94a3b8" stroke-width="2" x1="{CX-28}" y1="{CY-38}" x2="{CX-48}" y2="{CY-68}"/>
          <line stroke="#94a3b8" stroke-width="2" x1="{CX+28}" y1="{CY-38}" x2="{CX+48}" y2="{CY-68}"/>
          <line stroke="#94a3b8" stroke-width="2" x1="{CX}" y1="{CY+24}" x2="{CX}" y2="{CY+88}"/>
        """


def _medical(scene: bool, *, fx: bool = False) -> str:
    cross = "M" if not fx else "+"
    return f"""
          {droid_scene_backdrop("#38bdf8", scene)}
          {_glow()}
          <rect fill="#f8fafc" stroke="{OUTLINE}" stroke-width="3" x="{CX-34}" y="{CY-78}" width="68" height="44" rx="12"/>
          <rect fill="#e2e8f0" stroke="{OUTLINE}" stroke-width="3" x="{CX-30}" y="{CY-18}" width="60" height="96" rx="12"/>
          <path fill="#dc2626" d="M{CX} {CY-62} L{cross}{CX+12} {CY-44} L{CX} {CY-32} L{CX-12} {CY-44} Z"/>
          <rect fill="#94a3b8" x="{CX-48}" y="{CY+8}" width="18" height="48" rx="4"/>
        """


def _mouse(scene: bool, *, imperial: bool = False) -> str:
    color = "#374151" if imperial else "#64748b"
    return f"""
          {droid_scene_backdrop(color, scene)}
          {_glow()}
          <rect fill="{color}" stroke="{OUTLINE}" stroke-width="3" x="{CX-38}" y="{CY-18}" width="76" height="42" rx="8"/>
          <rect fill="#94a3b8" x="{CX-28}" y="{CY-8}" width="56" height="16" rx="3"/>
          <circle fill="#eab308" cx="{CX+24}" cy="{CY+2}" r="4"/>
        """


def _gonk(scene: bool) -> str:
    return f"""
          {droid_scene_backdrop("#64748b", scene)}
          {_glow()}
          <rect fill="#475569" stroke="{OUTLINE}" stroke-width="3" x="{CX-42}" y="{CY-42}" width="84" height="88" rx="10"/>
          <rect fill="#94a3b8" x="{CX-32}" y="{CY-28}" width="64" height="24" rx="4"/>
          <text x="{CX}" y="{CY+8}" text-anchor="middle" fill="#eab308" font-family="monospace" font-size="16" font-weight="700">GONK</text>
          <line class="outline" x1="{CX-18}" y1="{CY+46}" x2="{CX-18}" y2="{CY+88}"/>
          <line class="outline" x1="{CX+18}" y1="{CY+46}" x2="{CX+18}" y2="{CY+88}"/>
        """


def _pit(scene: bool) -> str:
    return f"""
          {droid_scene_backdrop("#f97316", scene)}
          {_glow()}
          <rect fill="#ea580c" stroke="{OUTLINE}" stroke-width="3" x="{CX-32}" y="{CY-32}" width="64" height="52" rx="8"/>
          <circle fill="#111827" cx="{CX-10}" cy="{CY-18}" r="5"/>
          <circle fill="#111827" cx="{CX+10}" cy="{CY-18}" r="5"/>
          <line class="outline" x1="{CX-16}" y1="{CY+20}" x2="{CX-24}" y2="{CY+78}"/>
          <line class="outline" x1="{CX+16}" y1="{CY+20}" x2="{CX+24}" y2="{CY+78}"/>
        """


def _dark_trooper(scene: bool) -> str:
    return f"""
          {droid_scene_backdrop("#111827", scene)}
          {_glow()}
          <rect fill="#111827" stroke="{OUTLINE}" stroke-width="3" x="{CX-40}" y="{CY-82}" width="80" height="52" rx="10"/>
          <rect fill="#374151" stroke="{OUTLINE}" stroke-width="3" x="{CX-36}" y="{CY-18}" width="72" height="98" rx="10"/>
          <rect fill="#1f2937" x="{CX-14}" y="{CY-62}" width="28" height="16" rx="3"/>
          <circle fill="#ef4444" cx="{CX-18}" cy="{CY-52}" r="4"/>
          <circle fill="#ef4444" cx="{CX+18}" cy="{CY-52}" r="4"/>
        """


def _l3(scene: bool) -> str:
    return f"""
          {droid_scene_backdrop("#eab308", scene)}
          {_glow()}
          <rect fill="#ca8a04" stroke="{OUTLINE}" stroke-width="3" x="{CX-36}" y="{CY-78}" width="72" height="48" rx="12"/>
          <rect fill="#eab308" stroke="{OUTLINE}" stroke-width="3" x="{CX-40}" y="{CY-18}" width="80" height="92" rx="14"/>
          <rect fill="#111827" x="{CX-24}" y="{CY+8}" width="48" height="24" rx="4" opacity="0.8"/>
          <line stroke="#64748b" stroke-width="2" x1="{CX-16}" y1="{CY+12}" x2="{CX+16}" y2="{CY+28}"/>
          <line class="outline" x1="{CX-40}" y1="{CY+22}" x2="{CX-72}" y2="{CY+52}"/>
        """


def _do_droid(scene: bool) -> str:
    return f"""
          {droid_scene_backdrop("#38bdf8", scene)}
          {_glow()}
          <ellipse fill="#475569" stroke="{OUTLINE}" stroke-width="3" cx="{CX}" cy="{CY-28}" rx="34" ry="28"/>
          <circle fill="#38bdf8" cx="{CX-8}" cy="{CY-32}" r="7"/>
          <rect fill="#64748b" stroke="{OUTLINE}" stroke-width="3" x="{CX-28}" y="{CY+2}" width="56" height="38" rx="10"/>
          <circle fill="#1f2937" cx="{CX-32}" cy="{CY+48}" r="12"/>
          <circle fill="#1f2937" cx="{CX+32}" cy="{CY+48}" r="12"/>
        """


def _g0t0(scene: bool) -> str:
    return f"""
          {droid_scene_backdrop("#dc2626", scene)}
          {_glow()}
          <circle fill="#111827" stroke="{OUTLINE}" stroke-width="3" cx="{CX}" cy="{CY-48}" r="38"/>
          <circle fill="#dc2626" cx="{CX}" cy="{CY-48}" r="18"/>
          <rect fill="#475569" stroke="{OUTLINE}" stroke-width="3" x="{CX-34}" y="{CY-2}" width="68" height="78" rx="12"/>
          <line class="outline" x1="{CX-34}" y1="{CY+18}" x2="{CX-68}" y2="{CY+48}"/>
          <line class="outline" x1="{CX+34}" y1="{CY+18}" x2="{CX+68}" y2="{CY+48}"/>
        """


def _4lom(scene: bool) -> str:
    return f"""
          {droid_scene_backdrop("#64748b", scene)}
          {_glow()}
          <rect fill="#475569" stroke="{OUTLINE}" stroke-width="3" x="{CX-26}" y="{CY-82}" width="52" height="36" rx="6"/>
          <rect fill="#64748b" stroke="{OUTLINE}" stroke-width="3" x="{CX-30}" y="{CY-32}" width="60" height="88" rx="8"/>
          <circle fill="#22d3ee" cx="{CX-10}" cy="{CY-68}" r="5"/>
          <circle fill="#22d3ee" cx="{CX+10}" cy="{CY-68}" r="5"/>
          <rect fill="#334155" x="{CX-52}" y="{CY+8}" width="22" height="38" rx="4"/>
        """


def _artillery(scene: bool, *, spider: bool = False, oct: bool = False) -> str:
    if oct:
        return f"""
          {droid_scene_backdrop("#64748b", scene)}
          {_glow()}
          <circle fill="#475569" stroke="{OUTLINE}" stroke-width="3" cx="{CX}" cy="{CY-38}" r="28"/>
          <line class="outline" stroke-width="5" x1="{CX}" y1="{CY-10}" x2="{CX}" y2="{CY+72}"/>
          <line class="outline" stroke-width="5" x1="{CX-38}" y1="{CY+8}" x2="{CX-72}" y2="{CY+58}"/>
          <line class="outline" stroke-width="5" x1="{CX+38}" y1="{CY+8}" x2="{CX+72}" y2="{CY+58}"/>
          <line class="outline" stroke-width="5" x1="{CX-28}" y1="{CY-18}" x2="{CX-58}" y2="{CY-48}"/>
          <line class="outline" stroke-width="5" x1="{CX+28}" y1="{CY-18}" x2="{CX+58}" y2="{CY-48}"/>
        """
    legs = 4 if spider else 3
    leg_svg = "\n".join(
        f'<line class="outline" stroke-width="5" x1="{CX}" y1="{CY+18}" x2="{CX + int(60 * math.cos(i))}" y2="{CY + 72}"/>'
        for i in range(-2, legs - 2)
    )
    return f"""
          {droid_scene_backdrop("#64748b", scene)}
          {_glow()}
          <rect fill="#475569" stroke="{OUTLINE}" stroke-width="3" x="{CX-48}" y="{CY-28}" width="96" height="38" rx="8"/>
          <rect fill="#334155" x="{CX-10}" y="{CY-58}" width="20" height="32" rx="4"/>
          {leg_svg}
        """


def _gatekeeper(scene: bool) -> str:
    return f"""
          {droid_scene_backdrop("#dc2626", scene)}
          <rect fill="#1f2937" stroke="{OUTLINE}" stroke-width="3" x="{CX-82}" y="{CY-82}" width="164" height="118" rx="8"/>
          <rect fill="#dc2626" x="{CX-24}" y="{CY-62}" width="48" height="34" rx="6"/>
          <circle fill="#eab308" cx="{CX}" cy="{CY-45}" r="8"/>
        """


def _labor(scene: bool, *, treadwell: bool = False) -> str:
    base = f"""
          {droid_scene_backdrop("#64748b", scene)}
          {_glow()}
          <rect fill="#475569" stroke="{OUTLINE}" stroke-width="3" x="{CX-38}" y="{CY-58}" width="76" height="48" rx="10"/>
          <rect fill="#94a3b8" stroke="{OUTLINE}" stroke-width="3" x="{CX-32}" y="{CY-2}" width="64" height="72" rx="8"/>
          <line class="outline" x1="{CX-32}" y1="{CY+18}" x2="{CX-62}" y2="{CY+48}"/>
          <line class="outline" x1="{CX+32}" y1="{CY+18}" x2="{CX+62}" y2="{CY+48}"/>
        """
    if treadwell:
        base += f'<ellipse fill="#334155" cx="{CX-28}" cy="{CY+78}" rx="18" ry="8"/><ellipse fill="#334155" cx="{CX+28}" cy="{CY+78}" rx="18" ry="8"/>'
    return base


def _bt1(scene: bool) -> str:
    return f"""
          {droid_scene_backdrop("#111827", scene)}
          {_glow()}
          <circle fill="#111827" stroke="{OUTLINE}" stroke-width="3" cx="{CX}" cy="{CY-48}" r="32"/>
          <circle fill="#ef4444" cx="{CX}" cy="{CY-48}" r="10"/>
          <rect fill="#374151" stroke="{OUTLINE}" stroke-width="3" x="{CX-28}" y="{CY-8}" width="56" height="62" rx="8"/>
          <rect fill="#dc2626" x="{CX-8}" y="{CY+54}" width="16" height="28" rx="3"/>
        """


def _000(scene: bool) -> str:
    return f"""
          {droid_scene_backdrop("#eab308", scene)}
          {_glow()}
          <rect fill="#ca8a04" stroke="{OUTLINE}" stroke-width="3" x="{CX-34}" y="{CY-78}" width="68" height="44" rx="12"/>
          <rect fill="#eab308" stroke="{OUTLINE}" stroke-width="3" x="{CX-38}" y="{CY-18}" width="76" height="88" rx="14"/>
          <circle fill="#111827" cx="{CX-12}" cy="{CY-62}" r="6"/>
          <circle fill="#111827" cx="{CX+12}" cy="{CY-62}" r="6"/>
          <text x="{CX}" y="{CY+28}" text-anchor="middle" fill="#450a0a" font-family="monospace" font-size="14">0-0-0</text>
        """


def _proxy(scene: bool) -> str:
    return f"""
          {droid_scene_backdrop("#38bdf8", scene)}
          {_glow()}
          <rect fill="#64748b" stroke="{OUTLINE}" stroke-width="3" x="{CX-30}" y="{CY-78}" width="60" height="42" rx="10"/>
          <rect fill="#475569" stroke="{OUTLINE}" stroke-width="3" x="{CX-34}" y="{CY-22}" width="68" height="92" rx="10"/>
          <rect fill="#2563eb" x="{CX-8}" y="{CY-68}" width="16" height="10" rx="2"/>
          <line class="outline" x1="{CX-34}" y1="{CY+12}" x2="{CX-68}" y2="{CY+42}"/>
          <line class="outline" x1="{CX+34}" y1="{CY+12}" x2="{CX+68}" y2="{CY+42}"/>
        """


def _buzz(scene: bool) -> str:
    return f"""
          {droid_scene_backdrop("#64748b", scene)}
          {_glow()}
          <circle fill="#475569" stroke="{OUTLINE}" stroke-width="3" cx="{CX}" cy="{CY-18}" r="28"/>
          <line class="outline" stroke-width="4" x1="{CX-18}" y1="{CY+8}" x2="{CX-42}" y2="{CY+38}"/>
          <line class="outline" stroke-width="4" x1="{CX+18}" y1="{CY+8}" x2="{CX+42}" y2="{CY+38}"/>
          <line class="outline" stroke-width="4" x1="{CX-8}" y1="{CY+18}" x2="{CX-28}" y2="{CY+58}"/>
          <line class="outline" stroke-width="4" x1="{CX+8}" y1="{CY+18}" x2="{CX+28}" y2="{CY+58}"/>
        """


def _crab(scene: bool) -> str:
    return f"""
          {droid_scene_backdrop("#64748b", scene)}
          {_glow()}
          <ellipse fill="#475569" stroke="{OUTLINE}" stroke-width="3" cx="{CX}" cy="{CY-8}" rx="48" ry="32"/>
          <circle fill="#dc2626" cx="{CX-16}" cy="{CY-12}" r="6"/>
          <circle fill="#dc2626" cx="{CX+16}" cy="{CY-12}" r="6"/>
          <line class="outline" stroke-width="5" x1="{CX-38}" y1="{CY+18}" x2="{CX-72}" y2="{CY+58}"/>
          <line class="outline" stroke-width="5" x1="{CX+38}" y1="{CY+18}" x2="{CX+72}" y2="{CY+58}"/>
          <line class="outline" stroke-width="5" x1="{CX-18}" y1="{CY+24}" x2="{CX-38}" y2="{CY+72}"/>
          <line class="outline" stroke-width="5" x1="{CX+18}" y1="{CY+24}" x2="{CX+38}" y2="{CY+72}"/>
        """


def _aqua(scene: bool) -> str:
    return f"""
          {droid_scene_backdrop("#0ea5e9", scene)}
          {_glow()}
          <ellipse fill="#0369a1" stroke="{OUTLINE}" stroke-width="3" cx="{CX}" cy="{CY-48}" rx="34" ry="28"/>
          <rect fill="#0284c7" stroke="{OUTLINE}" stroke-width="3" x="{CX-28}" y="{CY-12}" width="56" height="72" rx="10"/>
          <ellipse fill="#38bdf8" cx="{CX-12}" cy="{CY-52}" rx="8" ry="10"/>
          <line class="outline" x1="{CX-28}" y1="{CY+18}" x2="{CX-58}" y2="{CY+48}"/>
          <line class="outline" x1="{CX+28}" y1="{CY+18}" x2="{CX+58}" y2="{CY+48}"/>
        """


def _unique_variant(slug: str, kind: str, accent: str, scene: bool) -> str:
    """Hash-based unique markings for any fallback droid."""
    h = int(hashlib.md5(slug.encode()).hexdigest()[:8], 16)
    panels = []
    for i in range(4):
        px = 170 + ((h >> (i * 4)) & 0xF) * 8
        py = 200 + ((h >> (i * 4 + 2)) & 0xF) * 6
        pw = 18 + ((h >> (i * 2)) & 0x7) * 2
        panels.append(
            f'<rect fill="{accent}" opacity="0.55" stroke="{OUTLINE}" stroke-width="2" '
            f'x="{px}" y="{py}" width="{pw}" height="12" rx="3"/>'
        )
    mark = (h % 3) + 1
    return f"""
          {droid_scene_backdrop(accent, scene)}
          {_glow()}
          <rect class="fill-metal" stroke="{OUTLINE}" stroke-width="3" x="{CX-36}" y="{CY-68}" width="72" height="44" rx="10"/>
          <rect fill="{accent}" stroke="{OUTLINE}" stroke-width="3" x="{CX-32}" y="{CY-12}" width="64" height="88" rx="12"/>
          {''.join(panels)}
          <circle fill="#22c55e" cx="{CX-20 + mark * 4}" cy="{CY-48}" r="4"/>
          <circle fill="#ef4444" cx="{CX+20 - mark * 4}" cy="{CY-48}" r="4"/>
        """


# ---------------------------------------------------------------------------
# Slug -> renderer mapping (all 79 droids)
# ---------------------------------------------------------------------------

SlugRenderer = Callable[[bool], str]

SLUG_RENDERERS: dict[str, SlugRenderer] = {
    "r2-d2": lambda s: _r2_series(s, dome="#f8fafc", body="#2563eb", stripe="#dc2626"),
    "r2-q5": lambda s: _r2_series(s, dome="#111827", body="#111827", stripe="#dc2626", accent_panel="#64748b"),
    "r2-kt": lambda s: _r2_series(s, dome="#f8fafc", body="#ec4899", stripe="#dc2626", accent_panel="#f472b6"),
    "r4-p17": lambda s: _r2_series(s, dome="#dc2626", body="#991b1b", stripe="#111827", accent_panel="#ef4444", leg_stripe=False),
    "r3-s6": lambda s: _r2_series(s, dome="#eab308", body="#ca8a04", stripe="#111827", accent_panel="#fde047"),
    "r5-d4": lambda s: _r2_series(s, dome="#dc2626", body="#991b1b", stripe="#111827", accent_panel="#ef4444"),
    "r1-g4": lambda s: _r2_series(s, dome="#64748b", body="#475569", stripe="#94a3b8", accent_panel="#cbd5e1"),
    "u9-c4": lambda s: _r2_series(s, dome="#f8fafc", body="#059669", stripe="#dc2626", accent_panel="#34d399"),
    "t3-m4": lambda s: _r2_series(s, dome="#f8fafc", body="#0891b2", stripe="#eab308", accent_panel="#22d3ee"),
    "t7-o1": lambda s: _r2_series(s, dome="#f8fafc", body="#7c3aed", stripe="#eab308", accent_panel="#a78bfa"),
    "lothal-astromech": lambda s: _r2_series(s, dome="#f8fafc", body="#ea580c", stripe="#2563eb", accent_panel="#fb923c"),
    "bb-8": _bb8,
    "c-3po": lambda s: _c3po_series(s),
    "tc-14": lambda s: _c3po_series(s, gold="#cbd5e1"),
    "l3-37": _l3,
    "0-0-0": _000,
    "ap-5": lambda s: _c3po_series(s, gold="#94a3b8", wire=False),
    "ra-7": lambda s: _c3po_series(s, gold="#111827"),
    "cl-4d-4": lambda s: _c3po_series(s, gold="#64748b", wire=False),
    "s-0d": lambda s: _c3po_series(s, gold="#475569", wire=True),
    "b-4d4": lambda s: _c3po_series(s, gold="#eab308", wire=False),
    "k-2so": _k2so,
    "kx-security-droid": _k2so,
    "chopper": _chopper,
    "hk-47": lambda s: _hk_series(s, label="HK-47"),
    "hk-50": lambda s: _hk_series(s, label="HK-50"),
    "hk-51": lambda s: _hk_series(s, label="HK-51"),
    "ig-88": lambda s: _ig_series(s, dark=True),
    "ig-11": lambda s: _ig_series(s, dark=False),
    "c-21-highsinger": lambda s: _ig_series(s, dark=False),
    "bt-1": _bt1,
    "bd-1": _bd1,
    "b1-battle-droid": lambda s: _b1(s),
    "bx-commando-droid": lambda s: _b1(s, command=True),
    "oom-command-battle-droid": lambda s: _b1(s, command=True),
    "fa-4-pilot-droid": lambda s: _b1(s),
    "firefighter-b1": lambda s: _b1(s, firefighter=True),
    "rocket-battle-droid": lambda s: _b1(s, rocket=True),
    "lr-57-combat-droid": lambda s: _b1(s),
    "aqua-droid": _aqua,
    "crab-droid": _crab,
    "war-droid-mark-iv": lambda s: _b1(s, command=True),
    "b2-super-battle-droid": lambda s: _b2(s),
    "b3-ultra-battle-droid": lambda s: _b2(s, ultra=True),
    "droideka": lambda s: _droideka(s),
    "scorpenek-annihilator": lambda s: _droideka(s, scorpenek=True),
    "magnaguard": _magnaguard,
    "tactical-droid": lambda s: _tactical(s),
    "super-tactical-droid": lambda s: _tactical(s, super_droid=True),
    "oom-9": lambda s: _tactical(s, super_droid=True),
    "vulture-droid": _vulture,
    "probe-droid": lambda s: _probe(s),
    "id-9-seeker-droid": lambda s: _probe(s, seeker=True),
    "it-o": _ito,
    "mark-vii-inquisitor-droid": _ito,
    "2-1b": lambda s: _medical(s),
    "fx-7": lambda s: _medical(s, fx=True),
    "mse-6-mouse-droid": lambda s: _mouse(s),
    "mse-14": lambda s: _mouse(s, imperial=True),
    "gnk-power-droid": _gonk,
    "pit-droid": _pit,
    "ric-920": _pit,
    "dark-trooper": _dark_trooper,
    "d-o": _do_droid,
    "g0-t0": _g0t0,
    "4-lom": _4lom,
    "ev-9d9": lambda s: _4lom(s),
    "8d8": lambda s: _ig_series(s, dark=True),
    "buzz-droid": _buzz,
    "hailfire-droid": lambda s: _artillery(s),
    "dwarf-spider-droid": lambda s: _artillery(s, spider=True),
    "octuptarra-droid": lambda s: _artillery(s, oct=True),
    "tt-8l-gatekeeper": _gatekeeper,
    "asp-7-labor-droid": lambda s: _labor(s),
    "wed-treadwell": lambda s: _labor(s, treadwell=True),
    "asn-courier-droid": lambda s: _labor(s),
    "pk-worker-droid": lambda s: _labor(s),
    "j9-worker-droid": lambda s: _labor(s),
    "proxy": _proxy,
}


def droid_body(entry: dict, scene: bool) -> str:
    slug = entry["slug"]
    accent = entry["color"]
    name = entry["name"]
    dtype = entry["droid_type"]
    renderer = SLUG_RENDERERS.get(slug)
    if renderer:
        body = renderer(scene)
    else:
        body = _unique_variant(slug, entry.get("silhouette", "biped"), accent, scene)
    return _scene_wrap(body, scene, accent, name, dtype)


def droid_portrait_svg(entry: dict) -> str:
    slug = entry["slug"]
    return svg_wrap(entry["name"], entry["color"], droid_body(entry, False), slug)


def droid_scene_svg(entry: dict) -> str:
    slug = entry["slug"]
    return svg_wrap(f"{entry['name']} — scene", entry["color"], droid_body(entry, True), f"{slug}-scene")
