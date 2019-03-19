import sys
sys.path.append('../analysis/')
import numpy as np
import matplotlib.pyplot as plt
from read_waveform import read_waveform as rw
from write_waveform import write_waveform
import os

Nloops = len(os.listdir('./d1_baseline_shifted/'))
nhdr = 5
j = 0
index50_dist = np.array([])
center_index = 759


# Average index location of the rising 50% point is 759
# Going to shift the time and indices of the data vectors to center them around the 50% point

for i in range(j,Nloops):
    print i
    fname = 'C:/watchman/signal_chain_studies/d1/d1_baseline_shifted/D1--waveforms--%05d.txt' % i
    wname= 'C:/watchman/signal_chain_studies/d1/d1_50centered/D1--waveforms--%05d.txt' % i
    (t,y,hdr) = rw(fname,nhdr)  # Reading in files
    y_norm = y / min(y[370:1370])    # Normalizing to ease calculations
    check = y_norm >= 0.5   # 50% crossing criteria
    index = [k for k, x in enumerate(check) if x]   # code to enumerate index values
    index_50 = int(index[0])    # conversion into int
    t_50 = t[index_50]
    t_new = t - t_50    # Shifting t_50 to t = 0s
    t_50centered = np.roll(t_new, center_index - index_50)  # Rolling the data vectors to allign along a common point
    y_50centered = np.roll(y, center_index - index_50)
    if i == 0:
        y_stack = y_50centered
    if i != 0:
        y_stack = np.vstack([y_stack, y_50centered])
    write_waveform(t_50centered, y_50centered, wname, hdr)

    # index50_dist = np.append(index50_dist, index_50)
    # print index50_dist
    # plt.pause(1)

    # plt.plot(t_50centered,y_50centered / min(y[370:1370]),'b')
    # plt.plot(y_50centered / min(y[370:1370]),'b.')
    # plt.plot(t_50centered[center_index], y_50centered[center_index] / min(y[370:1370]),'ro')
    # plt.grid(True)
    # plt.show()


y_mean = np.mean(y_stack,0)
write_waveform(t_new, y_mean, './mean_waveform.txt', hdr)
plt.plot(t_new, y_mean, 'b')
plt.grid(True)
plt.title('Average SPE Waveform')



# avg_index = int(np.mean(index50_dist))
# print(avg_index)
# num_rows = len(y_stack)
# num_cols = len(y_stack[0])
# size = (num_rows, num_cols)
# print size
