from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from vector import Vector3D

plt.style.use("sigproc")

xx, yy = np.mgrid[-5:5:10j, -5:5:10j]
zz = (xx + 2 * yy) / 3

v1 = np.array((4, 1, 2))
v2 = np.array((0, 3, 2))
v3 = np.cross(v1, v2) / 2
ym = np.array((-2, -2, -2))
y1 = ym + v3

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.set(zlim3d=(-3, 7))

for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
    axis.set(pane_color=(0.0, 0.0, 0.0, 0.0))

ax.plot_surface(xx, yy, zz, alpha=0.25)

for e in (v1, v2, y1, ym):
    ax.add_artist(Vector3D((0, 0, 0), e))

ax.add_artist(Vector3D(y1, ym, ls="dashed", arrowstyle="->"))

ax.text(*(0.5 * (y1 + ym)), r"$P\,$", ha="right", va="top")
ax.text(*v1, r"$\vect{v}_1$", ha="left", va="center")
ax.text(*v2, r"$\vect{v}_2$", ha="left", va="bottom")
ax.text(*ym, r"$\mat{A}\vect{x}$", ha="right", va="top")
ax.text(*y1, r"$\vect{y}$", ha="right", va="bottom")

fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
