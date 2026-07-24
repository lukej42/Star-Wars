# Star Wars Worlds

An interactive Star Wars encyclopedia built with **Blazor WebAssembly**. Browse factions, characters, Jedi, Sith, planets, starships, droids, species, bounty hunters, settlements, and Force powers across the saga — from the films and series to *Knights of the Old Republic* — with rich detail pages, cinematic hero banners, an explorable galaxy map, and a responsive sidebar navigation.

## Features

| Section | Count | Description |
|---------|------:|-------------|
| **Galaxy Map** | 66 worlds | Pan, zoom, and search an interactive map of the galaxy. Click any marker for a quick preview and jump to the full planet page. |
| **Factions** | 7 | Major galactic powers — Republic, Confederacy, Empire, Rebel Alliance, New Republic, Hutt Cartel, and the ancient Sith Empire. |
| **Characters** | 102 | Heroes, villains, leaders, and supporting figures from across the saga (excluding dedicated Jedi/Sith directories). |
| **Jedi Directory** | 42 | Jedi Masters, Knights, and Padawans with rank, history, and legacy. |
| **Sith Directory** | 34 | Sith Lords and dark-side figures from the Rule of Two through the Old Republic era. |
| **Planets** | 66 | Worlds with region, coordinates, environment, culture, and timeline. |
| **Ships** | 126 | Starships and vehicles with class, era, production counts, and scene illustrations. |
| **Droids** | 79 | Astromechs, protocol units, battle droids, and iconic mechanical characters. |
| **Species** | 103 | Sentient and notable species with homeworlds, traits, and saga appearances. |
| **Bounty Hunters** | 116 | Hunters, mercenaries, and guns-for-hire from the underworld and beyond. |
| **Cities & Settlements** | 115 | Cities, spaceports, temples, and other locations across the galaxy. |
| **Force Powers** | 74 | Light-side, dark-side, and neutral Force abilities with lore and usage notes. |

Each directory entry includes a summary card in the index view and a full detail page with overview, history, significance, notable events, affiliations, timeline, and image gallery where profile data is available.

### Cinematic hero banners

Detail pages and most directory index pages use **1536×1024 (16:9) cinematic PNG matte paintings** as hero banners instead of small portrait thumbnails. Banners are named by slug:

| Directory | Hero asset path |
|-----------|-----------------|
| Characters | `/images/characters/{slug}-scene.png` |
| Jedi, Sith, Ships, Species, Bounty Hunters, Settlements, Force Powers, Droids | `/images/{category}/{slug}-scene.png` |
| Planets | `/images/planets/{slug}-hero.png` (banner only) |

Planet detail pages keep their full-page **space background** (`{slug}-space.png`) behind the content; the hero banner replaces only the small top portrait. Legacy SVG portraits and blueprints remain in `wwwroot/images/` for reference and older gallery entries, but the live UI prefers the cinematic PNG heroes.

### Galaxy Map

The map is built on an 8000 × 5000 coordinate system with:

- **Search** — type-ahead suggestions for all 66 worlds
- **Pan and zoom** — drag to move, toolbar controls from 20% to 600% zoom
- **Planet markers** — colour-coded by world, with click-to-preview panels
- **Deep links** — navigate straight to any planet detail page

### Navigation

The sidebar uses collapsible flyout menus for each directory, with colour-coded dots matching entry accent colours. On mobile, flyouts expand on tap and the menu closes after navigation.

## Tech stack

- [.NET 9](https://dotnet.microsoft.com/) with [Blazor WebAssembly](https://learn.microsoft.com/en-us/aspnet/core/blazor/)
- [Bootstrap 5](https://getbootstrap.com/) for layout and responsive styling
- Static JSON profiles served from `wwwroot/data/profiles/`
- Client-side routing with scoped CSS per component
- Python helper scripts under `scripts/` for catalogue generation, profile enrichment, and hero asset workflows

No backend server is required — the app runs entirely in the browser after the initial load.

## Prerequisites

- [.NET 9 SDK](https://dotnet.microsoft.com/download/dotnet/9.0) or later
- **Python 3** (optional) — only needed to regenerate catalogues, profiles, or hero assets

Verify your installation:

```bash
dotnet --version
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
├── Components/          # Shared UI shells (detail pages, planet layout, hero banners)
├── Data/                # Static catalogues (characters, planets, ships, …)
├── Layout/              # MainLayout and NavMenu
├── Models/              # C# record types for entries and profiles
├── Pages/               # Routable Blazor pages
├── scripts/             # Python generators, hero installers, coverage checks
├── Services/            # DirectoryProfileService (JSON profile loader)
├── wwwroot/
│   ├── css/             # Global styles
│   ├── data/profiles/   # Extended JSON content per entry
│   └── images/          # Cinematic PNG heroes, planet space art, legacy SVG assets
├── App.razor            # Router and 404 handling
├── Program.cs           # DI and host configuration
└── Star-Wars.csproj
```

## Routes

| Route | Page | Notes |
|-------|------|-------|
| `/` | Home | Landing page |
| `/galaxy-map` | Galaxy Map | Interactive world map |
| `/factions/{slug}` | Faction detail | e.g. `/factions/empire` |
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
| `/all-force-powers` | Force power index (all) | |
| `/all-light-side-powers` | Light-side powers index | |
| `/all-dark-side-powers` | Dark-side powers index | |
| `/force-powers/{slug}` | Force power detail | e.g. `/force-powers/force-lightning` |

Some iconic worlds also have short alias routes (e.g. `/tatooine`, `/coruscant`, `/bespin`, `/hoth`, `/mustafar`, `/dantooine`, `/naboo`, `/korriban`) that render the same planet detail view.

## Content architecture

Content is split into two layers:

1. **Catalogue data** (`Data/*.cs`) — name, slug, route, summary description, accent colour, and type-specific fields (rank, class, region, map coordinates, etc.). This is compiled into the app and drives navigation and index pages.

2. **Profile JSON** (`wwwroot/data/profiles/{category}/{slug}.json`) — extended content loaded at runtime by `DirectoryProfileService`. Each profile can include:

   ```json
   {
     "overview": "...",
     "history": "...",
     "significance": "...",
     "notableEvents": ["..."],
     "affiliations": ["..."],
     "timeline": [{ "era": "...", "event": "..." }],
     "gallery": [{ "path": "/images/...", "caption": "..." }]
   }
   ```

   Profiles are cached in memory after the first fetch. If a profile file is missing, the detail page falls back to the summary from the catalogue data.

### Profile coverage

| Category | Profiles |
|----------|----------:|
| Characters | 102 |
| Jedi | 42 |
| Sith | 34 |
| Planets | 66 |
| Ships | 126 |
| Droids | 79 |
| Species | 103 |
| Bounty Hunters | 116 |
| Settlements | 115 |
| Force Powers | 74 |

## Content scripts

The `scripts/` folder contains Python utilities for maintaining catalogues, profiles, and hero images. Common workflows:

| Task | Script |
|------|--------|
| Parse C# catalogues | `parse_csharp_data.py` |
| Regenerate character catalogue + profiles | `generate_character_catalog.py` |
| Regenerate directory profile JSON | `generate_directory_profiles.py` |
| Install directory hero PNGs into `wwwroot` | `install_directory_heroes.py` |
| Install planet hero banners | `install_planet_heroes.py` |
| Install character hero banners | `install_character_heroes.py` |
| Install droid hero banners | `install_droid_heroes.py` |
| Verify hero PNG coverage | `verify_hero_coverage.py`, `verify_planet_hero_coverage.py`, `verify_character_hero_coverage.py` |
| List missing heroes | `missing_heroes.py`, `missing_planet_heroes.py`, `missing_character_heroes.py` |
| Copy generated PNGs to wwwroot | `copy_hero_png.py` |

Run coverage checks from the repo root:

```bash
python3 scripts/verify_hero_coverage.py
python3 scripts/verify_planet_hero_coverage.py
python3 scripts/verify_character_hero_coverage.py
```

Hero prompt manifests live alongside the installers (`hero_manifest.json`, `planet_hero_manifest.json`, `character_hero_manifest.json`) for batch image generation.

## Adding new content

To add a new entry manually (e.g. a character):

1. Add a record to the appropriate `Data/*.cs` file with `Name`, `Slug`, `Route`, `Description`, and `Color`.
2. Create a matching JSON profile at `wwwroot/data/profiles/{category}/{slug}.json`.
3. Add a cinematic hero PNG under `wwwroot/images/{category}/{slug}-scene.png` (or `{slug}-hero.png` for planets).
4. The sidebar and index pages update automatically from the catalogue data — no route registration is needed beyond the existing `{Slug}` page templates.

For bulk additions, prefer the generator scripts — for example, `generate_character_catalog.py` merges hand-authored enrichments from `character_profile_enrichments.py` and `character_catalog_additions.py` into `CharacterData.cs` and the matching profile JSON files.

For planets, also set `X` and `Y` coordinates in `GalaxyData.cs` so the world appears on the galaxy map (see `GalaxyMapSettings.cs` for the coordinate bounds). Generate or copy `{slug}-space.png` for the full-page background and `{slug}-hero.png` for the detail banner.

## Disclaimer

This is a fan project for educational and personal use. *Star Wars* and all related names, characters, and imagery are trademarks of Lucasfilm Ltd. This project is not affiliated with, endorsed by, or sponsored by Lucasfilm or The Walt Disney Company.
