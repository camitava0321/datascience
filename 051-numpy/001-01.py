# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 15:18:19 2017

@author: Amitava
Ndarray Object
"""

import numpy as np
#Most important object - ndarray - an N-dimensional array type
#describes the collection of items of same type - the items can be accessed using a zero-based index.

#Each element in ndarray is an object of data-type object (dtype and
#takes the same size of block in the memory. 
#Any item extracted from ndarray object (by slicing) is a Python object of array scalar type

#An instance of ndarray class is constructed by various array creation routines
#The basic ndarray is created using an array function
#numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
#creates an ndarray from any object exposing array interface, 
#or from any method that returns an array.
#Parameters
#Sr.No. 	Parameter & Description
#1 	object Any object exposing the array interface method returns an array, or any (nested) sequence.
#2 	dtype  Desired data type of array, optional
#3 	copy   Optional. By default (true), the object is copied
#4 	order  C (row major) or F (column major) or A (any) (default)
#5 	subok  By default, returned array forced to be a base class array. If true, sub-classes passed through
#6 	ndmin  Specifies minimum dimensions of resultant array

a = np.array([1,2,8,14,25,36,43,55,68,76]) 
print a

# more than one dimensions 
a = np.array([[11, 22], [33, 44]]) 
print a

# minimum dimension 
a = np.array([1, 2, 3,4,5]) 
print a
# 2 dimension 
a = np.array([1, 2, 3,4,5], ndmin = 2) 
print a
# 3 dimension 
a = np.array([1, 2, 3,4,5], ndmin = 3) 
print a
# 4 dimension 
a = np.array([1, 2, 3,4,5], ndmin = 4) 
print a

# dtype parameter 
a = np.array([1, 2, 3], dtype = complex) 
print a

#The ndarray object consists of contiguous one-dimensional segment of computer memory, 
#combined with an indexing scheme that maps each item to a location in the memory block. 
#The memory block holds the elements in a row-major order (C style) or a column-major order 

#Vector to Numpy Array
#Vectors
cvalues = [25.3, 27, 36.2, 41, 55.8, 63.2, 70]
#Vector to array
C= np.array(cvalues)
print(C)
print(C*9/5 + 32)

fvalues=[x*9/5 + 32 for x in cvalues]
print (fvalues)