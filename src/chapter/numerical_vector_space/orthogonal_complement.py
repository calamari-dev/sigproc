from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from vector import Vector3D

plt.style.use("sigproc")

xx, yy = np.mgrid[-1:1:10j, -1:1:10j]
zz = 0.3 * (xx - yy)

e2 = np.array((7, -3, 3))
e3 = np.array((-3, 3, 10))
e1 = np.cross(e2, e3)
e1, e2, e3 = (e / np.linalg.norm(e, ord=2) for e in (e1, e2, e3))

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.set(zlim3d=(-0.6, 1.4))

for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
    axis.set(pane_color=(0.0, 0.0, 0.0, 0.0))

ax.plot_surface(xx, yy, zz, alpha=0.25)

for e in (e1, e2, e3):
    ax.add_artist(Vector3D((0, 0, 0), e))

ax.text(*e1, r"$\vect{e}_1$", ha="right", va="top")
ax.text(*e2, r"$\vect{e}_2$", ha="left", va="top")
ax.text(*e3, r"$\vect{e}_3$", ha="center", va="bottom")

fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
