"""Damage resolution — applies the damage-type × armor-class matrix."""
from __future__ import annotations

from typing import TYPE_CHECKING

from rts.combat.damage_types import ArmorClass, DamageType, damage_multiplier

if TYPE_CHECKING:
    from rts.core.entity import Entity


def apply_damage(target: "Entity", raw_amount: int, damage_type: DamageType | str) -> int:
    """Apply matrix-modified damage to a Damageable target. Returns final damage dealt."""
    armor = getattr(target, "armor_class", ArmorClass.LIGHT)
    mult = damage_multiplier(damage_type, armor)
    final = max(1, int(round(raw_amount * mult)))
    if hasattr(target, "take_damage"):
        # Pass the *final* amount with the original type; Damageable subtracts as-is.
        target.take_damage(final, damage_type if isinstance(damage_type, str) else damage_type.value)
    return final
