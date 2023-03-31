from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from vector import Vector2D

plt.style.use("sigproc")

fig, ax = plt.subplots()
t = np.linspace(0, 2 * np.pi, 300)
ax.plot(np.cos(t), np.sin(t), ls="dashed")

for i in range(0, 3):
    t = 2 * np.pi * i / 3 + np.pi / 2
    ax.add_artist(Vector2D((0, 0), (np.cos(t), np.sin(t))))


ax.axis("square")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
