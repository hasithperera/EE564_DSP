#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 08:42:54 2023
Author : Hasith Perera

"""

import numpy as np
import matplotlib.pyplot as plt


n_bits = 6

t = np.arange(1,1000,1e-3)
sig_len =  len(t)
f0 = 10

levels = 2**n_bits

data = []
bits = np.arange(0.25,6.25,0.25);
# bits = np.arange(0,6);

for i,rms_bits in enumerate(bits):
# input_sig = np.sin((2*np.pi*f0)*t)
# rms_bits = 6

    
    sig_rms = 2**rms_bits
    
    mu, sigma = 0, 1 # mean and standard deviation
    x = sig_rms*np.random.normal(mu, sigma, size=(sig_len,))
 
    x_clip = np.clip(x, -2**(n_bits-1), 2**(n_bits-1)-1)
    
    # print("sig rms:{}".format(np.sqrt(np.sum(x_clip*x_clip)/sig_len)))
 
    
    # level spacing 1 
    x_c = np.round(x,0)
    x_bar = np.round(x_clip,0)
    
    bins = np.arange(-2**(n_bits-1),2**(n_bits-1))
    
    x_bar_var = np.var(x_bar)
    x_vsr = np.var(x)
    print(x_bar_var)
    data.append(x_bar_var/x_vsr)
    
plt.plot(bits,data,'.-')
plt.ylabel(r"$\frac{<\hat{x}>}{<x\hat{x}>}$")
plt.xlabel("Sig-RMS bits")