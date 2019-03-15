import sys
sys.path.append('../analysis/')
import numpy as np
import matplotlib.pyplot as plt
from read_waveform import read_waveform as rw
import os

Nloops = len(os.listdir('./d1_baseline_shifted/'))
nhdr = 5
j = 0
start_index = 370
end_index = 1600
for i in range(j,Nloops):
    print i
    fname = 'C:/watchman/signal_chain_studies/d1/d1_baseline_shifted/D1--waveforms--%05d.txt' %i
    (t,y,hdr) = rw(fname,nhdr)
    y = y / min(y[start_index:end_index])
    t_window = t[start_index:end_index]
    y_window = y[start_index:end_index]
    norm_thresh = 0.05
    norm_thresh2 = 0.1

    max_location = y == 1
    max_index = [i for i, x in enumerate(max_location) if x]
    max_index = int(max_index[0])

    index_af_max = range(max_index, end_index)
    y_af_max = y[index_af_max]
    t_af_max = t[index_af_max]

    check10_fall = y_af_max <= 0.1
    t_10fall = t_af_max[check10_fall]
    y_10fall = y_af_max[check10_fall]
    t_10 = t_10fall[0]
    y_10 = y_10fall[0]

    # plt.plot(t_window,y_window,'b')
    # plt.plot([t_window[0],t_window[-1]],[norm_thresh, norm_thresh],'k--')
    # plt.plot([t_window[0],t_window[-1]],[norm_thresh2, norm_thresh2],'b--')
    # plt.plot(t_10, y_10, 'ro')
    # plt.grid(True)
    # plt.show()
