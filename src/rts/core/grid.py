"""NavGrid — tile-based occupancy grid for building placement and pathfinding."""
from __future__ import annotations

from typing import Iterator

from rts.config import TILE_SIZE


class NavGrid:
    """A 2D grid where each cell can be passable or blocked.

    Buildings mark cells as blocked when placed. The pathfinder reads this.
    """

    def __init__(self, width: int, height: int, *, tile_size: int = TILE_SIZE) -> None:
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self._blocked: list[list[bool]] = [
            [False] * height for _ in range(width)
        ]

    # --- Coord conversion --------------------------------------------------

    def world_to_cell(self, x: float, y: float) -> tuple[int, int]:
        return int(x // self.tile_size), int(y // self.tile_size)

    def cell_to_world(self, cx: int, cy: int) -> tuple[float, float]:
        return (cx + 0.5) * self.tile_size, (cy + 0.5) * self.tile_size

    # --- Bounds ------------------------------------------------------------

    def in_bounds(self, cx: int, cy: int) -> bool:
        return 0 <= cx < self.width and 0 <= cy < self.height

    # --- Occupancy ---------------------------------------------------------

    def is_passable(self, cx: int, cy: int) -> bool:
        if not self.in_bounds(cx, cy):
            return False
        return not self._blocked[cx][cy]

    def set_blocked(self, cx: int, cy: int, blocked: bool = True) -> None:
        if self.in_bounds(cx, cy):
            self._blocked[cx][cy] = blocked

    def block_rect(self, cx: int, cy: int, w: int, h: int) -> None:
        for x in range(cx, cx + w):
            for y in range(cy, cy + h):
                self.set_blocked(x, y, True)

    def unblock_rect(self, cx: int, cy: int, w: int, h: int) -> None:
        for x in range(cx, cx + w):
            for y in range(cy, cy + h):
                self.set_blocked(x, y, False)

    def rect_is_free(self, cx: int, cy: int, w: int, h: int) -> bool:
        for x in range(cx, cx + w):
            for y in range(cy, cy + h):
                if not self.is_passable(x, y):
                    return False
        return True

    # --- Neighbors (8-way) -------------------------------------------------

    _OFFSETS = (
        (-1, -1), (0, -1), (1, -1),
        (-1,  0),          (1,  0),
        (-1,  1), (0,  1), (1,  1),
    )

    def neighbors(self, cx: int, cy: int) -> Iterator[tuple[int, int]]:
        for dx, dy in self._OFFSETS:
            nx, ny = cx + dx, cy + dy
            if self.is_passable(nx, ny):
                # Block diagonal "corner cutting" through blocked orthogonals.
                if dx != 0 and dy != 0:
                    if not self.is_passable(cx + dx, cy) or not self.is_passable(cx, cy + dy):
                        continue
                yield nx, ny
