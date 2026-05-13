"""TechUp — race up the tech tree for high-end units. Vulnerable mid-game."""
from __future__ import annotations

from typing import TYPE_CHECKING

from rts.ai.ai_player import Strategy

if TYPE_CHECKING:
    from rts.ai.ai_player import AIPlayer
    from rts.world.game_world import GameWorld


class TechUpStrategy(Strategy):
    name = "tech_up"

    def tick(self, player: "AIPlayer", world: "GameWorld", dt: float) -> None:
        # TODO: 1. Take He-3 expansion early. 2. Build research lab + production.
        #       3. Skip cheap units; produce only mid/late-tier.
        #       4. Add minimum defensive presence to deter early all-ins.
        return
