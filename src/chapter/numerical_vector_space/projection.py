from pathlib import PurePath
import numpy as np
import matplotlib.pyplot as plt
from arrow import add_3d_vector

plt.style.use("sigproc")

v1 = np.array((0.5, -1.6, 0))
v2 = np.array((-0.8, -1, 0))
x1 = np.array((0, -0.8, 1.9))
xm = np.array((0, -0.8, 0))

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
ax.yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
ax.zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))

ax.set_xlim(-1, 1)
ax.set_ylim(-2, 0)
ax.set_zlim(0, 2)

add_3d_vector(ax, (0, 0, 0), v1)
add_3d_vector(ax, (0, 0, 0), v2)
add_3d_vector(ax, (0, 0, 0), x1)
add_3d_vector(ax, (0, 0, 0), xm)
add_3d_vector(ax, x1, xm, ls="dashed", arrowstyle="->")

ax.text(*(0.5 * (x1 + xm)), r"$\proj_V\,$", ha="right")
ax.text(*v1, r"$\vect{v}_1$", ha="right", va="top")
ax.text(*v2, r"$\vect{v}_2$", ha="right", va="top")
ax.text(*x1, r"$\vect{x}$", ha="right", va="bottom")
ax.text(*xm, r"$\vect{m}$", ha="right", va="top")

fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
