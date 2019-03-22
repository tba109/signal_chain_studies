import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def read_file(fname):
    dist = np.array([])
    fin = open(fname,'r')
    for line in fin:
        dist = np.append(dist, float(line.split(',')[0]))
    fin.close()
    return dist

# falling20_dist = read_file('falling20_dist.txt')
# falling50_dist = read_file('falling50_dist.txt')
# falling80_dist = read_file('falling80_dist.txt')
# rising20_dist = read_file('rising20_dist.txt')
# rising50_dist = read_file('rising50_dist.txt')
# rising80_dist = read_file('rising80_dist.txt')
rise_times = read_file('rise_time.txt')
fall_times = read_file('fall_time.txt')

bin_num = 200
fig = plt.figure(figsize=(6,4))
plt.hist(rise_times,bins = bin_num)
plt.hist(fall_times,bins = bin_num)
plt.title('Histogram of Crossing Times Relative to Rising 50% point')#,fontsize = 18)
plt.xlabel('Time [s]')#,fontsize = 18)
plt.ylabel('Count')#,fontsize = 18)
plt.legend(['rise times','fall times'])
fig.savefig('C:/Users/Andrew Blount/Desktop/rise&fall_hist.png',dpi = 300)
plt.show()
