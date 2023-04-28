from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft

plt.style.use("sigproc")

N = 32
K = N // 2 + 1
n = np.linspace(0, K - 1, num=K)
x = np.zeros(N)
x[0:3] = 1 / 3
y = np.abs(fft(x))

fig, ax = plt.subplots()
ax.ticklabel_format(style="sci", axis="y")
ax.stem(n, y[: K], label=r"$\abs{\hat{h}[k]}$")
ax.legend()
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
