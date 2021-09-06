# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 23:14:05 2017

@author: Amitava
Broadcasting
"""
import numpy as np 
#refers to the ability of NumPy to treat arrays of different shapes during arithmetic operations. 
#Arithmetic operations on arrays are usually done on corresponding elements. 
#If two arrays are of exactly the same shape, then these operations are smoothly performed.
a = np.array([1,2,3,4]) 
b = np.array([10,20,30,40]) 
c = a * b 
print c

#If the dimensions of two arrays are dissimilar, element-to-element operations are not possible. 
#However, operations on arrays of non-similar shapes is still possible in NumPy, b
#ecause of the broadcasting capability. 
#The smaller array is broadcast to the size of the larger array so that they have compatible shapes.

#Broadcasting is possible if the following rules are satisfied −
#    Array with smaller ndim than the other is prepended with '1' in its shape.
#    Size in each dimension of the output shape is maximum of the input sizes in that dimension.
#    An input can be used in calculation, if its size in a particular dimension matches the output size or its value is exactly 1.
#    If an input has a dimension size of 1, the first data entry in that dimension is used for all calculations along that dimension.

#A set of arrays is said to be broadcastable if the above rules produce a valid result and one of the following is true −
#    Arrays have exactly the same shape.
#    Arrays have the same number of dimensions and the length of each dimension is either a common length or 1.
#    Array having too few dimensions can have its shape prepended with a dimension of length 1, so that the above stated property is true.
a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]]) 
b = np.array([1.0,2.0,3.0])  
print 'First array:' 
print a 
print '\n'  
print 'Second array:' 
print b 
print '\n'  
print 'First Array + Second Array' 
print a + b




#NumPy tries to perform an operation even though the operands do not have the same shape. 
#we will multiply an array and a scalar
#The scalar is extended to the shape of an array operand, and then 
#the multiplication is performed. 
#We will download an audio file and make a new version that is quieter

import scipy.io.wavfile
import matplotlib.pyplot as plt
import urllib2
import numpy as np
response = urllib2.urlopen('http://www.thesoundarchive.com/austinpowers/smashingbaby.wav')
print response.info()
WAV_FILE = 'smashingbaby.wav'
filehandle = open(WAV_FILE, 'w')
filehandle.write(response.read())
filehandle.close()

#First, read the WAV file
#SciPy has a wavfile module that allows you to load sound data or generate WAV files
#The read() function returns a data array and sample rate. 
#In this example, we only care about the data.
sample_rate, data = scipy.io.wavfile.read(WAV_FILE)
print "Data type", data.dtype, "Shape", data.shape

#Now create a new array. 
#We will use NumPy to make a quieter audio sample. 
#It is just a matter of creating a new array with smaller values by multiplying with a constant. 
#This is broadcasting
#At the end, we need to make sure that we have the same data type as in the original array 
#because of the WAV format.
newdata = data * 0.2
newdata = newdata.astype(np.uint8)
print "Data type", newdata.dtype, "Shape", newdata.shape

#Now this new array can be written into a new WAV file
scipy.io.wavfile.write("quiet.wav",sample_rate, newdata)


#Plot the original and modified data array with Matplotlib
plt.subplot(2, 1, 1)
plt.title("Original")
plt.plot(data)
plt.subplot(2, 1, 2)
plt.title("Quiet")
plt.plot(newdata)
plt.show()

#The result is a plot of the original WAV file data and a new array with smaller values