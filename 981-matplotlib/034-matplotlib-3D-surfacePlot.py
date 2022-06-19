# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Matplotlib - 3D Surface plot
"""
"""
Surface plot shows a functional relationship between a designated dependent variable (Y), 
and two independent variables (X and Z). 
The plot is a companion plot to the contour plot. 
A surface plot is like a wireframe plot, but each face of the wireframe is a filled polygon. 
This can aid perception of the topology of the surface being visualized. 
The plot_surface() function x,y and z as arguments.
"""

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
x = np.outer(np.linspace(-2, 2, 30), np.ones(30))
y = x.copy().T # transpose
z = np.cos(x ** 2 + y ** 2)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(x, y, z,cmap='viridis', edgecolor='none')
ax.set_title('Surface plot')
plt.show()