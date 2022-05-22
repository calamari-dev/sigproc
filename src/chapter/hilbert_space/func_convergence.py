from pathlib import PurePath
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("sigproc")

x = np.linspace(0, 1, 100)

plt.figure()
plt.plot(x, x / 1, label=r"$f_1(x)$")
plt.plot(x, x / 2, label=r"$f_2(x)$")
plt.plot(x, x / 3, label=r"$f_3(x)$")
plt.plot(x, x * 0, label=r"$\phi(x)$")
plt.legend()
plt.axis([0, 1, 0, 1])
plt.axis("square")
plt.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
