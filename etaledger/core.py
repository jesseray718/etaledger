"""
etaledger.core — Order-0 atoms: measure, landauer, merkle, eta, energy.
"""
import hashlib
from typing import Dict, List, Tuple, Optional

LANDAUER = 2.85e-21
ARM_J_PER_CYCLE = 1.2e-10
C = 299792458.0

def measure(useful_j: float, human_j: float) -> float:
    """η = useful_joules / human_joules. Never divide by zero."""
    return useful_j / human_j if human_j > 0 else 0.0

def landauer_cost(bits_erased: int) -> float:
    return bits_erased * LANDAUER * 1e9

def capture(data: bytes) -> Tuple[str, float]:
    h = hashlib.sha256(data).hexdigest()
    bits = len(data) * 8
    human_j = bits * LANDAUER * 1e9
    return h, human_j

def merkle_root(leaves: List[str]) -> str:
    if not leaves:
        return hashlib.sha256(b"empty").hexdigest()
    layer = [hashlib.sha256(x.encode() if isinstance(x, str) else x).hexdigest() for x in leaves]
    while len(layer) > 1:
        nxt = []
        for i in range(0, len(layer), 2):
            left = layer[i]
            right = layer[i + 1] if i + 1 < len(layer) else left
            nxt.append(hashlib.sha256((left + right).encode()).hexdigest())
        layer = nxt
    return layer[0]

def arm_energy(cycles: int, freq_mhz: float = 650.0) -> float:
    scale = 2000.0 / max(freq_mhz, 100.0)
    return cycles * ARM_J_PER_CYCLE * scale

def emc2_residual(mass_kg: float = 1e-12) -> float:
    return mass_kg * C * C

def commit(trace: Dict) -> str:
    blob = str(sorted(trace.items())).encode()
    return hashlib.sha256(blob).hexdigest()

def raise_order(node_id: str, order: int) -> str:
    return f"{node_id}_o{order + 1}"

class BottleneckTracker:
    def __init__(self):
        self._scores: Dict[str, float] = {}
    def record(self, node_id: str, eta: float) -> None:
        self._scores[node_id] = eta
    def worst(self) -> str:
        if not self._scores:
            return "none"
        return min(self._scores, key=self._scores.get)
    def best(self) -> str:
        if not self._scores:
            return "none"
        return max(self._scores, key=self._scores.get)
    def all(self) -> Dict[str, float]:
        return dict(self._scores)
    def aggregate(self) -> float:
        vals = [v for v in self._scores.values() if v > 0]
        if not vals:
            return 0.0
        return len(vals) / sum(1.0 / v for v in vals)
