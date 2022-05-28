from pathlib import PurePath
import matplotlib.pyplot as plt
from arrow import add_2d_vector

plt.style.use("sigproc")

fig, ax = plt.subplots()

v1 = (1, 1)
v2 = (2, -1)
v3 = (-1, 0)

add_2d_vector(ax, (0, 0), v1)
add_2d_vector(ax, (0, 0), v2)
add_2d_vector(ax, (0, 0), v3)

ax.text(*v1, r"$\vect{v}_1$", ha="left", va="bottom")
ax.text(*v2, r"$\vect{v}_2$", ha="left", va="top")
ax.text(*v3, r"$\vect{v}_3$", ha="right", va="center")

ax.axis([-1.5, 2.5, -2, 2])
ax.axis("square")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
