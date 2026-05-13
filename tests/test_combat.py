"""Tests for damage-type vs armor-class matrix."""
from __future__ import annotations

from rts.combat.damage_types import ArmorClass, DamageType, damage_multiplier


def test_kinetic_beats_light_armor():
    assert damage_multiplier(DamageType.KINETIC, ArmorClass.LIGHT) > 1.0


def test_kinetic_penalized_against_heavy():
    assert damage_multiplier(DamageType.KINETIC, ArmorClass.HEAVY) < 1.0


def test_explosive_beats_heavy_armor():
    assert damage_multiplier(DamageType.EXPLOSIVE, ArmorClass.HEAVY) > 1.0


def test_energy_is_strongest_vs_medium():
    # Energy should not be the *best* vs light (kinetic wins there);
    # it should be the best vs medium of the three damage types.
    by_type = {
        dt: damage_multiplier(dt, ArmorClass.MEDIUM)
        for dt in DamageType
    }
    winner = max(by_type, key=by_type.get)
    assert winner == DamageType.ENERGY


def test_strings_accepted():
    # The function should accept string values too (matches Damageable.take_damage signature).
    assert damage_multiplier("kinetic", "light") > 1.0
