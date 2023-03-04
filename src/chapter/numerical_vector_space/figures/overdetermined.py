from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from vector import Vector3D

plt.style.use("sigproc")

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.set(zlim3d=(-5, 5))

xx, yy = np.mgrid[-5:5:2j, -6:4:2j]
ax.plot_surface(xx, yy, (xx + 2 * yy) / 3, alpha=0.25)

a1 = np.array([4, 1, 2])
a2 = np.array([0, 3, 2])
Ax = np.array([-2, -2, -2])
b = np.array([-4, -6, 4])

for v in (a1, a2, b, Ax):
    ax.add_artist(Vector3D([0, 0, 0], v))

ax.add_artist(Vector3D(b, Ax, ls="dashed", arrowstyle="->"))

ax.text(*(0.5 * (b + Ax)), r"$P\,$", ha="right", va="top")
ax.text(*a1, r"$\vect{a}_1$", ha="center", va="bottom")
ax.text(*a2, r"$\vect{a}_2$", ha="left", va="center")
ax.text(*Ax, r"$\mat{A}\vect{x}$", ha="center", va="top")
ax.text(*b, r"$\vect{b}$", ha="right", va="center")

fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
