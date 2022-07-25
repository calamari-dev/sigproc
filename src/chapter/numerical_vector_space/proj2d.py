from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from vector import Vector2D

plt.style.use("sigproc")

fig, ax = plt.subplots()
ax.set(
    xlim=(-0.15, 1.15),
    ylim=(-0.15, 1.15),
    xticks=[0, 0.5, 1],
    yticks=[0, 0.5, 1],
    xticklabels=["0.0", "0.5", "1.0"],
    yticklabels=["0.0", "0.5", "1.0"],
)

v = np.array((1, 0))
x = np.array((np.cos(np.pi / 3) + 0.2, np.sin(np.pi / 3)))
m = np.array((x[0], 0))

for p in (v, x, m):
    ax.add_artist(Vector2D((0, 0), p))

ax.add_artist(Vector2D(m, x, ls="dashed", arrowstyle="->"))

ax.text(*v, r"$\vect{v}$", ha="left", va="center")
ax.text(*x, r"$\vect{x}$", ha="right", va="bottom")
ax.text(*(m + (0, 0.03)), r"$\,\vect{m}$", ha="left", va="bottom")
ax.text(*((x + m) / 2), r"$\,\vect{x}-\vect{m}$", ha="left", va="center")

ax.axis("square")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
