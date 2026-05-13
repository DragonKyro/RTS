"""Resources — the two-resource economy (Metals + Helium-3) plus a per-player pool."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ResourceKind(Enum):
    METALS = "metals"
    HELIUM3 = "helium3"


@dataclass
class ResourceCost:
    """Stat-block field for buildable things."""

    metals: int = 0
    helium3: int = 0

    def __iter__(self):
        yield ResourceKind.METALS, self.metals
        yield ResourceKind.HELIUM3, self.helium3


class ResourcePool:
    """Per-player resource bank."""

    def __init__(self, metals: int = 0, helium3: int = 0) -> None:
        self._amounts: dict[ResourceKind, int] = {
            ResourceKind.METALS: int(metals),
            ResourceKind.HELIUM3: int(helium3),
        }

    @property
    def metals(self) -> int:
        return self._amounts[ResourceKind.METALS]

    @property
    def helium3(self) -> int:
        return self._amounts[ResourceKind.HELIUM3]

    def get(self, kind: ResourceKind) -> int:
        return self._amounts[kind]

    def add(self, kind: ResourceKind, amount: int) -> None:
        self._amounts[kind] += int(amount)

    def can_afford(self, cost: ResourceCost) -> bool:
        return self.metals >= cost.metals and self.helium3 >= cost.helium3

    def pay(self, cost: ResourceCost) -> bool:
        """Deduct cost atomically. Returns False (and changes nothing) if unaffordable."""
        if not self.can_afford(cost):
            return False
        self._amounts[ResourceKind.METALS] -= cost.metals
        self._amounts[ResourceKind.HELIUM3] -= cost.helium3
        return True

    def __repr__(self) -> str:
        return f"<ResourcePool metals={self.metals} helium3={self.helium3}>"
