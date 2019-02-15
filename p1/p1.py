# Wed Feb 6, 2018 5:57 pm EST
# if __name__ == '__main__':
# Imported packages

import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import signal
sys.path.append('../analysis/')
from read_waveform import read_waveform as rw
import time

################################
# Signal Parameters
show_plot = False
N = 4002              # Signal window size
fsps = 20000000000.   # Hz, Samples per second
Nloops = 100000
vthr = -0.00025

# Parameters for the filter
fc = 250000000.       # Hz, Filter cutoff frequency
wc = 2.*np.pi*fc/fsps # Discrete radial frequency
print('wc',wc)
numtaps = 51              # filter order + 1
lowpass = signal.firwin(numtaps, cutoff = wc/np.pi, window = 'blackman')
freq, response = signal.freqz(lowpass)
amp = 20*(np.log10(np.abs(response)))
plt.figure()
plt.plot(freq/np.pi , amp, 'b')
plt.ylabel('Amplitude Response [dB]')
plt.xlabel('Normalized Frequency')
plt.title('Transfer function frequency response')
plt.grid(True)
# plt.show()

fil = 'C:/watchman/data/20181212_watchman_spe/C2--waveforms--00020.txt'
nhdr = 5
(t,v,hdr) = rw(fil,nhdr)
y1 = signal.lfilter(lowpass, 1.0, v)
y2 = signal.filtfilt(lowpass,1.0, v)
z1 = y1[numtaps:len(y1)-1]
z2 = y2[numtaps:len(y1)-1]
ty = t[numtaps:len(y1)-1]
plt.figure()
plt.plot(t,v,'b')
plt.plot(ty,z2,'r',linewidth=3)
# plt.plot(ty,z1,'c')
plt.grid(True)
plt.show()

for i in range(Nloops):
    print('Displaying file #%05d' % i)
    fname = 'C:/watchman/data/20181212_watchman_spe/C2--waveforms--%05d.txt' % i
    fil = open(fname)
    (t,v,hdr) = rw(fname,nhdr)
    y2 = signal.filtfilt(lowpass,1.0, v)
    z2 = y2[numtaps:len(y1)-1]
    ty = t[numtaps:len(y1)-1]
    plt.figure()
    plt.plot(t,v,'b')
    plt.plot(ty,z2,'r',linewidth=2.5)
    plt.grid(True)
    plt.show()
    print('file #%05d: Done' % i)

    # for j in range(5):
    #     fil.readline()
    #     n = np.array([])
    #     x = np.array([])
    #     y = np.array([])
    #     ni = 0
    # for line in fil:
    #     print(line, type(line))
    #     n = np.append(n, ni)
    #     x = np.append(x, float(line.split(',')[0]))
    #     y = np.append(y, float(line.split(',')[1]))
    #     ni+=1
        # print(x,y)
        # time.sleep(1)





    # placeholder space
