from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq, ifft
from scipy.io import wavfile
from constant import constants

plt.style.use(["sigproc", "sigproc-wide"])

filename = "namine_ritsu.wav"
samplerate, data = wavfile.read(str(PurePath(__file__).parent / filename))

duration = data.shape[0] / samplerate
normalizer = 1 / np.sqrt(data.shape[0])
t = np.linspace(0, duration, num=data.shape[0])
data = data / 32767

x = fftfreq(data.shape[0], 1 / samplerate)
x = x[(x >= 0) & (x <= 5000)]
y = np.abs(normalizer * fft(data))

h = fft(np.log(y))
h[(t >= 1 / 350) & (t <= duration - 1 / 350)] = 0
h = np.exp(np.real(ifft(h)))

y[0] = np.nan
h[0] = np.nan

fig, ax = plt.subplots()
ax.set_xlabel("周波数 [Hz]")
ax.set_yscale("log")
ax.plot(
    x,
    y[: len(x)],
    lw=constants.observation_linewidth,
    color="gray",
    label=r"$\abs{\hat{x}_k}$",
)
ax.plot(x, h[: len(x)], label=r"$\hat{h}_k")
ax.legend()
fig.savefig(
    str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")), pad_inches=0.02
)
