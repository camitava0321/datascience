# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Matplotlib - Multiplots
"""
"""
We see how to create multiple subplots on same canvas.
The subplot() function returns the axes object at a given grid position.
Creating a subplot will delete any pre-existing subplot that overlaps with it beyond sharing a boundary.
"""
import matplotlib.pyplot as plt

#Signature - plt.subplot(subplot(nrows, ncols, index)
#In the current figure, the function creates and returns an Axes object, 
#at position index of a grid of nrows by ncolsaxes. 
#Indexes go from 1 to nrows * ncols, incrementing in row-major order.
#If nrows, ncols and index are all less than 10. 
#The indexes can also be given as single, concatenated, threedigitnumber.
#For example, subplot(2, 3, 3) and subplot(233) both create an Axes at the top right corner of the current figure, 
#occupying half of the figure height and a third of the figure width.


# plot a line, implicitly creating a subplot(111)
plt.plot([1,2,3])
# now create a subplot which represents the top plot of a grid with 2 rows and 1 column.
#Since this subplot will overlap the first, the plot (and its axes) previously created, will be removed
plt.subplot(211)
plt.plot(range(12))
plt.subplot(212, facecolor='y') # creates 2nd subplot with yellow background
plt.plot(range(12))

#%% - Multiplots
#The add_subplot() function of the figure class will not overwrite the existing plot −

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot([1,2,3])
ax2 = fig.add_subplot(221, facecolor='y')
ax2.plot([1,2,3])

#%% - Add Spot Function
#We may add an insert plot in the same figure by adding another axes object in the same figure canvas.
import numpy as np
import math
x = np.arange(0, math.pi*2, 0.05)
fig=plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
axes2 = fig.add_axes([0.55, 0.55, 0.3, 0.3]) # inset axes
y = np.sin(x)

axes1.plot(x, y, 'b')
axes2.plot(x,np.cos(x),'r')
axes1.set_title('sine')
axes2.set_title("cosine")
plt.show()