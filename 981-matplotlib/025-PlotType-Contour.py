# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Matplotlib - Contour Plot
"""
"""
Contour plots (sometimes called Level Plots) are a way to show a three-dimensional surface on a two-dimensional plane. 
It graphs two predictor variables X Y on the y-axis and a response variable Z as contours. 
These contours are sometimes called the z-slices or the iso-response values.

A contour plot is appropriate if you want to see how alue Z changes as a function of two inputs X and Y, 
such that Z = f(X,Y). 
A contour line or isoline of a function of two variables is a curve along which the function has a constant value.
The independent variables x and y are usually restricted to a regular grid called meshgrid. 
The numpy.meshgrid creates a rectangular grid out of an array of x values and an array of y values.

Matplotlib API contains contour() and contourf() functions that draw contour lines and filled contours, 
respectively. Both functions need three parameters x,y and z.
"""

import numpy as np
import matplotlib.pyplot as plt
xlist = np.linspace(-3.0, 3.0, 100)
ylist = np.linspace(-3.0, 3.0, 100)
X, Y = np.meshgrid(xlist, ylist)
Z = np.sqrt(X**2 + Y**2)
fig,ax=plt.subplots(1,1)
cp = ax.contourf(X, Y, Z)
fig.colorbar(cp) # Add a colorbar to a plot
ax.set_title('Filled Contours Plot')
#ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')
plt.show()