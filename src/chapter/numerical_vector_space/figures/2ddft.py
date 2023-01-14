from pathlib import PurePath

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from scipy import fftpack
import numpy as np
from PIL import Image

plt.style.use(["sigproc", "sigproc-wide"])

png = Image.open(str(PurePath(__file__).parent / "building.png"))
amp = np.abs(fftpack.fft2(png)) / np.sqrt(png.width * png.height)

fig, ax = plt.subplots()
img = ax.imshow(amp, norm=LogNorm(vmin=np.min(amp), vmax=np.max(amp)))
fig.colorbar(img)
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
