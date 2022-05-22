from pathlib import PurePath
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("sigproc")

x = np.linspace(-1, 2, 301)
phi = np.where((x > 0) & (x < 1), 1.0, 0.0)
phi[(x == 0) | (x == 1)] = np.nan

plt.figure()
plt.plot(x, phi)
plt.vlines(0, 0, 1, ls="dashed")
plt.vlines(1, 0, 1, ls="dashed")
plt.axis("equal")
plt.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
