# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Mathematical Functions
"""
import numpy as np 
#NumPy contains a large number of various mathematical operations. 
#NumPy provides standard trigonometric functions, 
#functions for arithmetic operations, handling complex numbers, etc.

#Trigonometric Functions
#NumPy has standard trigonometric functions which return trigonometric ratios for a given angle in radians.
a = np.array([0,30,45,60,90]) 
print 'Sine of different angles:' 
# Convert to radians by multiplying with pi/180 
print np.sin(a*np.pi/180) 
print '\n'  
print 'Cosine values for angles in array:' 
print np.cos(a*np.pi/180) 
print '\n'  
print 'Tangent values for given angles:' 
print np.tan(a*np.pi/180) 

#arcsin, arcos, and arctan functions return the trigonometric inverse of sin, cos, and tan of the given angle. The result of these functions can be verified by numpy.degrees() function by converting radians to degrees.
print 'Array containing sine values:' 
sin = np.sin(a*np.pi/180) 
print sin 
print '\n'  
print 'Compute sine inverse of angles. Returned values are in radians.' 
inv = np.arcsin(sin) 
print inv 
print '\n'  
print 'Check result by converting to degrees:' 
print np.degrees(inv) 
print '\n'  
print 'arccos and arctan functions behave similarly:' 
cos = np.cos(a*np.pi/180) 
print cos 
print '\n'  
print 'Inverse of cos:' 
inv = np.arccos(cos) 
print inv 
print '\n'  
print 'In degrees:' 
print np.degrees(inv) 
print '\n'  
print 'Tan function:' 
tan = np.tan(a*np.pi/180) 
print tan
print '\n'  
print 'Inverse of tan:' 
inv = np.arctan(tan) 
print inv 
print '\n'  
print 'In degrees:' 
print np.degrees(inv) 

#Functions for Rounding - numpy.around()
#This is a function that returns the value rounded to the desired precision. The function takes the following parameters.
#numpy.around(a,decimals)
Sr.No. 	Parameter & Description
#1 	
a
Input data
#2 	
decimals
The number of decimals to round to. Default is 0. If negative, the integer is rounded to position to the left of the decimal point

a = np.array([1.0,5.55, 123, 0.567, 25.532]) 
print 'Original array:' 
print a 
print '\n'  
print 'After rounding:' 
print np.around(a) 
print np.around(a, decimals = 1) 
print np.around(a, decimals = -1)

#numpy.floor()
#This function returns the largest integer not greater than the input parameter. The floor of the scalar x is the largest integer i, such that i <= x. Note that in Python, flooring always is rounded away from 0.
a = np.array([-1.7, 1.5, -0.2, 0.6, 10]) 
print 'The given array:' 
print a 
print '\n'  
print 'The modified array:' 
print np.floor(a)

#numpy.ceil()
#The ceil() function returns the ceiling of an input value, i.e. the ceil of the scalar x is the smallest integer i, such that i >= x.
a = np.array([-1.7, 1.5, -0.2, 0.6, 10]) 
print 'The given array:' 
print a 
print '\n'  
print 'The modified array:' 
print np.ceil(a)