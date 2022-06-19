# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Matplotlib - Violin Plot
"""
"""
Violin plots are similar to box plots, 
except that they also show the probability density of the data at different values. 
These plots include a marker for the median of the data and 
a box indicating the interquartile range, as in the standard box plots. 
Overlaid on this box plot is a kernel density estimation. 
Like box plots, violin plots are used to represent comparison of a variable distribution (or sample distribution) 
across different "categories".

A violin plot is more informative than a plain box plot. 
In fact while a box plot only shows summary statistics such as mean/median and interquartile ranges, 
the violin plot shows the full distribution of the data.
"""
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
collectn_1 = np.random.normal(100, 10, 200)
collectn_2 = np.random.normal(80, 30, 200)
collectn_3 = np.random.normal(90, 20, 200)
collectn_4 = np.random.normal(70, 25, 200)

## combine these different collections into a list
data_to_plot = [collectn_1, collectn_2, collectn_3, collectn_4]

# Create a figure instance
fig = plt.figure()

# Create an axes instance
ax = fig.add_axes([0,0,1,1])

# Create the boxplot
bp = ax.violinplot(data_to_plot)
plt.show()