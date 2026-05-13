"""Selection — the local human player's currently-selected entities + control groups."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from rts.core.entity import Entity


class Selection:
    def __init__(self) -> None:
        self.current: list["Entity"] = []
        self.groups: dict[int, list["Entity"]] = {}   # Ctrl+1..9 control groups

    def clear(self) -> None:
        self.current = []

    def set(self, entities: list["Entity"]) -> None:
        self.current = [e for e in entities if e.alive]

    def add(self, entities: list["Entity"]) -> None:
        for e in entities:
            if e.alive and e not in self.current:
                self.current.append(e)

    def remove_dead(self) -> None:
        self.current = [e for e in self.current if e.alive]

    def assign_group(self, group_id: int) -> None:
        self.groups[group_id] = list(self.current)

    def recall_group(self, group_id: int) -> None:
        if group_id in self.groups:
            self.current = [e for e in self.groups[group_id] if e.alive]
