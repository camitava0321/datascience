# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 23:23:15 2017

@author: Amitava
"""
import numpy as np

#Exercises:
#1) Create an arbitrary one dimensional array called "v".
a = np.array([3,8,12,18,7,11,30])

#2) Create a new array which consists of the odd indices of previously created array "v".
odd_elements = a[1::2]

#3) Create a new array in backwards ordering from v.
reverse_order = a[::-1]

#4) What will be the output of the following code:
#a = np.array([1, 2, 3, 4, 5])
#b = a[1:4]
#b[0] = 200
#print(a[1])

#The output will be 200, because slices are views in numpy and not copies.

#5) Create a two dimensional array called "m".
m = np.array([ [11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]])

#6) Create a new array from m, in which the elements of each row are in reverse order.
m[::,::-1]

#7) Another one, where the rows are in reverse order.
m[::-1]

#8) Create an array from m, where columns and rows are in reverse order.
m[::-1,::-1]

#9) Cut of the first and last row and the first and last column.
m[1:-1,1:-1]