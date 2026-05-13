"""GameWorld — the simulation root. Owns the map, entities, and tick order.

`update(dt)` runs subsystems in a fixed order each frame to avoid order-of-operations
bugs. See plan: commands → production → unit AI → movement → combat → gathering
→ fog of war → cull/events.
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Iterable

from rts.config import TILE_SIZE
from rts.core.events import EventBus
from rts.core.grid import NavGrid
from rts.core.spatial_hash import SpatialHash
from rts.world.game_map import GameMap

if TYPE_CHECKING:
    from rts.core.entity import Entity
    from rts.player.player import Player


class GameWorld:
    """Container for one match in progress."""

    def __init__(self, game_map: GameMap, players: list["Player"]) -> None:
        self.map = game_map
        self.players = players
        self.nav_grid = NavGrid(
            width=game_map.width,
            height=game_map.height,
            tile_size=game_map.tile_size,
        )
        # Apply terrain to the nav grid (BLOCKED / WATER tiles are impassable for ground).
        for cx in range(game_map.width):
            for cy in range(game_map.height):
                tile = game_map.tiles[cx][cy]
                if not tile.passable_for_ground:
                    self.nav_grid.set_blocked(cx, cy, True)

        self.spatial_hash = SpatialHash(cell_size=TILE_SIZE * 2)
        self.events = EventBus()
        self.entities: list["Entity"] = []
        self.time: float = 0.0

    # --- Entity lifecycle --------------------------------------------------

    def add_entity(self, entity: "Entity") -> None:
        self.entities.append(entity)
        self.spatial_hash.insert(entity)

    def remove_entity(self, entity: "Entity") -> None:
        try:
            self.entities.remove(entity)
        except ValueError:
            pass
        self.spatial_hash.remove(entity)

    def query_radius(self, x: float, y: float, radius: float) -> Iterable["Entity"]:
        return self.spatial_hash.query_radius(x, y, radius)

    # --- Tick --------------------------------------------------------------

    def update(self, dt: float) -> None:
        """Run one simulation step. Order matters."""
        self.time += dt

        # 1. Resolve player + AI commands
        for player in self.players:
            player.process_commands(self, dt)

        # 2. Production (buildings produce units / research progresses)
        # 3. Unit AI (target selection, command queue advancement)
        # 4. Pathfinding / movement
        # 5. Combat (attacks, projectile flight, damage)
        # 6. Resource gathering
        for entity in list(self.entities):
            if entity.alive:
                entity.update(dt)
            self.spatial_hash.update(entity)

        # 7. Fog of war refresh
        for player in self.players:
            player.refresh_fog(self)

        # 8. Cull dead entities, fire events
        dead = [e for e in self.entities if not e.alive]
        for e in dead:
            self.remove_entity(e)
            self.events.publish("entity_destroyed", {"entity": e})
