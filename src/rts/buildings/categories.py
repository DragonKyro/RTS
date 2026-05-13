"""Building category bases — concrete buildings extend one of these."""
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from rts.buildings.building import Building
from rts.core.mixins import Attacker, Producer

if TYPE_CHECKING:
    from rts.player.player import Player
    from rts.world.game_world import GameWorld


class ProductionBuilding(Building, Producer):
    """Queues and produces units (e.g. Barracks, Vehicle Bay, Spaceport)."""

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.init_producer()


class DefenseBuilding(Building, Attacker):
    """Static defenses (turrets). Pre-set the Attacker attributes in subclass __init__."""


class ResourceBuilding(Building):
    """Refineries / collectors — drop-off point for workers."""


class ResearchBuilding(Building):
    """Houses upgrade research."""


class UtilityBuilding(Building):
    """Power, supply cap, sensors — passive economy/support."""
