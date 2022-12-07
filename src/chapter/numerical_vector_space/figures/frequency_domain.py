from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq
from scipy.io import wavfile

plt.style.use(["sigproc", "sigproc-wide"])

filename = "namine_ritsu.wav"
samplerate, data = wavfile.read(str(PurePath(__file__).parent / filename))

duration = data.shape[0] / samplerate
t = np.linspace(0, duration, num=data.shape[0])
t = t[t < 0.1]
data = data[0:len(t)] / 32767

num = len(data)
y = fft(data) / np.sqrt(num)
x = fftfreq(num, 1 / samplerate)[:num // 2]
x = x[x <= 5000]

fig, ax = plt.subplots()
ax.set_xlabel("周波数 [Hz]")
ax.set_yscale("log")
ax.plot(x, np.abs(y[0:len(x)]), lw=0.4)
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
