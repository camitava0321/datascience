# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
"""

import numpy as np 
#ndarray objects can be saved to and loaded from the disk files. 

#The IO functions
#load() and save() functions handle /numPy binary files (with npy extension)
#loadtxt() and savetxt() functions handle normal text files

#The numpy.save() file stores the input array in a disk file with npy extension.
#NumPy introduces a simple file format for ndarray objects. 
#.npy file stores data, shape, dtype and other information required to reconstruct the ndarray in a disk file 
a = np.array([1,2,3,4,5]) 
np.save('outfile',a)

#To reconstruct array from outfile.npy, use load() function.
b = np.load('outfile.npy') 
print b 

#The save() and load() functions accept an additional Boolean parameter allow_pickles. 

#savetxt()
#The storage and retrieval of array data in simple text file format is done with savetxt() and loadtxt() functions.
#The savetxt() and loadtxt() functions accept additional optional parameters such as header, footer, and delimiter.
np.savetxt('out.txt',a) 
b = np.loadtxt('out.txt') 
print b 
