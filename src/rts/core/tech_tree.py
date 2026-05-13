"""Tech tree — a prerequisite graph gating what each faction can build/produce."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TechNode:
    """A buildable thing (building or unit class name) with prerequisites."""

    name: str
    requires: list[str] = field(default_factory=list)


class TechTree:
    """Map of name -> TechNode. Checks prerequisites against a set of completed names."""

    def __init__(self) -> None:
        self._nodes: dict[str, TechNode] = {}

    def add(self, name: str, requires: list[str] | None = None) -> None:
        self._nodes[name] = TechNode(name=name, requires=list(requires or []))

    def is_unlocked(self, name: str, completed: set[str]) -> bool:
        node = self._nodes.get(name)
        if node is None:
            return False
        return all(req in completed for req in node.requires)

    def missing_prereqs(self, name: str, completed: set[str]) -> list[str]:
        node = self._nodes.get(name)
        if node is None:
            return []
        return [req for req in node.requires if req not in completed]

    def __contains__(self, name: str) -> bool:
        return name in self._nodes

    def __repr__(self) -> str:
        return f"<TechTree nodes={len(self._nodes)}>"
