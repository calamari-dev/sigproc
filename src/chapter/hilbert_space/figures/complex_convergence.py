from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from constant import constants

plt.style.use("sigproc")

n = np.linspace(1, 100, num=100)
z = np.exp(1j * np.pi / 6) / n

fig, ax = plt.subplots()
ax.scatter(
    np.real(z),
    np.imag(z),
    label=r"$z_n$",
    linewidths=constants.observation_linewidth,
)
ax.legend()
ax.set_xticks(np.linspace(0, 1, num=6))
ax.axis("square")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
