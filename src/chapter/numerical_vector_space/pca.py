from pathlib import PurePath
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from arrow import add_2d_vector

plt.style.use("sigproc")

csv = pd.read_csv("pca.csv", sep=",")
pca = PCA(n_components=2)
pca.fit(csv)
v1, v2 = np.transpose(pca.components_ * np.sqrt(pca.explained_variance_).T)

fig, ax = plt.subplots()

ax.scatter(csv["x"], csv["y"], color="lightgray", linewidths=0.5)
add_2d_vector(ax, (0, 0), v1)
add_2d_vector(ax, (0, 0), v2)
ax.text(*v1, r"$\sigma_1\vect{v}_1$", ha="right", va="top")
ax.text(*v2, r"$\sigma_2\vect{v}_2$", ha="right", va="bottom")

ax.axis("equal")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
