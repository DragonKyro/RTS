"""Lightweight pub/sub bus for game events.

Decouples producers ("unit died") from consumers (UI, AI threat map, sound system).
"""
from __future__ import annotations

from collections import defaultdict
from typing import Callable


class EventBus:
    def __init__(self) -> None:
        self._listeners: dict[str, list[Callable[[dict], None]]] = defaultdict(list)

    def subscribe(self, event: str, handler: Callable[[dict], None]) -> None:
        self._listeners[event].append(handler)

    def unsubscribe(self, event: str, handler: Callable[[dict], None]) -> None:
        if handler in self._listeners.get(event, ()):
            self._listeners[event].remove(handler)

    def publish(self, event: str, payload: dict | None = None) -> None:
        payload = payload or {}
        # Iterate over a copy so handlers can subscribe/unsubscribe during dispatch.
        for handler in list(self._listeners.get(event, ())):
            handler(payload)
