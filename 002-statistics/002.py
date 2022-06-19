# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
Python - Measuring Variance
"""
"""
In statistics, variance is a measure of how far a value in a data set lies from the mean value. 
In other words, it indicates how dispersed the values are. 
It is measured by using standard deviation. The other method commonly used is skewness.

Both of these are calculated by using functions available in pandas library.
"""
#Measuring Standard Deviation
#Standard deviation is square root of variance. 
#variance is the average of squared difference of values in a data set from the mean value. 
#In python we calculate this value by using the function std() from pandas library.

import pandas as pd

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','Chanchal','Gasper','Naviya','Andres']),
   'Age':pd.Series([25,26,25,23,30,25,23,34,40,30,25,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)

# Calculate the standard deviation
print (df.std())

#%% - Measuring Skewness
#It used to determine whether the data is symmetric or skewed. 
#If the index is between -1 and 1, then the distribution is symmetric. 
#If the index is no more than -1 then it is skewed to the left and if it is at least 1, then it is skewed to the right

import pandas as pd

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','Chanchal','Gasper','Naviya','Andres']),
   'Age':pd.Series([25,26,25,23,30,25,23,34,40,30,25,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print (df.skew())
#So the distribution of age rating is symmetric while the distribution of age is skewed to the right.