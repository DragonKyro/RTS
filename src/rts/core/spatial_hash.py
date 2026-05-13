"""Spatial hash — broadphase for selection / range / neighbor queries.

Buckets entities by cell. O(1) insert/remove; querying a rectangle or radius
returns only the entities in the overlapping cells, much faster than scanning all.
"""
from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING, Iterable, Iterator

if TYPE_CHECKING:
    from rts.core.entity import Entity


class SpatialHash:
    def __init__(self, cell_size: float) -> None:
        self.cell_size = float(cell_size)
        self._buckets: dict[tuple[int, int], set] = defaultdict(set)
        self._entity_cell: dict[int, tuple[int, int]] = {}

    def _cell(self, x: float, y: float) -> tuple[int, int]:
        return int(x // self.cell_size), int(y // self.cell_size)

    def insert(self, entity: "Entity") -> None:
        cell = self._cell(entity.x, entity.y)
        self._buckets[cell].add(entity)
        self._entity_cell[entity.id] = cell

    def remove(self, entity: "Entity") -> None:
        cell = self._entity_cell.pop(entity.id, None)
        if cell is not None:
            self._buckets[cell].discard(entity)

    def update(self, entity: "Entity") -> None:
        """Re-bucket after the entity moved."""
        new_cell = self._cell(entity.x, entity.y)
        old_cell = self._entity_cell.get(entity.id)
        if old_cell == new_cell:
            return
        if old_cell is not None:
            self._buckets[old_cell].discard(entity)
        self._buckets[new_cell].add(entity)
        self._entity_cell[entity.id] = new_cell

    def query_rect(self, x0: float, y0: float, x1: float, y1: float) -> Iterator["Entity"]:
        if x1 < x0:
            x0, x1 = x1, x0
        if y1 < y0:
            y0, y1 = y1, y0
        cx0, cy0 = self._cell(x0, y0)
        cx1, cy1 = self._cell(x1, y1)
        seen: set[int] = set()
        for cx in range(cx0, cx1 + 1):
            for cy in range(cy0, cy1 + 1):
                for e in self._buckets.get((cx, cy), ()):
                    if e.id in seen:
                        continue
                    seen.add(e.id)
                    if x0 <= e.x <= x1 and y0 <= e.y <= y1:
                        yield e

    def query_radius(self, x: float, y: float, radius: float) -> Iterator["Entity"]:
        r2 = radius * radius
        for e in self.query_rect(x - radius, y - radius, x + radius, y + radius):
            dx, dy = e.x - x, e.y - y
            if dx * dx + dy * dy <= r2:
                yield e

    def all_entities(self) -> Iterable["Entity"]:
        seen: set[int] = set()
        for bucket in self._buckets.values():
            for e in bucket:
                if e.id not in seen:
                    seen.add(e.id)
                    yield e
