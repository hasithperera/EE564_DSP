#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 08:45:54 2023
Author : Hasith Perera

"""

import numpy as np
import matplotlib.pyplot as plt

import scipy as sp

n_bits = 6

N = 2**n_bits 
q = 1


x_hat_data = []
x_x_hat_data = []
rms_bits = np.arange(.25,6.25,.25)
for k in rms_bits:
    
    q = 1/(2**(k))
    
    x_x_hat = .5;
    x_hat = (N-.5) **2
    for m in range(1,N):
        x_hat = x_hat - 2*m*sp.special.erf(m*q/np.sqrt(2))
        x_x_hat = x_x_hat + np.exp((-(m*q)**2)/2)
    x_hat_data.append(x_hat)
    x_x_hat_data.append((2/np.pi)*(x_x_hat**2))
    
x_d = np.array(x_hat_data)
xx_d = np.array(x_x_hat_data)

cal = x_d/xx_d

plt.plot(rms_bits,cal)

i = np.argmin(cal)
plt.plot(rms_bits[i],cal[i],'o')
# plt.plot()
    # print(x_hat)
plt
    



