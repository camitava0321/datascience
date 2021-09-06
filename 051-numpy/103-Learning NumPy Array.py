# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Stride tricks for Sudoku
"""
import numpy as np

#The ndarray class has a field, strides, 
#which is a tuple indicating the number of bytes to step in each dimension when going through an array. 
#Let's apply some stride tricks to the problem of splitting a Sudoku puzzle to the 3 x 3 squares it is composed of

#First define the Sudoku puzzle array
#This one is filled with the contents of the actual solved Sudoku puzzle
sudoku = np.array([
[2, 8, 7, 1, 6, 5, 9, 4, 3],
[9, 5, 4, 7, 3, 2, 1, 6, 8],
[6, 1, 3, 8, 4, 9, 7, 5, 2],
[8, 7, 9, 6, 5, 1, 2, 3, 4],
[4, 2, 1, 3, 9, 8, 6, 7, 5],
[3, 6, 5, 4, 2, 7, 8, 9, 1],
[1, 9, 8, 5, 7, 3, 4, 2, 6],
[5, 4, 2, 9, 1, 6, 3, 8, 7],
[7, 3, 6, 2, 8, 4, 5, 1, 9]
])
shape = (3, 3, 3, 3)

#Now calculate the strides
#itemsize field of ndarray gives us the number of bytes in an array
#itemsize calculates the strides
strides = sudoku.itemsize * np.array([27, 3, 9, 1])

#Now we can split the puzzle into squares with the as_strided() function of the np.lib.stride_tricks module
squares = np.lib.stride_tricks.as_strided(sudoku, shape=shape, strides=strides)
print(squares)
#This prints separate Sudoku squares (some of the squares were omitted to save space),
#We have applied stride tricks to decompose a Sudoku puzzle in its constituent 3 x 3 squares
#The strides tell us how many bytes we need to skip at each step when going through the Sudoku array.