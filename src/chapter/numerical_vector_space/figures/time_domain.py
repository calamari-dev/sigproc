from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

plt.style.use(["sigproc", "sigproc-wide"])

filename = "namine_ritsu.wav"
samplerate, data = wavfile.read(str(PurePath(__file__).parent / filename))

duration = data.shape[0] / samplerate
t = np.linspace(0, duration, num=data.shape[0])
data = data / 32767

fig, ax = plt.subplots()
ax.plot(t, data, lw=0.4)
ax.set_xlabel("時刻 [s]")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
