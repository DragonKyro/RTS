"""End-screen — victory or defeat. Press ENTER to return to the main menu."""
from __future__ import annotations

import arcade

from rts.config import WINDOW_HEIGHT, WINDOW_WIDTH


class EndScreenView(arcade.View):
    def __init__(self, *, victory: bool, message: str = "") -> None:
        super().__init__()
        self._victory = victory
        self._message = message

    def on_draw(self) -> None:
        self.clear()
        title = "VICTORY" if self._victory else "DEFEAT"
        color = arcade.color.GOLD if self._victory else arcade.color.DARK_RED
        arcade.draw_text(
            title,
            x=WINDOW_WIDTH / 2,
            y=WINDOW_HEIGHT * 0.6,
            color=color,
            font_size=72,
            anchor_x="center",
        )
        if self._message:
            arcade.draw_text(
                self._message,
                x=WINDOW_WIDTH / 2,
                y=WINDOW_HEIGHT * 0.45,
                color=arcade.color.LIGHT_GRAY,
                font_size=18,
                anchor_x="center",
            )
        arcade.draw_text(
            "Press ENTER to return to menu",
            x=WINDOW_WIDTH / 2,
            y=WINDOW_HEIGHT * 0.20,
            color=arcade.color.LIGHT_GRAY,
            font_size=14,
            anchor_x="center",
        )

    def on_key_press(self, key: int, modifiers: int) -> None:
        if key in (arcade.key.ENTER, arcade.key.RETURN, arcade.key.ESCAPE):
            from rts.ui.views.main_menu_view import MainMenuView

            self.window.show_view(MainMenuView())
