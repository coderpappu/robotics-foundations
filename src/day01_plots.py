import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


x = np.linspace(0, 2 * np.pi, 200)
pts = np.random.randn(500, 2)
dist = np.linalg.norm(pts, axis=1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.plot(x, np.sin(x), label="sin(x)")
ax1.plot(x, np.cos(x), label="cos(x)")
ax1.legend()
ax1.set_title("Day 1: sine & cosine")

sc = ax2.scatter(pts[:, 0], pts[:, 1], c=dist, s=5)
ax2.set_aspect("equal")
ax2.set_title("500 random points (color = distance)")
fig.colorbar(sc, ax=ax2)

plt.tight_layout()
ROOT = Path(__file__).resolve().parent.parent   # robotics-foundations/
plt.savefig(ROOT / "notes" / "day01.png")
plt.show()

