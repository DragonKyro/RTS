"""Building — base class. All concrete buildings extend a category from `categories.py`."""
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from rts.core.entity import Entity
from rts.core.mixins import Damageable

if TYPE_CHECKING:
    from rts.player.player import Player
    from rts.world.game_world import GameWorld


class Building(Entity, Damageable):
    """All buildings have HP and a tile footprint. They don't move."""

    def __init__(
        self,
        *,
        world: "GameWorld",
        owner: Optional["Player"],
        x: float,
        y: float,
        hp: int,
        footprint: tuple[int, int],
        build_time: float,
        armor_class: str = "heavy",
    ) -> None:
        super().__init__(world=world, owner=owner, x=x, y=y)
        self.hp = hp
        self.max_hp = hp
        self.armor_class = armor_class
        self.footprint = footprint  # (width_cells, height_cells)
        self.build_time = build_time
        self.construction_progress = 0.0
        self.constructed: bool = False

    # --- Placement ---------------------------------------------------------

    @property
    def is_under_construction(self) -> bool:
        return not self.constructed

    def advance_construction(self, dt: float) -> bool:
        """Tick construction. Returns True when complete (this tick)."""
        if self.constructed:
            return False
        self.construction_progress += dt
        if self.construction_progress >= self.build_time:
            self.construction_progress = self.build_time
            self.constructed = True
            self.on_completed()
            return True
        return False

    def on_completed(self) -> None:
        """Override for buildings that activate behavior on completion."""

    def update(self, dt: float) -> None:
        if not self.constructed:
            self.advance_construction(dt)
