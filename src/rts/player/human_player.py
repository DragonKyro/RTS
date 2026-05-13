"""HumanPlayer — Player bound to mouse / keyboard input + on-screen selection."""
from __future__ import annotations

from rts.player.player import Player
from rts.player.selection import Selection


class HumanPlayer(Player):
    def __init__(self, *, index: int, faction) -> None:
        super().__init__(index=index, faction=faction, is_human=True)
        self.selection = Selection()
