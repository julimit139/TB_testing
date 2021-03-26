import dataExtraction as dE
import os
import numpy as np
import mne
from mne.preprocessing import (ICA, create_eog_epochs, create_ecg_epochs, corrmap)
import matplotlib.pyplot as plt

path1 = "D:/Data/Data/KT53.edf"
# path2 = "D:/Data/Data/test.edf"

raw = mne.io.read_raw_edf(path1)

raw.crop(tmax=60).load_data()
