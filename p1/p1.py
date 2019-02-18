# Wed Feb 6, 2018 5:57 pm EST
# if __name__ == '__main__':
# Imported packages

import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import signal
sys.path.append('../analysis/')
from read_waveform import read_waveform as rw
from write_waveform import write_waveform
import time
import os

################################
# Signal Parameters
show_plot = False
N = 4002              # Signal window size
fsps = 20000000000.   # Hz, Samples per second
Nloops = 100000
vthr = -0.00025
nhdr = 5

# Parameters for the filter
fc = 250000000.       # Hz, Filter cutoff frequency
wc = 2.*np.pi*fc/fsps # Discrete radial frequency
print('wc',wc)
numtaps = 51              # filter order + 1, chosen for balance of good performance and small transient size
lowpass = signal.firwin(numtaps, cutoff = wc/np.pi, window = 'blackman')    # blackman windowed lowpass filter
# frequency response of the filter

# freq, response = signal.freqz(lowpass)
# amp = 20*(np.log10(np.abs(response)))
# plt.figure()
# plt.plot(freq/np.pi , amp, 'b')
# plt.ylabel('Amplitude Response [dB]')
# plt.xlabel('Normalized Frequency')
# plt.title('Transfer function frequency response')
# plt.grid(True)
# plt.show()

# fil = 'C:/watchman/data/20181212_watchman_spe/C2--waveforms--00020.txt'
# (t,v,hdr) = rw(fil,nhdr)
# y1 = signal.lfilter(lowpass, 1.0, v)
# y2 = signal.filtfilt(lowpass,1.0, v)
# z1 = y1[numtaps:len(y1)-1]
# z2 = y2[numtaps:len(y1)-1]
# ty = t[numtaps:len(y1)-1]
# plt.figure()
# plt.plot(t,v,'b')
# plt.plot(ty,z2,'r',linewidth=3)
# # plt.plot(ty,z1,'c')
# plt.grid(True)
# plt.show()

j = 0
k = 0
h = 0
for i in range(Nloops):
    fname = 'C:/watchman/data/20181212_watchman_spe/C2--waveforms--%05d.txt' % i
    spe_wname = 'C:/watchman/signal_chain_studies/d1/data/D1--waveforms--%05d.txt' % j
    spe_not_there = 'C:/watchman/signal_chain_studies/d1/not_spe/D1--noise--%05d.txt' % k
    spe_unsure = 'C:/watchman/signal_chain_studies/d1/unsure_if_spe/D1--unsure--%05d.txt' % h
    if os.path.isfile(spe_wname):
        j = j + 1
    elif os.path.isfile(spe_not_there):
        k = k + 1
    elif os.path.isfile(spe_unsure):
        h += 1
    else:
        fil = open(fname)
        (t,v,hdr) = rw(fname,nhdr)

        y = signal.filtfilt(lowpass,1.0, v)
        y2 = y[numtaps:len(y)-1]
        t2 = t[numtaps:len(y)-1]

        plt.figure()
        plt.plot(t,v,'b')
        plt.plot(t2,y2,'r',linewidth = 2.5)

        # print(f)
        # plt.plot(t2,y2,'r',linewidth=2.5)
        plt.grid(True)
        print('Displaying file #%05d' % i)
        plt.show(block = False)
        plt.pause(1.5)
        plt.close()

        spe_check = 'pre-loop initialization'
        while spe_check != 'y' and spe_check != 'n' and spe_check != 'u':
            spe_check = raw_input('Is there a visible SPE? "y" or "n"\n')
        if spe_check == 'y':
            # Write data file to processed SPE folder
            write_waveform(t2, y2, spe_wname, hdr)
            j += 1
        elif spe_check == 'n':
            write_waveform(t2, y2, spe_not_there, hdr)
            k += 1
        elif spe_check == 'u':
            write_waveform(t2, y2, spe_unsure, hdr)
            h += 1
        print('file #%05d: Done' % i)






    # placeholder space
