# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 15:18:19 2017

@author: Amitava
Array From Existing Data
"""
import numpy as np 
#numpy.asarray(a, dtype = None, order = None)
#This function is similar to numpy.array except for the fact that it has fewer parameters. 
#This routine is useful for converting Python sequence into ndarray.
#Sr.No. 	Parameter & Description
#1 	
a
Input data in any form such as list, list of tuples, tuples, tuple of tuples or tuple of lists
#2 	
dtype
By default, the data type of input data is applied to the resultant ndarray
#3 	
order
C (row major) or F (column major). C is default

# convert list to ndarray 
x = [1,2,3] 
a = np.asarray(x) 
print a

# dtype is set 
a = np.asarray(x, dtype = float) 
print a
# ndarray from tuple 
x = (1,2,3) 
a = np.asarray(x) 
print a
# ndarray from list of tuples 
x = [(1,2,3),(4,5)] 
a = np.asarray(x) 
print a

#numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
#This function interprets a buffer as one-dimensional array. 
#Any object that exposes the buffer interface is used as parameter to return an ndarray.
#Sr.No. 	Parameter & Description
#1 	
buffer
Any object that exposes buffer interface
#2 	
dtype
Data type of returned ndarray. Defaults to float
#3 	
count
The number of items to read, default -1 means all data
#4 	
offset
The starting position to read from. Default is 0
Example

s = 'Hello World' 
a = np.frombuffer(s, dtype = 'S1') 
print a

#numpy.fromiter(iterable, dtype, count = -1)
#This function builds an ndarray object from any iterable object. 
#A new one-dimensional array is returned by this function.
#Sr.No. 	Parameter & Description
#1 	
iterable
Any iterable object
#2 	
dtype
Data type of resultant array
#3 	
count
The number of items to be read from iterator. Default is -1 which means all data to be read

#The following examples show how to use the built-in range() function to return a list object. 
#An iterator of this list is used to form an ndarray object.
# create list object using range function 
list = range(5) 
print list
# obtain iterator object from list 
it = iter(list)  
# use iterator to create ndarray 
x = np.fromiter(it, dtype = float) 
print x