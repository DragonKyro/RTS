"""Terran Directorate — balanced, armor-heavy, conventional military."""
from __future__ import annotations

from rts.buildings.terran.headquarters import TerranHeadquarters
from rts.core.tech_tree import TechTree
from rts.factions.faction import Faction
from rts.units.terran.engineer import Engineer


class TerranDirectorate(Faction):
    display_name = "Terran Directorate"
    theme_tag = "terran"
    color = (60, 130, 200)   # cool steel blue

    building_roster = {
        "headquarters": TerranHeadquarters,
        # TODO: barracks, vehicle_bay, spaceport, refinery, research_lab,
        #       turret, wall, reactor, habitat
    }
    unit_roster = {
        "engineer": Engineer,
        # TODO: marine, apc, tank, gunship
    }

    starting_buildings = ["headquarters"]
    starting_units = [("engineer", 4)]

    def _build_tech_tree(self) -> TechTree:
        tree = TechTree()
        tree.add("headquarters", requires=[])
        tree.add("engineer", requires=["headquarters"])
        # TODO: tree.add("barracks", requires=["headquarters"]) etc.
        return tree
