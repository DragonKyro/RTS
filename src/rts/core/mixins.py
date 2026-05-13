"""Behavior mixins — composed onto Entity subclasses.

Mixins are *attribute-protocol* style: they provide methods and expect their host
to have set the required attributes. Subclasses initialize attributes explicitly
(no cooperative __init__ kwargs juggling).
"""
from __future__ import annotations

import math
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from rts.core.entity import Entity


class Damageable:
    """Host must set: hp, max_hp, armor_class."""

    hp: int
    max_hp: int
    armor_class: str

    def take_damage(self, amount: int, damage_type: str = "kinetic") -> None:
        self.hp -= int(amount)
        if self.hp <= 0:
            self.hp = 0
            self.on_death()

    def on_death(self) -> None:
        # Default: destroy self. Subclasses can override (e.g. for death animations).
        if hasattr(self, "destroy"):
            self.destroy()  # type: ignore[attr-defined]


class Attacker:
    """Host must set: x, y, damage, damage_type, attack_range, attack_cooldown."""

    x: float
    y: float
    damage: int
    damage_type: str
    attack_range: float
    attack_cooldown: float

    _cooldown_remaining: float = 0.0
    target: Optional["Entity"] = None

    def in_range_of(self, other: "Entity") -> bool:
        dx, dy = other.x - self.x, other.y - self.y
        return dx * dx + dy * dy <= self.attack_range * self.attack_range

    def try_attack(self, dt: float) -> bool:
        """Tick the cooldown and attack the current target if possible. Returns True if attacked."""
        self._cooldown_remaining = max(0.0, self._cooldown_remaining - dt)
        target = self.target
        if target is None or not target.alive:
            return False
        if self._cooldown_remaining > 0.0:
            return False
        if not self.in_range_of(target):
            return False
        if hasattr(target, "take_damage"):
            target.take_damage(self.damage, self.damage_type)  # type: ignore[attr-defined]
        self._cooldown_remaining = self.attack_cooldown
        return True


class Movable:
    """Host must set: x, y, speed. Mixin manages `path` (list of (x,y) waypoints)."""

    x: float
    y: float
    speed: float

    path: list[tuple[float, float]]

    def init_movable(self) -> None:
        """Optional helper — subclasses should call this in __init__ to ensure `path` exists."""
        self.path = []

    def set_destination(
        self,
        dest: tuple[float, float],
        path: Optional[list[tuple[float, float]]] = None,
    ) -> None:
        if path is None:
            self.path = [dest]
        else:
            self.path = list(path)

    def stop(self) -> None:
        self.path = []

    def update_movement(self, dt: float) -> bool:
        """Advance one tick along the path. Returns True if reached the final waypoint this tick."""
        if not self.path:
            return False
        tx, ty = self.path[0]
        dx, dy = tx - self.x, ty - self.y
        dist = math.hypot(dx, dy)
        step = self.speed * dt
        if dist <= step or dist == 0.0:
            self.x, self.y = tx, ty
            self.path.pop(0)
            return not self.path
        self.x += dx / dist * step
        self.y += dy / dist * step
        return False


class Producer:
    """Host must set: production_queue, production_progress (float seconds), rally_point.

    Use `init_producer()` to set defaults.
    """

    production_queue: list[type]
    production_progress: float
    rally_point: Optional[tuple[float, float]]

    def init_producer(self) -> None:
        self.production_queue = []
        self.production_progress = 0.0
        self.rally_point = None

    def enqueue(self, unit_type: type) -> None:
        self.production_queue.append(unit_type)

    def cancel_last(self) -> Optional[type]:
        if self.production_queue:
            return self.production_queue.pop()
        return None

    def update_production(self, dt: float, build_time_lookup) -> Optional[type]:
        """Advance production. Returns a finished unit type to spawn, or None.

        build_time_lookup: callable taking a unit type, returning its build_time in seconds.
        """
        if not self.production_queue:
            return None
        current = self.production_queue[0]
        self.production_progress += dt
        if self.production_progress >= build_time_lookup(current):
            self.production_progress = 0.0
            return self.production_queue.pop(0)
        return None


class Gatherer:
    """Host must set: carry_capacity, gather_rate, carrying (int), carrying_kind."""

    carry_capacity: int
    gather_rate: float
    carrying: int
    carrying_kind: Optional[str]

    def init_gatherer(self, carry_capacity: int = 10, gather_rate: float = 1.0) -> None:
        self.carry_capacity = carry_capacity
        self.gather_rate = gather_rate
        self.carrying = 0
        self.carrying_kind = None

    @property
    def is_full(self) -> bool:
        return self.carrying >= self.carry_capacity
