from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from constant import constants

plt.style.use("sigproc")

t = np.linspace(0, np.pi / 2, num=300)
n = np.linspace(1, 7, num=7)
z = np.exp(1j * np.pi / 6) / n

fig, ax = plt.subplots()
ax.plot(0.4 * np.cos(t), 0.4 * np.sin(t))
ax.scatter(
    np.real(z),
    np.imag(z),
    label=r"$z_n$",
    linewidths=constants.scatter_linewidth,
)
ax.legend()
ax.set_xticks(np.arange(0, 1, 0.2))
ax.axis("square")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
