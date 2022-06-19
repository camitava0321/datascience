# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Matplotlib - Subplot2grid() Function
"""
"""
This function gives more flexibility in creating an axes object at a specific location of the grid. 
It also allows the axes object to be spanned across multiple rows or columns.
"""
import matplotlib.pyplot as plt

#Plt.subplot2grid(shape, location, rowspan, colspan)
#In the following example, 
#a 3X3 grid of the figure object is filled with axes objects of varying sizes in row and column spans, 
#each showing a different plot.

a1 = plt.subplot2grid((3,3),(0,0),colspan = 2)
a2 = plt.subplot2grid((3,3),(0,2), rowspan = 3)
a3 = plt.subplot2grid((3,3),(1,0),rowspan = 2, colspan = 2)

import numpy as np
x = np.arange(1,10)

a2.plot(x, x*x)
a2.set_title('square')
a1.plot(x, np.exp(x))
a1.set_title('exp')
a3.plot(x, np.log(x))
a3.set_title('log')
plt.tight_layout()

plt.show()