from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from constant import constants

plt.style.use("sigproc")

t = np.linspace(0, np.pi / 2, 300)
n = np.linspace(1, 7, 7)

fig, ax = plt.subplots()
ax.set(xlim=(0, 1.5), ylim=(0, 1.5))

ax.plot(0.4 * np.cos(t), 0.4 * np.sin(t))
ax.scatter(
    np.cos(np.pi / 6) / n,
    np.sin(np.pi / 6) / n,
    label=r"$z_n$",
    linewidths=constants.scatter_linewidth,
)
ax.legend()

ax.axis("square")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
