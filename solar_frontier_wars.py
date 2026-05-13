"""Entry point — lets `python solar_frontier_wars.py` work without installing the package."""
from __future__ import annotations

import sys
from pathlib import Path

_SRC = Path(__file__).resolve().parent / "src"
if _SRC.is_dir() and str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rts.app import run

if __name__ == "__main__":
    run()
