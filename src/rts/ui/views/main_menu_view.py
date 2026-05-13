"""Main menu — title screen. Press SPACE to play, ESC to quit."""
from __future__ import annotations

import arcade

from rts.config import WINDOW_HEIGHT, WINDOW_WIDTH


class MainMenuView(arcade.View):
    def on_show_view(self) -> None:
        arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)

    def on_draw(self) -> None:
        self.clear()
        arcade.draw_text(
            "SOLAR FRONTIER WARS",
            x=WINDOW_WIDTH / 2,
            y=WINDOW_HEIGHT * 0.66,
            color=arcade.color.WHITE,
            font_size=48,
            anchor_x="center",
        )
        arcade.draw_text(
            "A real-time strategy in the StarCraft / C&C tradition",
            x=WINDOW_WIDTH / 2,
            y=WINDOW_HEIGHT * 0.58,
            color=arcade.color.LIGHT_GRAY,
            font_size=16,
            anchor_x="center",
        )
        arcade.draw_text(
            "Press SPACE to start  -  ESC to quit",
            x=WINDOW_WIDTH / 2,
            y=WINDOW_HEIGHT * 0.30,
            color=arcade.color.LIGHT_GRAY,
            font_size=20,
            anchor_x="center",
        )

    def on_key_press(self, key: int, modifiers: int) -> None:
        if key == arcade.key.SPACE:
            from rts.ui.views.faction_select_view import FactionSelectView

            self.window.show_view(FactionSelectView())
        elif key == arcade.key.ESCAPE:
            self.window.close()
