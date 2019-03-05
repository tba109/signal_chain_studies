import os
files = os.listdir('.')

for i in range(len(files)):
    os.rename(files[i],'D1--waveforms--%05d.txt' % i)

def fix_names(directory,fname):
    files = os.listdir(directory)
    for i in range(len(files)):
        os.rename(files[i],fname + '--%05d.txt' % i)
