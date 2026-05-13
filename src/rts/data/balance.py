"""Top-level tuning knobs. Adjust here; downstream stat tables import these."""
from __future__ import annotations

# Economy
WORKER_GATHER_RATE = 1.0       # resources per second per worker at a node
DEFAULT_NODE_AMOUNT = 1500     # starting amount in a resource node

# Combat
MIN_DAMAGE_FLOOR = 1           # damage never rounds below this after armor

# Supply
SUPPLY_PER_HABITAT = 8         # supply cap added per habitat-equivalent building
