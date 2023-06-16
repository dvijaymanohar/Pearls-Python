# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 12:41:44 2022

@author: remon
"""

import numpy as np
#import matplotlib.pyplot as plt
import random
import struct

#7864.30e6
def gen_bin():
    fs_clock_speed      = 7864.32e6         #Set sampling frequency of the DACs
    amplitude           = -5                #Set max amplitude of signal
    interpolation_rate  = 1                 #Set interpolation rate
    num_samples         = 2**13             #Set number of samples to produce
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
    #div = 16
    #freq = fs_clock_speed/div
    #trange = np.arange(0,num_samples)
    #sine = np.sin(2*np.pi*trange/div)
    #print(sine)
    #plt.plot(sine)

    unit_block = list(np.arange(0,2**15-1,2**3)) + list(np.arange(2**15-1,0,-2**3))
    print(2**16)
    print(num_samples)
    print(len(unit_block))
    print(num_samples/len(unit_block))
    #sig2 = np.round(sig1/max(np.abs(sig1))*num_bits*(10**(amplitude/20)))
    #sig2_dbfs = np.round(sig1/max(np.abs(sig1))*num_bits*(10**(amplitude_fs/20)))
    num = 0


    #unit_block = list(np.linspace(0,2**16-1,2**16))+list(np.linspace(2**16-1,0,2**16))#+list(np.arange())
    numblocks = int(num_samples/len(unit_block))
    sig2 = unit_block*numblocks

    sig = np.uint16(sig2)
    #plt.plot(sig)
    #plt.show()
    

    File = open(filename,"wb")
    for s in sig2:
        File.write(struct.pack('h',int(s)))


    return

def main():
    gen_bin()


if __name__ == "__main__":
    main()

   
   



