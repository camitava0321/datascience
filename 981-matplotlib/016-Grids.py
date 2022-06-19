# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Matplotlib - Grids
"""
"""
The grid() function of axes object sets visibility of grid inside the figure to on or off. 
You can also display major / minor (or both) ticks of the grid. 
Additionally color, linestyle and linewidth properties can be set in the grid() function.
"""
import matplotlib.pyplot as plt

import numpy as np

fig, axes = plt.subplots(1,3, figsize = (12,4))
x = np.arange(1,11)

axes[0].plot(x, x**3, 'g',lw=2)
axes[0].grid(True)
axes[0].set_title('default grid')
axes[1].plot(x, np.exp(x), 'r')
axes[1].grid(color='b', ls = '-.', lw = 0.25)
axes[1].set_title('custom grid')
axes[2].plot(x,x)
axes[2].set_title('no grid')
fig.tight_layout()

plt.show()