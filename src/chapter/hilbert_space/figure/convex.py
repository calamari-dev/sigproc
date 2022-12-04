from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as interp

plt.style.use("sigproc")

t = np.linspace(0, 2 * np.pi, num=4)
u = np.linspace(0, 1, num=300)
tck, _ = interp.splprep([np.cos(t), np.sin(t)], s=0, per=True)
curve = interp.splev(u, tck)

fig, ax = plt.subplots()
ax.fill(*curve, facecolor="gray")
ax.axis("equal")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
