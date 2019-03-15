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
    norm_thresh = 0.5

    max_location = y == 1
    max_index = [i for i, x in enumerate(max_location) if x]
    max_index = int(max_index[0])

    index_b4_max = range(start_index, max_index)
    index_af_max = range(max_index, end_index)

    y_b4_max = y[index_b4_max]
    y_af_max = y[index_af_max]
    t_b4_max = t[index_b4_max]
    t_af_max = t[index_af_max]

    check50_rise = y_b4_max >= norm_thresh
    check50_fall = y_af_max <= norm_thresh
    t_50fall = t_af_max[check50_fall]
    y_50fall = y_af_max[check50_fall]
    t_50rise = t_b4_max[check50_rise]
    y_50rise = y_b4_max[check50_rise]

    t_50r = t_50rise[0]
    y_50r = y_50rise[0]
    t_50f = t_50fall[0]
    y_50f = y_50fall[0]

    fwhm = t_50f - t_50r
    t_samp = t[1] - t[0]
    fwhm_samp = int(fwhm / t_samp)
    print('Full width half max samples: %i' % fwhm_samp)

    plt.plot(t_window,y_window,'b-')
    plt.plot([t_window[0],t_window[-1]],[norm_thresh, norm_thresh],'k--')
    plt.plot([t_50r, t_50f], [y_50r, y_50f], 'ro')
    plt.grid(True)
    plt.show()
