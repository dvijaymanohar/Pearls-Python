# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 12:41:44 2022

@author: remon
"""

import numpy as np
#import matplotlib.pyplot as plt
import random

#7864.30e6
def gen_bin():
    fs_clock_speed      = 10000e6         #Set sampling frequency of the DACs
    amplitude           = -5                #Set max amplitude of signal
    interpolation_rate  = 1                 #Set interpolation rate
    num_samples         = 20*2**15             #Set number of samples to produce
    num_bits            = 2**15             #Set number of bits per sample
    amplitude_fs        = 0
    fs = fs_clock_speed/interpolation_rate


    #filedir = "C:/Users/remon/Desktop/QBird/Mark4/"         #Insert path the folder here
    filename = "signal_data.bin"                             #Insert filename here
    filenamebin2 = 'internal_check.bin'
    #%%

    #unit_block = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]

    #Counter

    #for i in 

    #numblocks = int(num_samples/len(unit_block))
    #sig1 = unit_block*numblocks
    #print(sig1)
    #Create binaries from samples

    #sig2 = np.round(sig1/max(np.abs(sig1))*num_bits*(10**(amplitude/20)))
    #sig2_dbfs = np.round(sig1/max(np.abs(sig1))*num_bits*(10**(amplitude_fs/20)))
    num = 0
    unit_block = list(np.arange(0,2**16-1,1))+list(np.arange(2**16-1,0,-1))
    numblocks = int(num_samples/len(unit_block))
    sig2 = unit_block*numblocks
    #print(sig2[0:2**17])
    #sig = sig2
    #print(sig)
    sig = np.uint16(sig2)

    #plt.figure()
    #plt.plot(sig)
    #plt.show()

    File = open(filename,"wb")
    File.write(sig)
    return

def main():
    gen_bin()
    

if __name__ == "__main__":
    main()

   
   



