"""Turtle — defensive economy. Walls + turrets + late-game push."""
from __future__ import annotations

from typing import TYPE_CHECKING

from rts.ai.ai_player import Strategy

if TYPE_CHECKING:
    from rts.ai.ai_player import AIPlayer
    from rts.world.game_world import GameWorld


class TurtleStrategy(Strategy):
    name = "turtle"

    def tick(self, player: "AIPlayer", world: "GameWorld", dt: float) -> None:
        # TODO: 1. Saturate workers first. 2. Wall the base entry.
        #       3. Build turrets at choke points. 4. Tech up while waiting.
        return
