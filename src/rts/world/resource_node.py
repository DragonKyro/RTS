"""ResourceNode — a Metals deposit or Helium-3 vent that workers harvest."""
from __future__ import annotations

from typing import TYPE_CHECKING

from rts.core.entity import Entity
from rts.core.resources import ResourceKind

if TYPE_CHECKING:
    from rts.world.game_world import GameWorld


class ResourceNode(Entity):
    """An entity workers gather from. `amount_remaining` ticks down as workers haul."""

    def __init__(
        self,
        *,
        world: "GameWorld",
        x: float,
        y: float,
        kind: ResourceKind,
        amount: int = 1500,
    ) -> None:
        super().__init__(world=world, owner=None, x=x, y=y)
        self.kind = kind
        self.amount_remaining = int(amount)

    def harvest(self, amount: int) -> int:
        """Remove up to `amount` from the node. Returns how much was actually harvested."""
        taken = min(self.amount_remaining, max(0, int(amount)))
        self.amount_remaining -= taken
        if self.amount_remaining <= 0:
            self.destroy()
        return taken

    @property
    def is_depleted(self) -> bool:
        return self.amount_remaining <= 0
