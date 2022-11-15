from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np

plt.style.use(["sigproc", "sigproc-wide"])

x = np.linspace(0, 2, num=200)
n = np.linspace(0, 2, num=4)
fig, ax = plt.subplots()
ax.plot(x, np.sin(2 * np.pi * x), color="gray", label=r"$\sin(2\krez t)$")
ax.plot(x, np.sin(-np.pi * x), color="gray", label=r"$\sin(-\krez t)$")
ax.stem(n, np.sin(-np.pi * n), label="標本点")
ax.legend(loc="lower right")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
