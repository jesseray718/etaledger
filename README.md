# etaledger

**η = useful_joules / human_joules**

Thermodynamic efficiency measurement for any computation.

```python
from etaledger import measure, capture, merkle_root, BottleneckTracker

tracker = BottleneckTracker()
η = measure(useful_j=42.0, human_j=10.0)
tracker.record("inference", η)
print(tracker.worst(), tracker.aggregate())

h, j = capture(b"any data")
root = merkle_root([h, "another leaf"])
```

Core primitives: `measure`, `landauer_cost`, `capture`, `merkle_root`, `BottleneckTracker`, `commit`, `raise_order`.

License: GPL-3.0
