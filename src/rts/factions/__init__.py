"""Faction definitions — Terran Directorate, Belt Syndicate, Synthetic Collective."""

from rts.factions.belt_syndicate import BeltSyndicate
from rts.factions.faction import Faction
from rts.factions.synthetic_collective import SyntheticCollective
from rts.factions.terran_directorate import TerranDirectorate

ALL_FACTIONS: list[type[Faction]] = [
    TerranDirectorate,
    BeltSyndicate,
    SyntheticCollective,
]

__all__ = [
    "Faction",
    "TerranDirectorate",
    "BeltSyndicate",
    "SyntheticCollective",
    "ALL_FACTIONS",
]
