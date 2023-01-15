from pathlib import PurePath

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from scipy import fft
import numpy as np
from PIL import Image

plt.style.use(["sigproc", "sigproc-wide"])

png = Image.open(str(PurePath(__file__).parent / "pudding.png"))
mat = np.array(png.rotate(-90)).T / (2 ** 16 - 1)
amp = np.abs(fft.fftshift(fft.fft2(mat, norm="ortho")))

mm = 1 / 25.4
fig, ax = plt.subplots(figsize=(60 * mm, 45 * mm))
ax.set(xticks=[-531, 0, 531], xticklabels=[r"$-\krez$", r"$0$", r"$\krez$"])
ax.set(yticks=[-531, 0, 531], yticklabels=[r"$-\krez$", r"$0$", r"$\krez$"])
img = ax.pcolormesh(
    *np.mgrid[-531:532, -531:532],
    amp,
    norm=LogNorm(vmin=np.min(amp), vmax=np.max(amp)),
    rasterized=True
)
fig.colorbar(img)
ax.axis("square")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
