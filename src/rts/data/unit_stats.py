"""Per-unit stat blocks. Concrete unit classes pull from here at construction.

Add new units by appending a dataclass instance — don't bake stats into class bodies.
"""
from __future__ import annotations

from dataclasses import dataclass

from rts.core.resources import ResourceCost


@dataclass(frozen=True)
class UnitStats:
    hp: int
    speed: float
    radius: float
    armor_class: str
    cost: ResourceCost
    build_time: float
    supply_cost: int = 1
    # Combat (Attacker mixin) — None if not a combat unit
    damage: int = 0
    damage_type: str = "kinetic"
    attack_range: float = 0.0
    attack_cooldown: float = 1.0
    # Worker (Gatherer mixin) — defaults are ignored unless used
    carry_capacity: int = 0
    gather_rate: float = 0.0


# --- Terran Directorate -------------------------------------------------------

TERRAN_ENGINEER_STATS = UnitStats(
    hp=40,
    speed=80.0,
    radius=10.0,
    armor_class="light",
    cost=ResourceCost(metals=50),
    build_time=8.0,
    supply_cost=1,
    carry_capacity=10,
    gather_rate=1.0,
)
