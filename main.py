import dataExtraction as dE
import os
import numpy as np
import mne
import matplotlib.pyplot as plt


# extracting data from file
path = "D:/Data/PD_128/PD100.asc"
tup = dE.extractDataAsc(path)
data = tup[0]
sampling = tup[2]
print(sampling)
channels = tup[3]

# deleting unnecessary data
halfCleaned = np.delete(data, 0, 1)
fullCleaned = np.delete(halfCleaned, 19, 1)
data = fullCleaned


# initializing info object
info = mne.create_info(channels, sfreq=sampling)

# swapping data columns and rows
swapped = np.swapaxes(data, 0, 1)

# creating a Raw object
raw = mne.io.RawArray(swapped, info)

print(type(raw))


# basic operations
sampling_freq = raw.info['sfreq']
print(sampling_freq)
start_stop_seconds = np.array([10, 12])
start_sample, stop_sample = (start_stop_seconds * sampling_freq).astype(int)
channel_index = 0
raw_selection = raw[channel_index, start_sample:stop_sample]

x = raw_selection[1]
y = raw_selection[0].T
plt.plot(x, y)
plt.show()





