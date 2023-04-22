# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 12:41:44 2022

@author: remon
"""

import numpy as np
#import matplotlib.pyplot as plt
import random

#7864.30e6

fs_clock_speed      = 4000e6         #Set sampling frequency of the DACs
amplitude           = -5                #Set max amplitude of signal
interpolation_rate  = 1                 #Set interpolation rate
num_samples         = 2**15             #Set number of samples to produce
num_bits            = 2**15             #Set number of bits per sample
amplitude_fs        = 0
fs = fs_clock_speed/interpolation_rate


#filedir = "C:/Users/remon/Desktop/QBird/Mark4/"         #Insert path the folder here
filename = "signal_data.bin"                             #Insert filename here
filenamebin2 = 'internal_check.bin'
#%%

unit_block = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]*8+[0,0,0,0,0,0,0,0]*8*7 +[1,1,1,1,1,1,1,1]*8+[0,0,0,0,0,0,0,0]*8*7 + [1,1,1,1,1,1,1,1]*4*8+[0,0,0,0,0,0,0,0]*8*4 + [1,1,1,1,1,1,1,1]*4*8+[0,0,0,0,0,0,0,0]*8*4

numblocks = int(num_samples/len(unit_block))
sig1 = unit_block*numblocks

#Create binaries from samples

sig2 = np.round(sig1/max(np.abs(sig1))*num_bits*(10**(amplitude/20)))
sig2_dbfs = np.round(sig1/max(np.abs(sig1))*num_bits*(10**(amplitude_fs/20)))
sig = sig2
sig = np.int16(sig)

File = open(filename,"wb")
File.write(sig)

   
   



