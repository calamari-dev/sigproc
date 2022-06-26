from pathlib import PurePath
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("sigproc")

n = np.linspace(1, 7, 7)
theta = np.linspace(0, np.pi / 2, 300)

plt.figure()
plt.plot(0.4 * np.cos(theta), 0.4 * np.sin(theta))
plt.scatter(
    np.cos(np.pi / 6) / n, np.sin(np.pi / 6) / n, label=r"$z_n$", linewidths=0.4
)
plt.legend()
plt.axis([0, 1.5, 0, 1.5])
plt.axis("square")
plt.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
