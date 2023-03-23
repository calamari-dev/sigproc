from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np

plt.style.use(["sigproc", "sigproc-wide"])

t = np.linspace(0, 10, 1000)
fig, ax = plt.subplots()
x = 0.8 * np.sin(t * t) + 0.3 * np.cos(4 * t) + 0.2 * np.sin(5 * t)
ax.plot(t, x)
ax.set_xlabel("時刻[s]")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
