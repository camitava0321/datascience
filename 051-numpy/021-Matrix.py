# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
import numpy as np  
"""
import numpy.matlib 
import numpy as np 
#NumPy package contains a Matrix library numpy.matlib. This module has functions that return matrices instead of ndarray objects.
#matlib.empty()
#The matlib.empty() function returns a new matrix without initializing the entries. The function takes the following parameters.
#numpy.matlib.empty(shape, dtype, order)
#Sr.No. 	Parameter & Description
#1 	
shape
int or tuple of int defining the shape of the new matrix
#2 	
Dtype
Optional. Data type of the output
#3 	
order
C or F

print np.matlib.empty((2,2)) 
# filled with random data

#numpy.matlib.zeros()
#This function returns the matrix filled with zeros.
print np.matlib.zeros((2,2)) 

#numpy.matlib.ones()
#This function returns the matrix filled with 1s.
print np.matlib.ones((2,2))

#numpy.matlib.eye()
#This function returns a matrix with 1 along the diagonal elements and the zeros elsewhere. The function takes the following parameters.
#numpy.matlib.eye(n, M,k, dtype)
#Sr.No. 	Parameter & Description
#1 	
n
The number of rows in the resulting matrix
#2 	
M
The number of columns, defaults to n
#3 	
k
Index of diagonal
#4 	
dtype
Data type of the output

print np.matlib.eye(n = 3, M = 4, k = 0, dtype = float)

#numpy.matlib.identity()
#The numpy.matlib.identity() function returns the Identity matrix of the given size. An identity matrix is a square matrix with all diagonal elements as 1.
print np.matlib.identity(5, dtype = float)

#numpy.matlib.rand()
#The numpy.matlib.rand() function returns a matrix of the given size filled with random values.
print np.matlib.rand(3,3)
#Note that a matrix is always two-dimensional, whereas ndarray is an n-dimensional array. Both the objects are inter-convertible.

i = np.matrix('1,2;3,4') 
print i 

j = np.asarray(i) 
print j 

k = np.asmatrix (j) 
print k