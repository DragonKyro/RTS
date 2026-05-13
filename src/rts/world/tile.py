"""Tile types — terrain categorization for the game map."""
from __future__ import annotations

from enum import Enum


class TileType(Enum):
    PASSABLE = "passable"        # Open terrain — units may walk, buildings may be placed
    BUILD_ONLY = "build_only"    # Mining-grade rock etc. — buildings ok, units can pass
    BLOCKED = "blocked"          # Cliffs, deep void — nothing
    WATER = "water"              # Air-only (or future amphibious units)


class Tile:
    """Lightweight per-cell terrain record."""

    __slots__ = ("type", "elevation")

    def __init__(self, tile_type: TileType = TileType.PASSABLE, elevation: int = 0) -> None:
        self.type = tile_type
        self.elevation = elevation

    @property
    def passable_for_ground(self) -> bool:
        return self.type in (TileType.PASSABLE, TileType.BUILD_ONLY)

    @property
    def buildable(self) -> bool:
        return self.type in (TileType.PASSABLE, TileType.BUILD_ONLY)
