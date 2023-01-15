from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np

plt.style.use(["sigproc", "sigproc-wide"])

t = np.linspace(-np.pi, np.pi, num=300)
xx, yy = np.meshgrid(t, t)
zz = np.cos(3 * xx + 4 * yy)

mm = 1 / 25.4
fig, ax = plt.subplots(figsize=(60 * mm, 45 * mm))

ax.set(xticks=[-np.pi, 0, np.pi], xticklabels=[r"$-\krez$", r"$0$", r"$\krez$"])
ax.set(yticks=[-np.pi, 0, np.pi], yticklabels=[r"$-\krez$", r"$0$", r"$\krez$"])
img = ax.pcolormesh(xx, yy, zz, rasterized=True)
fig.colorbar(img)
ax.axis("square")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
