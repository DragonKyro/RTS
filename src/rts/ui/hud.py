"""HUD — top resource bar + bottom command/info shell. Owned by GameView."""
from __future__ import annotations

from typing import TYPE_CHECKING

import arcade

from rts.config import WINDOW_HEIGHT, WINDOW_WIDTH
from rts.ui.minimap import Minimap

if TYPE_CHECKING:
    from rts.player.human_player import HumanPlayer


_TOP_BAR_HEIGHT = 32
_BOTTOM_BAR_HEIGHT = 140
_MINIMAP_SIZE = 140


class HUD:
    def __init__(self, *, human_player: "HumanPlayer", map_width: int, map_height: int) -> None:
        self._human = human_player
        self._minimap = Minimap(map_width=map_width, map_height=map_height, size=_MINIMAP_SIZE)

    def draw(self) -> None:
        self._draw_top_bar()
        self._draw_bottom_bar()
        self._minimap.draw(
            x=WINDOW_WIDTH - _MINIMAP_SIZE - 8,
            y=8,
        )

    def _draw_top_bar(self) -> None:
        arcade.draw_lbwh_rectangle_filled(
            0, WINDOW_HEIGHT - _TOP_BAR_HEIGHT, WINDOW_WIDTH, _TOP_BAR_HEIGHT, (20, 24, 32)
        )
        res = self._human.resources
        arcade.draw_text(
            f"Metals: {res.metals}    Helium-3: {res.helium3}    "
            f"Supply: {self._human.supply_used}/{self._human.supply_cap}",
            x=12,
            y=WINDOW_HEIGHT - _TOP_BAR_HEIGHT + 8,
            color=arcade.color.WHITE,
            font_size=14,
        )
        arcade.draw_text(
            self._human.faction.display_name,
            x=WINDOW_WIDTH - 12,
            y=WINDOW_HEIGHT - _TOP_BAR_HEIGHT + 8,
            color=self._human.faction.color,
            font_size=14,
            anchor_x="right",
        )

    def _draw_bottom_bar(self) -> None:
        arcade.draw_lbwh_rectangle_filled(
            0, 0, WINDOW_WIDTH, _BOTTOM_BAR_HEIGHT, (20, 24, 32)
        )
        # TODO: selection portrait + stats panel + context-sensitive command panel.
        arcade.draw_text(
            "(command panel — stub)",
            x=12,
            y=_BOTTOM_BAR_HEIGHT - 22,
            color=arcade.color.LIGHT_GRAY,
            font_size=12,
        )
