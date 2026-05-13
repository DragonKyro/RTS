"""Game view — owns the GameWorld, HUD, and camera. Drives the simulation tick."""
from __future__ import annotations

from pathlib import Path

import arcade

from rts.ai.ai_player import AIPlayer
from rts.config import TILE_SIZE, WINDOW_HEIGHT, WINDOW_WIDTH
from rts.factions.faction import Faction
from rts.factions.terran_directorate import TerranDirectorate
from rts.player.human_player import HumanPlayer
from rts.ui.hud import HUD
from rts.world.game_map import GameMap
from rts.world.game_world import GameWorld


_DEFAULT_MAP_PATH = Path(__file__).resolve().parents[3].parent / "maps" / "default.json"


class GameView(arcade.View):
    """The in-match screen. Skeleton: shows an empty map + HUD shell. Click ESC to pause."""

    def __init__(self, *, player_faction: Faction) -> None:
        super().__init__()
        self._faction = player_faction
        self._world: GameWorld | None = None
        self._human: HumanPlayer | None = None
        self._ai: AIPlayer | None = None
        self._hud: HUD | None = None

    # --- Lifecycle ---------------------------------------------------------

    def on_show_view(self) -> None:
        arcade.set_background_color(arcade.color.DARK_GRAY)
        # Load map (fall back to a generated empty one if the file is missing).
        try:
            game_map = GameMap.load(_DEFAULT_MAP_PATH)
        except (FileNotFoundError, OSError):
            game_map = GameMap.empty(width=60, height=40)

        # Players — human + a single AI opponent (Terran by default, swap later).
        self._human = HumanPlayer(index=0, faction=self._faction)
        self._human.init_fog(game_map.width, game_map.height)
        self._ai = AIPlayer(index=1, faction=TerranDirectorate())
        self._ai.init_fog(game_map.width, game_map.height)

        self._world = GameWorld(game_map=game_map, players=[self._human, self._ai])
        self._hud = HUD(human_player=self._human, map_width=game_map.width, map_height=game_map.height)

    # --- Tick --------------------------------------------------------------

    def on_update(self, dt: float) -> None:
        if self._world is not None:
            self._world.update(dt)

    # --- Draw --------------------------------------------------------------

    def on_draw(self) -> None:
        self.clear()
        # TODO: draw terrain, fog of war, entities, projectiles, selection box.
        # For the skeleton we just stamp a "MATCH IN PROGRESS" placeholder and the HUD.
        arcade.draw_text(
            "MATCH IN PROGRESS — (skeleton; world rendering not yet implemented)",
            x=WINDOW_WIDTH / 2,
            y=WINDOW_HEIGHT * 0.55,
            color=arcade.color.LIGHT_GRAY,
            font_size=18,
            anchor_x="center",
        )
        arcade.draw_text(
            f"Playing as: {self._faction.display_name}",
            x=WINDOW_WIDTH / 2,
            y=WINDOW_HEIGHT * 0.48,
            color=self._faction.color,
            font_size=22,
            anchor_x="center",
        )
        arcade.draw_text(
            "ESC to return to main menu",
            x=WINDOW_WIDTH / 2,
            y=WINDOW_HEIGHT * 0.20,
            color=arcade.color.LIGHT_GRAY,
            font_size=14,
            anchor_x="center",
        )
        if self._hud is not None:
            self._hud.draw()

    # --- Input -------------------------------------------------------------

    def on_key_press(self, key: int, modifiers: int) -> None:
        if key == arcade.key.ESCAPE:
            from rts.ui.views.main_menu_view import MainMenuView

            self.window.show_view(MainMenuView())
