"""Selection box — renders the drag-select rectangle during a mouse drag."""
from __future__ import annotations

import arcade


def draw_selection_box(start: tuple[float, float], end: tuple[float, float]) -> None:
    x0, y0 = start
    x1, y1 = end
    left, right = min(x0, x1), max(x0, x1)
    bottom, top = min(y0, y1), max(y0, y1)
    arcade.draw_lbwh_rectangle_outline(
        left, bottom, right - left, top - bottom, arcade.color.LIGHT_GREEN, 1
    )
