from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from vector import Vector3D

plt.style.use("sigproc")

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.set(zlim3d=(-1.5, 5.5))

xx, yy = np.mgrid[-1:5:2j, -5:1:2j]
uu, vv = np.mgrid[-4:2:2j, -2:4:2j]
zz = 0.25 * (xx + yy)
ww = 4 + 0.25 * (uu + vv)
ax.plot_surface(xx, yy, zz, alpha=0.25)
ax.plot_surface(uu, vv, ww, alpha=0.25)

a = np.array([-3, 3, 4])
w = np.array([4, -3, 1])

ax.add_artist(Vector3D([0, 0, 0], a))
ax.add_artist(Vector3D([0, 0, 0], w))
ax.add_artist(Vector3D(w, a + w, ls="dashed", arrowstyle="->"))

ax.text(0, 0, 0, r"$O$", ha="right", va="top")
ax.text(*a, r"$\vect{a}$", ha="left", va="center")
ax.text(*w, r"$\vect{w}$", ha="center", va="top")
ax.text(*(a + w), r"$\vect{a}\mathrlap{{}+\vect{w}}$", ha="left", va="center")

fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
