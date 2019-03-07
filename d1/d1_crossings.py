import sys
sys.path.append('../analysis/')
import numpy as np
import matplotlib.pyplot as plt
from read_waveform import read_waveform as rw
import os

Nloops = len(os.listdir('./d1_normalized/'))
nhdr = 5
j = 0

for i in range(j,Nloops):
    fname = 'C:/watchman/signal_chain_studies/d1/d1_normalized/D1--waveforms--%05d.txt' % i
    (t,y,hdr) = rw(fname,nhdr)
    y = y[370:1370]
    t = t[370:1370]
    check50 = y >= 0.5
    check20 = y >= 0.2
    check80 = y >= 0.8
    my_50crossing = t[check50]
    my_20crossing = t[check20]
    my_80crossing = t[check80]
    y50 = y[check50]
    y20 = y[check20]
    y80 = y[check80]

    rising50 = my_50crossing[0]
    falling50 = my_50crossing[-1]

    rising20 = my_20crossing[0]
    falling20 = my_20crossing[-1]

    rising80 = my_80crossing[0]
    falling80 = my_80crossing[-1]

    print('rising 20: %e' %rising20)
    print('rising 50: %e' %rising50)
    print('rising 80: %e' %rising80)
    print('\n')
    print('falling 80: %e' %falling80)
    print('falling 50: %e' %falling50)
    print('falling 20: %e' %falling20)
    print('\n')

    plt.plot(t,y,'b')
    plt.plot([t[0],t[-1]],[0.5,0.5],'k--')
    plt.plot([t[0],t[-1]],[0.2,0.2],'k--')
    plt.plot([t[0],t[-1]],[0.8,0.8],'k--')
    plt.plot([rising20, falling20],[y20[0], y20[-1]],'ro')
    plt.plot([rising50, falling50],[y50[0], y50[-1]],'ro')
    plt.plot([rising80, falling80],[y80[0], y80[-1]],'ro')

    plt.grid(True)
    plt.show()
