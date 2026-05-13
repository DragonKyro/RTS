"""Command objects — issued by HumanPlayer (input) and AIPlayer (strategy).

Both kinds of player produce the same Command types so the GameWorld doesn't
need to know which is which.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from rts.core.entity import Entity


@dataclass
class Command:
    """Base — all commands carry a list of actors (units/buildings) to apply to."""

    actors: list["Entity"]


@dataclass
class MoveCommand(Command):
    dest: tuple[float, float]


@dataclass
class AttackCommand(Command):
    target: "Entity"


@dataclass
class AttackMoveCommand(Command):
    """Move toward `dest`, auto-engaging hostiles encountered along the way."""

    dest: tuple[float, float]


@dataclass
class GatherCommand(Command):
    """Worker harvests from `node` and returns to nearest drop-off."""

    node: "Entity"


@dataclass
class BuildCommand(Command):
    """Worker constructs a `building_key` at `(x, y)` (world coords; will be snapped)."""

    building_key: str
    x: float
    y: float


@dataclass
class ProduceCommand(Command):
    """Building queues a unit of `unit_key`. Actor is the building."""

    unit_key: str


@dataclass
class StopCommand(Command):
    """Cancel current orders for the actors."""


@dataclass
class HoldPositionCommand(Command):
    """Stop moving and engage anything in range, but don't pursue."""
