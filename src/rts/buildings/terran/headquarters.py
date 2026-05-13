"""Terran Directorate Headquarters — central building. Produces workers."""
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from rts.buildings.categories import ProductionBuilding
from rts.data.building_stats import TERRAN_HQ_STATS

if TYPE_CHECKING:
    from rts.player.player import Player
    from rts.world.game_world import GameWorld


class TerranHeadquarters(ProductionBuilding):
    """Resource drop-off point + worker producer.

    Equivalent of: SC Command Center, C&C Construction Yard.
    """

    DISPLAY_NAME = "Directorate Headquarters"

    def __init__(
        self,
        *,
        world: "GameWorld",
        owner: Optional["Player"],
        x: float,
        y: float,
    ) -> None:
        stats = TERRAN_HQ_STATS
        super().__init__(
            world=world,
            owner=owner,
            x=x,
            y=y,
            hp=stats.hp,
            footprint=stats.footprint,
            build_time=stats.build_time,
            armor_class=stats.armor_class,
        )
        # Buildings the HQ ships pre-built; mark constructed immediately.
        self.constructed = True
        self.construction_progress = self.build_time
