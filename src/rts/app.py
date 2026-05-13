"""GameApp — the Arcade window. Wires up the initial View."""
from __future__ import annotations

import arcade

from rts.config import WINDOW_HEIGHT, WINDOW_TITLE, WINDOW_WIDTH


class GameApp(arcade.Window):
    """Root Arcade window. Owns the active View."""

    def __init__(self) -> None:
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, resizable=True)
        from rts.ui.views.main_menu_view import MainMenuView

        self.show_view(MainMenuView())


def run() -> None:
    GameApp()
    arcade.run()
