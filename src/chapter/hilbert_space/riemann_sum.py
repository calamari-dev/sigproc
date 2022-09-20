from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("sigproc")

x = np.linspace(0, 1, num=100)
n = np.linspace(0, 1, num=7)

f = x**3 - 0.5 * x + 0.5
g = n**3 - 0.5 * n + 0.5
g[-1] = g[-2]

fig, ax = plt.subplots()
ax.fill_between(
    n, g, step="post", label=r"$\sum f(n\increment t)\increment t$", color="gray", lw=0
)
ax.plot(x, f, label=r"$f(t)$")
ax.legend()
ax.axis([0, 1, 0, 1])
ax.axis("square")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
