from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from text import Text3D

plt.style.use("sigproc")

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.set(xlim=(-1, 2), ylim=(-1, 2), zlim3d=(0, 3))
ax.set(zticks=[0, 1, 2, 3], zticklabels=["0", "$a_1$", "$a_2$", "$a_3$"])

for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
    axis.set(pane_color=(0.0, 0.0, 0.0, 0.0))

xy = [np.array(x) for x in ([0.5, -1, 0], [-1, -1, 0], [0, 0.5, 0])]
z = [1, 2, 3]

ax.bar3d(
    *zip([*xy[0], 1.5, 1.5, z[0]], [*xy[1], 1.5, 1, z[1]], [*xy[2], 2, 1.5, z[2]]),
    color="lightgray",
    shade=True
)

text = Text3D(xy[0] + np.array([0.5, 0.55, z[0]]), r"$A_1$", size=0.6)
ax.add_patch(text)
text.to_3d()

text = Text3D(xy[1] + np.array([0.5, 0.35, z[1]]), r"$A_2$", size=0.6)
ax.add_patch(text)
text.to_3d()

text = Text3D(xy[2] + np.array([0.75, 0.55, z[2]]), r"$A_3$", size=0.6)
ax.add_patch(text)
text.to_3d()

ax.view_init(elev=40, azim=-60)
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
