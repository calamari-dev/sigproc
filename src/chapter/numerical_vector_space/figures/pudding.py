from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

plt.style.use(["sigproc", "sigproc-wide"])

png = Image.open(str(PurePath(__file__).parent / "pudding.png"))
mat = np.array(png.rotate(-90)).T / (2**16 - 1)

mm = 1 / 25.4
fig, ax = plt.subplots(figsize=(60 * mm, 45 * mm))
img = ax.pcolormesh(mat, rasterized=True)
fig.colorbar(img)
ax.axis("square")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
