from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
import pywt

plt.style.use("sigproc")

phi, psi, x = pywt.Wavelet("dmey").wavefun(level=5)
t = x[np.argmax(phi)]
x, phi = np.transpose([(x[k] - t, phi[k]) for k in range(len(x)) if abs(x[k] - t) < 8])

plt.figure()
plt.plot(x, phi)
plt.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
