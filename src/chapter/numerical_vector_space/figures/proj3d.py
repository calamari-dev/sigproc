from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from vector import Vector3D

plt.style.use("sigproc")

v1 = np.array((0.5, -1.6, 0))
v2 = np.array((-0.8, -1, 0))
x1 = np.array((0, -0.8, 1.9))
xm = np.array((0, -0.8, 0))

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.set(xlim=(-1, 1), ylim=(-2, 0), zlim3d=(0, 2))

for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
    axis.set(pane_color=(0.0, 0.0, 0.0, 0.0))

for x in (v1, v2, x1, xm):
    ax.add_artist(Vector3D((0, 0, 0), x))

ax.add_artist(Vector3D(x1, xm, ls="dashed", arrowstyle="->"))

ax.text(*(0.5 * (x1 + xm)), r"$\proj_V\,$", ha="right")
ax.text(*v1, r"$\vect{v}_1$", ha="right", va="top")
ax.text(*v2, r"$\vect{v}_2$", ha="right", va="top")
ax.text(*x1, r"$\vect{x}$", ha="right", va="bottom")
ax.text(*xm, r"$\vect{m}$", ha="right", va="top")

fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
