from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("sigproc")

n = 7
x = np.linspace(0, 1, num=100)
k = np.linspace(0, 1, num=n)

f = x**3 - 0.5 * x + 0.5
g = k**3 - 0.5 * k + 0.5

fig, ax = plt.subplots()
ax.fill_between(
    k, g, step="post", label=r"$\sum f(n\increment t)\increment t$", color="gray", lw=0
)
ax.plot(x, f, label=r"$f(t)$")
ax.legend()
ax.axis([0, 1, 0, 1])
ax.axis("square")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
