# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Multi Panel Categorical Plots
"""
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
#Categorical data can we visualized using two plots, 
#you can either use the functions pointplot(), or the higher-level function factorplot().

#Factorplot
#Factorplot draws a categorical plot on a FacetGrid. 
#Using ‘kind’ parameter we can choose the plot like boxplot, violinplot, barplot and stripplot. 
#FacetGrid uses pointplot by default.

df = sb.load_dataset('exercise')
sb.factorplot(x = "time", y = "pulse", hue = "kind",data = df)
plt.show()

#We can use different plot to visualize the same data using the kind parameter.
sb.factorplot(x = "time", y = "pulse", hue = "kind", kind = 'violin',data = df);
plt.show()

#In factorplot, the data is plotted on a facet grid.
#Facet grid forms a matrix of panels defined by row and column by dividing the variables. 
#Due of panels, a single plot looks like multiple plots. 
#It is very helpful to analyze all combinations in two discrete variables.

sb.factorplot(x = "time", y = "pulse", hue = "kind", kind = 'violin', col = "diet", data = df);
plt.show()

#The advantage of using Facet is, we can input another variable into the plot. 
#The above plot is divided into two plots based on a third variable called ‘diet’ using the ‘col’ parameter.

#We can make many column facets and align them with the rows of the grid −
df = sb.load_dataset('titanic')
sb.factorplot("alive", col = "deck", col_wrap = 3,data = df[df.deck.notnull()],kind = "count")
plt.show()