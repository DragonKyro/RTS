# CLAUDE.md — RTS project notes

Context for any Claude session working on this repo. Read this first.

## What this project is

A single-player-vs-AI 2D real-time strategy game in the StarCraft / Command & Conquer tradition, built on Python Arcade. See [README.md](README.md) for the player-facing overview.

**Theme: Solar Frontier Wars.** Near-future sci-fi. *Not* medieval fantasy — that was explicitly excluded by the user.

**Three factions** with similar-but-not-identical rosters:
- **Terran Directorate (TD)** — balanced, armor-heavy, conventional
- **Belt Syndicate (BS)** — fast, cheap, swarm
- **Synthetic Collective (SC)** — high-tech, expensive, energy weapons

**Two resources**: Metals (base economy) and Helium-3 (gates advanced tech).

## Architecture (must follow)

The project structure plan lives at `~/.claude/plans/splendid-knitting-seahorse.md` and is the source of truth for layout.

Key invariants:

- **Source layout is `src/rts/`** (src layout). Concrete factions/units/buildings live in faction-specific subfolders: `units/terran/`, `buildings/belt/`, etc.
- **Shallow inheritance + mixin composition.** `Entity` is the base; behavior comes from mixins in `src/rts/core/mixins.py`: `Damageable`, `Attacker`, `Movable`, `Producer`, `Gatherer`. Don't deepen the tree — compose only the mixins a class actually needs.
- **Faction is a registry**, not a god class. It exposes `building_roster`, `unit_roster`, `starting_units`, `starting_resources`, `tech_tree`, `theme_tag`. Concrete units/buildings live in `units/<faction>/` and `buildings/<faction>/`.
- **Stats are data, not code.** Numeric values (hp, dmg, speed, cost, build_time) live in `src/rts/data/unit_stats.py` and `building_stats.py` as dataclasses. Concrete classes pull stats at construction. Balance changes = one-file edits.
- **Player/AI symmetry.** `AIPlayer` emits the same `Command` objects (`MoveCommand`, `AttackCommand`, `BuildCommand`, `GatherCommand`) as `HumanPlayer`. Keep this symmetry; it makes AI debugging tractable.
- **World tick order is fixed** (in `GameWorld.update(dt)`): commands → production → unit AI → pathfinding/movement → combat → resource gathering → fog of war → cull/events. Don't reshuffle without thinking through the consequences.
- **Movement model**: units move freely in 2D, but buildings snap to a tile grid. Pathfinding = A* on a NavGrid (buildings mark cells impassable) → steering with neighbor avoidance for smooth motion between waypoints. Air units bypass the nav grid.

## Naming

- Don't reuse StarCraft proper-noun names (Marine, Zergling, SCV, Probe, etc.) — invent thematic equivalents that fit Solar Frontier Wars. E.g. TD has `Marine`-analog called something else, BS has a `Raider`, SC has a `Drone`.
- Faction prefixes: TD / BS / SC are fine internally but use full names in user-facing strings.

## Tech / tooling

- **Python 3.11+**, type hints throughout, `dataclasses` for stat blocks.
- **Engine:** `arcade.Window` + `arcade.View` for screens, `arcade.Sprite` / `arcade.SpriteList` for entities, `arcade.Camera` for scroll/zoom.
- **Tests:** `pytest`, focused on pure-logic modules (pathfinding, combat resolution, tech tree, AI build orders). Don't try to integration-test the rendering loop.
- **Packaging:** `pyproject.toml`, `src/` layout. Run via `python solar_frontier_wars.py` or `python -m rts`.

## Conventions

- Prefer editing existing files over creating new ones.
- Default to no comments. Only add a comment when the *why* is non-obvious.
- Keep faction archetypes consistent: TD = balanced, BS = swarm/fast, SC = tech/expensive. New units should fit their faction's identity.
- When adding a unit or building, the workflow is: (1) pick the right category base, (2) compose the mixins you need, (3) add stats to the data table, (4) register in the faction's roster.

## Out of scope (for now)

- Multiplayer — single-player vs AI only.
- Map editor / level editor UI — maps are JSON files in `maps/`.
- Modding support / hot-reload.

## When you need more context

- Approved structure plan: `~/.claude/plans/splendid-knitting-seahorse.md`
- Memory files: `~/.claude/projects/c--Users-klui-Desktop-Kyle-P-RTS/memory/` (project overview, architecture, plan pointer)
