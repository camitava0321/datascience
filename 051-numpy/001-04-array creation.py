# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 15:18:19 2017

@author: Amitava
Array Creation Routines
"""
import numpy as np 
#A new ndarray object can be constructed by any of the following array creation routines or 
#using a low-level ndarray constructor.

#numpy.empty - creates an uninitialized array of specified shape and dtype. 
#numpy.empty(shape, dtype = float, order = 'C')
#Sr.No. 	Parameter & Description
#1 	
Shape
Shape of an empty array in int or tuple of int
#2 	
Dtype
Desired output data type. Optional
#3 	
Order
'C' for C-style row-major array, 'F' for FORTRAN style column-major array

x = np.empty([3,2], dtype = int) 
print x
#The elements in an array show random values as they are not initialized.

#Arrays of Ones and of Zeros
#Two ways to initialize Arrays with Zeros or Ones. 

#numpy.zeros(shape, dtype = float, order = 'C')
#Returns a new array of specified size, filled with zeros.
#Sr.No. 	Parameter & Description
#1 	
Shape
Shape of an empty array in int or sequence of int
#2 	
Dtype
Desired output data type. Optional
#3 	
Order
'C' for C-style row-major array, 'F' for FORTRAN style column-major array

# array of five zeros. Default dtype is float 
x = np.zeros(5) 
print x
x = np.zeros((5,), dtype = np.int) 
print x
x = np.zeros((2,4))
print(x)
# custom type 
x = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])  
print x

#numpy.ones(shape, dtype = None, order = 'C')
#Returns a new array of specified size and type, filled with ones.
#The method ones(t) takes a tuple t with the shape of the array and fills the array accordingly with ones. 
#By default it will be filled with Ones of type float. 
#For integer Ones, one has to set the optional parameter dtype to int:
#Sr.No. 	Parameter & Description
#1 	
Shape
Shape of an empty array in int or tuple of int
#2 	
Dtype
Desired output data type. Optional
#3 	
Order
'C' for C-style row-major array, 'F' for FORTRAN style column-major array

# array of five ones. Default dtype is float 
x = np.ones(5) 
print x
x = np.ones((2,3))
print(x)
x = np.ones((3,4),dtype=int)
print(x)
x = np.ones([2,2], dtype = complex) 
print x

#Another interesting way to create an array with Ones or with Zeros
#Numpy supplies for this purpose the methods ones_like(a) and zeros_like(a).
x = np.array([2,5,18,14,4])
E = np.ones_like(x)
print(E)
E1 = E+x
print E1
Z = np.zeros_like(E1)
print(Z)