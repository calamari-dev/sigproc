from pathlib import PurePath
import numpy as np
import matplotlib.pyplot as plt
from arrow import add_3d_vector

plt.style.use("sigproc")

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
ax.yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
ax.zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))

x, y = np.meshgrid(np.linspace(-1, 1, num=10), np.linspace(-1, 1, num=10))
z = 0.3 * (x - y)
ax.plot_surface(x, y, z, alpha=0.25)
ax.set_zlim(-0.6, 1.4)

e1 = np.array((7, -3, 3))
e3 = np.array((-3, 3, 10))
e2 = np.cross(e1, e3)

e1 = e1 / np.linalg.norm(e1, ord=2)
e2 = e2 / np.linalg.norm(e2, ord=2)
e3 = e3 / np.linalg.norm(e3, ord=2)

add_3d_vector(ax, (0, 0, 0), e1)
add_3d_vector(ax, (0, 0, 0), e2)
add_3d_vector(ax, (0, 0, 0), e3)

ax.text(*e1, r"$\vect{e}_1$", ha="left", va="top")
ax.text(*e2, r"$\vect{e}_2$", ha="right", va="top")
ax.text(*e3, r"$\vect{e}_3$", ha="center", va="bottom")

fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
