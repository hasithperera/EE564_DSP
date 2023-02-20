#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 08:42:54 2023
Author : Hasith Perera

"""

import numpy as np
import matplotlib.pyplot as plt


n_bits = 6

t = np.arange(1,10,1e-3)
sig_len =  len(t)
f0 = 10

for i,rms_bits in enumerate([2,4,6,2,4,6]):
# input_sig = np.sin((2*np.pi*f0)*t)
# rms_bits = 6

    if i > 2:      
        n_bits = 8
    
    levels = 2**n_bits
    
    sig_rms = 2**rms_bits
    
    mu, sigma = 0, 1 # mean and standard deviation
    x = sig_rms*np.random.normal(mu, sigma, size=(sig_len,))
    x_clip = np.clip(x, -2**(n_bits-1), 2**(n_bits-1)-1)
    
    # print("sig rms:{}".format(np.sqrt(np.sum(x_clip*x_clip)/sig_len)))
 
    
   
    
    # level spacing 1 
    x_bar = np.round(x_clip,0)
    
    
    # print(x_bar[0:10])
    
    # plt.plot(t,x,'.-')
    # plt.plot(t,x_bar)
    
    # plt.plot(x,x_bar,'.')
    
    # # plt.grid()
    
    plt.figure(1)
    # print(i+1)
    plt.subplot(2,3,i+1)
    bins = np.arange(-2**(n_bits-1),2**(n_bits-1))
    
    #use auto binning
    indx_x,bins = np.histogram(x,len(bins),normed=1)
    plt.plot(bins[0:-1]+.5,indx_x)
    
    indx_x_bar,bins = np.histogram(x_bar,np.arange(-2**(n_bits-1),2**(n_bits-1)),normed=1)
    plt.plot(bins[0:-1]+.5,indx_x_bar)
    plt.legend(['x',r'$\hat{x}$'])
    
    ## clip count :
    clip_cnt_l = np.sum(x<-2**(n_bits-1))
    clip_cnt_h = np.sum(x>2**(n_bits-1)-1)
    
    print("clip count:{}+{}".format(clip_cnt_l,clip_cnt_h))
    print("clip count from hist:{},{}".format(indx_x_bar[0],indx_x_bar[-1]))
    print("ADC bits:{}".format(n_bits))
    print("sig bits:{}".format(rms_bits))
    print("clip per:{:.2f}%".format((clip_cnt_l+clip_cnt_h)*100/len(x)))
    
    # break
    # plt.figure(1)
    # plt.subplot(2,3,i+1)
    # plt.plot(t[0:200],x[0:200],'o-')
    # plt.plot(t[0:200],x_bar[0:200],'.-')
    # plt.xlabel('t')
    # plt.ylabel('voltage')
    # plt.legend(['x',r'$\hat{x}$'])
    # plt.title('{}-bits'.format(n_bits))