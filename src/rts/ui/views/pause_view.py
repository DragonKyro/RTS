"""Pause overlay — freeze the game tick and show a small menu."""
from __future__ import annotations

import arcade

from rts.config import WINDOW_HEIGHT, WINDOW_WIDTH


class PauseView(arcade.View):
    def __init__(self, resume_view: arcade.View) -> None:
        super().__init__()
        self._resume_view = resume_view

    def on_draw(self) -> None:
        # Draw the underlying view first so the pause overlay sits on top.
        self._resume_view.on_draw()
        arcade.draw_lbwh_rectangle_filled(
            0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, (0, 0, 0, 160)
        )
        arcade.draw_text(
            "PAUSED",
            x=WINDOW_WIDTH / 2,
            y=WINDOW_HEIGHT / 2,
            color=arcade.color.WHITE,
            font_size=48,
            anchor_x="center",
            anchor_y="center",
        )
        arcade.draw_text(
            "ESC or P to resume",
            x=WINDOW_WIDTH / 2,
            y=WINDOW_HEIGHT / 2 - 50,
            color=arcade.color.LIGHT_GRAY,
            font_size=16,
            anchor_x="center",
        )

    def on_key_press(self, key: int, modifiers: int) -> None:
        if key in (arcade.key.ESCAPE, arcade.key.P):
            self.window.show_view(self._resume_view)
