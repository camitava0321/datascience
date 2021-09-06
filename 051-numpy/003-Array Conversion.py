# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 15:56:26 2017

@author: Amitava
Converting arrays
"""
import numpy as np
#convert a NumPy array to a Python list with the tolist()
b = np.array([ 1.+1.j, 3.+2.j])
b.tolist()

#astype() - converts an array to an array of the specified type
b
b.astype(int)
#We are losing the imaginary part when casting from complex type to int.
#The astype() function also accepts the name of a type as a string
b.astype('complex')
#This won't show any warning this time, because we used the proper data type.