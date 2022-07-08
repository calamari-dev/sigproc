from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("sigproc")

x = np.linspace(-1, 2, 301)
phi = np.where((x > 0) & (x < 1), 1.0, 0.0)
phi[(x == 0) | (x == 1)] = np.nan

plt.figure()
plt.plot(x, phi)
plt.axis("equal")
plt.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
