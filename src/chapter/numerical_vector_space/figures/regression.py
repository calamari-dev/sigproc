from pathlib import PurePath

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from constant import constants

plt.style.use(["sigproc", "sigproc-small"])

fig, ax = plt.subplots()
n = np.linspace(0, 2, 20)
x = np.linspace(0, 2, 100)
csv = pd.read_csv(
    str(PurePath(__file__).parent / "regression.csv"), sep=",", header=None
)
ax.scatter(n, csv[0], label=r"$(x_i,y_i)$", linewidths=constants.scatter_linewidth)
ax.plot(x, x**2 - 1.5 * x + 0.5, label=r"$f(\vect{c};x)$")
ax.legend()
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
