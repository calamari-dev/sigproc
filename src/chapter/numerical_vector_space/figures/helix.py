from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from vector import Vector3D

plt.style.use("sigproc")

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
    axis.set(pane_color=(0.0, 0.0, 0.0, 0.0))

t = np.linspace(0, 6 * np.pi, 300)
ax.add_artist(Vector3D((0, 0, 0), (6 * np.pi, 0, 0)))
ax.plot(t, np.cos(t), np.sin(t))
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
