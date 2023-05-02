#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 09:36:30 2023

@author: hasith
"""

import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import time

def butterfly(x, w):

    return [x[i] + w * x[i + 1] for i in range(len(x) // 2)] + \
           [x[i] - w * x[i + 1] for i in range(len(x) // 2)]

def decimate_fft(x):

    n = len(x)
    if n == 1:
        return x
    else:
        xe = decimate_in_frequency_fft(x[::2])
        xo = decimate_in_frequency_fft(x[1::2])
        w = np.exp(-2j * np.pi / n)
        for k in range(n // 2):
            xe[k], xo[k] = butterfly([xe[k], xo[k]], w ** k)
        return np.concatenate([xe, xo])


if __name__=='__main__':
    

    bits = []
    run_time = []
    np_fft = []
    
    with open('data.txt','a+') as fp:
        fp.write("# fft time experiment data file")
        fp.write("#bits,my_fft,np_fft\n")
    
    for bit in range(7,15):
        print(2**bit)
           
        N = 2**bit
        t = np.linspace(0,5,N)
        dt = t[1]-t[0]
        f = 1/dt

        f0 = 3*f/N;
        x = 128*np.sin(2*np.pi*f0*t)
        dt = time.time()
        fft = decimate_fft(x)
        my_time = time.time()-dt
        run_time.append(my_time)
        bits.append(bit)
        
        dt = time.time()
        y = np.fft.fft(x)
        np_time = time.time()-dt
        np_fft.append(np_time)
        with open('data.txt','a+') as fp:
            fp.write("{},{},{}\n".format(bit,my_time,np_time))
        
    
    plt.plot(bits,run_time)
    plt.plot(bits,np_fft)
    plt.legend(['my_time','np_time'])