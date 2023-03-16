from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("sigproc")

n = np.linspace(0, 32, num=32, endpoint=False)
fig, ax = plt.subplots()
x = 0.8 * np.sin(n / 5) + 0.2 * np.sin(2 * n)
y = [(x[n % 32] + x[(n - 1) % 32] + x[(n - 2) % 32]) / 3 for n in range(0, 32)]
ax.plot(n, x, "o", color="gray", label=r"$x[n]$")
ax.plot(n, y, "x", label=r"$y[n]$")
ax.legend()
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
