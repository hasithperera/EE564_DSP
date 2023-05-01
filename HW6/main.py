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
    
   
    t = np.linspace(0,5,2**4)
    dt = t[1]-t[0]
    df = 1 / dt
    f = 2
    y = 255*(.5*np.sin(2*np.pi*t*f)+.5)
    
    fft = []
    
    for i in range(0,len(t)):
        fft.append(DFT(y,i))
#    print(a)
    
    plt.plot(t,y)
    plt.figure()
    plt.plot(np.abs(fft))
    plt.plot(np.abs(np.fft.fft(y)),'o')
    
    plt.legend(['my DFT','np.fft.fft'])
    
#    print(fft)