# -*- coding: utf-8 -*-

## HW6

import numpy as np
import matplotlib.pyplot as plt

def DFT(x,k):
    
    N = len(x)
    val = 0
    for i in range(0,N):
        val = val + x[i]*np.exp(-2j*np.pi*k*i/N)
    return val


    
if __name__=='__main__':
    
    N = 2**6
    t = np.linspace(0,5,N)
    dt = t[1]-t[0]
    f = 1 / dt

    
    # range +/- 128 signed 8 bits
    # exact 3rd bin
    f0 = 3*f/N
    y = 128*(np.sin(2*np.pi*t*f0))
    
    # range +/- 64
    # close to 7
    
    f1 = 7*f/N + .1
    y1 = 64*(np.sin(2*np.pi*t*f1))
    
    # noise
    snr= .2
    ns = 128*(2*(np.random.rand(N)-.5))*snr
    
    y = y + y1
    y_ns = y + ns
    
    
    fft = []
    fft2 = []
    
    for i in range(0,len(t)):
        fft.append(DFT(y,i))
        fft2.append(DFT(y_ns,i))
#    print(a)
    plt.figure(1)
    plt.subplot(211)
    plt.plot(t,y)
    plt.plot(t,y_ns)
    plt.legend(['signal','signal with noise'])
    
    
#    plt.figure(2)
    plt.subplot(212)
    plt.plot(np.abs(fft))
    plt.plot(np.abs(fft2))
#    plt.plot(np.abs(np.fft.fft(y)),'o')
    
    plt.legend(['signal','signal with noise'])
    
#    print(fft)