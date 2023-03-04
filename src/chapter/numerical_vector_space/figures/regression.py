from pathlib import PurePath

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.style.use(["sigproc", "sigproc-small"])

fig, ax = plt.subplots()
x = np.linspace(0, 2, 100)
csv = pd.read_csv(
    str(PurePath(__file__).parent / "regression.csv"), sep=",", header=None
)
ax.plot(csv[0], csv[1], "o", label=r"$(x_i,y_i)$")
ax.plot(x, x**2 - 1.5 * x + 0.5, label=r"$f(\vect{c};x)$")
ax.legend()
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
