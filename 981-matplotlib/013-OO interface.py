# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Matplotlib - Object-oriented Interface
"""
"""
It is easy to quickly generate plots with the matplotlib.pyplot module, 
But the use of object-oriented approach is recommended as it gives more control and customization of your plots. 
Most of the functions are also available in the matplotlib.axes.Axes class.

The main idea behind using the more formal object-oriented method is 
to create figure objects and then just call methods or attributes off of that object. 
This approach helps better in dealing with a canvas that has multiple plots on it.

In object-oriented interface, 
Pyplot is used only for a few functions such as figure creation, 
and the user explicitly creates and keeps track of the figure and axes objects. 
At this level, the user uses Pyplot to create figures, and through those figures, 
one or more axes objects can be created. These axes objects are then used for most plotting actions.
"""

from matplotlib import pyplot as plt
import numpy as np
import math

#If you are using Jupyter notebook, 
#the %matplotlib inline directive has to be issued; 
#the otherwistshow() function of pyplot module displays the plot.

#The Data Points for the plot
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)

#We first create a figure instance which provides an empty canvas.
fig = plt.figure()

#We Nnw add axes to figure. 
#The add_axes() method requires a list object of 4 elements corresponding to 
#left, bottom, width and height of the figure. Each number must be between 0 and 1 −
ax=fig.add_axes([0,0,1,1])

#We set the labels for x and y axis as well as title −
ax.set_title("sine wave")
ax.set_xlabel('angle')
ax.set_ylabel('sine')

#now we invoke the plot() method of the axes object.
ax.plot(x,y)