"""Tests for TechTree prerequisite gating."""
from __future__ import annotations

from rts.core.tech_tree import TechTree


def test_unlocked_with_no_prereqs():
    t = TechTree()
    t.add("headquarters")
    assert t.is_unlocked("headquarters", completed=set())


def test_blocked_by_missing_prereqs():
    t = TechTree()
    t.add("headquarters")
    t.add("barracks", requires=["headquarters"])
    t.add("marine", requires=["barracks"])

    assert not t.is_unlocked("barracks", completed=set())
    assert t.is_unlocked("barracks", completed={"headquarters"})
    assert not t.is_unlocked("marine", completed={"headquarters"})
    assert t.is_unlocked("marine", completed={"headquarters", "barracks"})


def test_missing_prereqs_reports_chain():
    t = TechTree()
    t.add("barracks", requires=["headquarters", "power_plant"])
    missing = t.missing_prereqs("barracks", completed={"headquarters"})
    assert missing == ["power_plant"]


def test_unknown_node_is_locked():
    t = TechTree()
    assert not t.is_unlocked("does_not_exist", completed=set())
