from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as interp

plt.style.use("sigproc")

x = (-1, 0, 1, 0, 0, -1)
y = (0, 1, 0, -1, 0, 0)
tck, _ = interp.splprep([x, y], s=0, per=True)
u = np.linspace(0, 1, num=300)
curve = interp.splev(u, tck)

fig, ax = plt.subplots()
ax.fill(*curve, facecolor="gray")
ax.axis("equal")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
