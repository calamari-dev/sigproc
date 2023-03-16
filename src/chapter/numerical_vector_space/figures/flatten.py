from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
from PIL import Image
from scipy import fft

plt.style.use("sigproc")

png = Image.open(str(PurePath(__file__).parent / "pudding.png"))
mat = np.array(png.rotate(-90)).T / (2**16 - 1)
frr = fft.fftshift(fft.fft2(mat, norm="ortho"))
xx, yy = np.mgrid[-531:532, -531:532]
frr[(xx ** 2 + yy ** 2 > 100) & (np.abs(6 * xx - yy) < 50)] = 1e-4
mat = np.abs(fft.ifft2(fft.ifftshift(frr), norm="ortho"))
mat = mat / np.max(mat)

mm = 1 / 25.4
fig, ax = plt.subplots(figsize=(55 * mm, 40 * mm))
img = ax.pcolormesh(mat, rasterized=True)
fig.colorbar(img)
ax.axis("square")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
