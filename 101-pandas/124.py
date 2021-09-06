# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
IO Tools
"""
#two functions for reading text files (or the flat files) are 
#read_csv() and read_table()
#They both use the same parsing code to intelligently convert tabular data into a DataFrame object −
#pandas.read_csv(filepath_or_buffer, sep=',', delimiter=None, header='infer',names=None, index_col=None, usecols=None
#pandas.read_csv(filepath_or_buffer, sep='\t', delimiter=None, header='infer',names=None, index_col=None, usecols=None

#read.csv
#read.csv reads data from the csv files and creates a DataFrame object.
import pandas as pd
df=pd.read_csv("temp.csv")
print (df)

#custom index
#This specifies a column in the csv file to customize the index using index_col.
df=pd.read_csv("temp.csv",index_col=['S.No'])
print df

#Converters
#dtype of the columns can be passed as a dict.
df = pd.read_csv("temp.csv", dtype={'Salary': np.float64})
print df.dtypes
#By default, the dtype of the Salary column is int, but the result shows it as float because we have explicitly casted the type.

#header_names
#Specify the names of the header using the names argument.
df=pd.read_csv("temp.csv", names=['a', 'b', 'c','d','e'])
print df

#Observe, the header names are appended with the custom names, but the header in the file has not been eliminated. 
#Now, we use the header argument to remove that.
#If the header is in a row other than the first, pass the row number to header. This will skip the preceding rows.
df=pd.read_csv("temp.csv",names=['a','b','c','d','e'],header=0)
print df

#skiprows
#skiprows skips the number of rows specified.
df=pd.read_csv("temp.csv", skiprows=2)
print df