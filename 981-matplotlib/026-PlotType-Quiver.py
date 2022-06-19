# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Matplotlib - Quiver Plot
"""
"""
A quiver plot displays the velocity vectors as arrows with components (u,v) at the points (x,y).

quiver(x,y,u,v)

The above command plots vectors as arrows at the coordinates specified in each corresponding pair of elements in x and y.
Parameters

The following table lists down the different parameters for the Quiver plot −
x 	1D or 2D array, sequence. The x coordinates of the arrow locations
y 	1D or 2D array, sequence. The y coordinates of the arrow locations
u 	1D or 2D array, sequence. The x components of the arrow vectors
v 	1D or 2D array, sequence. The y components of the arrow vectors
c 	1D or 2D array, sequence. The arrow colors
"""
#The following code draws a simple quiver plot −

import matplotlib.pyplot as plt
import numpy as np
x,y = np.meshgrid(np.arange(-2, 2, .2), np.arange(-2, 2, .25))
z = x*np.exp(-x**2 - y**2)
v, u = np.gradient(z, .2, .2)
fig, ax = plt.subplots()
q = ax.quiver(x,y,u,v)
plt.show()