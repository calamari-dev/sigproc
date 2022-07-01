from pathlib import PurePath
import numpy as np
import matplotlib.pyplot as plt
from arrow import Vector2D

plt.style.use("sigproc")

u = np.array((1, 1))
v = np.array((2, -1))
x = 0.5 * (u + v)

fig, ax = plt.subplots()
ax.set(xlim=(-0.15, 3.85), ylim=(-2, 2))

ax.add_artist(Vector2D((0, 0), u))
ax.add_artist(Vector2D((0, 0), v))
ax.add_artist(Vector2D((0, 0), x))

ax.text(*u, r"$\vect{v}_1$", ha="left", va="bottom")
ax.text(*v, r"$\vect{v}_2$", ha="left", va="top")
ax.text(*x, r"$\vect{x}=(\vect{v}_1+\vect{v}_2)/2$", ha="left", va="center")

ax.axis("square")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
