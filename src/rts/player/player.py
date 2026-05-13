"""Player base — shared state between human and AI controllers."""
from __future__ import annotations

from typing import TYPE_CHECKING

from rts.config import (
    DEFAULT_STARTING_SUPPLY,
    DEFAULT_SUPPLY_CAP,
    FOW_REVEAL_RADIUS_TILES,
)
from rts.core.resources import ResourcePool
from rts.world.fog_of_war import FogOfWar

if TYPE_CHECKING:
    from rts.core.entity import Entity
    from rts.factions.faction import Faction
    from rts.player.commands import Command
    from rts.world.game_world import GameWorld


class Player:
    """Owns a faction, resources, supply, fog-of-war, and a set of entities."""

    def __init__(
        self,
        *,
        index: int,
        faction: "Faction",
        is_human: bool = False,
    ) -> None:
        self.index = index
        self.faction = faction
        self.is_human = is_human
        self.resources: ResourcePool = faction.make_starting_resources()
        self.supply_used: int = DEFAULT_STARTING_SUPPLY
        self.supply_cap: int = DEFAULT_SUPPLY_CAP
        self.owned_entities: list["Entity"] = []
        self.completed_tech: set[str] = set()
        self.fog: FogOfWar | None = None
        self.pending_commands: list["Command"] = []
        self.defeated: bool = False

    # --- Setup -------------------------------------------------------------

    def init_fog(self, width: int, height: int) -> None:
        self.fog = FogOfWar(width=width, height=height)

    # --- Entity ownership --------------------------------------------------

    def add_entity(self, entity: "Entity") -> None:
        self.owned_entities.append(entity)

    def remove_entity(self, entity: "Entity") -> None:
        if entity in self.owned_entities:
            self.owned_entities.remove(entity)

    # --- Commands ----------------------------------------------------------

    def queue_command(self, command: "Command") -> None:
        self.pending_commands.append(command)

    def process_commands(self, world: "GameWorld", dt: float) -> None:
        """Subclasses override (HumanPlayer drains input queue, AIPlayer plans)."""
        # Drain the queue — default behavior is to clear (subclasses dispatch).
        while self.pending_commands:
            cmd = self.pending_commands.pop(0)
            self._dispatch(world, cmd)

    def _dispatch(self, world: "GameWorld", command: "Command") -> None:
        """Apply one command. Skeleton: stubs out the major command types."""
        # TODO: wire this up to actual unit behavior. For the skeleton it's a no-op.
        return

    # --- Fog of war --------------------------------------------------------

    def refresh_fog(self, world: "GameWorld") -> None:
        if self.fog is None:
            return
        self.fog.reset_visible()
        for entity in self.owned_entities:
            if not entity.alive:
                continue
            cx, cy = world.nav_grid.world_to_cell(entity.x, entity.y)
            self.fog.reveal(cx, cy, FOW_REVEAL_RADIUS_TILES)

    def __repr__(self) -> str:
        return f"<Player #{self.index} {self.faction.display_name} human={self.is_human}>"
