# RTS — Solar Frontier Wars

A single-player-vs-AI 2D real-time strategy game inspired by **StarCraft** and **Command & Conquer**, built on [Python Arcade](https://api.arcade.academy/).

Set in the near-future solar system: three factions battle over Metals and Helium-3 across the Inner Belt.

## Factions

| Faction | Style | Identity |
|---|---|---|
| **Terran Directorate** | Balanced, armor-heavy | Earth-based military, conventional weapons, well-rounded roster |
| **Belt Syndicate** | Fast, cheap, swarm | Asteroid miners turned warlords; guerrilla and hit-and-run |
| **Synthetic Collective** | High-tech, expensive | Self-replicating AI/robotic forces, energy weapons, late-game power |

Rosters are intentionally *similar but not identical* — each faction has analogous infantry / vehicle / air / worker units, but their stats and roles differ.

## Project layout

Top-level (see [plan](#planning) for the full breakdown under `src/rts/`):

```
RTS/
├── src/rts/        # Game source (OOP: core, factions, units, buildings, ai, ui, world, ...)
├── assets/         # Sprites, tiles, sounds, music
├── maps/           # Map definition files
├── tests/          # pytest suites for pure-logic modules
├── solar_frontier_wars.py   # Entry point
└── pyproject.toml  # Package metadata + deps
```

Source tree is organized so factions, units, and buildings can be added without modifying the engine. Behavior is composed via mixins (`Damageable`, `Attacker`, `Movable`, `Producer`, `Gatherer`) rather than deep inheritance.

## Status

**Scaffolded.** Engine, faction registry, mixin-based unit/building hierarchy, A* pathfinding, fog of war, AI/Human player base, and Arcade view shells (main menu → faction select → game) are all in place. Gameplay logic (commands actually moving units, buildings actually producing) is not yet wired — the game boots to a placeholder match screen.

The Terran Directorate has one building (Headquarters) and one unit (Engineer) wired end-to-end to demonstrate the pattern. Belt Syndicate and Synthetic Collective have empty rosters pending faction-specific work.

## Running

```bash
python -m venv .venv
.venv\Scripts\activate            # Windows (PowerShell: .venv\Scripts\Activate.ps1)
pip install -r requirements.txt
python solar_frontier_wars.py     # or: python -m rts
```

Boots to the main menu. Press SPACE → arrow keys to pick a faction → ENTER to enter the (placeholder) match view. ESC backs out of any screen.

## Testing

```bash
pytest tests/
```

23 tests cover the pure-logic foundations: NavGrid (coord conversion, occupancy, neighbor queries with diagonal corner-cut prevention), A* pathfinding (straight paths, obstacle avoidance, unreachable cases), ResourcePool (atomic pay), TechTree (prerequisite gating), and the damage-type × armor-class matrix.

## Tech stack

- Python 3.11+
- [Python Arcade](https://api.arcade.academy/) for window / sprites / input
- Pure-Python A* on a navigation grid + steering for smooth 2D movement (units move freely; buildings snap to a tile grid)
- `pytest` for tests
