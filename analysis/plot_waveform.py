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
import read_waveform as rw

###############################################################
# Plot the data
def plot_raw(x,y,xlim=None,ylim=None):
    plt.plot(x,y,xlim,ylim)
    plt.show()
    
###############################################################
# For running independently
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(prog="plot_raw",description="Plot raw data.")
    parser.add_argument("--xlim",nargs='+',type=float,help="limits for x axis")
    parser.add_argument("--ylim",nargs='+',type=float,help="limits for y axis")
    parser.add_argument("--nhdr",type=int,help='number of header lines to skip in the raw file',default=0)
    parser.add_argument("--fname",type=str,help="only plot the data in this file (use absolute path)")
    args = parser.parse_args()
    
    x,y,header = rw.read_waveform(args.fname,args.nhdr)
    print '-----------------------------------'
    for ih in header:
        print ih[:-1]
    plot_raw(x,y,args.xlim,args.ylim)
