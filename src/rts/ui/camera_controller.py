"""Camera controller — WASD / arrow keys + edge-scroll + zoom. Wraps an Arcade Camera2D."""
from __future__ import annotations

from typing import Optional

from rts.config import CAMERA_EDGE_SCROLL_MARGIN, CAMERA_SCROLL_SPEED


class CameraController:
    """Tracks camera position + zoom; the GameView reads `.position` for rendering.

    Decoupled from `arcade.Camera2D` so the module imports cleanly without arcade.
    The view bridges the two by reading `position` each frame.
    """

    def __init__(self, *, world_width: float, world_height: float, viewport: tuple[int, int]) -> None:
        self.world_width = world_width
        self.world_height = world_height
        self.viewport_w, self.viewport_h = viewport
        self.position: tuple[float, float] = (world_width / 2, world_height / 2)
        self.zoom: float = 1.0
        self.mouse_pos: Optional[tuple[int, int]] = None
        self.keys_held: set[int] = set()

    def update(self, dt: float, scroll_keys: dict[str, tuple[int, ...]]) -> None:
        dx, dy = 0.0, 0.0
        if any(k in self.keys_held for k in scroll_keys.get("left", ())):
            dx -= 1
        if any(k in self.keys_held for k in scroll_keys.get("right", ())):
            dx += 1
        if any(k in self.keys_held for k in scroll_keys.get("up", ())):
            dy += 1
        if any(k in self.keys_held for k in scroll_keys.get("down", ())):
            dy -= 1
        if self.mouse_pos is not None:
            mx, my = self.mouse_pos
            if mx < CAMERA_EDGE_SCROLL_MARGIN:
                dx -= 1
            elif mx > self.viewport_w - CAMERA_EDGE_SCROLL_MARGIN:
                dx += 1
            if my < CAMERA_EDGE_SCROLL_MARGIN:
                dy -= 1
            elif my > self.viewport_h - CAMERA_EDGE_SCROLL_MARGIN:
                dy += 1
        if dx == 0.0 and dy == 0.0:
            return
        px, py = self.position
        px += dx * CAMERA_SCROLL_SPEED * dt
        py += dy * CAMERA_SCROLL_SPEED * dt
        # Clamp to world bounds
        px = max(0.0, min(self.world_width, px))
        py = max(0.0, min(self.world_height, py))
        self.position = (px, py)
