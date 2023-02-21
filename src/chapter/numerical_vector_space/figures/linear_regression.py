from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from constant import constants

plt.style.use(["sigproc", "sigproc-small"])

fig, ax = plt.subplots()
x = [1, 2, 3]
y = [0, 3, 1]

for i in range(0, 3):
    z = x[i] / 2 + 1 / 3
    ax.vlines(x[i], min(y[i], z), max(y[i], z), color="gray", ls="dashed")

ax.plot([0, 4], [1 / 3, 7 / 3])
ax.scatter(x, y, linewidths=constants.scatter_linewidth)
ax.axis("equal")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
