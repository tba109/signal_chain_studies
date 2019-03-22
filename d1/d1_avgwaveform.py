import sys
sys.path.append('../analysis/')
import numpy as np
import matplotlib.pyplot as plt
from read_waveform import read_waveform as rw
from write_waveform import write_waveform
import os

Nloops = len(os.listdir('./d1_50centered/'))
nhdr = 5
j = 0
center_index = 759
fsps = 20000000000.
dt = 1.0/fsps
fname = 'C:/watchman/signal_chain_studies/d1/d1_50centered/D1--waveforms--00000.txt'
(t,y,hdr) = rw(fname,nhdr)
num_points = len(y)

y_mean = 0
# for i in range(j,Nloops):
#     print i
#     fname = 'C:/watchman/signal_chain_studies/d1/d1_50centered/D1--waveforms--%05d.txt' % i
#     (t,y,hdr) = rw(fname,nhdr)
#     y_norm = y / min(y)
#     y_mean = y_mean + y_norm
#     # print(y[center_index])
#     # if i == 0:
#     #     y_stack = y_norm
#     # if i != 0:
#     #     y_stack = np.vstack([y_stack, y_norm])
#     # plt.plot(t,y_norm)
#     # plt.show()

# y_mean = y_mean / Nloops
# tstart = -4.0*10**(-8)
# tend = tstart + (num_points-1)*dt
# t_mean = np.arange(tstart,tend + dt, dt)
(t_mean,y_mean,hdr) = rw('./mean_waveform.txt',nhdr)

# write_waveform(t_mean, y_mean, './mean_waveform.txt', hdr)
fig = plt.figure(figsize=(6,4))
plt.plot(t_mean, y_mean, 'b')
plt.title('Average Normalized SPE Waveform')
plt.xlabel('Time [s]')
plt.ylabel('Normalized Amplitude')
plt.grid(True)
fig.savefig('C:/Users/Andrew Blount/Desktop/mean_SPE.png',dpi = 300)
plt.show()
