from pathlib import PurePath

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from constant import constants
from scipy.io import wavfile

plt.style.use(["sigproc", "sigproc-wide"])
mpl.rc("figure", figsize=(2.8740, 3.5433))
lw = constants.observation_linewidth

filename = "phone.wav"
samplerate, data = wavfile.read(str(PurePath(__file__).parent / filename))

x = (data.astype(np.double) - 128) / 127
t = np.linspace(0, len(x) / samplerate, num=len(x), endpoint=False)
x = x[t <= 0.2]
t = t[t <= 0.2]
w = np.zeros(len(x))

for i in range(0, 256):
    w[i] = 0.5 * (1 - np.cos(2 * np.pi * i / 256))

fig, axs = plt.subplots(4, 1)
axs[0].plot(t, w, label=r"$w$")
axs[0].legend(loc="upper right")

w = np.roll(w, samplerate // 10)

axs[1].plot(t, w, label=r"$\translate{n}\conj{w}$")
axs[1].legend(loc="upper right")
axs[2].plot(t, x, label=r"$x$", lw=lw)
axs[2].legend(loc="upper right")
axs[3].plot(t, w * x, label=r"$x\cdot\translate{n}\conj{w}$", lw=lw)
axs[3].legend(loc="upper right")
axs[3].set_xlabel("時刻[s]")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
