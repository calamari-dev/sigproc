from pathlib import PurePath

import matplotlib.pyplot as plt
import pandas as pd
from constant import constants

plt.style.use("sigproc")

csv = pd.read_csv("pca.csv", sep=",")
fig, ax = plt.subplots()
ax.scatter(csv["x"], csv["y"], linewidths=constants.scatter_linewidth)
ax.axis("equal")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
