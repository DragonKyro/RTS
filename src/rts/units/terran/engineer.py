"""Terran Directorate Engineer — the worker unit. Gathers Metals/He-3, builds buildings."""
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from rts.data.unit_stats import TERRAN_ENGINEER_STATS
from rts.units.categories import WorkerUnit

if TYPE_CHECKING:
    from rts.player.player import Player
    from rts.world.game_world import GameWorld


class Engineer(WorkerUnit):
    """Worker: gathers resources, constructs buildings, repairs (TBD)."""

    DISPLAY_NAME = "Engineer"

    def __init__(
        self,
        *,
        world: "GameWorld",
        owner: Optional["Player"],
        x: float,
        y: float,
    ) -> None:
        stats = TERRAN_ENGINEER_STATS
        super().__init__(
            world=world,
            owner=owner,
            x=x,
            y=y,
            hp=stats.hp,
            speed=stats.speed,
            radius=stats.radius,
            armor_class=stats.armor_class,
        )
        self.init_gatherer(
            carry_capacity=stats.carry_capacity,
            gather_rate=stats.gather_rate,
        )
