# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
Panel
"""
#%% - imports
import pandas as pd
import numpy as np

#%% - Basics
"""
pandas.Panel() - 3D container of data. 
The term Panel data is derived from econometrics and 
is partially responsible for the name pandas − pan(el)-da(ta)-s.

The names for the 3 axes are intended to give some semantic meaning 
to describe operations involving panel data. They are −
    items − axis 0, each item corresponds to a DataFrame contained inside.
    major_axis − axis 1, it is the index (rows) of each of the DataFrames.
    minor_axis − axis 2, it is the columns of each of the DataFrames.

Constructor
pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)

Parameters
data - takes various forms like ndarray, series, map, lists, dict, 
       constants and also another DataFrame
items - axis=0
major_axis - axis=1
minor_axis - axis=2
dtype - Data type of each column
copy - Copy data. Default, false
"""
#A Panel can be created using multiple ways like −
#    From ndarrays
#    From dict of DataFrames
#%% - Create an Empty Panel
#An empty panel can be created using the Panel constructor as follows −
p = pd.Panel()
print p

#%% - Create Panel - creating an empty panel
#From 3D ndarray
data = np.random.rand(2,4,5)
p = pd.Panel(data)
print p
#Observe the dimensions of the empty panel and the above panel, 
#all the objects are different.


#%% - Create Panel - From dict of DataFrame Objects
#creating an empty panel
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print p

#%% - Selecting the Data from Panel
#Select the data from the panel using −
#    Items
#    Major_axis
#    Minor_axis

#Using Items
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print p['Item1']

#We have two items, and we retrieved item1. 
#The result is a DataFrame with 4 rows and 3 columns, 
#which are the Major_axis and Minor_axis dimensions.

#Using major_axis
#Data can be accessed using the method panel.major_axis(index).
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print p.major_xs(1)

#Using minor_axis
#Data can be accessed using the method panel.minor_axis(index).
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print p.minor_xs(1)

#Observe the changes in the dimensions.