"""Belt Syndicate — fast, cheap, swarm. Asteroid miners turned warlords."""
from __future__ import annotations

from rts.factions.faction import Faction


class BeltSyndicate(Faction):
    display_name = "Belt Syndicate"
    theme_tag = "belt"
    color = (210, 110, 50)   # rust orange

    # TODO: Wire up faction-specific buildings/units when implemented.
    building_roster = {}
    unit_roster = {}
    starting_buildings = []
    starting_units = []
