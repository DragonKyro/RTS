"""Unit — base class. All units move and have HP."""
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from rts.core.entity import Entity
from rts.core.mixins import Damageable, Movable

if TYPE_CHECKING:
    from rts.player.player import Player
    from rts.world.game_world import GameWorld


class Unit(Entity, Damageable, Movable):
    """Base for all in-world controllable units.

    Subclasses (from `units.categories`) layer Attacker / Gatherer on top.
    """

    def __init__(
        self,
        *,
        world: "GameWorld",
        owner: Optional["Player"],
        x: float,
        y: float,
        hp: int,
        speed: float,
        radius: float = 12.0,
        armor_class: str = "light",
    ) -> None:
        super().__init__(world=world, owner=owner, x=x, y=y)
        self.hp = hp
        self.max_hp = hp
        self.armor_class = armor_class
        self.speed = speed
        self.radius = radius
        self.init_movable()
        # Command queue (current order + shift-queued orders); populated by player/AI
        self.command_queue: list = []

    def update(self, dt: float) -> None:
        self.update_movement(dt)
