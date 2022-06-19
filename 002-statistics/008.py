# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
Python - Correlation
"""
"""
Correlation refers to some statistical relationships involving dependence between two data sets. 
Simple examples of dependent phenomena include the correlation between the physical appearance of parents 
and their offspring, and the correlation between the price for a product and its supplied quantity.

We take example of the iris data set available in seaborn python library. 
In it we try to establish the correlation between the length and the width of the sepals and 
petals of three species of iris flower. 
Based on the correlation found, a strong model could be created which easily distinguishes one species from another.
"""
import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset('iris')
 
#without regression
sns.pairplot(df, kind="scatter")
plt.show()