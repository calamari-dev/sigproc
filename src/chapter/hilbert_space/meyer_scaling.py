from pathlib import PurePath
import numpy as np
import pywt
import matplotlib.pyplot as plt

plt.style.use("sigproc")
wavelet = pywt.Wavelet("dmey")
phi, psi, x = wavelet.wavefun(level=5)
t = x[np.argmax(phi)]
x, phi = np.transpose([(x[k] - t, phi[k]) for k in range(len(x)) if abs(x[k] - t) < 8])

plt.figure()
plt.plot(x, phi)
plt.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
