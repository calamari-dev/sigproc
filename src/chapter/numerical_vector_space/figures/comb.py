from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np

plt.style.use(["sigproc", "sigproc-wide"])

n = np.linspace(-6, 6, num=13)
d0 = np.zeros(13)
d1 = np.zeros(13)
d0[n % 5 == 0] = 1
d1[n % 5 == 1] = 1

fig, ax = plt.subplots()
ax.stem(n, d0, label=r"$\delta[n]$")
ax.stem(n, d1, label=r"$(\lagop\delta)[n]$", linefmt="--", markerfmt="x")
ax.legend()
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
