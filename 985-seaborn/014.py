# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Pair Grid
"""
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
#PairGrid allows us to draw a grid of subplots using the same plot type to visualize data.
#Unlike FacetGrid, it uses different pair of variable for each subplot. It forms a matrix of sub-plots. 
#It is also sometimes called as “scatterplot matrix”.

#The usage of pairgrid is similar to facetgrid. First initialise the grid and then pass the plotting function.
df = sb.load_dataset('iris')
sb.set(style="ticks")
g = sb.PairGrid(df); g.map(plt.scatter)
plt.show()

#Variousmodels
#It is also possible to plot a different function on the diagonal to show the univariate distribution of the variable in each column.
g = sb.PairGrid(df); g.map_diag(plt.hist)
g = sb.PairGrid(df); g.map_offdiag(plt.scatter);

#Histogram Dots
#We can customize the color of these plots using another categorical variable. 
#For example, the iris dataset has four measurements for each of three different species of iris flowers so you can see how they differ.
g.map_diag(plt.hist)
g = sb.PairGrid(df); g.map_offdiag(plt.scatter, cmap="Blues_d");

#We can use a different function in the upper and lower triangles to see different aspects of the relationship.
g = sb.PairGrid(df); g.map_upper(plt.scatter)
g = sb.PairGrid(df); g.map_lower(sb.kdeplot, cmap = "Blues_d")
g = sb.PairGrid(df); g.map_diag(sb.kdeplot, lw = 3, legend = False);
plt.show()