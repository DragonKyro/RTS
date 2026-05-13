"""GameMap — terrain grid + resource node + spawn point definitions.

Maps are loaded from JSON files in `maps/`. See `maps/default.json` for the schema.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

from rts.config import TILE_SIZE
from rts.core.resources import ResourceKind
from rts.world.tile import Tile, TileType


@dataclass
class ResourceNodeSpec:
    kind: ResourceKind
    x: int   # cell
    y: int   # cell
    amount: int = 1500


@dataclass
class SpawnSpec:
    player_index: int
    x: int   # cell
    y: int   # cell


@dataclass
class GameMap:
    width: int   # cells
    height: int  # cells
    tile_size: int = TILE_SIZE
    tiles: list[list[Tile]] = field(default_factory=list)
    resource_nodes: list[ResourceNodeSpec] = field(default_factory=list)
    spawns: list[SpawnSpec] = field(default_factory=list)
    name: str = "default"

    @classmethod
    def empty(cls, width: int, height: int) -> "GameMap":
        tiles = [[Tile(TileType.PASSABLE) for _ in range(height)] for _ in range(width)]
        return cls(width=width, height=height, tiles=tiles)

    @classmethod
    def load(cls, path: str | Path) -> "GameMap":
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        w, h = int(data["width"]), int(data["height"])
        # Tiles: optional. Default to all-passable if not provided.
        raw_tiles = data.get("tiles")
        if raw_tiles:
            tiles = [
                [Tile(TileType(raw_tiles[x][y])) for y in range(h)]
                for x in range(w)
            ]
        else:
            tiles = [[Tile(TileType.PASSABLE) for _ in range(h)] for _ in range(w)]

        resources = [
            ResourceNodeSpec(
                kind=ResourceKind(n["kind"]),
                x=int(n["x"]),
                y=int(n["y"]),
                amount=int(n.get("amount", 1500)),
            )
            for n in data.get("resource_nodes", [])
        ]
        spawns = [
            SpawnSpec(player_index=int(s["player"]), x=int(s["x"]), y=int(s["y"]))
            for s in data.get("spawns", [])
        ]
        return cls(
            width=w,
            height=h,
            tile_size=int(data.get("tile_size", TILE_SIZE)),
            tiles=tiles,
            resource_nodes=resources,
            spawns=spawns,
            name=str(data.get("name", Path(path).stem)),
        )
