# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018
@author: Amitava Chakraborty
Byte Swapping - numpy.ndarray.byteswap()
"""
#Data stored in the memory of a computer depends on which architecture the CPU uses. 
#It may be little-endian (least significant is stored in the smallest address) or 
#big-endian (most significant byte in the smallest address).

#The numpy.ndarray.byteswap() function toggles between the two representations: bigendian and little-endian.
import numpy as np 
a = np.array([1, 256, 8755], dtype = np.int16) 

print 'Our array is:' 
print a  

print 'Representation of data in memory in hexadecimal form:'  
print map(hex,a)  
# byteswap() function swaps in place by passing True parameter 

print 'Applying byteswap() function:' 
print a.byteswap(True) 

print 'In hexadecimal form:' 
print map(hex,a) 
# We can see the bytes being swapped