# Spinoff theme: Fractured Earth

This is an alternate-universe variant of the game considered during initial design (2026-05-13) and set aside in favor of **Solar Frontier Wars**. Kept here in case we want to spin off a second campaign / mod / standalone version later.

## Setting

Post-apocalyptic Earth, roughly 50 years after a civilizational collapse (climate collapse, resource wars, pandemic, take your pick — leave it ambiguous so factions can disagree on the cause). The biosphere is wounded but recovering. Surviving humans cluster around defensible terrain: fortified arcologies, scrap-built river towns, deep caves, mutated forests.

Visual tone: gritty, scavenged, dust + rust + bioluminescent fungi. Closer to **Command & Conquer: Tiberian Sun** than to StarCraft. Vehicles are improvised — APCs are welded buses, gunships are converted crop-dusters.

## Three factions

### Coalition (the "Terran Directorate" analog)
Organized military remnant. Holds a chain of fortified arcologies. Disciplined, conventional warfare, heavy armor. Believes humanity's future is in reclaiming centralized power.
- **Aesthetic:** olive drab + concrete, NATO/IDF-style hardware refurbished and improvised on.
- **Roster archetype:** balanced. Strong infantry, capable tanks, decent air.
- **Hook:** they're the "default" faction, easy onboarding.

### Scavengers / "the Reach" (the "Belt Syndicate" analog)
Raider clans, river-town traders, and salvage crews loosely federated under charismatic warlords. Improvised everything. Asymmetric, mobile, ambush-heavy.
- **Aesthetic:** rust + leather + spray-paint warnings, Mad Max / Tarkovsky's Stalker.
- **Roster archetype:** swarm, fast, cheap, fragile. Vehicles are kitbashed and unreliable but cheap to replace.
- **Hook:** map control through movement and harassment. Rewards aggressive play.

### Bio-Hive / "the Verdancy" (the "Synthetic Collective" analog)
A bioengineered ecosystem that may or may not be sentient. Worshipped/feared by its symbiote-humans. Grows its army instead of building one. Late-game biomass weapons rival anything else on the map.
- **Aesthetic:** spore clouds, chitin armor, bioluminescent vein-patterns, things-that-shouldn't-be-alive. The faction's "buildings" are grown organisms — they pulse, they bleed.
- **Roster archetype:** tech / late-game / expensive. Slow ramp, terrifying ceiling. Mid-tier units are disposable spore-creatures; top-tier are walking siege beasts.
- **Hook:** the most visually distinctive faction. Sells the box.

## Resources

Single-resource economy or two-resource, TBD. Candidates:
- **Scrap** — the universal base resource (gathered from wrecks / ruins / asteroids — but here it's wrecks).
- **Bio-mass** or **Pre-collapse Tech** — the gas/exotic equivalent. Bio-Hive cares about biomass; Coalition cares about pre-collapse tech caches; Scavengers can use either.

Faction-asymmetric resources are *interesting* but a balance nightmare — note for future selves: probably easier to stay symmetric and let factions just convert the same resource differently.

## What's appealing about this theme

- Gritty / weighty / serious — every unit feels expensive and mortal.
- Bio-Hive is the standout aesthetic — nothing else looks like a faction made of grown organisms.
- Maps can use real-world terrain (drowned coastlines, choked freeways, overgrown cities) which is easier to art-direct than alien moons.
- Strong campaign material: each faction has a moral position on the collapse.

## What we'd lose vs. Solar Frontier Wars

- Less variety in unit "flight." Solar lets us have orbital drops, vacuum operations, asteroid maps. Fractured Earth is mostly ground + low-altitude.
- Harder to justify a clean grid for buildings (a wrecked city isn't gridded). Workable but needs explicit framing ("we build on cleared foundations").
- Bio-Hive will be 2–3× more art-intensive than the other two factions. Plan accordingly.

## If we revisit

The engine choices in the approved plan (mixin-based entities, faction-as-registry, data-driven stats) should port cleanly. The work is almost entirely in:
- Faction class trio (`coalition.py`, `scavengers.py`, `bio_hive.py`)
- Concrete buildings + units under `buildings/<faction>/` and `units/<faction>/`
- Stat tables in `data/`
- Art / sprites in `assets/sprites/<faction>/`
- Maybe an alternate `world/` terrain set (ruins, vegetation, irradiated zones)

The Solar Frontier Wars core systems don't need to change.
