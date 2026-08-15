"""
etaledger — Thermodynamic efficiency measurement for computation.
Core law: η = useful_joules / human_joules
"""
__version__ = "0.1.0"
from .core import (
    measure, landauer_cost, capture, merkle_root,
    arm_energy, emc2_residual, commit, raise_order, BottleneckTracker,
)
__all__ = [
    "measure", "landauer_cost", "capture", "merkle_root",
    "arm_energy", "emc2_residual", "commit", "raise_order", "BottleneckTracker",
]
