#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 15:35:58 2023

@author: hasith
"""

import numpy as np

bin_num = ""
bits = 8


bin_num = "10010001"

def xnor(a,b):
    if a=='1' and b=='0':
        return'0'
    if a=='0'and b=='1':
        return '0'
    return '1'

def bin2uint(bits):
    n = 0
    for i in range(0,len(bits)):
#       print(i,bits[len(bits)-i-1])
       n = n + int(bits[len(bits)-i-1])*2**i
    return n

def LFSR(seed='',bits=8):
    """ Feedback data based on
    https://docs.xilinx.com/v/u/en-US/xapp052
    """
    
    feedback_table = { 8:[6,5,4],
                      16:[15,13,4],
            }
    feedback_bits = feedback_table[bits]
    
    bin_num = seed
    if seed=='':
        for i in range(0,bits):
            bin_num = "{}{}".format(bin_num,int(np.random.rand() > 0.5))
            
        print("Init random seed:{}".format(bin_num))
    
    msb = bin_num[len(bin_num)-1]
    bin_num_o = bin_num
    bin_num = bin_num[0:-1]
 
#    print(bin_num)
    for fb in feedback_bits:
#        print("feedback_bit_val:",bin_num_o[fb-1],msb,xnor(msb,bin_num_o[fb-1]))
#        print(fb)
        msb = xnor(msb,bin_num_o[fb-1]) 

    return "{}{}".format(str(msb),bin_num)
    

if __name__=='__main__':
    
    n_data = []
    n = '00000000'
#    n =''
    count = 255;
    for ii in range(0,count):
        n_data.append(bin2uint(n))
        n = LFSR(n,bits)
        
    plt.hist(n_data,255)
#    plt.plot(freq)
    #one step
   