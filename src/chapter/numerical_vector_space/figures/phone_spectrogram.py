from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
from scipy import signal
from constant import constants
from scipy.io import wavfile

plt.style.use(["sigproc", "sigproc-wide"])

filename = "phone_spectrogram.wav"
samplerate, data = wavfile.read(str(PurePath(__file__).parent / filename))

x = (data.astype(np.double) - 128) / 127
f, t, spec = signal.spectrogram(
    x, fs=samplerate, window="hann", nperseg=256, noverlap=255, nfft=len(x)
)

fig, ax = plt.subplots()
img = ax.pcolormesh(
    t, f, spec, norm=LogNorm(vmin=1e-10, vmax=np.max(spec)), rasterized=True
)
fig.colorbar(img)
ax.set_xlabel("時刻[s]")
ax.set_ylabel("周波数[Hz]")
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
