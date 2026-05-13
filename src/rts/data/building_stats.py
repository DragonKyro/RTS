"""Per-building stat blocks."""
from __future__ import annotations

from dataclasses import dataclass

from rts.core.resources import ResourceCost


@dataclass(frozen=True)
class BuildingStats:
    hp: int
    footprint: tuple[int, int]   # (w_cells, h_cells)
    armor_class: str
    cost: ResourceCost
    build_time: float
    supply_provided: int = 0
    power_provided: int = 0
    power_required: int = 0


TERRAN_HQ_STATS = BuildingStats(
    hp=1500,
    footprint=(4, 4),
    armor_class="heavy",
    cost=ResourceCost(metals=400),
    build_time=60.0,
    supply_provided=10,
)
