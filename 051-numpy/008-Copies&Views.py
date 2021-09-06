# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 23:21:38 2017

@author: Amitava
Copies & Views
"""

import numpy as np
#Copy - the contents are physically stored in another location
#View - a different view of the same memory content is provided

#No Copy
#Simple assignments do not make the copy of array object. 
#Instead, it uses the same id() of the original array to access it. 
#The id() returns a universal identifier of Python object, similar to the pointer in C.
#Any changes in either gets reflected in the other. 
#For example, the changing shape of one will change the shape of the other too.
a = np.arange(6) 
print a  
print id(a)  
b = a 
print b  
print id(b)  

print 'Change shape of b:' 
b.shape = 3,2 
print b  
print 'Shape of a also gets changed:' 
print a

#View or Shallow Copy
#NumPy has ndarray.view() method which is a new array object that looks at the same data of the original array. 
#Unlike the earlier case, change in dimensions of the new array doesn’t change dimensions of the original.
# To begin with, a is 3X2 array 
a = np.arange(6).reshape(3,2) 
print 'Array a:' 
print a  
print 'Create view of a:' 
b = a.view() 
print b  
print 'id() for both the arrays are different:' 
print 'id() of a:', id(a), "   ",'id() of b:',id(b)  
# Change the shape of b. It does not change the shape of a 
b.shape = 2,3 
print 'Shape of b:' 
print b  
print 'Shape of a:' 
print a

#Slice of an array creates a view.
a = np.array([[10,10], [2,3], [4,5]]) 
print 'Our array is:' 
print a  
print 'Create a slice:' 
s = a[:, :2] 
print s 

#Deep Copy
#The ndarray.copy() function creates a deep copy. 
#It is a complete copy of the array and its data, and doesn’t share with the original array.
a = np.array([[10,10], [2,3], [4,5]]) 
print 'Array a is:' 
print a  
print 'Create a deep copy of a:' 
b = a.copy() 
print 'Array b is:' 
print b 
#b does not share any memory of a 
print 'Can we write b is a' 
print b is a  
print 'Change the contents of b:' 
b[0,0] = 100 
print 'Modified array b:' 
print b  
print 'a remains unchanged:' 
print a

#numpy.copy()
#copy(obj, order='K')
#Return an array copy of the given object 'obj'.
#Parameter 	Meaning
#obj 	      array_like input data. 
#order 	   The possible values are {'C', 'F', 'A', 'K'}. 
#This parameter controls the memory layout of the copy. 
#'C' means C-order, 
#'F' means Fortran-order, 
#'A' means 'F' if the object 'obj' is Fortran contiguous, 'C' otherwise. 
#'K' means match the layout of 'obj' as closely as possible.

x = np.array([[42,22,12],[44,53,66]], order='F')
y = x.copy()
x[0,0] = 1001
print(x)
print(y)

print(x.flags['C_CONTIGUOUS'])
print(y.flags['C_CONTIGUOUS'])


#Views should not be confused with the concept of database views
#Views in the NumPy are not read-only, and you don't have the possibility to protect the underlying data. 
#It is important to know when we are dealing with a shared array view and 
#when we have a copy of array data. 
#A slice, for instance, will create a view. 
#This means that if you assign a slice to a variable and then change the underlying array, 
#the value of this variable will change. 

#We will create an array from the famous Lena image, 
#copy the array, 
#create a view, and 
#at the end, modify the view. 
#The Lena image array comes from a SciPy function.
#create a copy of the Lena array
import scipy.misc as scp
face = scp.face()
face.shape
#deep copy
acopy = face.copy()
#Now we create a view of the array
aview = face.view()
#The array is not readonly - make all of them updatable
face.flags['WRITEABLE']=True
acopy.flags['WRITEABLE']=True
aview.flags['WRITEABLE']=True
#Change a particular pixel value of the image
aview[20][2][2] = 102

import matplotlib.pyplot as plt
plt.subplot(221)
plt.imshow(face)
plt.subplot(222)
plt.imshow(acopy)
plt.subplot(223)
plt.imshow(aview)
#zerorise every data
aview.flat = 0

plt.subplot(224)
plt.imshow(aview)
plt.show()
#by changing the view at the end of the program, 
#we changed the original face array
#But the copied array was unaffected