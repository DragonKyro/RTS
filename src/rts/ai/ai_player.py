"""AIPlayer — orchestrates a swappable Strategy that emits the same Commands a human would."""
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from rts.player.player import Player

if TYPE_CHECKING:
    from rts.factions.faction import Faction
    from rts.world.game_world import GameWorld


class Strategy:
    """Base strategy. Override `tick` to enqueue commands on `player`."""

    name: str = "noop"

    def tick(self, player: "AIPlayer", world: "GameWorld", dt: float) -> None:
        """Run one strategy step. Default: do nothing."""


class AIPlayer(Player):
    def __init__(
        self,
        *,
        index: int,
        faction: "Faction",
        strategy: Optional[Strategy] = None,
    ) -> None:
        super().__init__(index=index, faction=faction, is_human=False)
        self.strategy: Strategy = strategy or Strategy()
        self._strategy_tick_accumulator: float = 0.0
        self._strategy_tick_interval: float = 0.5  # AI thinks twice per second

    def process_commands(self, world: "GameWorld", dt: float) -> None:
        # Step the strategy on its own slower clock to avoid per-frame thrash.
        self._strategy_tick_accumulator += dt
        if self._strategy_tick_accumulator >= self._strategy_tick_interval:
            self._strategy_tick_accumulator = 0.0
            self.strategy.tick(self, world, dt)
        # Then dispatch whatever commands the strategy enqueued.
        super().process_commands(world, dt)
