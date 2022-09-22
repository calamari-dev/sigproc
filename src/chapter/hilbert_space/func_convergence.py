from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("sigproc")

x = np.linspace(0, 1, num=300)

fig, ax = plt.subplots()

for i in range(1, 4):
    ax.plot(x, np.abs(np.sin(i * np.pi * x)) / i, label="$f_" + str(i) + "(x)$")

ax.legend()
ax.axis([0, 1, 0, 1])
ax.axis("square")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
