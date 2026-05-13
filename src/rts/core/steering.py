"""Steering — smooths A* path-following with neighbor avoidance.

The pathfinder returns coarse waypoints. Steering blends these with local repulsion
from nearby units so movement looks fluid instead of grid-locked.

This is a stub for the skeleton — it currently just path-follows without avoidance.
Replace `update_movement_with_avoidance` with proper steering when needed.
"""
from __future__ import annotations

import math
from typing import TYPE_CHECKING, Iterable

if TYPE_CHECKING:
    from rts.units.unit import Unit


def update_movement_with_avoidance(
    unit: "Unit",
    dt: float,
    neighbors: Iterable["Unit"],
    *,
    avoidance_radius: float = 24.0,
    avoidance_weight: float = 0.5,
) -> bool:
    """Advance unit along its path, nudging away from `neighbors` that are too close.

    Returns True if the unit reached the final waypoint this tick.
    """
    if not unit.path:
        return False

    tx, ty = unit.path[0]
    dx, dy = tx - unit.x, ty - unit.y
    dist = math.hypot(dx, dy)

    # Base direction toward the waypoint
    if dist > 0.0:
        ux, uy = dx / dist, dy / dist
    else:
        ux, uy = 0.0, 0.0

    # Repulsion from neighbors
    rx, ry = 0.0, 0.0
    for other in neighbors:
        if other is unit:
            continue
        ox, oy = unit.x - other.x, unit.y - other.y
        d = math.hypot(ox, oy)
        if 0.0 < d < avoidance_radius:
            strength = (avoidance_radius - d) / avoidance_radius
            rx += ox / d * strength
            ry += oy / d * strength

    # Blend
    vx = ux + rx * avoidance_weight
    vy = uy + ry * avoidance_weight
    mag = math.hypot(vx, vy)
    if mag > 0.0:
        vx /= mag
        vy /= mag

    step = unit.speed * dt
    if dist <= step:
        unit.x, unit.y = tx, ty
        unit.path.pop(0)
        return not unit.path
    unit.x += vx * step
    unit.y += vy * step
    return False
