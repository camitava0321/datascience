# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 23:21:06 2017

@author: Amitava
"""
import numpy as np

#Arrays of Ones and of Zeros
#Two ways to initialize Arrays with Zeros or Ones. 
#The method ones(t) takes a tuple t with the shape of the array and fills the array accordingly with ones. 
#By default it will be filled with Ones of type float. 
#For integer Ones, one has to set the optional parameter dtype to int:
E = np.ones((2,3))
print(E)
F = np.ones((3,4),dtype=int)
print(F)

#Same for the method zeros()
Z = np.zeros((2,4))
print(Z)

#Another interesting way to create an array with Ones or with Zeros
#Numpy supplies for this purpose the methods ones_like(a) and zeros_like(a).
x = np.array([2,5,18,14,4])
E = np.ones_like(x)
print(E)
E1 = E+x
print E1
Z = np.zeros_like(E1)
print(Z)
