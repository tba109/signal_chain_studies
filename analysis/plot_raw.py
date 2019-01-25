#!/usr/bin/env python

################################################################
# Fri Jan 25 12:40:29 EST 2019
# 
# A python command line interface for plotting raw images. 
#
# Revision Log:
#
################################################################

import sys
sys.path.append('../')
sys.path.append('')
import numpy as np
import matplotlib.pyplot as plt
import os

###############################################################
# Plot the data
def plot_raw(x,y,xlim=None,ylim=None):
    plt.plot(x,y,xlim,ylim)
    plt.show()


###############################################################
# Plot the data
def test(xlim=None,ylim=None):
    x = np.arange(0,10,0.1)
    y = [np.random.normal(0,0.05) for i in range(len(x))]
    for i in range(10): 
        y[10+i] = y[i]+1.
    plot_raw(x,y,xlim,ylim)
    

###############################################################
# For running independently
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(prog="plot_raw",description="Plot raw data.")
    parser.add_argument("--xlim",nargs='+',type=float,help="limits for x axis")
    parser.add_argument("--ylim",nargs='+',type=float,help="limits for y axis")
    parser.add_argument("--nhdr",type=int,help='number of header lines to skip in the raw file',default=0)
    parser.add_argument("--test",action='store_true',help="create a test plot")
    parser.add_argument("--fname",type=str,help="only plot the data in this file (use absolute path)")
    parser.add_argument("--path",type=str,help="path for files in analysis",default="~/20181212_watchman_spe/")
    parser.add_argument("--n",type=int,help="number of files to run",default=1)
    args = parser.parse_args()

    # Test case for plotting
    if(args.test):
        test(args.xlim,args.ylim)
        sys.exit()
    
    # fin = open(args.fname)
    # for line in fin: 
    #     print line

    # Plot a single file
    with open(args.fname) as fin:
        try:
            for i in range(args.nhdr): 
                print fin.readline()
            x = []
            y = []
            for line in fin: 
                x.append(float(line.split(',')[0]))
                y.append(float(line.split(',')[1]))
            plot_raw(x,y,args.xlim,args.ylim)
            fin.close()
        except: 
            print 'Error: could not open file %s' % args.fname
            sys.exit(-1)
    

