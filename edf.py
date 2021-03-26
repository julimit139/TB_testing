import dataExtraction as dE
import os
import numpy as np
import mne
from mne.preprocessing import (ICA, create_eog_epochs, create_ecg_epochs, corrmap)
import matplotlib.pyplot as plt

path1 = "D:/Data/Data/KT53.edf"
# path2 = "D:/Data/Data/test.edf"

raw = mne.io.read_raw_edf(path1)

print(type(raw))


# basic operations
sampling_freq = raw.info['sfreq']
start_stop_seconds = np.array([10, 12])
start_sample, stop_sample = (start_stop_seconds * sampling_freq).astype(int)
channel_index = 0
raw_selection = raw[channel_index, start_sample:stop_sample]

x = raw_selection[1]
y = raw_selection[0].T
plt.plot(x, y)
plt.show()