"""Tests for NavGrid — coord conversion, occupancy, neighbor queries."""
from __future__ import annotations

from rts.core.grid import NavGrid


def test_coord_round_trip():
    g = NavGrid(width=10, height=10, tile_size=32)
    cx, cy = g.world_to_cell(40, 80)
    assert (cx, cy) == (1, 2)
    wx, wy = g.cell_to_world(1, 2)
    # cell_to_world returns the cell center
    assert wx == 1.5 * 32
    assert wy == 2.5 * 32


def test_bounds():
    g = NavGrid(5, 5)
    assert g.in_bounds(0, 0)
    assert g.in_bounds(4, 4)
    assert not g.in_bounds(-1, 0)
    assert not g.in_bounds(5, 0)
    assert not g.in_bounds(0, 5)


def test_block_and_unblock_rect():
    g = NavGrid(10, 10)
    assert g.rect_is_free(2, 2, 3, 3)
    g.block_rect(2, 2, 3, 3)
    assert not g.rect_is_free(2, 2, 3, 3)
    assert not g.is_passable(3, 3)
    assert g.is_passable(5, 2)  # just outside the block
    g.unblock_rect(2, 2, 3, 3)
    assert g.rect_is_free(2, 2, 3, 3)


def test_neighbors_skips_blocked_and_diagonal_corner_cuts():
    g = NavGrid(5, 5)
    # Block the cell directly to the right of (2,2) and above (2,2).
    # Then (3,3) (a diagonal of (2,2)) should be excluded due to corner-cutting.
    g.set_blocked(3, 2, True)   # right neighbor
    g.set_blocked(2, 3, True)   # top neighbor
    neighbors = set(g.neighbors(2, 2))
    assert (3, 2) not in neighbors  # directly blocked
    assert (2, 3) not in neighbors  # directly blocked
    assert (3, 3) not in neighbors  # would cut through both blocked neighbors
    assert (1, 2) in neighbors      # left is open
    assert (2, 1) in neighbors      # bottom is open
