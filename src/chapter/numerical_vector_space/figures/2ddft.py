from pathlib import PurePath

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from scipy import fft
import numpy as np
from PIL import Image

plt.style.use(["sigproc", "sigproc-wide"])

png = Image.open(str(PurePath(__file__).parent / "building.png"))
amp = np.abs(fft.fftshift(fft.fft2(png, norm="ortho")))

mm = 1 / 25.4
fig, ax = plt.subplots(figsize=(60 * mm, 45 * mm))
img = ax.pcolormesh(
    *np.mgrid[-531:532, -531:532],
    amp,
    norm=LogNorm(vmin=np.min(amp), vmax=np.max(amp)),
    rasterized=True
)
fig.colorbar(img)
ax.axis("square")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
