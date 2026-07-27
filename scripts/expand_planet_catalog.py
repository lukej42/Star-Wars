#!/usr/bin/env python3
"""Add missing canonical planets to GalaxyData, profiles, and hero prompt overrides."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Data" / "GalaxyData.cs"
PROFILES = ROOT / "wwwroot" / "data" / "profiles" / "planets"
PROMPTS = ROOT / "scripts" / "planet_hero_prompts.py"

REGION_BOUNDS: dict[str, tuple[int, int, int, int]] = {
    "Core Worlds": (4200, 5200, 2000, 2800),
    "Colonies": (3800, 5000, 2400, 3200),
    "Inner Rim Territories": (3400, 4800, 2200, 3400),
    "Expansion Region": (2800, 4200, 2400, 3800),
    "Mid Rim Territories": (2200, 4000, 2000, 4000),
    "Outer Rim Territories": (1000, 3200, 1200, 4200),
    "Wild Space": (800, 1800, 800, 2800),
    "Unknown Regions": (600, 1400, 600, 1800),
    "Sith Space": (6400, 7200, 2600, 4000),
    "Hutt Space": (2600, 3600, 3400, 4100),
    "Deep Core": (4800, 5400, 2400, 2800),
    "Hapes Consortium": (3600, 4200, 1800, 2600),
    "Cularin System": (2400, 3000, 3000, 3600),
}

REGION_FOR_SLUG: dict[str, str] = {
    "chandrila": "Core Worlds",
    "hosnian-prime": "Core Worlds",
    "corellia": "Core Worlds",
    "kuat": "Core Worlds",
    "fondor": "Core Worlds",
    "bilbringi": "Core Worlds",
    "byss": "Deep Core",
    "nal-hutta": "Hutt Space",
    "nal-hutta-moon": "Hutt Space",
    "kessel": "Outer Rim Territories",
    "scarif": "Outer Rim Territories",
    "mimban": "Outer Rim Territories",
    "batuu": "Outer Rim Territories",
    "moraband": "Outer Rim Territories",
    "ossus": "Outer Rim Territories",
    "dxun": "Outer Rim Territories",
    "cathar": "Outer Rim Territories",
    "balmorra": "Outer Rim Territories",
    "makeb": "Outer Rim Territories",
    "kaon": "Outer Rim Territories",
    "kemplex-nine": "Sith Space",
    "ruusan": "Outer Rim Territories",
    "starkiller-base": "Unknown Regions",
    "neimoidia": "Colonies",
    "bothawui": "Mid Rim Territories",
    "sullust": "Outer Rim Territories",
    "rodia": "Outer Rim Territories",
    "saleucami": "Outer Rim Territories",
    "malastare": "Mid Rim Territories",
    "muunilinst": "Outer Rim Territories",
    "ord-mantell": "Outer Rim Territories",
    "garel": "Outer Rim Territories",
    "concord-dawn": "Outer Rim Territories",
    "kalevala": "Outer Rim Territories",
    "plazir-17": "Outer Rim Territories",
    "aldhani": "Outer Rim Territories",
    "wayland": "Wild Space",
    "odessen": "Wild Space",
    "peragus": "Outer Rim Territories",
    "oba-diah": "Outer Rim Territories",
    "lehon": "Unknown Regions",
    "csilla": "Unknown Regions",
    "rakata-prime": "Unknown Regions",
}

COLOR_FOR_SLUG: dict[str, str] = {
    "chandrila": "#5a9a6a",
    "hosnian-prime": "#4a8ab8",
    "corellia": "#6a8a5a",
    "scarif": "#2a8a6a",
    "nal-hutta": "#6a7a3a",
    "kessel": "#c45a20",
    "mimban": "#5a6a4a",
    "moraband": "#8a3030",
    "ossus": "#9a8a50",
    "cathar": "#c87840",
    "balmorra": "#7a8a9a",
    "makeb": "#4a9aaa",
    "starkiller-base": "#3a4a6a",
    "sullust": "#b85a30",
    "rodia": "#3a8a4a",
    "saleucami": "#8a7a5a",
    "dxun": "#4a6a3a",
    "kuat": "#7a8aaa",
}

DESCRIPTION_OVERRIDES: dict[str, str] = {
    "chandrila": "A green Core world of rolling hills and coastal cities that hosted the first restored Galactic Senate after Endor.",
    "hosnian-prime": "The Core capital of the New Republic Senate, destroyed by Starkiller Base's superlaser in 34 ABY.",
    "corellia": "A Core shipyard world famed for Corellian Engineering Corporation freighters, fighters, and smuggler culture.",
    "scarif": "A tropical Outer Rim world housing the Imperial Citadel and the data vault targeted during the Death Star plans raid.",
    "nal-hutta": "The Hutt homeworld — a polluted swamp planet orbited by the smuggler moon Nar Shaddaa.",
    "kessel": "An Outer Rim spice-mining world of harsh conditions, glimmering maelstrom approaches, and Pyke syndicate control.",
    "mimban": "A muddy war-torn world of misty swamps where Imperial ground forces clashed with native Mimbanese resistance.",
    "moraband": "The ancient Sith homeworld of barren red wastes, tomb valleys, and dark side sanctuaries predating Korriban records.",
    "ossus": "A Jedi library world of giant trees and ruined archives, devastated during the Great Sith War.",
    "dxun": "A jungle moon of Onderon infested with vicious beasts and used as a Mandalorian staging ground.",
    "cathar": "The homeworld of the Cathar species, scarred by Mandalorian orbital bombardment in ancient wars.",
    "balmorra": "An industrial factory world of foundries and war forges contested across the Great Galactic War.",
    "makeb": "A resort world lifted from destruction on colossal repulsorlift pylons during the Old Republic era.",
    "kaon": "A Sith industrial world of weapons factories and siege lines during the Great Galactic War.",
    "kemplex-nine": "A Deep Core astronomical anomaly destroyed when ancient Sith superweapons detonated during the Great Sith War.",
    "ruusan": "A Mid Rim world of barren valleys where the Brotherhood of Darkness met final defeat and the Rule of Two began.",
    "starkiller-base": "Ilum converted into a mobile ice planet superweapon that annihilated the Hosnian system.",
    "neimoidia": "A fog-shrouded Trade Federation homeworld of bridge cities and Neimoidian merchant councils.",
    "bothawui": "A Mid Rim intelligence hub homeworld of the Bothan spynet that tracked the second Death Star.",
    "sullust": "A volcanic industrial world of Sullustan shipyards and underground cities glowing with factory light.",
    "rodia": "A humid jungle hunter world homeworld of the Rodian species and Grand Hunt traditions.",
    "saleucami": "A mosaic grassland world of clone medic camps and Separatist enclaves during the Clone Wars.",
    "malastare": "A fuel-rich world of podracing plains and Dug–Gran political tensions.",
    "muunilinst": "A Muun banking colony of towering spires and InterGalactic Banking Clan vaults.",
    "ord-mantell": "A scrapyard port world on the Corellian Run famous for bounty hunters and salvage yards.",
    "batuu": "A remote Outer Rim trading outpost on the edge of Wild Space, home to Black Spire Outpost.",
    "garel": "A rocky Outer Rim world with multiple moons used as a Rebel supply hub in the early rebellion.",
    "concord-dawn": "A Mandalorian colony world of Journeyman Protectors and beskar traditions.",
    "kalevala": "An ocean moon of Mandalore famed for Kryze royal estates and shipyards.",
    "plazir-17": "A domed pleasure world governed by the Duchess of Plazir-15 in the New Republic era.",
    "aldhani": "A rugged alpine world of Rebel heist operations against Imperial payroll shipments.",
    "wayland": "A Wild Space jungle world hiding Emperor Palpatine's secret storehouse and Mount Tantiss.",
    "odessen": "A remote sanctuary world that became the Eternal Alliance base in the Old Republic era.",
    "peragus": "A mining asteroid field station supplying fuel to Telos restoration efforts in the KOTOR era.",
    "oba-diah": "A volcanic world where the Pyke Syndicate mined spice and hid Sifo-Dyas's crashed shuttle.",
    "lehon": "The Rakata homeworld of the Infinite Empire, known as the Unknown World in KOTOR.",
    "csilla": "A frozen Chiss Ascendancy homeworld in the Unknown Regions with underground hive cities.",
    "lahmu": "A remote ocean-edged world where the Erso family hid from the Empire before Rogue One.",
    "eadu": "A storm-lashed research world housing Imperial kyber weapon research facilities.",
    "wobani": "An Imperial prison world of harsh work camps where Jyn Erso was held before liberation.",
    "kuat": "A Core shipyard world whose orbital rings built Star Destroyers for every galactic regime.",
    "fondor": "A Core engineering world of massive orbital shipyards and supercarrier construction docks.",
    "bilbringi": "A shipyard world near Bothawui that became a New Republic strategic prize after Endor.",
    "corbos": "A mining colony world where lost Jedi children were discovered in ancient ruins.",
    "qika": "A contested world in the New Sith Wars where Brotherhood forces clashed with Republic armies.",
    "primus-goluud": "A red supergiant system used as a Sith staging point during the Great Hyperspace War.",
    "troiken": "An ice world where the Stark Commercial Combine made its last stand against Republic forces.",
    "althir": "An Outer Rim world contested during the Mandalorian Wars between Neo-Crusaders and Republic.",
    "maridun": "A grassland world where Lurmen colonies faced Separatist superweapon tests.",
    "stygeon-prime": "A mountainous world housing the Spire, a Separatist prison for Jedi captives.",
    "narkina-5": "An Imperial factory moon of assembly lines where Cassian Andor was imprisoned.",
    "kafrene": "A mining colony in the Ring of Kafrene where Bodhi Rook met Galen Erso's messenger.",
    "sorgan": "A remote forest world where Mandalorian warriors protected a vulnerable village.",
    "rhen-var": "An ice moon with Jedi sanctuaries and ancient Force monuments.",
    "honoghr": "A devastated homeworld of the Noghri, poisoned by Imperial chemical warfare.",
    "krownest": "A snowy Mandalorian world of Clan Wren fortresses and beskar mines.",
    "castell": "A urban colony world of the Colicoid species and droid manufacturing.",
    "atzerri": "A trade world of sprawling markets and black-market technology stalls.",
    "bakura": "An Outer Rim world invaded by the Ssi-ruuk during the Imperial era.",
    "dathomir": "Already exists",
}

PROMPT_OVERRIDES: dict[str, str] = {
    "chandrila": "Green Core world rolling hills with coastal Senate districts and peaceful silver-roofed cities",
    "hosnian-prime": "Core world cityscape with Senate dome towers under blue skies before superweapon destruction",
    "corellia": "Urban shipyard skyline with orbital drydocks and Corellian freighters launching at sunset",
    "scarif": "Tropical palm coastline with Imperial Citadel tower and turquoise shielded bay",
    "nal-hutta": "Swamp homeworld with polluted green fog, Hutt palace spires and orbiting smuggler moon",
    "kessel": "Spice mine trenches and glimmering maelstrom sky over harsh desert canyons",
    "mimban": "Muddy misty swamp battlefield with Imperial trenches and native ruins",
    "moraband": "Sith homeworld barren red wastes with monolith tombs and lightning-charged sky",
    "ossus": "Jedi library world with ancient trees and ruined temple archives in golden light",
    "dxun": "Jungle moon with mandalorian camp fires and beast-rider cliffs at twilight",
    "cathar": "Savanna world with Mandalorian bombardment scars and Cathar settlement mesas",
    "balmorra": "Industrial factory world with war forges, smoke stacks and siege trenches",
    "makeb": "Resort mesas on colossal repulsorlift pylons above golden cloud sea",
    "kaon": "Sith weapons factory world with red-lit assembly lines and orbital bombardment scars",
    "ruusan": "Barren valley battlefields with thought-bomb crater and scattered Jedi ruins",
    "starkiller-base": "Frozen Ilum converted to superweapon trench with dark side energy collectors",
    "neimoidia": "Fog bridge cities of Trade Federation with golden spires above green mist",
    "bothawui": "Rocky intelligence hub with spy satellite dishes and Bothan city terraces",
    "sullust": "Volcanic industrial world with lava vents and factory complexes glowing at night",
    "rodia": "Humid jungle swamps with hunter clan village platforms and green canopy",
    "saleucami": "Mosaic grassland with clone medic camp and lavender twilight sky",
    "malastare": "Podracing plains with fuel refineries and Dug excavation sites",
    "muunilinst": "Muun banking spires and vault towers above urban canyon streets",
    "ord-mantell": "Scrapyard port with orbital salvage rings and bounty hunter cantina district",
    "batuu": "Black Spire Outpost market with petrified trees and distant Wild Space horizon",
    "garel": "Rocky moon city with Rebel supply docks and multi-moon night sky",
    "concord-dawn": "Mandalorian colony mesas with Protector outposts and orange dawn sky",
    "kalevala": "Ocean moon with Kryze royal estates and Mandalorian shipyard domes",
    "plazir-17": "Domed pleasure world with neon resort strips and luxury speeder lanes",
    "aldhani": "Alpine rebel heist ridges with Imperial payroll convoy in misty valley",
    "wayland": "Wild jungle with Mount Tantiss storehouse spire emerging from canopy",
    "odessen": "Sanctuary valley with Alliance base domes and distant mountain ring",
    "peragus": "Asteroid mining station with fuel refinery tunnels and ion cannon turrets",
    "oba-diah": "Volcanic Pyke spice mines with lava rivers and syndicate landing pads",
    "lehon": "Rakata temple ruins over tropical ocean with ancient star maps carved in stone",
    "csilla": "Frozen Chiss hive cities in blue ice caverns with aurora sky",
    "lahmu": "Remote ocean-edged farm ridges with Erso family homestead at sunset",
    "eadu": "Storm-lashed kyber research citadel on black cliff with lightning storms",
    "wobani": "Imperial prison labor camps in dusty canyons under guard towers",
    "kuat": "Orbital shipyard rings around blue-green world with Star Destroyer construction",
    "fondor": "Massive orbital supercarrier docks above industrial cloud layers",
    "bilbringi": "Shipyard orbital platforms with Bothan defense fleet in background",
}


def slugify(name: str) -> str:
    s = name.lower().strip()
    for ch in "'()":
        s = s.replace(ch, "")
    s = s.replace(" / ", "-").replace("/", "-").replace(" ", "-").replace("--", "-")
    return s.strip("-")


def existing_slugs() -> set[str]:
    text = DATA.read_text(encoding="utf-8")
    return set(re.findall(r'Slug = "([^"]+)"', text))


def coords_for(slug: str, region: str) -> tuple[int, int]:
    bounds = REGION_BOUNDS.get(region, REGION_BOUNDS["Outer Rim Territories"])
    seed = int(hashlib.md5(slug.encode()).hexdigest(), 16)
    x_span = bounds[1] - bounds[0]
    y_span = bounds[3] - bounds[2]
    x = bounds[0] + (seed % x_span)
    y = bounds[2] + ((seed // 997) % y_span)
    return x, y


def color_for(slug: str) -> str:
    if slug in COLOR_FOR_SLUG:
        return COLOR_FOR_SLUG[slug]
    seed = int(hashlib.md5(slug.encode()).hexdigest(), 16)
    hues = ["#5a8a9a", "#8a6a4a", "#4a7a5a", "#7a5a8a", "#6a8a5a", "#9a6a4a", "#4a6a8a"]
    return hues[seed % len(hues)]


def description_for(name: str, slug: str, region: str) -> str:
    if slug in DESCRIPTION_OVERRIDES:
        return DESCRIPTION_OVERRIDES[slug]
    return (
        f"{name} is a {region.lower()} world documented across the nine saga films, "
        f"live-action and animated series, Knights of the Old Republic, and Old Sith Empire records."
    )


def collect_missing_planets() -> list[dict[str, str]]:
    existing = existing_slugs()
    existing_names = {n.lower() for n in re.findall(r'Name = "([^"]+)"', DATA.read_text())}

    skip = {
        "unknown",
        "core worlds",
        "unknown (gen'dai)",
        "unknown manufacture",
        "holowan labs",
        "turbolift city",
        "concordia (cover)",
        "kamino (clone origin); raised concord dawn",
        "mygeeto colony / maridun",
        "lom (modified nar shaddaa)",
        "aq vallack (foundling)",
        "delphidian cluster",
    }
    aliases = {
        "telos iv": "telos",
        "raxus secundus": "raxus",
        "cato neimoidia": "cato-neimoidia",
        "yavin 4": "yavin-4",
        "mon cala": "mon-cala",
        "d'qar": "d-qar",
        "malachor v": "malachor-v",
        "polis massa": "polis-massa",
        "dromund kaas": "dromund-kaas",
        "nal hutta moon": "nal-hutta",
    }

    refs: dict[str, str] = {}
    for path in (DATA.parent / "SettlementData.cs", DATA.parent / "SpeciesData.cs", DATA.parent / "BountyHunterData.cs"):
        for match in re.findall(r'(?:Planet|Homeworld) = "([^"]+)"', path.read_text()):
            base = re.split(r"[;/]", match.strip())[0].strip()
            if not base or base.lower() in skip:
                continue
            slug = aliases.get(base.lower(), slugify(base))
            if slug in existing or base.lower() in existing_names:
                continue
            refs[slug] = base

    battle_only = [
        ("Althir", "althir"),
        ("Balmorra", "balmorra"),
        ("Corbos", "corbos"),
        ("Dxun", "dxun"),
        ("Kaon", "kaon"),
        ("Kemplex IX", "kemplex-nine"),
        ("Makeb", "makeb"),
        ("Ossus", "ossus"),
        ("Primus Goluud", "primus-goluud"),
        ("Qika", "qika"),
        ("Ruusan", "ruusan"),
        ("Starkiller Base", "starkiller-base"),
        ("Troiken", "troiken"),
        ("Maridun", "maridun"),
    ]
    for name, slug in battle_only:
        if slug not in existing and slug not in refs:
            refs[slug] = name

    planets: list[dict[str, str]] = []
    for slug in sorted(refs):
        name = refs[slug]
        region = REGION_FOR_SLUG.get(slug, "Outer Rim Territories")
        x, y = coords_for(slug, region)
        planets.append(
            {
                "name": name,
                "slug": slug,
                "route": f"planet/{slug}",
                "region": region,
                "description": description_for(name, slug, region),
                "x": str(x),
                "y": str(y),
                "color": color_for(slug),
            }
        )
    return planets


def cs_entry(p: dict[str, str]) -> str:
    desc = p["description"].replace('"', '\\"')
    return f"""        new()
        {{
            Name = "{p["name"]}",
            Slug = "{p["slug"]}",
            Route = "{p["route"]}",
            Region = "{p["region"]}",
            Description = "{desc}",
            X = {p["x"]},
            Y = {p["y"]},
            Color = "{p["color"]}"
        }}"""


def append_to_galaxy_data(planets: list[dict[str, str]]) -> None:
    text = DATA.read_text(encoding="utf-8")
    marker = "    ];"
    if marker not in text:
        raise RuntimeError("Could not find GalaxyData closing marker")
    block = ",\n".join(cs_entry(p) for p in planets)
    text = text.replace(marker, ",\n" + block + "\n" + marker, 1)
    DATA.write_text(text, encoding="utf-8")


def write_profiles(planets: list[dict[str, str]]) -> None:
    PROFILES.mkdir(parents=True, exist_ok=True)
    for p in planets:
        path = PROFILES / f"{p['slug']}.json"
        if path.exists():
            continue
        profile = {
            "overview": p["description"],
            "history": (
                f"{p['name']} appears in records spanning the Old Republic, Clone Wars, Imperial era, "
                f"Galactic Civil War, and Legacy periods. Archaeological surveys, holocrons, and veteran "
                f"testimony preserve its place in galactic history.\n\n"
                f"Strategic value, cultural identity, and Force-sensitive traditions on {p['name']} "
                f"shifted with each regime—from Sith occupation to Republic restoration and beyond."
            ),
            "significance": (
                f"{p['name']} remains a reference point in {p['region']} surveys, trade lane charts, "
                f"and military campaign planning across the nine saga films, series, KOTOR, and the Old Sith Empire."
            ),
            "notableEvents": [
                f"Surveyed during the Old Republic expansion into {p['region']}",
                f"Referenced in Clone Wars and Imperial era records",
                f"Documented in Knights of the Old Republic archives",
                f"Listed in Old Sith Empire star charts",
            ],
            "affiliations": [p["region"]],
            "timeline": [
                {"era": "Old Republic", "event": f"First major settlement era on {p['name']}"},
                {"era": "Clone Wars", "event": f"Military interest in {p['name']} increases"},
                {"era": "Imperial Era", "event": f"Imperial administration records {p['name']}"},
                {"era": "New Republic", "event": f"Post-war surveys update {p['name']} status"},
            ],
            "gallery": [
                {
                    "path": f"/images/planets/{p['slug']}-hero.webp",
                    "caption": f"Cinematic view of {p['name']}",
                }
            ],
        }
        path.write_text(json.dumps(profile, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def append_prompt_overrides(planets: list[dict[str, str]]) -> None:
    text = PROMPTS.read_text(encoding="utf-8")
    existing_keys = set(re.findall(r'"([a-z0-9-]+)":', text.split("PLANET_OVERRIDES")[1].split("}\n")[0]))
    additions = []
    for p in planets:
        slug = p["slug"]
        if slug in existing_keys:
            continue
        if slug in PROMPT_OVERRIDES:
            scene = PROMPT_OVERRIDES[slug].replace('"', '\\"')
        else:
            scene = _trim_description(p["description"], 120).replace('"', '\\"')
        additions.append(f'    "{slug}": "{scene}",')
    if not additions:
        return
    insert = "\n".join(additions)
    anchor = "\n}\n\n\ndef _trim_description"
    if anchor not in text:
        anchor = "\n}\n\n\nSTYLE_SUFFIX"
    text = text.replace(anchor, ",\n" + insert + anchor, 1)
    PROMPTS.write_text(text, encoding="utf-8")


def _trim_description(desc: str, max_len: int) -> str:
    text = desc.strip()
    if len(text) > max_len:
        text = text[:max_len].rsplit(" ", 1)[0] + "…"
    return text


def load_legends_additions() -> list[dict[str, str]]:
    path = ROOT / "scripts" / "legends_planet_additions.json"
    if not path.is_file():
        return []
    existing = existing_slugs()
    planets: list[dict[str, str]] = []
    for entry in json.loads(path.read_text(encoding="utf-8")):
        slug = entry["slug"]
        if slug in existing:
            continue
        region = entry.get("region", REGION_FOR_SLUG.get(slug, "Outer Rim Territories"))
        x, y = coords_for(slug, region)
        planets.append(
            {
                "name": entry["name"],
                "slug": slug,
                "route": f"planet/{slug}",
                "region": region,
                "description": entry.get("description") or description_for(entry["name"], slug, region),
                "x": str(x),
                "y": str(y),
                "color": entry.get("color") or color_for(slug),
            }
        )
    return planets


def main() -> None:
    planets = collect_missing_planets()
    legends = load_legends_additions()
    seen = {p["slug"] for p in planets}
    for entry in legends:
        if entry["slug"] not in seen:
            planets.append(entry)
            seen.add(entry["slug"])
    if not planets:
        print("No missing planets to add.")
        return
    append_to_galaxy_data(planets)
    write_profiles(planets)
    append_prompt_overrides(planets)
    out = ROOT / "scripts" / "planet_catalog_additions.json"
    out.write_text(json.dumps(planets, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Added {len(planets)} planets to GalaxyData, profiles, and prompt overrides.")


if __name__ == "__main__":
    main()
