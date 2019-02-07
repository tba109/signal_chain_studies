# Wed Feb 6, 2018 5:57 pm EST

# Imported packages

import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import signal
sys.path.append('../analysis/')
from read_waveform import read_waveform as rw

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
M = 400              # number of points in the kernel


fil = "../C2--waveforms--00000.txt"
nhdr = 5
(t,v,hdr) = rw(fil,nhdr)
plt.plot(t,v)
plt.grid(True)
plt.show()

# numtaps = 501
#
n2 = np.arange(-N/2,N/2,1)
h = [np.sin(wc*n2i)/(n2i*np.pi*wc) if n2i != 0 else 1./np.pi for n2i in n2]
# print 'Sinc function for LPF'
# plt.plot(n2,h)
# plt.show()

# Truncate and zero pad
h2 = h[int(len(h)/2-M/2):int(len(h)/2+M/2)] # M points around 0
for i in range(4002-len(h2)): # pad with zeros
    h2.append(0.)
plt.plot(h2)
plt.show()
print(len(h),len(h2))



# if __name__ == '__main__':
#     dt = 0.01
#     t = np.arange(0.0,4.0+dt,dt)
#     x = np.sin(2.0*np.pi*t)
#     xn = x + 0.08 * np.random.randn(len(x))
#     # b = 1.0/3.0*np.ones(3)
#     M = 20
#     b = 1.0/M * np.ones(M)
#     a = np.array([1.0, 0])
#     print('b = ',b)
#     print('a = ',a)
#
#     y = signal.lfilter(b, a, xn)
#     print('Length of x = ' + str(len(x)))
#     print('Length of y = ' + str(len(y)))
#     # print(x,y)
#
#     plt.plot(t,xn,'-.k',linewidth = 1.0)
#     plt.plot(t,y,'b')
#     plt.grid(True)
#     plt.show()
