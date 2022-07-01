from pathlib import PurePath
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("sigproc")

csv = pd.read_csv("pca.csv", sep=",")
fig, ax = plt.subplots()
ax.axis("equal")
ax.scatter(csv["x"], csv["y"], linewidths=0.5)
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
