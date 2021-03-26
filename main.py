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

raw.crop(tmin=0.0, tmax=60.0, include_tmax=True).load_data()



