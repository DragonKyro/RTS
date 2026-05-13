"""Damage types and armor classes — drive a rock-paper-scissors matchup matrix."""
from __future__ import annotations

from enum import Enum


class DamageType(Enum):
    KINETIC = "kinetic"      # Bullets, slugs — TD signature
    ENERGY = "energy"        # Lasers, plasma — SC signature
    EXPLOSIVE = "explosive"  # Rockets, grenades — anti-armor


class ArmorClass(Enum):
    LIGHT = "light"      # Infantry, drones
    MEDIUM = "medium"    # Light vehicles, fortified infantry
    HEAVY = "heavy"      # Tanks, buildings


# Damage multipliers: [damage_type][armor_class] -> float
# Tweak in `data/balance.py` (or override there if we want runtime balance changes).
DAMAGE_MATRIX: dict[DamageType, dict[ArmorClass, float]] = {
    DamageType.KINETIC:   {ArmorClass.LIGHT: 1.25, ArmorClass.MEDIUM: 1.0, ArmorClass.HEAVY: 0.5},
    DamageType.ENERGY:    {ArmorClass.LIGHT: 1.0,  ArmorClass.MEDIUM: 1.25, ArmorClass.HEAVY: 0.75},
    DamageType.EXPLOSIVE: {ArmorClass.LIGHT: 0.75, ArmorClass.MEDIUM: 1.0,  ArmorClass.HEAVY: 1.5},
}


def damage_multiplier(damage_type: DamageType | str, armor_class: ArmorClass | str) -> float:
    dt = DamageType(damage_type) if not isinstance(damage_type, DamageType) else damage_type
    ac = ArmorClass(armor_class) if not isinstance(armor_class, ArmorClass) else armor_class
    return DAMAGE_MATRIX[dt][ac]
