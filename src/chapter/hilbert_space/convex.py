from pathlib import PurePath
import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt

plt.style.use("sigproc")

theta = np.linspace(0, 2 * np.pi, 4)
tck, _ = interp.splprep([np.cos(theta), np.sin(theta)], s=0, per=True)
u = np.linspace(0, 1, num=100)
curve = interp.splev(u, tck)

plt.figure()
plt.fill(curve[0], curve[1], facecolor="gray")
plt.axis("equal")
plt.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
