import sys
sys.path.append('../analysis/')
import numpy as np
import matplotlib.pyplot as plt
from read_waveform import read_waveform as rw
import os

Nloops = len(os.listdir('./d1_50centered/'))
nhdr = 5
j = 0
start_index = 370
end_index = 1600

def read_file(fname):
    dist = np.array([])
    fin = open(fname,'r')
    for line in fin:
        dist = np.append(dist, float(line.split(',')[0]))
    fin.close()
    return dist

def write_file(fname,dist):
    fout = open(fname,'w')
    for entry in dist:
        line = '%.7e,\n' % entry
        fout.write(line)
    fout.close()

fwhm = read_file('fwhm.txt')
fwhm_mean = np.mean(fwhm)
t_span = 20 * fwhm_mean
t_start = -0.25e-7
t_end = t_start + t_span
charge_dist = np.array([])


# for i in range(j,Nloops):
#     if i%2 == 0:
#         print i
#     fname = 'C:/watchman/signal_chain_studies/d1/d1_50centered/D1--waveforms--%05d.txt' %i
#     (t,y,hdr) = rw(fname,nhdr)
#     charge_check = (t >= t_start) & (t <= t_end)
#     t_charge = t[charge_check]
#     y_charge = y[charge_check]
#
#     y_charge_mean = np.mean(y_charge)
#     charge = (y_charge_mean * t_span)/50.*10**12 # Calculation of charge then conversion to picoCoulombs
#     charge_dist = np.append(charge_dist, charge)
    # print charge

    # plt.plot(t,y / min(y),'b.')
    # plt.plot(t_charge, y_charge / min(y_charge), 'r')
    # plt.plot([t_start, t_start],[0,1],'k--')
    # plt.plot([t_end, t_end], [0,1],'k--')
    # plt.grid(True)
    # plt.show()


charge_dist = read_file('./charge_dist.txt')
write_file('./charge_dist.txt',charge_dist)
bin_num = 200
fig = plt.figure(figsize=(6,4))
plt.hist(charge_dist,bins = bin_num)
plt.title('Histogram of Charge')#,fontsize = 18)
plt.xlabel('Charge [pC]')#,fontsize = 18)
plt.ylabel('Count')#,fontsize = 18)
fig.savefig('C:/Users/Andrew Blount/Desktop/charge_hist.png',dpi = 300)
plt.show()
