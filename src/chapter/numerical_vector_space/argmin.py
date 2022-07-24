from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("sigproc")

x = np.linspace(0, 8, 300)
fig, ax = plt.subplots()
ax.set(xticks=[0, np.pi, 2 * np.pi], xticklabels=["0", r"$\krez$", r"$2\krez$"])
ax.plot(x, np.exp(-x))
ax.plot(x, np.abs(np.sin(x)))
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
