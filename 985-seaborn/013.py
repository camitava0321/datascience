# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Facet Grid - Plotting Small Multiples of Data Subsets
"""
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

#A useful approach to explore medium-dimensional data, 
#is by drawing multiple instances of the same plot on different subsets of your dataset.

#This technique is commonly called as “lattice”, or “trellis” plotting, 
#and it is related to the idea of “small multiples”.

#To use these features, data has to be in a Pandas DataFrame.

#In the previous chapter, we have seen the FacetGrid example 
#where FacetGrid class helps in visualizing distribution of one variable 
#as well as the relationship between multiple variables separately within subsets of your dataset using multiple panels.

#A FacetGrid can be drawn with up to three dimensions − row, col, and hue. 
#The first two have obvious correspondence with the resulting array of axes; 
#think of the hue variable as a third dimension along a depth axis, where different levels are plotted with different colors.

#FacetGrid object takes a dataframe as input and 
#the names of the variables that will form the row, column, or hue dimensions of the grid.
#The variables should be categorical and 
#the data at each level of the variable will be used for a facet along that axis.

df = sb.load_dataset('tips')
sb.set(style="ticks")

#initialize the facetgrid object (doesn’t draw anything on them)
g = sb.FacetGrid(df, col = "time"); g.map(plt.hist, "tip")
#The main approach for visualizing data on this grid is with the FacetGrid.map() method. 
#Let us look at the distribution of tips in each of these subsets, using a histogram.

#The number of plots is more than one because of the parameter col. 
#We discussed about col parameter in our previous chapters.

#To make a relational plot, pass the multiple variable names.
g = sb.FacetGrid(df, col = "sex", hue = "smoker") ; g.map(plt.scatter, "total_bill", "tip", alpha=0.7)
plt.show()