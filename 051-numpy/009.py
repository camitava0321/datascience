# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 23:22:27 2017

@author: Amitava
"""

#Identity Array
#An identity array is a square array with ones on its main diagonal. There are two ways to create identity array.
#    identy
#    eye

#The identity Function
#We can create identity arrays with the function identity:
#identity(n, dtype=None)
#The parameters:
#Parameter 	Meaning
#n 	      An integer number defining the number of rows and columns of the output, i.e. 'n' x 'n'
#dtype 	   An optional argument, defining the data-type of the output. The default is 'float'

#The output of identity is an 'n' x 'n' array with its main diagonal set to one, and all other elements are 0.

import numpy as np
np.identity(4)

np.identity(4, dtype=int) # equivalent to np.identity(3, int)


#The eye Function
#Another way to create identity arrays provides the function eye. 
#It returns a 2-D array with ones on the diagonal and zeros elsewhere.
#eye(N, M=None, k=0, dtype=float)
#Parameter 	Meaning
#N 	      An integer number defining the rows of the output array.
#M 	      An optional integer for setting the number of columns in the output. If it is None, it defaults to 'N'.
#k 	      Defining the position of the diagonal. The default is 0. 0 refers to the main diagonal. A positive value refers to an upper diagonal, and a negative value to a lower diagonal.
#dtype 	   Optional data-type of the returned array.

#eye returns an ndarray of shape (N,M). 
#All elements of this array are equal to zero, except for the 'k'-th diagonal, whose values are equal to one.

np.eye(5, 8, k=1, dtype=int)
