"""Synthetic Collective — high-tech, expensive, AI/robotic. Late-game powerhouse."""
from __future__ import annotations

from rts.factions.faction import Faction


class SyntheticCollective(Faction):
    display_name = "Synthetic Collective"
    theme_tag = "synthetic"
    color = (120, 220, 200)   # teal / energy-cyan

    # TODO: Wire up faction-specific buildings/units when implemented.
    building_roster = {}
    unit_roster = {}
    starting_buildings = []
    starting_units = []
