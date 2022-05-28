from pathlib import PurePath
import matplotlib.pyplot as plt
from arrow import add_2d_vector

plt.style.use("sigproc")

fig, ax = plt.subplots()

v1 = (1, 1)
v2 = (2, -1)
x = (1.5, 0)

add_2d_vector(ax, (0, 0), v1)
add_2d_vector(ax, (0, 0), v2)
add_2d_vector(ax, (0, 0), x)

ax.text(*v1, r"$\vect{v}_1$", ha="left", va="bottom")
ax.text(*v2, r"$\vect{v}_2$", ha="left", va="top")
ax.text(*x, r"$\vect{x}=(\vect{v}_1+\vect{v}_2)/2$", ha="left", va="center")

ax.axis([-0.25, 3.75, -2, 2])
ax.axis("square")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
