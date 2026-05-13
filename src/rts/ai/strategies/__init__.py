"""Concrete strategies. Pluggable via AIPlayer(strategy=...)."""

from rts.ai.strategies.rusher import RusherStrategy
from rts.ai.strategies.tech_up import TechUpStrategy
from rts.ai.strategies.turtle import TurtleStrategy

__all__ = ["RusherStrategy", "TechUpStrategy", "TurtleStrategy"]
