"""ThreatMap — coarse-grained danger heatmap. AI consults this to plan routes."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from rts.world.game_world import GameWorld


class ThreatMap:
    """One float per coarse cell. Higher = more dangerous for our units."""

    def __init__(self, width: int, height: int, *, cells_per_tile: int = 4) -> None:
        self.cells_per_tile = cells_per_tile
        self.width = max(1, width // cells_per_tile)
        self.height = max(1, height // cells_per_tile)
        self._values: list[list[float]] = [[0.0] * self.height for _ in range(self.width)]

    def clear(self) -> None:
        for col in self._values:
            for i in range(len(col)):
                col[i] = 0.0

    def add(self, cx: int, cy: int, value: float) -> None:
        ccx, ccy = cx // self.cells_per_tile, cy // self.cells_per_tile
        if 0 <= ccx < self.width and 0 <= ccy < self.height:
            self._values[ccx][ccy] += value

    def get(self, cx: int, cy: int) -> float:
        ccx, ccy = cx // self.cells_per_tile, cy // self.cells_per_tile
        if 0 <= ccx < self.width and 0 <= ccy < self.height:
            return self._values[ccx][ccy]
        return 0.0

    def refresh(self, world: "GameWorld", for_player_index: int) -> None:
        """Rebuild from current world state. TODO: include enemy combat units / defenses."""
        self.clear()
