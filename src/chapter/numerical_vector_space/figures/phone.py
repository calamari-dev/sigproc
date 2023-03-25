from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from constant import constants
from scipy.io import wavfile

plt.style.use(["sigproc", "sigproc-wide"])

filename = "stft.wav"
samplerate, data = wavfile.read(str(PurePath(__file__).parent / filename))

x = (data.astype(np.double) - 128) / 127
t = np.linspace(0, 1000 * len(x) / samplerate, num=len(x))

fig, ax = plt.subplots()
ax.plot(t, x, lw=constants.observation_linewidth)
ax.set_xlabel("時刻[ms]")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
