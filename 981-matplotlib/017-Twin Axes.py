# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Matplotlib - Twin Axes
"""
"""
It is considered useful to have dual x or y axes in a figure, 
more so, when plotting curves with different units together. 
Matplotlib supports this with the twinx and twiny functions.
"""
#In the following example, the plot has dual y axes, one showing exp(x) and the other showing log(x) −
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
a1 = fig.add_axes([0,0,1,1])

x = np.arange(1,11)

a1.plot(x,np.exp(x))
a1.set_ylabel('exp')
a2 = a1.twinx()
a2.plot(x, np.log(x),'ro-')
a2.set_ylabel('log')
fig.legend(labels = ('exp','log'),loc='upper left')
plt.show()