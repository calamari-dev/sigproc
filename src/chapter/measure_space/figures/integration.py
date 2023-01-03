from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np

plt.style.use(["sigproc", "sigproc-small"])

x = np.linspace(0, 1, num=300)
f = 6 * x**2 * (1 - x)
g = np.zeros(300)
div = 8

for y in np.linspace(0, 1, num=div, endpoint=False):
    g[(f >= y) & (f <= y + 1 / div)] = y

major = np.array([0, 0.5, 1])
minor = np.setdiff1d(np.linspace(0, 1, num=div + 1), major)

fig, ax = plt.subplots()
ax.set_yticks(major)
ax.set_yticks(minor, minor=True)
ax.fill_between(x, g, step="post", label=r"$\phi_3$", color="gray", lw=0)
ax.plot(x, f, label=r"$f$")
ax.grid(axis="y", which="both")
ax.legend()
ax.axis("square")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
