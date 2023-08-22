# -*- coding: utf-8 -*-
"""
Scipy Examples
@author: AMITAVA
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

"""
SciPy Organization
SciPy is organized into subpackages covering different scientific computing domains.
Subpackage	    Description
cluster	        Clustering algorithms
constants	    Physical and mathematical constants
fftpack	        Fast Fourier Transform routines
integrate	    Integration and ordinary differential equation solvers
interpolate	    Interpolation and smoothing splines
io	            Input and Output
linalg	        Linear algebra
ndimage	        N-dimensional image processing
odr	            Orthogonal distance regression
optimize	    Optimization and root-finding routines
signal	        Signal processing
sparse	        Sparse matrices and associated routines
spatial	        Spatial data structures and algorithms
special	        Special functions
stats	        ßStatistical distributions and functions

Scipy sub-packages need to be imported separately, for example:
from scipy import linalg, optimize
Because of their ubiquitousness, some of the functions in these subpackages are also made available in the 
scipy namespace to ease their use in interactive sessions and programs. 
In addition, many basic array functions from numpy are also available at the top-level of the scipy package. 
"""
#%% - Basic functions
#Interaction with Numpy
#Scipy builds on Numpy
#So for all basic array handling needs one can use Numpy functions.

#The top level of scipy also contains functions from numpy and numpy.lib.scimath - better to use them directly from numpy

#Index Tricks
#There are some class instances that make special use of the slicing functionality - efficient means for array construction. 

#For example, rather than writing something like the following
a = np.concatenate(([3], [0]*5, np.arange(-1, 1.002, 2/9.0)))
print (a)
#with the r_ command one can enter this as
b = np.r_[3,[0]*5,-1:1:10j]
#“r” - for row concatenation because 
#if the objects between commas are 2 dimensional arrays, they are stacked by rows (and thus must have commensurate columns). 
#Equivalent command c_ - stacks 2d arrays by columns but works identically to r_ for 1d arrays.
print (b)

#Note : 
#1. the slicing syntax to construct ranges. 
#2. Use of the complex number 10j as the step size in the slicing syntax. 
#This non-standard use allows the number to be interpreted as the number of points 
#to produce in the range rather than as a step size 
#(note we would have used the long integer notation, 10L, but this notation may go away in Python as the integers become unified). 
#This non-standard usage may be unsightly to some, 
#but it gives the user the ability to quickly construct complicated vectors in a very readable fashion. 
#When the number of points is specified in this way, the end- point is inclusive.


#function mgrid - used to construct 1d ranges as a convenient substitute for arange. 
#It also allows the use of complex-numbers in the step-size to indicate the number of points to place between the (inclusive) end-points. 
#The real purpose of this function however is to produce N, N-d arrays 
#which provide coordinate arrays for an N-dimensional volume. 
print (np.mgrid[0:5,0:5])
print (np.mgrid[0:5:4j,0:5:4j])

#Polynomials
#Two ways to deal with 1-d polynomials 
#1. poly1d class from Numpy - accepts coefficients or polynomial roots to initialize a polynomial. 
#The polynomial object can then be manipulated in algebraic expressions, integrated, differentiated, and evaluated. 
#It even prints like a polynomial:
from numpy import poly1d
p = poly1d([3,4,5])
print(p)
print(p*p)
print(p.integ(k=6))
print(p.deriv())
p([4, 5])

#2. As an array of coefficients with the first element of the array giving the coefficient of the highest power. 
#There are explicit functions to add, subtract, multiply, divide, integrate, differentiate, and evaluate polynomials 
#represented as sequences of coefficients.

#Vectorizing functions (vectorize)
#Feature of NumPy - to convert an ordinary Python function that accepts scalars and returns scalars 
#into a “vectorized-function” with the same broadcasting rules as other Numpy functions (i.e. the Universal functions, or ufuncs). 
#Suppose we have a Python function named addsubtract defined as:
def addsubtract(a,b):
    if a > b:
        return a - b
    else:
        return a + b
#which defines a function of two scalar variables and returns a scalar result. 
#The class vectorize can be used to “vectorize “this function so that
vec_addsubtract = np.vectorize(addsubtract)
print (vec_addsubtract)
#returns a function which takes array arguments and returns an array result:

vec_addsubtract([0,3,6,9],[1,3,5,7])

#Type handling
#Note the difference between np.iscomplex/np.isreal and np.iscomplexobj/np.isrealobj. 
#The former command is array based and returns byte arrays of ones and zeros providing the result of the element-wise test. 
#The latter command is object based and returns a scalar describing the result of the test on the entire object.

#Often it is required to get just the real and/or imaginary part of a complex number. 
#While complex numbers and arrays have attributes that return those values, 
#if one is not sure whether or not the object will be complex-valued, 
#it is better to use the functional forms np.real and np.imag. 
#These functions succeed for anything that can be turned into a Numpy array. 
#Consider also the function np.real_if_close which transforms a complex-valued number with tiny imaginary part into a real number.

#Occasionally the need to check whether or not a number is a scalar 
#(Python (long)int, Python float, Python complex, or rank-0 array) occurs in coding. 
#This functionality is provided in the convenient function np.isscalar which returns a 1 or a 0.

#Finally, ensuring that objects are a certain Numpy type occurs often enough that it has been given 
#a convenient interface in SciPy through the use of the np.cast dictionary. 
#The dictionary is keyed by the type it is desired to cast to and 
#the dictionary stores functions to perform the casting. 
#Thus, np.cast['f'](d) returns an array of np.float32 from d. 
#This function is also useful as an easy way to get a scalar of a certain type:
np.cast['f'](np.pi)

#Other useful functions
#There are also several other useful functions which should be mentioned. 
#For doing phase processing, the functions angle, and unwrap are useful. 
#Also, the linspace and logspace functions return equally spaced samples in a linear or log scale. 
#Finally, it’s useful to be aware of the indexing capabilities of Numpy. 
#Mention should be made of the function select which extends the functionality of where 
#to include multiple conditions and multiple choices. 
#The calling convention is select(condlist,choicelist,default=0). 
#select is a vectorized form of the multiple if-statement. 
#It allows rapid construction of a function which returns an array of results based on a list of conditions. 
#Each element of the return array is taken from the array in a choicelist 
#corresponding to the first condition in condlist that is true. For example
x = np.r_[-2:3]
x
np.select([x > 3, x >= 0], [0, x+2])

#Some additional useful functions can also be found in the module scipy.misc. 
#For example the factorial and comb functions compute  and  using either exact integer arithmetic 
#(thanks to Python’s Long integer object), or 
#by using floating-point precision and the gamma function. 
#Another function returns a common image used in image processing: lena.

#Finally, two functions are provided that are useful for approximating derivatives of functions using discrete-differences. 
#The function central_diff_weights returns weighting coefficients for an equally-spaced -point approximation to the derivative of order o.
#These weights must be multiplied by the function corresponding to these points and 
#the results added to obtain the derivative approximation. 
#This function is intended for use when only samples of the function are available. 
#When the function is an object that can be handed to a routine and evaluated, 
#the function derivative can be used to automatically evaluate the object at the correct points 
#to obtain an N-point approximation to the o-th derivative at a given point.