# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
DataFrame
"""
#%% - imports
import pandas as pd
import numpy as np

#%% - Basics
"""
pandas.DataFrame - 2D data structure
data is aligned in a tabular fashion in rows and columns.

Features
    Potentially columns are of different types
    Size – Mutable
    Labeled axes (rows and columns)
    Can Perform Arithmetic operations on rows and columns

Structure
Like an SQL table or a spreadsheet data representation.

Constructor
pandas.DataFrame( data, index, columns, dtype, copy)

Parameters
data - takes various forms like 
       ndarray, series, map, lists, dict, constants and 
       also another DataFrame.
index - For the row labels - Index is Optional 
        Default np.arrange(n) if no index is passed.
columns - column labels
          the optional default - np.arrange(n). 
          This is only true if no index is passed.
dtype - Data type of each column.
copy - used for copying of data, if the default is False.
"""
#%% - Create DataFrame - Empty DataFrame
#A basic DataFrame, which can be created is an Empty Dataframe.
df = pd.DataFrame()
print df

#%% - Create a DataFrame from Lists
#created using a single list
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print df

#created using a list of lists.
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print df

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print df
#Observe, the dtype parameter changes the type of Age column to floating point.

#%% - Create a DataFrame from Dict of ndarrays / Lists

#Create a DataFrame - by passing a dict of objects that can be converted to series-like.
dataFrame2 = pd.DataFrame({'A': 1.,
                               'B': pd.Timestamp('20170101'),
                               'C': pd.Series(1,index=list(range(4)),dtype='float32'),
                               'D': np.array([3]*4, dtype='int32'),
                               'E': pd.Categorical(['test','train','test','train']),
                               'F': 'foo'})
print dataFrame2    

#All the ndarrays must be of same length. 
#If index is passed - length of the index should equal to the length of the arrays

#If no index is passed, then by default, 
#index will be range(n), where n is the array length.
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print df
#Observe the values 0,1,2,3. 
#They are the default index assigned to each using the function range(n).

#create an indexed DataFrame using arrays.
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print df
#Observe, the index parameter assigns an index to each row.



#%% - Create a DataFrame from List of Dicts
#List of Dictionaries can be passed as input data to create a DataFrame. 
#The dictionary keys are by default taken as column names.

#create a DataFrame by passing a list of dictionaries.
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print df
#Observe, NaN (Not a Number) is appended in missing areas.

#create a DataFrame by passing a list of dictionaries and the row indices.
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
print df

#create a DataFrame with a list of dictionaries, 
#row indices, and column indices.
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

#With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])

#With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print df1
print df2
#Observe, df2 DataFrame is created with a column index other than the dictionary key
#thus, appended the NaN’s in place. 
#Whereas, df1 is created with column indices same as dictionary keys, 
#so NaN’s appended.

#%% - Create a DataFrame from Dict of Series
#Dictionary of Series can be passed to form a DataFrame. 
#The resultant index is the union of all the series indexes passed.
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print df
#Observe, for the series one, there is no label ‘d’ passed, 
#but in the result, for the d label, NaN is appended with NaN.

#%% - Create a DataFrame by passing a numpy array, with a datetime index and labeled columns
dates = pd.date_range('20170101',periods=6)
print dates

dataFrame = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print dataFrame

#%% - Data Access
#See the top & bottom rows of the frame
print dataFrame.head()
print dataFrame.tail()

#Display the index, columns, and the underlying numpy data
print dataFrame.index
print dataFrame.columns
print dataFrame.values

#Describe shows a quick statistic summary of your data
print dataFrame.describe()

#Transposing the data
print dataFrame.T

#Sorting by an axis
print dataFrame.sort_index(axis=1, ascending=False)

#%% - Column Selection
#select a column from the DataFrame.
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print df ['one']

#%% - Column Addition
#add a new column to an existing data frame - with index
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)

# Adding a new column to an existing DataFrame object 
#with column label by passing new series
print ("Adding a new column by passing as Series:")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print df

print ("Adding a new column using the existing columns in DataFrame:")
df['four']=df['one']+df['three']
print df

#add a new column to an existing data frame - with no index
d = {'one' : pd.Series([1, 2, 3]), 
      'two' : pd.Series([1, 2, 3, 4])}

df = pd.DataFrame(d)

# Adding a new column to an existing DataFrame object 
#with column label by passing new series
print ("Adding a new column by passing as Series:")
df['three']=pd.Series([10,20,30])
print df

print ("Adding a new column using the existing columns in DataFrame:")
df['four']=df['one']+df['three']
print df

#%% - Column Deletion
#Columns can be deleted or popped
# Using the previous DataFrame, we will delete a column
# using del function
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 
     'three' : pd.Series([10,20,30], index=['a','b','c'])}

df = pd.DataFrame(d)
print ("Our dataframe is:")
print df

# using del function
print ("Deleting the first column using DEL function:")
del df['one']
print df

# using pop function
print ("Deleting another column using POP function:")
df.pop('two')
print df

#%% - Row Selection
#Selection by Label
#Rows can be selected by passing row label to a loc function.
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print df.loc['b']
#The result is a series with labels as column names of the DataFrame. 
#And, the Name of the series is the label with which it is retrieved.

#Selection by integer location
#Rows can be selected by passing integer location to an iloc function.
df = pd.DataFrame(d)
print df.iloc[2]

#Slice Rows
#Multiple rows can be selected using ‘ : ’ operator.
df = pd.DataFrame(d)
print df[2:4]

#%% - Row Addition
#Add new rows to a DataFrame using the append function. 
#This function will append the rows at the end.
df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)
print df

#%% - Row Deletion
#Use index label to delete or drop rows from a DataFrame. 
#If label is duplicated, then multiple rows will be dropped.

#in the example, the labels are duplicate. 
#Let us drop a label and will see how many rows will get dropped.
df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)

# Drop rows with label 0
df = df.drop(0)

print df