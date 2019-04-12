import sys
sys.path.append('../analysis/')
import numpy as np
import matplotlib.pyplot as plt
from read_waveform import read_waveform as rw
import os

# Following SPE files from d1_cleaned don't meet necessary crossing time criteria: 00438, 01463, 02001, 06347, 07761, 08673, 09082

Nloops = len(os.listdir('./d1_50centered/'))
nhdr = 5
j = 0

rising20_dist = np.array([])
rising50_dist = np.array([])
rising80_dist = np.array([])

falling20_dist = np.array([])
fwhm_dist = np.array([])
falling80_dist = np.array([])

for i in range(j,Nloops):
    print i
    fname = 'C:/watchman/signal_chain_studies/d1/d1_50centered/D1--waveforms--%05d.txt' % i
    # print(fname)
    (t,y,hdr) = rw(fname,nhdr)
    y = y / min(y)
    # y_window = y[370:1370]
    # t_window = t[370:1370]
    max_location = y == 1
    max_index = [i for i, x in enumerate(max_location) if x]
    max_index = int(max_index[0])
    index_b4_max = range(500,max_index)
    index_af_max = range(max_index, len(y)-1)
    # print(index_af_max)

    y_b4_max = y[index_b4_max]
    y_af_max = y[index_af_max]

    t_b4_max = t[index_b4_max]
    t_af_max = t[index_af_max]

    # tmax = t[max_index]
    # tmax=0
    # print('tmax %e' %tmax)


    check20_rise = y_b4_max >= 0.2
    check50_rise = y_b4_max >= 0.5
    check80_rise = y_b4_max >= 0.8

    check20_fall = y_af_max <= 0.2
    check50_fall = y_af_max <= 0.5
    check80_fall = y_af_max <= 0.8

    t_20rise = t_b4_max[check20_rise]
    t_50rise = t_b4_max[check50_rise]
    t_80rise = t_b4_max[check80_rise]

    t_20fall = t_af_max[check20_fall]
    t_50fall = t_af_max[check50_fall]
    t_80fall = t_af_max[check80_fall]

    y20_rise = y_b4_max[check20_rise]
    y50_rise = y_b4_max[check50_rise]
    y80_rise = y_b4_max[check80_rise]

    y20_fall = y_af_max[check20_fall]
    y50_fall = y_af_max[check50_fall]
    y80_fall = y_af_max[check80_fall]

    rising20 = t_20rise[0]
    falling20 = t_20fall[0]
    rising20_dist = np.append(rising20_dist,rising20)
    falling20_dist = np.append(falling20_dist,falling20)

    rising50 = t_50rise[0]
    fwhm = t_50fall[0]
    rising50_dist = np.append(rising50_dist,rising50)
    fwhm_dist = np.append(fwhm_dist,fwhm)

    rising80 = t_80rise[0]
    falling80 = t_80fall[0]
    rising80_dist = np.append(rising80_dist,rising80)
    falling80_dist = np.append(falling80_dist,falling80)



    # print('rising 20: %e' %rising20)
    # print('rising 50: %e' %rising50)
    # print('rising 80: %e' %rising80)
    # print('\n')
    # plt.pause(1)
    # print('falling 80: %e' %falling80)
    # print('falling 50: %e' %falling50)
    # print('falling 20: %e' %falling20)
    # print('Current falling 20 distribution',falling20_dist)
    # print('\n')

    # plt.plot(y,'b.')
    # plt.plot([rising20, falling20],[y20_rise[0], y20_fall[0]],'ro')
    # plt.plot([rising50, fwhm],[y50_rise[0], y50_fall[0]],'ro')
    # plt.plot([rising80, falling80],[y80_rise[0], y80_fall[0]],'ro')
    # plt.plot( [min(t),max(t)], [0.5,0.5], 'k--')
    # plt.plot( [min(t),max(t)], [0.2,0.2], 'k--')
    # plt.plot( [min(t),max(t)], [0.8,0.8], 'k--')
    # plt.grid(True)
    # plt.show()
rise_time = rising80_dist - rising20_dist
fall_time = falling20_dist - falling80_dist

fout_rising20 = 'rising20_dist.txt'
fout_falling20 = 'falling20_dist.txt'
# fout_rising50 = 'rising50_dist.txt'   # Just a file of zeros since times are centered around r50
fout_fwhm = 'fwhm.txt'   # Actually the FWHM
fout_rising80 = 'rising80_dist.txt'
fout_falling80 = 'falling80_dist.txt'

def write_file(fname,arg,dist):
    fout = open(fname,arg)
    for entry in dist:
        line = '%.7e,\n' % entry
        fout.write(line)
    fout.close()

write_file(fout_rising20,'w',rising20_dist)
# write_file(fout_rising50,'w',rising50_dist)
write_file(fout_rising80,'w',rising80_dist)
write_file(fout_falling20,'w',falling20_dist)
write_file(fout_fwhm,'w',fwhm_dist)
write_file(fout_falling80,'w',falling80_dist)
write_file('rise_time.txt','w',rise_time)
write_file('fall_time.txt','w',fall_time)

# plt.hist(rising50_dist, bins = 'auto')
# plt.title('Rising 50% histogram with automated bins')
