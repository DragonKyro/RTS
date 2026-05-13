"""Minimap — small overview in the bottom-right of the HUD."""
from __future__ import annotations

import arcade


class Minimap:
    def __init__(self, *, map_width: int, map_height: int, size: int = 140) -> None:
        self.map_width = map_width
        self.map_height = map_height
        self.size = size

    def draw(self, *, x: float, y: float) -> None:
        # Background
        arcade.draw_lbwh_rectangle_filled(x, y, self.size, self.size, (30, 36, 50))
        arcade.draw_lbwh_rectangle_outline(x, y, self.size, self.size, arcade.color.LIGHT_GRAY, 1)
        # TODO: draw fog of war, owned entities, enemies in vision, camera frustum.
