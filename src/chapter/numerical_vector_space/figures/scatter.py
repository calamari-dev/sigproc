from pathlib import PurePath

import matplotlib.pyplot as plt
import pandas as pd
from constant import constants

plt.style.use("sigproc")

csv = pd.read_csv(str(PurePath(__file__).parent / "pca.csv"), sep=",", header=None)
fig, ax = plt.subplots()
ax.set(xlim=(-17, 17), ylim=(-17, 17))
ax.scatter(csv[0], csv[1], linewidths=constants.scatter_linewidth)
ax.axis("equal")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
