from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq
from scipy.io import wavfile

plt.style.use(["sigproc", "sigproc-wide"])

filename = "common_voice_ja_23919598.wav"
samplerate, data = wavfile.read(str(PurePath(__file__).parent / filename))

num = data.shape[0]
duration = num / samplerate
y = fft(data / 32767)
x = fftfreq(num, 1 / samplerate)[:num // 2]
x = x[x <= 5000]

fig, ax = plt.subplots()
ax.set_xlabel("周波数 [Hz]")
ax.set_yscale("log")
ax.plot(x, np.abs(y[0:len(x)]) / np.sqrt(num), lw=0.4)
ax.set_yticks([1e-3, 1e-1], minor=False)
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
