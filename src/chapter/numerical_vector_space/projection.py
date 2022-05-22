from pathlib import PurePath
import numpy as np
import matplotlib.pyplot as plt
from arrow import add_3d_vector

plt.style.use("sigproc")

e1 = np.array((0.5, -0.8, 0))
e2 = np.array((-0.8, -0.5, 0))
x1 = 0.08 * np.array((0, -5, 12))
x2 = 0.08 * np.array((0, -5, 0))

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
ax.yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
ax.zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 0)

add_3d_vector(ax, (0, 0, 0), e1)
add_3d_vector(ax, (0, 0, 0), e2)
add_3d_vector(ax, (0, 0, 0), x1)
add_3d_vector(ax, (0, 0, 0), x2)
add_3d_vector(ax, x1, x2, ls="dashed", arrowstyle="->")

ax.text(*(0.5 * (x1 + x2)), r"$\proj_V\,$", ha="right")
ax.text(*e1, r"$\vect{e}_1$", ha="right", va="top")
ax.text(*e2, r"$\vect{e}_2$", ha="right", va="top")
ax.text(*x1, r"$\vect{x}$", ha="right", va="bottom")
ax.text(*x2, r"$\vect{m}$", ha="right", va="top")

fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
