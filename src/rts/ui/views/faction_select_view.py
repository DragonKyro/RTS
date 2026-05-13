"""Faction selection screen — arrow keys to pick a faction, ENTER to start a match."""
from __future__ import annotations

import arcade

from rts.config import WINDOW_HEIGHT, WINDOW_WIDTH
from rts.factions import ALL_FACTIONS


class FactionSelectView(arcade.View):
    def __init__(self) -> None:
        super().__init__()
        self._selected = 0
        self._faction_instances = [cls() for cls in ALL_FACTIONS]

    def on_show_view(self) -> None:
        arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)

    def on_draw(self) -> None:
        self.clear()
        arcade.draw_text(
            "SELECT FACTION",
            x=WINDOW_WIDTH / 2,
            y=WINDOW_HEIGHT * 0.85,
            color=arcade.color.WHITE,
            font_size=36,
            anchor_x="center",
        )
        for i, faction in enumerate(self._faction_instances):
            highlighted = i == self._selected
            color = arcade.color.YELLOW if highlighted else arcade.color.LIGHT_GRAY
            label = ("> " if highlighted else "  ") + faction.display_name
            arcade.draw_text(
                label,
                x=WINDOW_WIDTH / 2,
                y=WINDOW_HEIGHT * (0.60 - 0.10 * i),
                color=color,
                font_size=24,
                anchor_x="center",
            )
        arcade.draw_text(
            "UP/DOWN to choose  -  ENTER to start  -  ESC to go back",
            x=WINDOW_WIDTH / 2,
            y=WINDOW_HEIGHT * 0.12,
            color=arcade.color.LIGHT_GRAY,
            font_size=14,
            anchor_x="center",
        )

    def on_key_press(self, key: int, modifiers: int) -> None:
        if key in (arcade.key.UP, arcade.key.W):
            self._selected = (self._selected - 1) % len(self._faction_instances)
        elif key in (arcade.key.DOWN, arcade.key.S):
            self._selected = (self._selected + 1) % len(self._faction_instances)
        elif key in (arcade.key.ENTER, arcade.key.RETURN):
            from rts.ui.views.game_view import GameView

            faction = self._faction_instances[self._selected]
            self.window.show_view(GameView(player_faction=faction))
        elif key == arcade.key.ESCAPE:
            from rts.ui.views.main_menu_view import MainMenuView

            self.window.show_view(MainMenuView())
