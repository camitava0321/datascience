# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 15:18:19 2017

@author: Amitava
Array Attributes
"""
import numpy as np 
#Shape of an Array
#ndarray.shape - returns a tuple consisting of array dimensions. It can also be used to resize the array.
a = np.array([[1,2,3],[4,5,6]]) 
print a.shape
#The shape is a tuple of integers. 
#These numbers denote the lengths of the corresponding array dimension. 

#The "shape" of an array is a tuple with the number of elements per axis (dimension). 
x = np.array([ [67, 63, 87],
               [77, 69, 59],
               [85, 87, 99],
               [79, 72, 71],
               [63, 89, 93],
               [68, 92, 78]])

print(x.shape)
#There is also an equivalent function
print(np.shape(x))
#Numbering of axis
#The shape of an array tells us also something about the order in which the 
#indices are processed, i.e. first rows, then columns and after that the further dimensions.

#"shape" can also be used to change the shape of an array.
# this resizes the ndarray 
a.shape = (3,2) 
print a 
x.shape = (3, 6)
print(x)
#or
x.shape = (2, 9)
print(x)
#The new shape must correspond to the number of elements of the array, 
#i.e. the total size of the new array must be the same as the old one. 
#We will raise an exception, if this is not the case:
x.shape = (4, 4)
#The above code will result in an error

#further examples.
#The shape of a scalar is an empty tuple:
x = np.array(11)
print(np.shape(x))
#shape of a 3-dim array
B = np.array([ [[111, 112], [121, 122]],
               [[211, 212], [221, 222]],
               [[311, 312], [321, 322]] ])
print(B.shape)


#NumPy also provides a reshape function to resize an array.
a = np.array([[1,2,3],[4,5,6]]) 
b = a.reshape(3,2) 
print b

#ndarray.ndim - returns the number of array dimensions.
# an array of evenly spaced numbers 
a = np.arange(24) 
print a
# this is one dimensional array 
a.ndim  
# now reshape it - 2 4x3 matrices 
b = a.reshape(2,4,3) 
print b 
# b is having three dimensions

#numpy.itemsize - returns the length of each element of array in bytes.
#dtype of array is int8 (1 byte) 
x = np.array([1,2,3,4,5], dtype = np.int8) 
print x.itemsize

x = np.array([1,2,3,4,5], dtype = np.int32) 
print x.itemsize

# dtype of array is now float32 (4 bytes) 
x = np.array([1,2,3,4,5], dtype = np.float32) 
print x.itemsize

#numpy.flags - The ndarray object has the following attributes. Its current values are returned by this function.
#Sr.No. 	Attribute & Description
#1 	   C_CONTIGUOUS (C)     The data is in a single, C-style contiguous segment
#2 	   F_CONTIGUOUS (F)     The data is in a single, Fortran-style contiguous segment
#3 	   OWNDATA (O)          The array owns the memory it uses or borrows it from another object
#4 	   WRITEABLE (W)        The data area can be written to. Setting this to False locks the data, making it read-only
#5 	   ALIGNED (A)          The data and all elements are aligned appropriately for the hardware
#6 	   UPDATEIFCOPY (U)     This array is a copy of some other array. When this array is deallocated, the base array will be updated with the contents of this array

#The following example shows the current values of flags.
x = np.array([1,2,3,4,5]) 
print x.flags




#ndim - gives the number of array dimensions
b = np.array([[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],[12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]])
b.ndim

#size - displays the number of elements
b.size

#nbytes - gives the total number of bytes an array requires
#a product of the itemsize and size attributes
b.nbytes
b.size * b.itemsize

#T - the transpose() function
b.resize(6,4)
b
b.T

#Complex numbers in NumPy are represented by 'j'
b = np.array([1.j + 1, 2.j + 3])
b
#real - the real part of an array, or 
#the array itself if it only contains real numbers
b.real
#imag - imaginary part of an array
b.imag


#flat - returns a numpy.flatiter object
#This is the only way to acquire a flatiter—we do not have access to a flatiter constructor.
#The flat iterator enables us to loop through an array as if it is a flat array
b = np.arange(4).reshape(2,2)
b
f = b.flat
f
for item in f: print item

#It is possible to directly get an element with the flatiter object
b.flat[2]

#It is also possible to get multiple elements
b.flat[[1,3]]

#The flat attribute is settable. 
#Setting the value of the flat attribute leads to overwriting the values of the whole array
b.flat = 7
b

#You can even get selected elements as follows:
b.flat[[1,3]] = 1
b