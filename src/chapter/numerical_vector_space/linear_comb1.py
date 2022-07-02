from pathlib import PurePath
import matplotlib.pyplot as plt
from arrow import Vector2D

plt.style.use("sigproc")

v1 = (1, 1)
v2 = (2, -1)
v3 = (-1, 0)

fig, ax = plt.subplots()
ax.set(xlim=(-1.5, 2.5), ylim=(-2, 2))

ax.add_artist(Vector2D((0, 0), v1))
ax.add_artist(Vector2D((0, 0), v2))
ax.add_artist(Vector2D((0, 0), v3))

ax.text(*v1, r"$\vect{v}_1$", ha="left", va="bottom")
ax.text(*v2, r"$\vect{v}_2$", ha="left", va="top")
ax.text(*v3, r"$\vect{v}_3$", ha="right", va="center")

ax.axis("square")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
