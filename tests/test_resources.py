"""Tests for ResourcePool affordability + atomic pay."""
from __future__ import annotations

from rts.core.resources import ResourceCost, ResourceKind, ResourcePool


def test_initial_amounts():
    p = ResourcePool(metals=100, helium3=20)
    assert p.metals == 100
    assert p.helium3 == 20
    assert p.get(ResourceKind.METALS) == 100


def test_add_resources():
    p = ResourcePool()
    p.add(ResourceKind.METALS, 50)
    p.add(ResourceKind.HELIUM3, 5)
    assert p.metals == 50
    assert p.helium3 == 5


def test_can_afford_and_pay():
    p = ResourcePool(metals=100, helium3=10)
    cost = ResourceCost(metals=60, helium3=5)
    assert p.can_afford(cost)
    assert p.pay(cost)
    assert p.metals == 40
    assert p.helium3 == 5


def test_pay_is_atomic_when_unaffordable():
    p = ResourcePool(metals=10, helium3=10)
    cost = ResourceCost(metals=50, helium3=5)
    assert not p.can_afford(cost)
    assert not p.pay(cost)
    # Nothing changed
    assert p.metals == 10
    assert p.helium3 == 10
