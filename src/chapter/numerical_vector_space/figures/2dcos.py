from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("sigproc")

t = np.linspace(0, 2 * np.pi, num=50, endpoint=False)
xx, yy = np.meshgrid(t, t)
zz = np.cos(3 * xx + 4 * yy)

mm = 1 / 25.4
fig, ax = plt.subplots(figsize=(55 * mm, 40 * mm))
img = ax.pcolormesh(xx, yy, zz, rasterized=True)
fig.colorbar(img)
ax.axis("square")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
