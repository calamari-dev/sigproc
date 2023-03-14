from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from scipy import fft

plt.style.use("sigproc")

n = np.linspace(-25, 25, num=50, endpoint=False)
t = np.linspace(0, 2 * np.pi, num=50, endpoint=False)
uu, vv = np.meshgrid(n, n)
xx, yy = np.meshgrid(t, t)
zz = np.cos(3 * xx + 5 * yy)
amp = np.abs(fft.fftshift(fft.fft2(zz, norm="ortho")))

mm = 1 / 25.4
fig, ax = plt.subplots(figsize=(55 * mm, 40 * mm))
img = ax.pcolormesh(uu, vv, amp, rasterized=True)
fig.colorbar(img)
ax.axis("square")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
