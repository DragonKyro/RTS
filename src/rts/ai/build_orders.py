"""Build orders — ordered (faction, strategy) -> sequence of build/produce steps.

The AI consults this to know "what's next" while its economy + supply allow it.
Steps are simple tuples; the strategy translates them to Commands.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BuildStep:
    kind: str           # "build" or "produce"
    key: str            # roster key (e.g. "barracks", "marine")
    repeat: int = 1


# Example: TD rusher opener. Replace with real values when factions are fleshed out.
TERRAN_RUSHER_OPENER: list[BuildStep] = [
    BuildStep("produce", "engineer", repeat=4),
    # TODO: BuildStep("build", "barracks"),
    # TODO: BuildStep("produce", "marine", repeat=8),
]


def get_opener(faction_theme: str, strategy_name: str) -> list[BuildStep]:
    """Look up an opener. Falls back to an empty list (AI idles)."""
    if faction_theme == "terran" and strategy_name == "rusher":
        return list(TERRAN_RUSHER_OPENER)
    return []
