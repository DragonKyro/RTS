"""Scouting — pick a scout, send it to high-value cells, record what's seen."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from rts.ai.ai_player import AIPlayer
    from rts.world.game_world import GameWorld


def pick_next_scout_target(
    player: "AIPlayer", world: "GameWorld"
) -> tuple[int, int] | None:
    """Return a cell the scout should investigate next, or None if no priorities.

    Priorities (TODO): enemy spawn estimate → contested resource nodes → map corners.
    """
    # Skeleton: return None so the AI doesn't scout yet.
    return None
