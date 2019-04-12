import sys
sys.path.append('../analysis/')
import numpy as np
import matplotlib.pyplot as plt
from read_waveform import read_waveform as rw
from write_waveform import write_waveform
import os


Nloops = len(os.listdir('./d1_cleaned/'))
nhdr = 5
vthresh_win = -0.0115
vthresh_out = -0.013
n = 0
# print(Nloops)
j = 7935
if True:
    for i in range(j,Nloops):
        print i
        fname = 'C:/watchman/signal_chain_studies/d1/d1_cleaned/D1--waveforms--%05d.txt' % i
        wname = 'C:/watchman/signal_chain_studies/d1/d1_baseline_shifted/D1--waveforms--%05d.txt' % i
        (t,y,hdr) = rw(fname,nhdr)
        baseline = np.mean(y[0:200])
        y_window = y[370:1370]
        y_new = (y - baseline)
        # y_max = min(y_new[370:1370])
        # y_new = y_new / y_max   # Shifting and normalizing the SPEs
        write_waveform(t,y_new,wname,hdr)
        # plt.plot(t,y_new,'b')
        # plt.grid(True)
        # plt.show()
if False:
    for i in range(j,Nloops):
        # print i
        fname = 'C:/watchman/signal_chain_studies/d1/d1_cleaned/D1--waveforms--%05d.txt' % i
        (t,y,hdr) = rw(fname,nhdr)
        y = y[0:len(y)-50]  # Don't want to consider spikes at the end of data set
        t = t[0:len(t)-50]
        y_window = y[370:1370]
        t_window = t[370:1370]
        y_out = np.append(y[0:370], y[1370:len(y)])


        # if min(y_window) > vthresh_win or min(y_out) < vthresh_out:   # Used for sorting through bad SPEs, not needed for baseline shift
            # print i
            # n += 1
            # print n
            # plt.plot(t,y,'b')
            # plt.plot(t,vthresh_win*np.ones(len(y)),'k')
            # plt.plot(t,vthresh_out*np.ones(len(y)),'r')
            # plt.plot(t_window[0]*np.ones(2),np.array([-0.01, -0.016]),'k--' )
            # plt.plot(t_window[-1]*np.ones(2),np.array([-0.01, -0.016]),'k--' )
            # plt.grid(True)
            # plt.show()
            # os.remove(fname)  # Deleting files that don't meet criteria
            # print('file #%i removed' %i)

# print('Total number of shifted SPEs: %i' %n)
# 258 shifted SPEs when only looking at window
# file no 9565 is a double SPE detected by introducing the second check
# 282 shifted or double SPEs detected after implementing second check
