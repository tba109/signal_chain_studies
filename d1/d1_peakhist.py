import sys
sys.path.append('../analysis/')
import numpy as np
import matplotlib.pyplot as plt
from read_waveform import read_waveform as rw
import os

Nloops = len(os.listdir('./d1_50centered/'))
nhdr = 5
j = 0
peak_dist = np.array([])

for i in range(j,Nloops):
    print i
    fname = 'C:/watchman/signal_chain_studies/d1/d1_50centered/D1--waveforms--%05d.txt' %i
    (t,y,hdr) = rw(fname,nhdr)
    y_window = y[500:1000]
    t_window = t[500:1000]
    peak = min(y_window)
    t_peak = t[y == peak]
    peak_dist = np.append(peak_dist, peak)


    plt.plot(t,y,'b.')
    plt.plot(t_peak[0],peak,'ro')
    plt.grid(True)
    plt.show()

# def write_file(fname,dist):
#     fout = open(fname,'w')
#     for entry in dist:
#         line = '%.7e,\n' % entry
#         fout.write(line)
#     fout.close()
#
# bin_num = 200
# fig = plt.figure(figsize=(6,4))
# plt.hist(peak_dist * 1000,bins = bin_num)
# plt.title('Histogram of Amplitudes')#,fontsize = 18)
# plt.xlabel('Amplitudes [V]')#,fontsize = 18)
# plt.ylabel('Count')#,fontsize = 18)
# fig.savefig('C:/Users/Andrew Blount/Desktop/amplitude_hist.png',dpi = 300)
# plt.show()
#
#
# write_file('./peak_dist.txt', peak_dist)
