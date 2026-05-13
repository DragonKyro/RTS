"""Keyboard handling — track held keys for camera scrolling, modifiers, hotkeys."""
from __future__ import annotations


class KeyboardHandler:
    def __init__(self) -> None:
        self._held: set[int] = set()

    def press(self, key: int) -> None:
        self._held.add(key)

    def release(self, key: int) -> None:
        self._held.discard(key)

    def is_held(self, key: int) -> bool:
        return key in self._held

    def any_held(self, keys) -> bool:
        return any(k in self._held for k in keys)
