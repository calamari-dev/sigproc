from pathlib import PurePath
import matplotlib.pyplot as plt
from vector import Vector2D

plt.style.use("sigproc")

fig, ax = plt.subplots()
ax.set(xlim=(-1.5, 2.5), ylim=(-2, 2))
v1, v2, v3 = ((1, 1), (2, -1), (-1, 0))

for v in (v1, v2, v3):
    ax.add_artist(Vector2D((0, 0), v))

ax.text(*v1, r"$\vect{v}_1$", ha="left", va="bottom")
ax.text(*v2, r"$\vect{v}_2$", ha="left", va="top")
ax.text(*v3, r"$\vect{v}_3$", ha="right", va="center")

ax.axis("square")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
