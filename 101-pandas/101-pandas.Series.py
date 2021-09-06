# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
Series
"""
#%% - imports
import pandas as pd
import numpy as np

#%% - Basics
"""
pandas.Series
Series - 1D array labeled array 
  capable of holding data of any type 
  (integer, string, float, python objects, etc.). 
  The axis labels are collectively called index.
    Homogeneous data
    Size Immutable
    Values of Data Mutable
"""
#Empty Series - A basic series
s = pd.Series()
print s
#default dtype is float64

"""
Object Creation
Create a Series by passing a list of values, 
letting pandas create a default integer index:
"""
series = pd.Series([1,3,6,10,np.nan,15,21])
print series

#%% - Create a Series from ndarray
"""
A series can be created using various inputs like −
    Array
    Dict
    Scalar value or constant
"""
#If data is an ndarray, then index passed must be of the same length. 
#If no index is passed, then by default index will be range(n) 
#where n is array length, i.e., [0,1,2,3…. range(len(array))-1].
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print s
#We did not pass any index, 
#so by default, it assigned the indexes ranging from 0 to len(data)-1, 
#i.e., 0 to 3.

#%% - pass index
#Now we pass the index values
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print s
#we can see the customized indexed values in the output.

#%% - Create a Series from dict (a dict can be passed as input)
#if no index is specified, then the dictionary keys are taken 
#in a sorted order to construct index. 
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print s
#Observe − Dictionary keys are used to construct index.

#If index is passed, 
#the values in data corresponding to the labels in the index 
#will be pulled out.
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print s
#Observe − Index order is persisted and 
#the missing element is filled with NaN (Not a Number).

#%% - Create a Series from Scalar
#If data is a scalar value, an index must be provided. 
#The value will be repeated to match the length of index
s = pd.Series(5, index=[0, 1, 2, 3])
print s

#%% - Accessing Data from Series with Position
#Data in the series can be accessed similar to that in an numpy ndarray.
s = pd.Series([1,2,3,4,5,6,7,8],index = ['a','b','c','d','e','x','y','z'])
#counting starts from 0 for the array

#retrieve the first element
print s[0]

#retrieve the first three element
#a : inserted in front - all items till that index-1 will be extracted
print s[:3]
print s[3:]
#two parameters (with : between them) - items between the two indexes
#(not including the stop index)
print s[1:5]
#retrieve the last three element
print s[-3:]

#%% - Retrieve Data Using Label (Index)
#A Series is like a fixed-size dict 
#in that you can get and set values by index label.

#Retrieve a single element using index label value.
print s['a']

#Retrieve multiple elements using a list of index label values.
print s[['a','c','d']]

#If a label is not contained, an exception is raised.
print s['f']

#%% - Series Basic Functionality
"""
We will focus on the DataFrame objects 
because of its importance in the real time data processing and 
also discuss a few other DataStructures.

S.No. 	Attribute or Method 	Description
1 	axes 	Returns a list of the row axis labels.
2 	dtype 	Returns the dtype of the object.
3 	empty 	Returns True if series is empty.
4 	ndim 	Returns the number of dimensions of the underlying data, by definition 1.
5 	size 	Returns the number of elements in the underlying data.
6 	values 	Returns the Series as ndarray.
7 	head() 	Returns the first n rows.
8 	tail() 	Returns the last n rows.

"""
#%% - Create a Series and see all the above tabulated attributes operation. 
#Create a series with 100 random numbers
s = pd.Series(np.random.randn(4))
print s

#axes - Returns the list of the labels of the series.
print ("The axes are:")
print s.axes

#The above result is a compact format of a list of values from 0 to 5, 
#i.e., [0,1,2,3,4].

#empty - Returns the Boolean value saying 
#whether the Object is empty or not. 
#True indicates that the object is empty.
print ("Is the Object empty?")
print s.empty

#ndim - Returns the number of dimensions of the object. By definition, a Series is a 1D data structure, so it returns
print ("The dimensions of the object:")
print s.ndim

#size - Returns the size(length) of the series.
print ("The size of the object:")
print s.size

#values - Returns the actual data in the series as an array.
print ("The actual data series is:")
print s.values

#Head & Tail - 
#To view a small sample of a Series or the DataFrame object, 
#use the head() and the tail() methods.

#head() returns the first n rows(observe the index values). 
#The default number of elements to display is five, 
#but you may pass a custom number.
print ("The first two rows of the data series:")
print s.head(2)

#tail() returns the last n rows(observe the index values). 
#The default number of elements to display is five, 
#but you may pass a custom number.
print ("The last two rows of the data series:")
print s.tail(2)
#%% - Create a series from a csv
df = pd.read_csv('gdp.csv', index_col=False, header=0);
print df.columns
index = df['date']
s = pd.Series(df['gross_domestic_product'].values, index=df['date']) # here we convert the DataFrame into a Serie
print s

#%% - plot a Series
s.plot.bar(color='blue')

s.plot.hist()
import matplotlib.pyplot as plt
mask1 = s < 16500
mask2 = s > 16500
print s[mask1]

plt.bar(s[mask1].index, s[mask1].values, color='grey')
plt.bar(s[mask2].index, s[mask2].values, color='red')
plt.xticks(range(len(s)), s.index, rotation=80)
plt.show()