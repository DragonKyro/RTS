"""Projectile — travels from a launcher to a target, applies damage on hit."""
from __future__ import annotations

import math
from typing import TYPE_CHECKING, Optional

from rts.core.entity import Entity

if TYPE_CHECKING:
    from rts.player.player import Player
    from rts.world.game_world import GameWorld


class Projectile(Entity):
    """A simple homing-or-ballistic projectile.

    For the skeleton this homes on `target`. If the target dies en route the
    projectile expires harmlessly.
    """

    def __init__(
        self,
        *,
        world: "GameWorld",
        owner: Optional["Player"],
        x: float,
        y: float,
        target: Entity,
        damage: int,
        damage_type: str,
        speed: float = 400.0,
    ) -> None:
        super().__init__(world=world, owner=owner, x=x, y=y)
        self.target = target
        self.damage = damage
        self.damage_type = damage_type
        self.speed = speed

    def update(self, dt: float) -> None:
        if not self.alive:
            return
        if not self.target.alive:
            self.destroy()
            return
        dx, dy = self.target.x - self.x, self.target.y - self.y
        dist = math.hypot(dx, dy)
        step = self.speed * dt
        if dist <= step:
            # Hit
            if hasattr(self.target, "take_damage"):
                self.target.take_damage(self.damage, self.damage_type)
            self.destroy()
            return
        self.x += dx / dist * step
        self.y += dy / dist * step
