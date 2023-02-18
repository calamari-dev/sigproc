from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from vector import Vector3D

plt.style.use("sigproc")

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.set(zlim3d=(-2, 6))

for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
    axis.set(pane_color=(0.0, 0.0, 0.0, 0.0))

xx, yy = np.mgrid[-4:4:2j, -4:4:2j]
zz = 0.25 * (xx + yy)
ax.plot_surface(xx, yy, zz, alpha=0.25)
ax.plot_surface(xx, yy, 4 + zz, alpha=0.25)

a = np.array([-3, 3, 4])
w = np.array([4, -2, 0.5])

ax.add_artist(Vector3D([0, 0, 0], a))
ax.add_artist(Vector3D([0, 0, 0], w))
ax.add_artist(Vector3D(w, a + w, ls="dashed", arrowstyle="->"))

ax.text(0, 0, 0, r"$O$", ha="right", va="top")
ax.text(*a, r"$\vect{a}$", ha="right", va="center")
ax.text(*w, r"$\vect{w}$", ha="center", va="top")
ax.text(*(a + w), r"$\vect{a}+\vect{w}$", ha="center", va="center")

fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
