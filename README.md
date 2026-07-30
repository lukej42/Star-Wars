# Star Wars Worlds

An interactive Star Wars encyclopedia built with **Blazor WebAssembly**. Browse galactic history, chronicles, governments, factions, characters, Jedi, Sith, planets, starships, droids, species, bounty hunters, settlements, military units, wars and conflicts, and Force powers across the saga — from the films and series to *Knights of the Old Republic* and *The Old Republic* — with rich detail pages, cinematic hero banners, related-archive cross-links, an explorable galaxy map, a multi-row timeline chart, and responsive sidebar navigation.

## Features

| Section | Count | Description |
|---------|------:|-------------|
| **Galaxy Map** | 100 worlds | Pan, zoom, and search an interactive map of the galaxy. Click any marker for a quick preview and jump to the full planet page. |
| **Timelines** | 8 eras | Full galactic chronology with a multi-row interactive time chart — Major Events, Republic Era, High Republic, Clone Wars, Imperial Era, New Republic, First Order Era, and Legends. |
| **Chronicles** | 10 | Narrative galactic-history eras from the Dawn of the Jedi through the New Jedi Order — extended profiles with linked major events, factions, characters, planets, and ships. |
| **Governments** | 13 | Governing bodies and councils (Galactic Senate, Dark Council, Separatist Parliament, Hutt Grand Council, and others) with detail pages and cinematic hero banners. |
| **Factions** | 11 | Major galactic powers and syndicates with cinematic heroes and full profiles — Republic, Confederacy, Empire, Rebel Alliance, New Republic, Hutts, Sith Empire, First Order, Resistance, Mandalorians, and Trade Federation. |
| **Military Units** | 100 | Army and navy formations across 11 faction militaries — stormtrooper corps, droid armies, starfighter wings, capital ships, and more. |
| **Wars & Conflicts** | 10 wars · 59 battles | Major galactic wars with linked famous battle detail pages. |
| **Characters** | 104 | Heroes, villains, leaders, and supporting figures from across the saga (excluding dedicated Jedi/Sith directories). |
| **Jedi Directory** | 47 | Jedi Masters, Knights, and Padawans with rank, history, and legacy — including *KOTOR* / *TOR* figures such as Revan, Bastila Shan, Satele Shan, and Meetra Surik. |
| **Sith Directory** | 34 | Sith Lords and dark-side figures from the Rule of Two through the Old Republic era. |
| **Planets** | 1,489 | Worlds with region, atlas coordinates, environment, culture, and timeline. |
| **Ships** | 126 | Starships and vehicles with class, era, production counts, and scene illustrations. |
| **Droids** | 79 | Astromechs, protocol units, battle droids, and iconic mechanical characters. |
| **Species** | 103 | Sentient and notable species with homeworlds, traits, and saga appearances. |
| **Bounty Hunters** | 116 | Hunters, mercenaries, and guns-for-hire from the underworld and beyond. |
| **Cities & Settlements** | 115 | Cities, spaceports, temples, and other locations across the galaxy. |
| **The Force** | 8 topics · 7 forms | Force philosophy, kyber crystals, lightsaber construction, and the seven classic lightsaber forms. |
| **Force Powers** | 74 | Light-side, dark-side, and neutral Force abilities with lore and usage notes. |

Each directory entry includes a summary card in the index view and a full detail page with overview, history, significance, notable events, affiliations, timeline, and image gallery where profile data is available. Many detail pages also include a **Related Archives** section — thumbnail cross-links to factions, characters, planets, ships, chronicles, governments, and other connected entries.

### Galactic History (Chronicles)

The **Chronicles** section (`/chronicles`) provides a narrative history of the galaxy across ten major epochs:

1. Dawn of the Jedi
2. Sith Empire
3. Old Republic
4. High Republic
5. Fall of the Republic
6. Reign of the Empire
7. Age of Rebellion
8. New Republic
9. Rise of the First Order
10. New Jedi Order

The **Galactic History** index (`/chronicles/galactic-history`) links to each era. Chronicle detail pages use `DirectoryDetailShell` with:

- A cinematic hero banner and date-range meta line
- **Government** and **Head of State** linked fields in the hero intro (e.g. Galactic Senate / Supreme Chancellor; Dark Council / Sith Emperor)
- Rich markdown overview, history, and significance sections
- **Major events** with optional route links
- **Key factions**, **Major characters** (four per column), **Planets**, and **Ships** linked lists
- Films, series, games, and books where applicable
- **Related Archives** cross-links at the foot of the page

Chronicle data is authored in `scripts/chronicle_profile_data.py` and generated via `generate_chronicle_profiles.py`.

### Governments

Government detail pages (`/governments/{slug}`) cover the major political institutions referenced by chronicles and factions:

| Government | Era |
|------------|-----|
| Je'daii Order | Pre-Republic |
| Dark Council | Sith Empire |
| Galactic Senate | Galactic Republic |
| Imperial Ruling Council | Galactic Empire |
| Alliance Civil Government | Rebel Alliance |
| New Republic Senate | New Republic |
| First Order Supreme Council | First Order |
| Jedi High Council | New Jedi Order |
| Separatist Parliament | Confederacy |
| Hutt Grand Council | Hutt Cartel |
| Resistance High Command | Resistance |
| Mandalorian Clans | Mandalorian culture |
| Trade Federation Directorate | Trade Federation |

Each government page includes overview, history, significance, timeline, gallery, and Related Archives cross-links. Hero images are **1536×1024 `.webp` cinematic banners** at `/images/governments/{slug}-scene.webp`.

### Timelines

The **Full Timeline** page (`/timelines`) provides:

- A cinematic directory hero banner spanning galactic history
- A **multi-row time chart** (`GalacticTimelineChart`) — one row per era with colour-coded bars, date ranges, and axis ticks from 25,000 BBY through 34 ABY
- A piecewise scale that compresses deep time and expands the modern era for readability
- Clickable era rows linking to detailed timeline pages
- A grid of all eight historic periods below the chart

Timeline detail pages cover Major Events, Republic Era, High Republic, Clone Wars, Imperial Era, New Republic, First Order Era, and Legends Timeline — each with extended profile content and a cinematic hero banner.

### Factions

Faction pages use the same modern detail layout as characters and Jedi (`DirectoryDetailShell`). Each of the 11 factions includes:

- A cinematic `.webp` hero banner
- Extended profile JSON (overview, history, significance, events, affiliations, timeline)
- Meta line showing years active, capital, and government *type*
- **Head of Government** and **Head of State** linked fields in the hero intro (e.g. Galactic Senate / Supreme Chancellor; Dark Council / Sith Emperor)
- SVG emblem assets in the gallery (via `generate_faction_logos.py`)
- **Related Archives** cross-links

Governance mappings live in `scripts/faction_profile_enrichments.py` (`FACTION_GOVERNANCE`) and are written to profile JSON by `generate_faction_profiles.py`.

### Military Units

The **Military Units** directory (`/all-military-units`) organises **100 units** across **11 faction militaries**, each split into **Army** and **Navy** branches:

- Galactic Republic, Confederacy, Galactic Empire, Rebel Alliance, New Republic, First Order, Resistance, Mandalorian, Sith Empire, Old Republic, and Other

Routes follow `/military-units/{faction-slug}`, `/military-units/{faction-slug}/army`, `/military-units/{faction-slug}/navy`, and per-unit detail pages. Unit pages include cinematic army/navy hero banners (`{faction-slug}-army-hero.webp` / `{faction-slug}-navy-hero.webp` for listings; per-unit heroes for individual entries).

### Wars & Conflicts

The **Wars & Conflicts** section covers **10 major wars** (Clone Wars, Galactic Civil War, Mandalorian Wars, Great Galactic War, and others) with **59 famous battle** detail pages under `/wars-conflicts/battles/{slug}`. War and battle pages include cinematic hero banners and Related Archives cross-links.

### Related Archives (cross-links)

A site-wide **cross-link graph** connects related entries across directories. `EntityCrossLinkService` loads pre-built link data from `wwwroot/data/cross-links.json` (generated by `scripts/generate_cross_links.py` / `cross_link_builder.py`).

Cross-links appear as **Related Archives** thumbnail cards on detail pages for chronicles, factions, governments, ships, species, settlements, military units, Force powers, lightsaber forms, wars, and battles. `CrossLinkImageResolver` and `CrossLinkRouteValidator` ensure routes and hero thumbnails resolve correctly across all categories.

Curated overrides for complex relationships (e.g. *KOTOR* Jedi/Sith cross-links) live in `scripts/related_archive_overrides.py` and `scripts/chronicle_entity_links.py`.

### Cinematic hero banners

Detail pages and directory index pages use **1536×1024 (16:9) cinematic `.webp` matte paintings** as hero banners instead of small portrait thumbnails.

| Directory | Entry hero | Index hero |
|-----------|------------|------------|
| Chronicles | `/images/chronicles/{slug}-scene.webp` | `/images/chronicles/galactic-history-directory-hero.webp` |
| Governments | `/images/governments/{slug}-scene.webp` | — |
| Characters | `/images/characters/{slug}-scene.webp` | `/images/characters/characters-directory-hero.webp` |
| Factions | `/images/factions/{slug}-scene.webp` | `/images/factions/factions-directory-hero.webp` |
| Timelines | `/images/timelines/{slug}-scene.webp` | `/images/timelines/timelines-directory-hero.webp` |
| Jedi | `/images/jedi/{slug}-scene.webp` | `/images/jedi/jedi-directory-hero.webp` |
| Sith | `/images/sith/{slug}-scene.webp` | `/images/sith/sith-directory-hero.webp` |
| Military Units | `/images/military-units/{slug}-hero.webp` | `/images/military-units/military-units-directory-hero.webp` |
| Wars & Conflicts | `/images/wars-conflicts/wars-{slug}-hero.webp` | — |
| Battles | `/images/wars-conflicts/battles-{slug}-hero.webp` | — |
| Planets | `/images/planets/{slug}-hero.webp` | `/images/planets/planets-directory-hero.webp` |
| Ships, Species, Bounty Hunters, Settlements, Force Powers, Droids | `/images/{category}/{slug}-scene.webp` | `/images/{category}/{category}-directory-hero.webp` |

Planet detail pages keep their full-page **space background** (`{slug}-space.webp`) behind the content; the hero banner replaces only the small top portrait. Legacy SVG portraits and blueprints remain in `wwwroot/images/` for reference and gallery entries, but the live UI prefers the cinematic `.webp` heroes.

### Galaxy Map

The map is built on an 8000 × 5000 coordinate system with:

- **Search** — type-ahead suggestions for all mapped worlds
- **Pan and zoom** — drag to move, toolbar controls from 20% to 600% zoom
- **Planet markers** — colour-coded by world, with click-to-preview panels
- **Deep links** — navigate straight to any planet detail page

### Navigation

The sidebar uses collapsible flyout menus for each directory, with colour-coded dots matching entry accent colours. **Chronicles** (with **Galactic History** and all ten era links) sits near the top; **Military Units** and **Wars & Conflicts** have nested faction and war flyouts. **The Force** groups philosophy topics, lightsaber forms, and Force powers. **Timelines** sits below Galaxy Map; **Factions** includes an **All Factions** index link with a grid-style icon matching other directories. On mobile, flyouts expand on tap and the menu closes after navigation.

## Tech stack

- [.NET 9](https://dotnet.microsoft.com/) with [Blazor WebAssembly](https://learn.microsoft.com/en-us/aspnet/core/blazor/)
- [Bootstrap 5](https://getbootstrap.com/) for layout and responsive styling
- Static JSON profiles served from `wwwroot/data/profiles/`
- Pre-built cross-link graph at `wwwroot/data/cross-links.json`
- Client-side routing with scoped CSS per component
- Python helper scripts under `scripts/` for catalogue generation, profile enrichment, cross-link building, and hero asset workflows

No backend server is required — the app runs entirely in the browser after the initial load.

## Prerequisites

- [.NET 9 SDK](https://dotnet.microsoft.com/download/dotnet/9.0) or later
- **Python 3** (optional) — only needed to regenerate catalogues, profiles, cross-links, or hero assets

Verify your installation:

```bash
dotnet --version
dotnet workload install wasm-tools   # required for Blazor WebAssembly builds
```

## Getting started

### Clone the repository

```bash
git clone https://github.com/lukej42/Star-Wars.git
cd Star-Wars
```

### Run locally

```bash
dotnet run
```

Then open the URL shown in the terminal (typically `https://localhost:5001` or `http://localhost:5000`).

### Build for production

```bash
dotnet publish -c Release
```

Published output is written to `bin/Release/net9.0/publish/wwwroot/` and can be deployed to any static host (Azure Static Web Apps, GitHub Pages, Netlify, etc.).

## Project structure

```
Star-Wars/
├── Components/          # DirectoryDetailShell, EntityCrossLinks, GalacticTimelineChart, …
├── Data/                # Static catalogues (ChroniclesData, GovernmentData, FactionData, …)
├── Layout/              # MainLayout and NavMenu
├── Models/              # C# record types for entries, profiles, and cross-links
├── Pages/               # Routable Blazor pages (GalacticHistory, GovernmentPage, …)
├── scripts/             # Python generators, cross-link builder, hero installers
├── Services/            # DirectoryProfileService, EntityCrossLinkService
├── wwwroot/
│   ├── css/             # Global styles (timeline chart, governance links, cross-links)
│   ├── data/
│   │   ├── profiles/    # Extended JSON content per entry
│   │   └── cross-links.json
│   └── images/          # Cinematic .webp heroes, planet space art, legacy SVG assets
├── App.razor            # Router and 404 handling
├── Program.cs           # DI and host configuration
└── Star-Wars.csproj
```

## Routes

| Route | Page | Notes |
|-------|------|-------|
| `/` | Home | Landing page |
| `/galaxy-map` | Galaxy Map | Interactive world map |
| `/chronicles` | Chronicles hub | Links to Galactic History |
| `/chronicles/galactic-history` | Galactic History index | All ten narrative eras |
| `/chronicles/galactic-history/{slug}` | Chronicle era detail | e.g. `/chronicles/galactic-history/old-republic` |
| `/governments/{slug}` | Government detail | e.g. `/governments/galactic-senate` |
| `/timelines` | Full Timeline | Multi-row galactic time chart |
| `/timelines/{slug}` | Timeline era detail | e.g. `/timelines/clone-wars` |
| `/all-factions` | Faction index | |
| `/factions/{slug}` | Faction detail | e.g. `/factions/empire` |
| `/all-military-units` | Military unit index | |
| `/military-units/{faction}` | Faction military overview | |
| `/military-units/{faction}/army` | Army listing | |
| `/military-units/{faction}/navy` | Navy listing | |
| `/military-units/{faction}/army/{unit}` | Army unit detail | |
| `/military-units/{faction}/navy/{unit}` | Navy unit detail | |
| `/wars-conflicts/{slug}` | War detail | e.g. `/wars-conflicts/clone-wars` |
| `/wars-conflicts/battles/{slug}` | Battle detail | e.g. `/wars-conflicts/battles/battle-of-yavin` |
| `/all-characters` | Character index | |
| `/characters/{slug}` | Character detail | e.g. `/characters/han-solo` |
| `/all-jedi` | Jedi index | |
| `/jedi/{slug}` | Jedi detail | e.g. `/jedi/obi-wan-kenobi` |
| `/all-sith` | Sith index | |
| `/sith/{slug}` | Sith detail | e.g. `/sith/darth-vader` |
| `/all-planets` | Planet index | |
| `/planet/{slug}` | Planet detail | e.g. `/planet/tatooine` |
| `/all-ships` | Ship index | |
| `/ships/{slug}` | Ship detail | e.g. `/ships/millennium-falcon` |
| `/all-droids` | Droid index | |
| `/droids/{slug}` | Droid detail | e.g. `/droids/r2-d2` |
| `/all-species` | Species index | |
| `/species/{slug}` | Species detail | e.g. `/species/human` |
| `/all-bounty-hunters` | Bounty hunter index | |
| `/bounty-hunters/{slug}` | Bounty hunter detail | e.g. `/bounty-hunters/boba-fett` |
| `/all-cities-settlements` | Settlement index | |
| `/settlements/{slug}` | Settlement detail | e.g. `/settlements/mos-eisley` |
| `/the-force/{slug}` | The Force topic detail | e.g. `/the-force/jedi-code` |
| `/the-force/lightsaber-forms/{slug}` | Lightsaber form detail | e.g. `/the-force/lightsaber-forms/form-v` |
| `/all-force-powers` | Force power index (all) | |
| `/all-light-side-powers` | Light-side powers index | |
| `/all-dark-side-powers` | Dark-side powers index | |
| `/force-powers/{slug}` | Force power detail | e.g. `/force-powers/force-lightning` |

Some iconic worlds also have short alias routes (e.g. `/tatooine`, `/coruscant`, `/bespin`, `/hoth`, `/mustafar`, `/dantooine`, `/naboo`, `/korriban`) that render the same planet detail view.

## Content architecture

Content is split into two layers:

1. **Catalogue data** (`Data/*.cs`) — name, slug, route, summary description, accent colour, and type-specific fields (rank, class, region, map coordinates, era dates, governance type, etc.). This is compiled into the app and drives navigation and index pages.

2. **Profile JSON** (`wwwroot/data/profiles/{category}/{slug}.json`) — extended content loaded at runtime by `DirectoryProfileService`. Each profile can include:

   ```json
   {
     "overview": "...",
     "history": "...",
     "significance": "...",
     "dateRange": "...",
     "government": { "value": "Galactic Senate", "route": "governments/galactic-senate" },
     "headOfGovernment": { "value": "Galactic Senate", "route": "governments/galactic-senate" },
     "headOfState": { "value": "Supreme Chancellor", "route": "governments/galactic-senate" },
     "majorEvents": [{ "text": "...", "route": "wars-conflicts/clone-wars" }],
     "keyFactions": [{ "label": "...", "value": "...", "route": "factions/republic" }],
     "majorCharacters": [{ "label": "...", "value": "...", "route": "jedi/yoda", "emphasized": true, "emphasisTone": "jedi" }],
     "planets": [{ "label": "...", "value": "...", "route": "planet/coruscant" }],
     "ships": [{ "label": "...", "value": "...", "route": "ships/venator-class" }],
     "notableEvents": ["..."],
     "affiliations": ["..."],
     "timeline": [{ "era": "...", "event": "..." }],
     "gallery": [{ "path": "/images/...", "caption": "..." }]
   }
   ```

   Profiles are cached in memory after the first fetch. If a profile file is missing, the detail page falls back to the summary from the catalogue data.

   Chronicle profiles use `government` + `headOfState`. Faction profiles use `headOfGovernment` + `headOfState`. Emphasized governance links render in red (Sith) or blue (Jedi) via `DirectoryDetailShell`.

3. **Cross-links** (`wwwroot/data/cross-links.json`) — pre-built Related Archives links per entity, generated from catalogue relationships and hand-authored overrides. Loaded by `EntityCrossLinkService`.

### Profile coverage

| Category | Profiles |
|----------|----------:|
| Planets | 1,489 |
| Bounty Hunters | 116 |
| Settlements | 115 |
| Characters | 104 |
| Ships | 126 |
| Species | 103 |
| Droids | 79 |
| Force Powers | 74 |
| Jedi | 47 |
| Sith | 34 |
| Factions | 11 |
| Governments | 13 |
| Chronicles | 10 |
| Timelines | 8 |

**1,141** extended profiles across all categories, plus the cross-link graph.

## Content scripts

The `scripts/` folder contains Python utilities for maintaining catalogues, profiles, cross-links, and hero images. Common workflows:

| Task | Script |
|------|--------|
| Parse C# catalogues | `parse_csharp_data.py` |
| Regenerate character catalogue + profiles | `generate_character_catalog.py` |
| Regenerate directory profile JSON | `generate_directory_profiles.py` |
| Regenerate faction profiles | `generate_faction_profiles.py` |
| Regenerate timeline profiles | `generate_timeline_profiles.py` |
| Regenerate chronicle profiles | `generate_chronicle_profiles.py` |
| Regenerate government profiles | `generate_government_profiles.py` |
| Build cross-link graph | `generate_cross_links.py`, `cross_link_builder.py` |
| Generate faction SVG emblems | `generate_faction_logos.py` |
| Generate military unit hero banners | `generate_military_unit_hero_images.py` |
| Install faction hero banners | `install_faction_heroes.py` |
| Install chronicle hero banners | `install_chronicle_heroes.py` |
| Install government hero banners | `install_government_heroes.py` |
| Install timeline hero banners | `install_timeline_heroes.py` |
| Install military unit hero banners | `install_military_unit_heroes.py`, `install_military_army_heroes.py` |
| Install wars & conflicts hero banners | `install_wars_conflicts_heroes.py` |
| Install directory hero images into `wwwroot` | `install_directory_heroes.py` |
| Install planet hero banners | `install_planet_heroes.py` |
| Install character hero banners | `install_character_heroes.py` |
| Install droid hero banners | `install_droid_heroes.py` |
| Verify hero coverage | `verify_hero_coverage.py`, `verify_planet_hero_coverage.py`, `verify_character_hero_coverage.py`, `verify_faction_hero_coverage.py`, `verify_timeline_hero_coverage.py` |
| List missing heroes | `missing_heroes.py`, `missing_planet_heroes.py`, `missing_character_heroes.py` |

Hand-authored enrichments live in `*_profile_enrichments.py`, `*_catalog_additions.py`, and dedicated data modules:

| Module | Purpose |
|--------|---------|
| `chronicle_profile_data.py` | Ten galactic-history era profiles, governance links, major events |
| `chronicle_era_links.py` | Chronicle Related Archives curation |
| `chronicle_entity_links.py` | Entity-specific chronicle cross-link rules |
| `faction_profile_enrichments.py` | Faction profiles and `FACTION_GOVERNANCE` mappings |
| `kotor_directory_enrichments.py` | *KOTOR* / *TOR* Jedi and Sith profile content |
| `related_archive_overrides.py` | Curated cross-link overrides across directories |

Hero prompt manifests live alongside the installers (`hero_manifest.json`, `planet_hero_manifest.json`, `character_hero_manifest.json`, `government_hero_manifest.json`, `military_army_hero_manifest.json`, `wars_conflicts_hero_manifest.json`) for batch image generation.

Run coverage checks from the repo root:

```bash
python3 scripts/verify_timeline_hero_coverage.py
python3 scripts/verify_faction_hero_coverage.py
python3 scripts/verify_hero_coverage.py
python3 scripts/verify_planet_hero_coverage.py
python3 scripts/verify_character_hero_coverage.py
```

Regenerate content after catalogue or enrichment changes:

```bash
python3 scripts/generate_chronicle_profiles.py
python3 scripts/generate_government_profiles.py
python3 scripts/generate_faction_profiles.py
python3 scripts/generate_cross_links.py
python3 scripts/install_government_heroes.py
python3 scripts/install_chronicle_heroes.py
```

## Adding new content

To add a new entry manually (e.g. a character):

1. Add a record to the appropriate `Data/*.cs` file with `Name`, `Slug`, `Route`, `Description`, and `Color`.
2. Create a matching JSON profile at `wwwroot/data/profiles/{category}/{slug}.json`.
3. Add a cinematic hero `.webp` under `wwwroot/images/{category}/{slug}-scene.webp` (or `{slug}-hero.webp` for planets and military units).
4. Regenerate cross-links if the entry should appear in Related Archives: `python3 scripts/generate_cross_links.py`
5. The sidebar and index pages update automatically from the catalogue data — no route registration is needed beyond the existing `{Slug}` page templates.

For bulk additions, prefer the generator scripts:

- **Characters** — `generate_character_catalog.py` merges enrichments from `character_profile_enrichments.py` and `character_catalog_additions.py`
- **Factions** — add to `FactionData.cs`, enrich via `faction_profile_enrichments.py` (including `FACTION_GOVERNANCE` for Head of Government / Head of State links), then run `generate_faction_profiles.py`
- **Chronicles** — add to `ChroniclesData.cs`, author in `chronicle_profile_data.py`, then run `generate_chronicle_profiles.py`
- **Governments** — add to `GovernmentData.cs`, add a hero prompt to `government_hero_manifest.json`, generate/install the banner, then run `generate_government_profiles.py`
- **Timelines** — add to `TimelineData.cs` (including `ChartStart` / `ChartEnd` for the time chart), enrich via `timeline_profile_enrichments.py`, then run `generate_timeline_profiles.py`
- **Jedi / Sith** — add to `JediData.cs` or `SithData.cs`, enrich via `kotor_directory_enrichments.py` or related modules, regenerate directory profiles and cross-links

For planets, also set `X` and `Y` coordinates in `GalaxyData.cs` so the world appears on the galaxy map (see `GalaxyMapSettings.cs` for the coordinate bounds). Generate or copy `{slug}-space.webp` for the full-page background and `{slug}-hero.webp` for the detail banner.

## Disclaimer

This is a fan project for educational and personal use. *Star Wars* and all related names, characters, and imagery are trademarks of Lucasfilm Ltd. This project is not affiliated with, endorsed by, or sponsored by Lucasfilm or The Walt Disney Company.
