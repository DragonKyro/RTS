"""Fog of war — per-player visibility grid.

Each player maintains two grids over the map:
- `visible`: currently in line-of-sight this tick
- `explored`: ever seen (so we remember terrain even when not currently visible)
"""
from __future__ import annotations


class FogOfWar:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.visible: list[list[bool]] = [[False] * height for _ in range(width)]
        self.explored: list[list[bool]] = [[False] * height for _ in range(width)]

    def reset_visible(self) -> None:
        for col in self.visible:
            for i in range(len(col)):
                col[i] = False

    def reveal(self, cx: int, cy: int, radius: int) -> None:
        """Reveal a circular area around (cx, cy)."""
        r2 = radius * radius
        x0 = max(0, cx - radius)
        x1 = min(self.width - 1, cx + radius)
        y0 = max(0, cy - radius)
        y1 = min(self.height - 1, cy + radius)
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                dx = x - cx
                dy = y - cy
                if dx * dx + dy * dy <= r2:
                    self.visible[x][y] = True
                    self.explored[x][y] = True

    def is_visible(self, cx: int, cy: int) -> bool:
        if 0 <= cx < self.width and 0 <= cy < self.height:
            return self.visible[cx][cy]
        return False

    def is_explored(self, cx: int, cy: int) -> bool:
        if 0 <= cx < self.width and 0 <= cy < self.height:
            return self.explored[cx][cy]
        return False
