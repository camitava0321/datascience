# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Iterating Over Array
"""
import numpy as np
#iterator object numpy.nditer - efficient multidimensional iterator object
#to iterate over an array - Each element of an array is visited using Python’s standard Iterator interface.

#A 3X4 array using arange() and iterate over it using nditer.
a = np.arange(0,60,5)
a = a.reshape(3,4)
print 'Original array is:'
print a
print '\n'
print 'Modified array is:'
for x in np.nditer(a):
   print x,

#The order of iteration is chosen to match the memory layout of an array, 
#without considering a particular ordering. 
#This can be seen by iterating over the transpose of the above array.
a = np.arange(0,60,5) 
a = a.reshape(3,4) 
print 'Original array is:'
print a 
print '\n'  
print 'Transpose of the original array is:' 
b = a.T 
print b 
print '\n'  
print 'Modified array is:' 
for x in np.nditer(b): 
   print x,

#Iteration Order
#If the same elements are stored using F-style order, 
#the iterator chooses the more efficient way of iterating over an array.
a = np.arange(0,60,5)
a = a.reshape(3,4)
print 'Original array is:'
print a
print '\n'
print 'Transpose of the original array is:'
b = a.T
print b
print '\n'
print 'Sorted in C-style order:'
c = b.copy(order = 'C')
print c
for x in np.nditer(c):
   print x,
print '\n'

print 'Sorted in F-style order:'
c = b.copy(order = 'F')
print c
for x in np.nditer(c):
   print x,


#It is possible to force nditer object to use a specific order by explicitly mentioning it.
a = np.arange(0,60,5) 
a = a.reshape(3,4) 
print 'Original array is:' 
print a 
print '\n'  
print 'Sorted in C-style order:' 
for x in np.nditer(a, order = 'C'): 
   print x,  
print '\n' 
print 'Sorted in F-style order:' 
for x in np.nditer(a, order = 'F'): 
   print x,

#Modifying Array Values
#The nditer object has another optional parameter called op_flags. Its default value is read-only, but can be set to read-write or write-only mode. This will enable modifying array elements using this iterator.
a = np.arange(0,60,5)
a = a.reshape(3,4)
print 'Original array is:'
print a
print '\n'
for x in np.nditer(a, op_flags = ['readwrite']):
   x[...] = 2*x
print 'Modified array is:'
print a

#External Loop
#The nditer class constructor has a ‘flags’ parameter, which can take the following values −
#Sr.No. 	Parameter & Description
#1 	c_index C_order index can be racked
#2 	f_index Fortran_order index is tracked
#3 	multi-index Type of indexes with one per iteration can be tracked
#4 	external_loop Causes values given to be one-dimensional arrays with multiple values instead of zero-dimensional array

#In the following example, one-dimensional arrays corresponding to each column is traversed by the iterator.
a = np.arange(0,60,5) 
a = a.reshape(3,4) 
print 'Original array is:' 
print a 
print '\n'  
print 'Modified array is:' 
for x in np.nditer(a, flags = ['external_loop'], order = 'F'):
   print x,

#Broadcasting Iteration
#If two arrays are broadcastable, a combined nditer object is able to iterate upon them concurrently. Assuming that an array a has dimension 3X4, and there is another array b of dimension 1X4, the iterator of following type is used (array b is broadcast to size of a).
a = np.arange(0,60,5) 
a = a.reshape(3,4) 
print 'First array is:' 
print a 
print '\n'  
print 'Second array is:' 
b = np.array([1, 2, 3, 4], dtype = int) 
print b  
print '\n' 
print 'Modified array is:' 
for x,y in np.nditer([a,b]): 
   print "%d:%d" % (x,y),