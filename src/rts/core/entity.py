"""Entity — base class for everything that lives in the game world."""
from __future__ import annotations

import itertools
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from rts.player.player import Player
    from rts.world.game_world import GameWorld


class Entity:
    """Base for buildings, units, projectiles, resource nodes — anything in the world.

    Subclasses extend this with mixins (Damageable, Movable, etc.) from `core.mixins`.
    """

    _id_counter = itertools.count(1)

    def __init__(
        self,
        *,
        world: "GameWorld",
        owner: Optional["Player"],
        x: float,
        y: float,
    ) -> None:
        self.id: int = next(Entity._id_counter)
        self.world = world
        self.owner = owner
        self.x = float(x)
        self.y = float(y)
        self.alive: bool = True
        self.sprite = None  # set by subclasses that render via arcade.Sprite

    # --- Lifecycle ---------------------------------------------------------

    def update(self, dt: float) -> None:
        """Per-tick update. Override in subclasses."""

    def draw(self) -> None:
        """Render. Default: defer to the attached sprite if present."""
        if self.sprite is not None:
            self.sprite.draw()

    def destroy(self) -> None:
        """Mark for removal at end of tick. World will cull it."""
        self.alive = False

    def __repr__(self) -> str:
        return f"<{type(self).__name__} id={self.id} pos=({self.x:.0f},{self.y:.0f}) alive={self.alive}>"
