# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
Descriptive Statistics
"""
#%% - imports
import pandas as pd
import numpy as np

#%% - descriptive statistics and other related operations on DataFrame
"""
Most of these are aggregations like sum(), mean(), 
but some of them, like sumsum(), produce an object of the same size. 
Generally speaking, these methods take an axis argument, 
just like ndarray.{sum, std, ...}, 
but the axis can be specified by name or integer

    DataFrame − “index” (axis=0, default), “columns” (axis=1)
Let us create a DataFrame and 
use this object throughout this chapter for all the operations.
"""
#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print df

#%% - Functions & Description
"""
Functions under Descriptive Statistics in Python Pandas. 
The following table list down the important functions −
S.No. 	Function 	Description
1 	count() 	Number of non-null observations
2 	sum() 	Sum of values
3 	mean() 	Mean of Values
4 	median() 	Median of Values
5 	mode() 	Mode of values
6 	std() 	Standard Deviation of the Values
7 	min() 	Minimum Value
8 	max() 	Maximum Value
9 	abs() 	Absolute Value
10 	prod() 	Product of Values
11 	cumsum() 	Cumulative Sum
12 	cumprod() 	Cumulative Product

DataFrame is a Heterogeneous data structure. 
Hence generic operations don’t work with all functions.
    Functions like sum(), cumsum() work with both numeric and character (or) 
    string data elements without any error. 
    Though in practice, character aggregations are never used generally, 
    these functions do not throw any exception.

    Functions like abs(), cumprod() throw exception 
    when the DataFrame contains character or string data 
    because such operations cannot be performed.
"""
#Summarizing Data
#The describe() function computes a summary of statistics 
#pertaining to the DataFrame columns.
print df.describe()

#This function gives the mean, std and IQR values. 
#And, function excludes the character columns and 
#given summary about numeric columns. 
#'include' is the argument which is used to pass necessary information 
#regarding what columns need to be considered for summarizing. 
#Takes the list of values; by default, 'number'.
#    object − Summarizes String columns
#    number − Summarizes Numeric columns
#    all − Summarizes all columns together (Should not pass it as a list value)

print df.describe(include=['object'])
print df. describe(include='all')
#%% - Specific Functions - sum()
#Returns the sum of the values for the requested axis. 
#By default, axis is index (axis=0).
print df.sum()
#Each individual column is added individually (Strings are appended).

#For axis=1
print df.sum(1)

#%% - Specific Functions - mean()
#Returns the average value
print df.mean()


#%% - Specific Functions - std()
#Returns the Bressel standard deviation of the numerical columns.
print df.std()