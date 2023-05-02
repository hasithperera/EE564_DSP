#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 14:28:06 2023

@author: hasith
"""



import numpy as np
import matplotlib.pyplot as plt



def butterfly(x, w):

    return [x[i] + w * x[i + 1] for i in range(len(x) // 2)] + \
           [x[i] - w * x[i + 1] for i in range(len(x) // 2)]

def decimate_fft(x):

    n = len(x)
    if n == 1:
        return x
    else:
        xe = decimate_fft(x[::2])
        xo = decimate_fft(x[1::2])
        w = np.exp(-2j * np.pi / n)
        for k in range(n // 2):
            xe[k], xo[k] = butterfly([xe[k], xo[k]], w ** k)
        return np.concatenate([xe, xo])


# Example usage
x = [0,1, 2, 3, 4, 5, 6, 7]
X = decimate_fft(x)

for i in range(0,8):
    print("r: {} im:{}".format(np.real(X[i]),np.imag(X[i])))