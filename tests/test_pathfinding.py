"""Tests for A* pathfinding."""
from __future__ import annotations

from rts.core.grid import NavGrid
from rts.core.pathfinding import find_path


def test_trivial_same_cell():
    g = NavGrid(5, 5)
    path = find_path(g, (1, 1), (1, 1))
    assert path == [(1, 1)]


def test_finds_straight_path():
    g = NavGrid(10, 10)
    path = find_path(g, (0, 0), (9, 0))
    assert path is not None
    assert path[0] == (0, 0)
    assert path[-1] == (9, 0)


def test_avoids_blocked_cells():
    g = NavGrid(7, 3)
    # Wall in the middle column except for the top cell — path must go around it.
    for y in range(2):
        g.set_blocked(3, y, True)
    path = find_path(g, (0, 0), (6, 0))
    assert path is not None
    # Path must not include any (3, y<2) cells
    for cell in path:
        assert cell not in {(3, 0), (3, 1)}


def test_returns_none_when_goal_blocked():
    g = NavGrid(5, 5)
    g.set_blocked(2, 2, True)
    assert find_path(g, (0, 0), (2, 2)) is None


def test_returns_none_when_goal_surrounded():
    g = NavGrid(5, 5)
    # Boxing in the goal makes it unreachable — A* can't step into it.
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]:
        g.set_blocked(2 + d[0], 2 + d[1], True)
    assert find_path(g, (0, 0), (2, 2)) is None


def test_out_of_bounds_returns_none():
    g = NavGrid(5, 5)
    assert find_path(g, (-1, 0), (3, 3)) is None
    assert find_path(g, (0, 0), (10, 10)) is None
