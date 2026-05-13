"""Default hotkey bindings. Single source of truth so views/HUD can render them."""
from __future__ import annotations

import arcade

# Camera scroll (also driven by mouse-edge scroll)
SCROLL_UP_KEYS = (arcade.key.W, arcade.key.UP)
SCROLL_DOWN_KEYS = (arcade.key.S, arcade.key.DOWN)
SCROLL_LEFT_KEYS = (arcade.key.A, arcade.key.LEFT)
SCROLL_RIGHT_KEYS = (arcade.key.D, arcade.key.RIGHT)

# Common commands
STOP_KEY = arcade.key.S          # context-dependent (when nothing else maps here)
ATTACK_MOVE_KEY = arcade.key.A
HOLD_POSITION_KEY = arcade.key.H

# Build menu / production hotkeys per faction are wired in faction-specific UI.

# System
PAUSE_KEY = arcade.key.P
QUIT_KEY = arcade.key.ESCAPE
