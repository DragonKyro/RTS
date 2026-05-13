"""Unit category bases — concrete units extend one of these."""
from __future__ import annotations

from rts.core.mixins import Attacker, Gatherer
from rts.units.unit import Unit


class WorkerUnit(Unit, Gatherer):
    """Workers harvest resources and build buildings.

    Subclass __init__ should call self.init_gatherer(...) with carry params.
    """

    can_construct: bool = True


class InfantryUnit(Unit, Attacker):
    """Light, foot-mobile combat unit."""


class VehicleUnit(Unit, Attacker):
    """Tracked / wheeled / hover vehicle. Heavier armor, slower production."""


class AirUnit(Unit, Attacker):
    """Flying unit — bypasses ground nav grid; only intercepted by anti-air."""

    is_air: bool = True


class HeroUnit(Unit, Attacker):
    """Optional faction-defining elite. Typically one-per-player and expensive."""
