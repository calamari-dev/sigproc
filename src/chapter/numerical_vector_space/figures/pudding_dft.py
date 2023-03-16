from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
from PIL import Image
from scipy import fft

plt.style.use("sigproc")

png = Image.open(str(PurePath(__file__).parent / "pudding.png"))
mat = np.array(png.rotate(-90)).T / (2**16 - 1)
amp = np.abs(fft.fftshift(fft.fft2(mat, norm="ortho")))

mm = 1 / 25.4
fig, ax = plt.subplots(figsize=(55 * mm, 40 * mm))
img = ax.pcolormesh(
    *np.mgrid[-531:532, -531:532],
    amp,
    norm=LogNorm(vmin=np.min(amp), vmax=np.max(amp)),
    rasterized=True
)
fig.colorbar(img)
ax.axis("square")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
