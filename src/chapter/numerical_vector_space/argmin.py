from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("sigproc")

x = np.linspace(0, 8, 300)
fig, ax = plt.subplots()
ax.plot(x, np.exp(-x))
ax.plot(x, np.abs(np.sin(x)))
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
