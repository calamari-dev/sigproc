from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from vector import Vector3D

plt.style.use("sigproc")

xx, yy = np.mgrid[-5:5:10j, -5:5:10j]
zz = (xx + 2 * yy) / 3

e1 = np.array((4, 1, 2))
e2 = np.array((0, 3, 2))
pr = np.cross(e1, e2) / 2
xm = np.array((-2, -2, -2))
y1 = xm + pr

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.set(zlim3d=(-3, 7))

for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
    axis.set(pane_color=(0.0, 0.0, 0.0, 0.0))

ax.plot_surface(xx, yy, zz, alpha=0.25)

for e in (e1, e2, y1, xm):
    ax.add_artist(Vector3D((0, 0, 0), e))

ax.add_artist(Vector3D(y1, xm, ls="dashed", arrowstyle="->"))

ax.text(*(0.5 * (y1 + xm)), r"$P\,$", ha="right", va="top")
ax.text(*e1, r"$\vect{e}_1$", ha="left", va="center")
ax.text(*e2, r"$\vect{e}_2$", ha="left", va="bottom")
ax.text(*xm, r"$\mat{A}\vect{x}$", ha="right", va="top")
ax.text(*y1, r"$\vect{y}$", ha="right", va="bottom")

fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
