from pathlib import PurePath

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
from scipy import signal
from scipy.io import wavfile

plt.style.use("sigproc")

filename = "phone_spectrogram.wav"
samplerate, data = wavfile.read(str(PurePath(__file__).parent / filename))

x = (data.astype(np.double) - 128) / 127
f, t, spec = signal.spectrogram(
    x, fs=samplerate, window="hann", nperseg=64, noverlap=63, nfft=len(x)
)
f = f / 1000

fig, ax = plt.subplots()
ax.pcolormesh(t, f, spec, norm=LogNorm(vmin=1e-10, vmax=np.max(spec)), rasterized=True)
fig.savefig(str(PurePath(__file__).parent / (PurePath(__file__).stem + ".pdf")))
