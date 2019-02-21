import os
files = os.listdir('.')

for i in range(len(files)):
    os.rename(files[i],'D1--waveforms--%05d.txt' % i)
