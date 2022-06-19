# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Matplotlib - Subplots() Function
"""
"""
Matplotlib’s pyplot API has a convenience function called subplots() 
which acts as a utility wrapper and helps in creating common layouts of subplots, 
including the enclosing figure object, in a single call.
"""
import matplotlib.pyplot as plt

#Plt.subplots(nrows, ncols)
#The two integer arguments to this function specify the number of rows and columns of the subplot grid. 
#The function returns a figure object and a tuple containing axes objects equal to nrows*ncols. 
#Each axes object is accessible by its index. 
#Here we create a subplot of 2 rows by 2 columns and 
#display 4 different plots in each subplot.

fig,a =  plt.subplots(2,2)

import numpy as np
x = np.arange(1,5)

a[0][0].plot(x,x*x)
a[0][0].set_title('square')
a[0][1].plot(x,np.sqrt(x))
a[0][1].set_title('square root')
a[1][0].plot(x,np.exp(x))
a[1][0].set_title('exp')
a[1][1].plot(x,np.log10(x))
a[1][1].set_title('log')

plt.show()