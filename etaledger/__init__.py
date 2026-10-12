"""
etaledger — Thermodynamic efficiency measurement for computation.
Core law: η = useful_joules / human_joules
"""
__version__ = "0.1.0"
from .core import (
    measure, human_joules, measure_eta_from_seconds, landauer_cost, capture, merkle_root,
    arm_energy, emc2_residual, commit, raise_order, BottleneckTracker,
    HUMAN_W_SUSTAINED,
)
__all__ = [
    "measure", "human_joules", "measure_eta_from_seconds", "landauer_cost", "capture", "merkle_root",
    "arm_energy", "emc2_residual", "commit", "raise_order", "BottleneckTracker",
    "HUMAN_W_SUSTAINED",
]
