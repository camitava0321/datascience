# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
Basic Functionality
"""
#%% - imports
import pandas as pd
import numpy as np

#%% - DataFrame Basic Functionality
#Important attributes or methods that help in DataFrame Basic Functionality.
"""
S.No. 	Attribute or Method 	Description
1 	T 	Transposes rows and columns.
2 	axes 	Returns a list with the row axis labels and column axis labels as the only members.
3 	dtypes 	Returns the dtypes in this object.
4 	empty 	True if NDFrame is entirely empty [no items]; if any of the axes are of length 0.
5 	ndim 	Number of axes / array dimensions.
6 	shape 	Returns a tuple representing the dimensionality of the DataFrame.
7 	size 	Number of elements in the NDFrame.
8 	values 	Numpy representation of NDFrame.
9 	head() 	Returns the last n rows.
10 	tail() 	Returns last n rows.
"""
#Create a DataFrame and see all how the above mentioned attributes operate.
#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Our data series is:")
print df

#T (Transpose) - Returns the transpose of the DataFrame. 
#The rows and columns will interchange.
print ("The transpose of the data series is:")
print df.T

#axes - Returns the list of row axis labels and column axis labels.
print ("Row axis labels and column axis labels are:")
print df.axes

#dtypes - Returns the data type of each column.
print ("The data types of each column are:")
print df.dtypes

#empty - Returns the Boolean value saying whether 
#the Object is empty or not; True indicates that the object is empty.
print ("Is the object empty?")
print df.empty

#ndim - Returns the number of dimensions of the object. By definition, DataFrame is a 2D object.
print ("The dimension of the object is:")
print df.ndim

#shape - Returns a tuple representing the dimensionality of the DataFrame. 
#Tuple (a,b), where a represents the number of rows and 
#b represents the number of columns.
print ("The shape of the object is:")
print df.shape

#size - Returns the number of elements in the DataFrame.
print ("The total number of elements in our object is:")
print df.size

#values - Returns the actual data in the DataFrame as an NDarray.
print ("The actual data in our data frame is:")
print df.values

#Head & Tail
#To view a small sample of a DataFrame object, 
#use the head() and tail() methods. 
#head() returns the first n rows (observe the index values). 
#The default number of elements to display is five, 
#but you may pass a custom number.
print ("The first two rows of the data frame is:")
print df.head(2)

#tail() returns the last n rows (observe the index values). 
#The default number of elements to display is five, 
#but you may pass a custom number.
print ("The last two rows of the data frame is:")
print df.tail(2)