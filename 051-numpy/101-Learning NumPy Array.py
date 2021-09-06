# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Adding arrays
"""
import numpy as np
#Add two vectors A & B
#A vector here means a 1d array. 
#A holds the squares of integers 0 to n
#B holds the cubes of integers 0 to n

#Python Solution
def pythonsum(n):
    a = range(n)
    b = range(n)
    c = []
    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])
    return c

#numpy solution
def numpysum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b
    return c

#Notice that numpysum() does not need a for loop. 

c=pythonsum(20)
print c
c=numpysum(20)
print c
#Notice - result from the numpysum does not have any commas. 
#Because it is not a Python list, but a NumPy array. 
#NumPy arrays are specialized data structures for numerical data
