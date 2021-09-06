# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

discrete_points = np.exp(2j * np.pi * np.arange(8) / 8)
print(discrete_points)

result = np.fft.fft(discrete_points)
print(result)

#%%

import matplotlib.pyplot as plt

#intervals
t = np.arange(256)

#Discrete Points
discrete_points1 = np.sin(t)
discrete_points2 = np.cos(t)
sp = np.fft.fft(discrete_points1)
sp1 = np.fft.fft(discrete_points2)

#Retrieve the frequencies
freq = np.fft.fftfreq(t.shape[-1])

#Plot the frequencies vs sampled points, real and imaginary
plt.plot(freq, sp.real, freq, sp.imag)
plt.plot(freq, sp1.real, freq, sp1.imag)
plt.show()

#%% - FFT with scipy
import matplotlib.pyplot as plt
from scipy.fftpack import fft

# Number of samplepoints
N = 600

# Sample spacing - must be regular
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)



#fig, ax = plt.subplots()
plt.subplot(3, 1, 1)
#ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.subplot(3, 1, 2)
#The high spike that we see is due to the DC (non-varying, i.e. freq = 0) portion 
#of the signal. We want to see non-DC frequency content - 
#so we need to plot from the offset 1 (not from offset 0 of the FFT of the signal).
plt.plot(xf[1:], 2.0/N * np.abs(yf[0:N//2])[1:])
plt.subplot(3, 1, 3)
plt.semilogy(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.show()
