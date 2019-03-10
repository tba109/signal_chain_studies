import numpy as np
import matplotlib.pyplot as plt

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
print(rising50_dist)

# fin = open('falling20_dist.txt','r')
# for line in fin:
#     falling20_dist = np.append(falling20_dist, float(line.split(',')[0]))
# fin.close()
# print(falling20_dist)
#
# fin = open('falling50_dist.txt','r')
# for line in fin:
#     falling50_dist = np.append(falling50_dist, float(line.split(',')[0]))
# fin.close()
#
# fin = open('falling80_dist.txt','r')
# for line in fin:
#     falling80_dist = np.append(falling80_dist, float(line.split(',')[0]))
# fin.close()
#
# fin = open('rising20_dist.txt','r')
# for line in fin:
#     rising20_dist = np.append(rising20_dist, float(line.split(',')[0]))
# fin.close()
#
# fin = open('rising50_dist.txt','r')
# for line in fin:
#     rising50_dist = np.append(rising50_dist, float(line.split(',')[0]))
# fin.close()
#
# fin = open('rising80_dist.txt','r')
# for line in fin:
#     rising80_dist = np.append(rising80_dist, float(line.split(',')[0]))
# fin.close()
