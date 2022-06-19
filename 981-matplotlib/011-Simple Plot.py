# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Matplotlib - Simple Plot
"""
"""
We will study a simple line plot of angle in radians vs. its sine value in Matplotlib. 
"""
#We import the Pyplot module from Matplotlib package is imported
import matplotlib.pyplot as plt

#We need an array of numbers to plot. 
#Various array functions are defined in the NumPy library which is imported with the np alias.
import numpy as np
import math

#We obtain the ndarray object of angles between 0 and 2π using the arange() function from the NumPy library.
x = np.arange(0, math.pi*2, 0.05)

#The ndarray object serves as values on x axis of the graph. 
#The corresponding sine values of angles in x to be displayed on y axis are obtained by the following statement −
y = np.sin(x)

#The values from two arrays are plotted using the plot() function.
plt.plot(x,y)

#We set the plot title, and labels for x and y axes.
plt.xlabel("angle")
plt.ylabel("sine")
plt.title('sine wave')

#The Plot viewer window is invoked by the show() function −
plt.show()