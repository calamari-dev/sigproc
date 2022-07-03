from pathlib import PurePath
import numpy as np
import matplotlib.pyplot as plt
from vector import Vector3D

plt.style.use("sigproc")

xx, yy = np.mgrid[-1:1:10j, -1:1:10j]
zz = 0.3 * (xx - yy)

e1 = np.array((7, -3, 3))
e3 = np.array((-3, 3, 10))
e2 = np.cross(e1, e3)

e1 = e1 / np.linalg.norm(e1, ord=2)
e2 = e2 / np.linalg.norm(e2, ord=2)
e3 = e3 / np.linalg.norm(e3, ord=2)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.set(zlim3d=(-0.6, 1.4))

for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
    axis.set(pane_color=(0.0, 0.0, 0.0, 0.0))

ax.plot_surface(xx, yy, zz, alpha=0.25)
ax.add_artist(Vector3D((0, 0, 0), e1))
ax.add_artist(Vector3D((0, 0, 0), e2))
ax.add_artist(Vector3D((0, 0, 0), e3))

ax.text(*e1, r"$\vect{e}_1$", ha="left", va="top")
ax.text(*e2, r"$\vect{e}_2$", ha="right", va="top")
ax.text(*e3, r"$\vect{e}_3$", ha="center", va="bottom")

fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
