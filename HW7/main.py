# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz
from scipy.signal import remez

# Define the filter parameters
fs = 1      # Sample rate, Hz
passband = [.1, .2]  # Passband frequency range, Hz
width = .1      # Width of the passband, Hz
N = 64  # Filter length

beta = 4
# Compute the filter coefficients using the firwin function
nyquist = fs / 2
cutoff = np.array(passband) / nyquist


plt.figure(1)

for i,win in enumerate(['hamming','hann','kaiser']):
    taps = []
    if i==2:
        taps = firwin(N, cutoff,pass_zero=False,window=('kaiser', beta))
    else:
        taps = firwin(N, cutoff,pass_zero=False,window=win)
    # Plot the frequency response of the filter
    # clear variables just to make sure
    freq = []
    mag = []
    freq, response = freqz(taps)
    mag = np.abs(response)
    phase = np.angle(response)
    
    plt.subplot(2, 1, 1)
    plt.plot(freq * fs / (2 * np.pi), 20*np.log(mag))
    
    plt.subplot(2, 1, 2)
    plt.plot(freq * fs / (2 * np.pi), phase)

band = [.1, .2]  # Desired pass band, Hz
trans_width = .02    # Width of transition from pass to stop, Hz
edges = [0, band[0] - trans_width, band[0], band[1],
         band[1] + trans_width, 0.5*fs]
taps = remez(N, edges, [0,1,0], Hz=fs)
freq, response = freqz(taps)
mag = np.abs(response)
phase = np.angle(response)

plt.subplot(2, 1, 1)
plt.plot(freq * fs / (2 * np.pi), 20*np.log(mag))
plt.title('Magnitude Response')
plt.xlabel('Frequency')
plt.ylabel('db')
plt.legend({'hamming','hann',r'kaiser,$\beta=4$','Parks McClellan'})

plt.subplot(2, 1, 2)
plt.plot(freq * fs / (2 * np.pi), phase)
plt.title('Phase Response')
plt.xlabel('Frequency (MHz)')
plt.ylabel('Phase (radians)')
plt.tight_layout()
    
   
plt.legend({'hamming','hann',r'kaiser,$\beta=4$','Parks McClellan'})
