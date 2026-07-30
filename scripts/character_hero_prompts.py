#!/usr/bin/env python3
"""Cinematic hero-banner prompts for Characters Directory entries."""

from __future__ import annotations

from parse_csharp_data import load_characters

STYLE_SUFFIX = (
    "Cinematic Star Wars digital illustration hero banner, 1536x1024, 16:9. "
    "Hyper-detailed sci-fi matte painting, dramatic rim lighting, rich atmospheric depth, "
    "premium encyclopedia header art quality. No text, no logos, no watermarks."
)

CHARACTER_OVERRIDES: dict[str, str] = {
    "han-solo": "Corellian smuggler in vest and boots beside the Millennium Falcon in a dusty spaceport hangar at sunset",
    "leia-organa": "Regal rebel leader in white diplomatic robes aboard a starship bridge with starfield viewport",
    "luke-skywalker": "Farm boy turned hero in desert tunic holding a lightsaber on Tatooine ridge at twin sunset",
    "chewbacca": "Towering Wookiee warrior with bowcaster on Millennium Falcon ramp with nebula backdrop",
    "din-djarin": "Beskar-armored Mandalorian bounty hunter with rifle in rocky frontier landscape twilight",
    "boba-fett": "Green Mandalorian armor hunter with jetpack on Tatooine dune sea under twin suns",
    "shmi-skywalker": "Kind mother figure in humble Tatooine robes at moisture farm doorway with warm amber sunset",
    "jar-jar-binks": "Tall amphibious alien in regal Gungan attire on Naboo plaza with waterfalls and golden domes",
    "padme-amidala": "Elegant senator in ornate Naboo royal gown in Theed palace garden with soft light",
    "rey": "Jakku scavenger with staff and desert wraps amid starship wreckage under harsh sun",
    "satele-shan": "Human female Jedi Grand Master with brown hair in white and blue Old Republic battle robes, blue lightsaber, Battle Meditation energy over ruined Coruscant Jedi Temple during Sith invasion",
    "finn": "Former stormtrooper without helmet in Resistance jacket on tropical base runway",
    "cassian-andor": "Undercover rebel intelligence officer in worn field jacket on rainy industrial world",
    "thrawn": "Blue-skinned Chiss admiral studying art holograms on Star Destroyer bridge",
    "general-grievous": "Cyborg general with four arms and cape on Separatist flagship bridge",
    "jabba-the-hutt": "Massive slug crime lord on throne dais in smoky palace chamber with alien court",
    "moff-gideon": "Imperial remnant leader in black cape with dark troopers in cruiser hangar",
    "mon-mothma": "Calm rebel chancellor in senatorial robes in hidden war room with holo maps",
    "lando-calrissian": "Suave administrator in cape before Cloud City tibanna sunset skyline",
    "amilyn-holdo": "Eccentric Resistance admiral with vivid hair aboard Raddus bridge with purple nebula",
}

DIRECTORY_HERO_PROMPT = (
    "Panoramic cinematic gathering of diverse galactic figures—smugglers, soldiers, senators, pilots, "
    "droids, and rebels—assembled on a starport observation deck overlooking a busy orbital skyline "
    "with starships launching and hyperspace lanes glowing in the distance. "
    + STYLE_SUFFIX
)


def _trim_description(desc: str, max_len: int = 160) -> str:
    text = desc.strip()
    if len(text) > max_len:
        text = text[:max_len].rsplit(" ", 1)[0] + "…"
    return text


def character_prompt(entry: dict[str, str]) -> str:
    slug = entry["slug"]
    if slug in CHARACTER_OVERRIDES:
        scene = CHARACTER_OVERRIDES[slug]
    else:
        name = entry.get("name", "figure")
        role = entry.get("role", "galactic figure")
        desc = _trim_description(entry.get("description", ""))
        scene = (
            f"Cinematic portrait scene of a {role.lower()}, {desc}. "
            f"Dramatic character-focused composition with environment reflecting their story"
        )
    return f"{scene}. {STYLE_SUFFIX}"


def all_character_prompts() -> dict[str, str]:
    return {e["slug"]: character_prompt(e) for e in load_characters()}


if __name__ == "__main__":
    prompts = all_character_prompts()
    print(f"Generated {len(prompts)} character hero prompts")
