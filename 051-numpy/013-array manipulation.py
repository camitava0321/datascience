# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Array Manipulation
"""
import numpy as np
#Several routines are available in NumPy package for manipulation of elements in ndarray object. 
#They can be classified into the following types −
#Changing Shape
#Sr.No. 	Shape & Description
#1 	reshape
Gives a new shape to an array without changing its data
numpy.reshape

This function gives a new shape to an array without changing the data. It accepts the following parameters −
numpy.reshape(arr, newshape, order')
Where,
Sr.No. 	Parameter & Description
1 	
arr
Array to be reshaped
2 	
newshape
int or tuple of int. New shape should be compatible to the original shape
3 	
order
'C' for C style, 'F' for Fortran style, 'A' means Fortran like order if an array is stored in Fortran-like contiguous memory, C style otherwise

a = np.arange(8)
print 'The original array:'
print a
print '\n'
b = a.reshape(4,2)
print 'The modified array:'
print b


2 	flat

A 1-D iterator over the array
numpy.ndarray.flat
Advertisements
Previous Page
Next Page  

This function returns a 1-D iterator over the array. It behaves similar to Python's built-in iterator.
Example
Live Demo

import numpy as np 
a = np.arange(8).reshape(2,4) 
print 'The original array:' 
print a 
print '\n' 

print 'After applying the flat function:' 
# returns element corresponding to index in flattened array 
print a.flat[5]

#3 	flatten - Returns a copy of the array collapsed into one dimension
#same as ravel(), but flatten() always allocates new memory - 
#so we can directly manipulate the array
b = np.array([[[ 0, 1, 2, 3], [ 4, 5, 6, 7], [ 8, 9, 10, 11]], [[12, 13, 14, 15],
[16, 17, 18, 19],
[20, 21, 22, 23]]])
b.flatten()
b

#4 	ravel - Returns a contiguous flattened array
#accomplish flattening 
b = np.array([[[ 0, 1, 2, 3], [ 4, 5, 6, 7], [ 8, 9, 10, 11]], [[12, 13, 14, 15],
[16, 17, 18, 19],
[20, 21, 22, 23]]])
b.ravel()
#ravel() returns a view of an array - original array remains as is 
b




#Transpose Operations
#Sr.No. 	Operation & Description
#1 	transpose - Permutes the dimensions of an array
b = np.array([[[ 0, 1, 2, 3], [ 4, 5, 6, 7], [ 8, 9, 10, 11]], [[12, 13, 14, 15],
[16, 17, 18, 19],
[20, 21, 22, 23]]])
b.transpose()

2 	ndarray.T
Same as self.transpose()
3 	rollaxis

Rolls the specified axis backwards
4 	swapaxes

Interchanges the two axes of an array
Changing Dimensions
Sr.No. 	Dimension & Description
1 	broadcast

Produces an object that mimics broadcasting
2 	broadcast_to

Broadcasts an array to a new shape
3 	expand_dims

Expands the shape of an array
4 	squeeze
Removes single-dimensional entries from the shape of an array


#Stacking arrays
a = np.arange(9).reshape(3,3)
a

b = 2 * a
b
#Arrays can be stacked horizontally, depth-wise, or vertically. 
#We use vstack(), dstack(), hstack(), column_stack(), row_stack(), and concatenate() functions
#Sr.No. 	Array & Description
#1 	concatenate Joins a sequence of arrays along an existing axis
np.concatenate((a, b), axis=1)
#same as hstack
#axis argument is set to 0 (default)
np.concatenate((a, b), axis=0)
#same as vstack

#2 	stack Joins a sequence of arrays along a new axis

#3 	hstack Stacks arrays in sequence horizontally (column wise)
#Horizontal stacking: we will form a tuple of ndarray and give it to the hstack() function. 
np.hstack((a, b))

#4 	vstack Stacks arrays in sequence vertically (row wise)
#Vertical stacking: We form a tuple & give to the vstack()
np.vstack((a, b))

#Depth stacking:dstack()
#stacking of a list of arrays along the third axis (depth). 
#For instance, we could stack two-dimensional arrays of image data on top of each other
np.dstack((a, b))

#Column stacking:column_stack()
#stacks one-dimensional arrays column-wise.
oned = np.arange(2)
oned
twice_oned = 2 * oned
twice_oned
np.column_stack((oned, twice_oned))

#Two-dimensional arrays are stacked the way hstack() stacks them
np.column_stack((a, b))
np.column_stack((a, b)) == np.hstack((a, b))

#Row stacking:row_stack()
#for 1d arrays, it just stacks the arrays in rows into a two-dimensional array
np.row_stack((oned, twice_oned))
#The row_stack() function for two-dimensional arrays are same as vstack() function
np.row_stack((a, b))
np.row_stack((a,b)) == np.vstack((a, b))




#Splitting Arrays
#Arrays can be split vertically, horizontally, or depth-wise. 
#functions : hsplit(), vsplit(), dsplit(), and split()
#We can either split arrays into arrays of the same shape or 
#indicate the position after which the split should occur.
a = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

#Sr.No. 	Array & Description
#1 	split   Splits an array into multiple sub-arrays
#with parameter axis=1:
np.split(a, 3, axis=1)
#same as hsplit
#with axis=0 - splits an array along the vertical axis
np.split(a, 3, axis=0)
#same as vsplit

#2 	hsplit  Splits an array into multiple sub-arrays horizontally (column-wise)
#split an array along its horizontal axis into three pieces of the same size and shape 
np.hsplit(a, 3)

#3 	vsplit  Splits an array into multiple sub-arrays vertically (row-wise)
np.vsplit(a, 3)

#Depth-wise splitting:dsplit() - splits an array depth-wise
#We will need an array of rank three first:
c = np.arange(27).reshape(3, 3, 3)
c
np.dsplit(c, 3)


#Adding / Removing Elements
#Sr.No. 	Element & Description
#1 	resize Returns a new array with the specified shape
b = np.array([[[ 0, 1, 2, 3], [ 4, 5, 6, 7], [ 8, 9, 10, 11]], [[12, 13, 14, 15],
[16, 17, 18, 19],
[20, 21, 22, 23]]])
#works just like the reshape() method but modifies the array it operates on:
b.resize((2,12))
b


2 	append

Appends the values to the end of an array
3 	insert

Inserts the values along the given axis before the given indices
4 	delete

Returns a new array with sub-arrays along an axis deleted
5 	unique

Finds the unique elements of an array