# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Matplotlib - Box Plot
"""
"""
A box plot which is also known as a box and whisker plot displays a summary of a set of data containing 
the minimum, first quartile, median, third quartile, and maximum. 
In a box plot, we draw a box from the first quartile to the third quartile. 
A vertical line goes through the box at the median. The whiskers go from each quartile to the minimum or maximum.
"""
#Let us create the data for the boxplots. 
#We use the numpy.random.normal() function to create the fake data. 
#It takes three arguments, mean and standard deviation of the normal distribution, and the number of values desired.

import numpy as np
np.random.seed(10)
collectn_1 = np.random.normal(100, 10, 200)
collectn_2 = np.random.normal(80, 30, 200)
collectn_3 = np.random.normal(90, 20, 200)
collectn_4 = np.random.normal(70, 25, 200)

#The list of arrays that we created above is the only required input for creating the boxplot. 
#Using the data_to_plot line of code, we can create the boxplot with the following code −

import matplotlib.pyplot as plt
fig = plt.figure()
# Create an axes instance
ax = fig.add_axes([0,0,1,1])
# Create the boxplot
data_to_plot = [collectn_1, collectn_2, collectn_3, collectn_4]
bp = ax.boxplot(data_to_plot)
plt.show()