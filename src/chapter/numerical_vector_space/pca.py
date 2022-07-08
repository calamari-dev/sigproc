from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from constant import constants
from sklearn.decomposition import PCA
from vector import Vector2D

plt.style.use("sigproc")

csv = pd.read_csv("pca.csv", sep=",")
pca = PCA(n_components=2)
pca.fit(csv)
v1, v2 = np.transpose(pca.components_ * np.sqrt(pca.explained_variance_).T)

fig, ax = plt.subplots()

ax.scatter(
    csv["x"], csv["y"], color="lightgray", linewidths=constants.scatter_linewidth
)
ax.add_artist(Vector2D((0, 0), v1))
ax.add_artist(Vector2D((0, 0), v2))

ax.text(*v1, r"$\sigma_1\vect{v}_1$", ha="right", va="top")
ax.text(*v2, r"$\sigma_2\vect{v}_2$", ha="right", va="bottom")

ax.axis("equal")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
