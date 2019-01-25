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
sys.path.append('../analysis/')
import numpy as np
import matplotlib.pyplot as plt
import downsample

###############################################################
# Reorder an event list
def plot_raw(fname):
    print ''
    

###############################################################
# For running independently
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(prog="plot_raw",description="Plot raw data.")
    parser.add_argument("--center_thr",type=int,help="center_threshold",default=100)
    parser.add_argument("--version",action="version",version="%(prog)s 1.1")
    parser.add_argument("--verbose",help="Print additional debugging info",action="store_true")

    args = parser.parse_args()
    mc = MrXClass.MrXClass()

    # Setup logging
    if not args.loud:
        logging.basicConfig(filename='log.txt',format='%(asctime)s %(name)s %(levelname)s %(message)s',level=logging.DEBUG,filemode='w')
    
    if args.verbose:
        # print args
        print "----------------------------------------------------------"
    
    # Default to the COM port if specified, otherwise use ttyUSB port
    if args.COM != None:
        port = "COM" + str(args.COM)
        mc.rs232_setup(port)
    elif args.ttyUSB !=None:
        port = "/dev/ttyUSB" + str(args.ttyUSB)
        mc.rs232_setup(port)
    else:
        logging.warning("nop_bram: No valid COM or ttyUSB found. This will be a dry run.")
        mc.dryrun = True

    if args.verbose: 
        print mc.rs232

    # Open the FITS file
    if args.fits == None:
        print "\nError! Must specify a FITS list! Bailing!\n"
        exit(-1)
    
    fits_list = open(args.fits)
    

    sram_adr=0
    sram_stop_adr=0
    fn=0
    pyg_list = []
    x_size = 0
    y_size = 0
    for ff in fits_list:
        ff = ff[:-1]
        print 'processing %s' % ff
        hdulist = fits.open(ff)

        # print hdulist[0].header.tostring
        scidata = hdulist[0].data
        y_size = len(scidata)
        x_size = len(scidata[0])

        for i in range(len(scidata)):
            for j in range(len(scidata[0])):
                scidata[i][j] = int(tr.truncr(scidata[i][j],args.truncr))

        # Pregrade the images
        x = python_grader.python_grader(scidata,args.center_thr,args.surround_thr,fn)
        for xi in x: 
            pyg_list.append(xi)
        
        # Setup center threshold and surrounding threshold now, because we can!
        mc.exe_cmd('set','center_thr','0',str(args.center_thr),False)
        mc.exe_cmd('set','split_thr','0',str(args.surround_thr),False)

        # Create the commmand
        sram_stop_adr = scidata_to_mrx(mc,scidata,sram_adr,args.verbose)
        sram_adr = sram_stop_adr+1
        fn+=1

    # Send sram_stop_adr
    sram_stop_adr_str = '%012x' % (sram_stop_adr)
    mc.exe_cmd('set','sram_stop_adr','0',sram_stop_adr_str,True)
    print 'sram_stop_adr = %s' % sram_stop_adr_str

    # Run the line processor and read in the event queues
    if args.verbose: print "----------------------------------------------------------"
    mc.exe_cmd('set','lp','0','0',False)
    sleep(1)

    erp_list0 = proc_q(mc,0,args.verbose)
    erp_list1 = proc_q(mc,1,args.verbose)
    erp_list2 = proc_q(mc,2,args.verbose)    
    
    # Create a master ERP list
    erp_list = []
    for el0 in erp_list0: 
        erp_list.append(el0)
    for el1 in erp_list1: 
        erp_list.append(el1)
    for el2 in erp_list2: 
        erp_list.append(el2)

    # Reorder the ERP list
    erp_list = reorder_list(erp_list,x_size,y_size)
    
    # Write the ERP List
    ferp_str = ff + '-erp_evt_list.txt'
    try: 
        ferp = open(ferp_str,'w')
    except: 
        print 'Can\'t open file %s, bailing!' % ferp_str
        sys.exit()
    for el in erp_list: 
        ferp.write(el)
    ferp.close()

    # Reorder the PYG list
    pyg_list = reorder_list(pyg_list,x_size,y_size)
    print 'pyg_list'

    # Write the PYG list
    fpyg_str = ff + '-pyg_evt_list.txt'
    try: 
        fpyg = open(fpyg_str,'w')
    except: 
        print 'Can\'t open file %s, bailing!' % ferp_str
        sys.exit()
    for pyg in pyg_list: 
        fpyg.write(pyg)
    fpyg.close()

    fits_list.close()
    mc.rs232_close()

