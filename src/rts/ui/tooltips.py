"""Tooltips — hover-info popup, e.g. cost and prerequisites for a build button."""
from __future__ import annotations

import arcade


def draw_tooltip(x: float, y: float, lines: list[str]) -> None:
    if not lines:
        return
    pad = 6
    line_height = 16
    width = 8 + max(len(line) for line in lines) * 8
    height = pad * 2 + line_height * len(lines)
    arcade.draw_lbwh_rectangle_filled(x, y, width, height, (10, 10, 14, 220))
    arcade.draw_lbwh_rectangle_outline(x, y, width, height, arcade.color.LIGHT_GRAY, 1)
    for i, line in enumerate(lines):
        arcade.draw_text(
            line,
            x=x + pad,
            y=y + height - pad - line_height * (i + 1) + 2,
            color=arcade.color.WHITE,
            font_size=11,
        )
