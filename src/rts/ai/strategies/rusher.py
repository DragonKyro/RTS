"""Rusher — early aggression. Builds minimum economy, masses cheapest combat unit."""
from __future__ import annotations

from typing import TYPE_CHECKING

from rts.ai.ai_player import Strategy

if TYPE_CHECKING:
    from rts.ai.ai_player import AIPlayer
    from rts.world.game_world import GameWorld


class RusherStrategy(Strategy):
    name = "rusher"

    def tick(self, player: "AIPlayer", world: "GameWorld", dt: float) -> None:
        # TODO: 1. Maintain ~6 workers. 2. Build one infantry production building.
        #       3. Pump cheap combat units. 4. Attack-move at the enemy spawn
        #          when we have N units (N grows over time).
        return
