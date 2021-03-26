import os
import numpy as np
import mne
import matplotlib.pyplot as plt
import sklearn

sample_data_folder = mne.datasets.sample.data_path()
sample_data_raw_file = os.path.join(sample_data_folder, 'MEG', 'sample', 'sample_audvis_raw.fif')

raw = mne.io.read_raw_fif(sample_data_raw_file)
raw.crop(tmax=60).load_data()