"""Command panel — context-sensitive grid of build/produce/order buttons.

Skeleton: stores the active button set; rendering is done by HUD when wired up.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class CommandButton:
    label: str
    hotkey: Optional[str]
    on_click: Callable[[], None]
    enabled: bool = True


class CommandPanel:
    def __init__(self) -> None:
        self.buttons: list[CommandButton] = []

    def set_buttons(self, buttons: list[CommandButton]) -> None:
        self.buttons = list(buttons)

    def clear(self) -> None:
        self.buttons = []
