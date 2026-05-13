"""A* pathfinding on a NavGrid."""
from __future__ import annotations

import heapq
import math
from typing import Optional

from rts.core.grid import NavGrid


_SQRT2 = math.sqrt(2)


def _heuristic(a: tuple[int, int], b: tuple[int, int]) -> float:
    """Octile distance — admissible for 8-way movement with diagonal cost √2."""
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    return (dx + dy) + (_SQRT2 - 2) * min(dx, dy)


def _step_cost(a: tuple[int, int], b: tuple[int, int]) -> float:
    return _SQRT2 if (a[0] != b[0] and a[1] != b[1]) else 1.0


def find_path(
    grid: NavGrid,
    start_cell: tuple[int, int],
    goal_cell: tuple[int, int],
    *,
    max_expansions: int = 100_000,
) -> Optional[list[tuple[int, int]]]:
    """Return list of cells from start to goal (inclusive), or None if unreachable.

    Both endpoints must be in-bounds. If the goal is blocked, no path is returned —
    callers wanting "as close as possible" should retry with a free adjacent cell.
    """
    if not grid.in_bounds(*start_cell) or not grid.in_bounds(*goal_cell):
        return None
    if not grid.is_passable(*goal_cell):
        return None
    if start_cell == goal_cell:
        return [start_cell]

    open_heap: list[tuple[float, int, tuple[int, int]]] = []
    counter = 0
    heapq.heappush(open_heap, (0.0, counter, start_cell))

    came_from: dict[tuple[int, int], tuple[int, int]] = {}
    g_score: dict[tuple[int, int], float] = {start_cell: 0.0}

    expansions = 0
    while open_heap:
        expansions += 1
        if expansions > max_expansions:
            return None

        _, _, current = heapq.heappop(open_heap)
        if current == goal_cell:
            # Reconstruct path
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        for neighbor in grid.neighbors(*current):
            tentative_g = g_score[current] + _step_cost(current, neighbor)
            if tentative_g < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + _heuristic(neighbor, goal_cell)
                counter += 1
                heapq.heappush(open_heap, (f, counter, neighbor))

    return None


def cells_to_world_waypoints(
    grid: NavGrid, cells: list[tuple[int, int]]
) -> list[tuple[float, float]]:
    """Convert a list of grid cells to world-space waypoints (cell centers)."""
    return [grid.cell_to_world(cx, cy) for cx, cy in cells]
