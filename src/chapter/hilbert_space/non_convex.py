from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as interp

plt.style.use("sigproc")

x = (-1, 0, 1, 0, 0, -1)
y = (0, 1, 0, -1, 0, 0)
tck, _ = interp.splprep([x, y], s=0, per=True)
u = np.linspace(0, 1, num=100)
curve = interp.splev(u, tck)

plt.figure()
plt.fill(curve[0], curve[1], facecolor="gray")
plt.axis("equal")
plt.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
