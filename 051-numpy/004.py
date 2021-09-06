# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 23:10:14 2017

@author: Amitava
"""

#Multidimensional arrays in numpy: 
#Zero-dimensional Arrays in Numpy

#Scalars are zero dimensional. 
#Create the scalar 42. 
#Applying the ndim method to our scalar, we get the dimension of the array. 
#We can also see that the type is a "numpy.ndarray" type.

import numpy as np
x = np.array(42)
print("x: ", x)
print("The type of x: ", type(x))
print("The dimension of x:", np.ndim(x))

#One-dimensional Arrays
#1-dimenional array - vectors.
#numpy arrays are containers of items of the same type.
#The homogenous type of the array can be determined with the attribute "dtype"
F = np.array([1, 1, 2, 3, 5, 8, 13, 21])
V = np.array([3.4, 6.9, 99.8, 12.8])
print("F: ", F)
print("V: ", V)
print("Type of F: ", F.dtype)
print("Type of V: ", V.dtype)
print("Dimension of F: ", np.ndim(F))
print("Dimension of V: ", np.ndim(V))

#Two- and Multidimensional Arrays
#Create by passing nested lists (or tuples) to the array method of numpy.
A = np.array([ [3.4, 8.7, 9.9], 
               [1.1, -7.8, -0.7],
               [4.1, 12.3, 4.8]])
print(A)
print(A.ndim)

B = np.array([ [[111, 112], [121, 122]],
               [[211, 212], [221, 222]],
               [[311, 312], [321, 322]] ])
print(B)
print(B.ndim)