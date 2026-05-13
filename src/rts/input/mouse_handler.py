"""Mouse handling — left-click select, drag-box select, right-click context command."""
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from rts.player.human_player import HumanPlayer
    from rts.world.game_world import GameWorld


class MouseHandler:
    """Holds drag-box state and turns mouse events into selection / commands.

    Skeleton: just records the drag rectangle. Real selection + command issuing
    plugs into the game view's on_mouse_* callbacks.
    """

    def __init__(self) -> None:
        self.drag_start: Optional[tuple[float, float]] = None
        self.drag_end: Optional[tuple[float, float]] = None
        self.is_dragging: bool = False

    def begin_drag(self, world_x: float, world_y: float) -> None:
        self.drag_start = (world_x, world_y)
        self.drag_end = (world_x, world_y)
        self.is_dragging = True

    def update_drag(self, world_x: float, world_y: float) -> None:
        if self.is_dragging:
            self.drag_end = (world_x, world_y)

    def end_drag(self) -> tuple[tuple[float, float], tuple[float, float]] | None:
        if not self.is_dragging or self.drag_start is None or self.drag_end is None:
            self.is_dragging = False
            return None
        rect = (self.drag_start, self.drag_end)
        self.drag_start = None
        self.drag_end = None
        self.is_dragging = False
        return rect
