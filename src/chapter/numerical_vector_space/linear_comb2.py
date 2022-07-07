from pathlib import PurePath
import matplotlib.pyplot as plt
from vector import Vector2D

plt.style.use("sigproc")

fig, ax = plt.subplots()
ax.set(xlim=(-0.15, 3.85), ylim=(-2, 2))
u, v, w = ((1, 1), (2, -1), (1.5, 0))

for x in (u, v, w):
    ax.add_artist(Vector2D((0, 0), x))

ax.text(*u, r"$\vect{v}_1$", ha="left", va="bottom")
ax.text(*v, r"$\vect{v}_2$", ha="left", va="top")
ax.text(*w, r"$\vect{x}=(\vect{v}_1+\vect{v}_2)/2$", ha="left", va="center")

ax.axis("square")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
