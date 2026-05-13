"""Faction — a registry of what a side can build and how it starts.

Factions are NOT god classes. They expose:
- `building_roster` and `unit_roster` (name -> class)
- `starting_units` and `starting_resources`
- `tech_tree` (prerequisite graph for builds)
- `color`, `display_name`, `theme_tag` (drives art folder lookup)
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from rts.config import DEFAULT_STARTING_HELIUM3, DEFAULT_STARTING_METALS
from rts.core.resources import ResourcePool
from rts.core.tech_tree import TechTree

if TYPE_CHECKING:
    from rts.buildings.building import Building
    from rts.units.unit import Unit


class Faction:
    """Base class. Concrete factions override the class attributes."""

    display_name: str = "Unnamed Faction"
    theme_tag: str = "default"
    color: tuple[int, int, int] = (200, 200, 200)

    building_roster: dict[str, type["Building"]] = {}
    unit_roster: dict[str, type["Unit"]] = {}

    starting_buildings: list[str] = []   # roster keys
    starting_units: list[tuple[str, int]] = []   # (roster key, count)
    starting_metals: int = DEFAULT_STARTING_METALS
    starting_helium3: int = DEFAULT_STARTING_HELIUM3

    def __init__(self) -> None:
        self.tech_tree = self._build_tech_tree()

    def _build_tech_tree(self) -> TechTree:
        """Override per faction to declare prerequisites between buildings/units."""
        return TechTree()

    def make_starting_resources(self) -> ResourcePool:
        return ResourcePool(metals=self.starting_metals, helium3=self.starting_helium3)

    def __repr__(self) -> str:
        return f"<Faction {self.display_name}>"
