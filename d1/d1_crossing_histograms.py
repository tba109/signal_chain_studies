import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def get_crossings(fname):
    dist = np.array([])
    fin = open(fname,'r')
    for line in fin:
        dist = np.append(dist, float(line.split(',')[0]))
    fin.close()
    return dist

falling20_dist = get_crossings('falling20_dist.txt')
falling50_dist = get_crossings('falling50_dist.txt')
falling80_dist = get_crossings('falling80_dist.txt')
rising20_dist = get_crossings('rising20_dist.txt')
rising50_dist = get_crossings('rising50_dist.txt')
rising80_dist = get_crossings('rising80_dist.txt')
# print(rising50_dist)

bin_num = 200
fig = plt.figure(figsize=(6,4))
plt.hist(rising20_dist,bins = bin_num)
plt.hist(rising50_dist,bins = bin_num)
plt.hist(rising80_dist,bins = bin_num)
plt.hist(falling80_dist,bins = bin_num)
plt.hist(falling50_dist,bins = bin_num)
plt.hist(falling20_dist,bins = bin_num)
plt.title('Histogram of crossing times relative to the maximum peak point')#,fontsize = 18)
plt.xlabel('Time [s]')#,fontsize = 18)
plt.ylabel('Count')#,fontsize = 18)
plt.legend(['r20','r50','r80','f80','f50','f20'])
fig.savefig('C:/Users/Andrew Blount/Desktop/Histograms.png',dpi = 300)
plt.show()
