# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Arithmetic Operations
"""
import numpy as np 
#Input arrays for performing arithmetic operations such as add(), subtract(), multiply(), and divide() must be either of the same shape or should conform to array broadcasting rules.
a = np.arange(9, dtype = np.float_).reshape(3,3) 
print 'First array:' 
print a 
print '\n'  
print 'Second array:' 
b = np.array([10,10,10]) 
print b 
print '\n'  
print 'Add the two arrays:' 
print np.add(a,b) 
print '\n'  
print 'Subtract the two arrays:' 
print np.subtract(a,b) 
print '\n'  
print 'Multiply the two arrays:' 
print np.multiply(a,b) 
print '\n'  
print 'Divide the two arrays:' 
print np.divide(a,b)

#Let us now discuss some of the other important arithmetic functions available in NumPy.
#numpy.reciprocal()
#This function returns the reciprocal of argument, element-wise. 
#For elements with absolute values larger than 1, 
#the result is always 0 because of the way in which Python handles integer division. 
#For integer 0, an overflow warning is issued.
a = np.array([0.25, 1.33, 1, 0, 100]) 
print 'Our array is:' 
print a 
print '\n'  
print 'After applying reciprocal function:' 
print np.reciprocal(a) 
print '\n'  
b = np.array([100], dtype = int) 
print 'The second array is:' 
print b 
print '\n'  
print 'After applying reciprocal function:' 
print np.reciprocal(b) 

#numpy.power()
#This function treats elements in the first input array as base and returns it raised to the power of the corresponding element in the second input array.
a = np.array([10,100,1000]) 
print 'Our array is:' 
print a 
print '\n'  
print 'Applying power function:' 
print np.power(a,2) 
print '\n'  
print 'Second array:' 
b = np.array([1,2,3]) 
print b 
print '\n'  
print 'Applying power function again:' 
print np.power(a,b)

#numpy.mod()
#This function returns the remainder of division of the corresponding elements in the input array. The function numpy.remainder() also produces the same result.
a = np.array([10,20,30]) 
b = np.array([3,5,7]) 
print 'First array:' 
print a 
print '\n'  
print 'Second array:' 
print b 
print '\n'  
print 'Applying mod() function:' 
print np.mod(a,b) 
print '\n'  
print 'Applying remainder() function:' 
print np.remainder(a,b) 

#The following functions are used to perform operations on array with complex numbers.
#    numpy.real() − returns the real part of the complex data type argument.
#    numpy.imag() − returns the imaginary part of the complex data type argument.
#    numpy.conj() − returns the complex conjugate, which is obtained by changing the sign of the imaginary part.
#    numpy.angle() − returns the angle of the complex argument. The function has degree parameter. If true, the angle in the degree is returned, otherwise the angle is in radians.

a = np.array([-5.6j, 0.2j, 11. , 1+1j]) 
print 'Our array is:' 
print a 
print '\n'  
print 'Applying real() function:' 
print np.real(a) 
print '\n'  
print 'Applying imag() function:' 
print np.imag(a) 
print '\n'  
print 'Applying conj() function:' 
print np.conj(a) 
print '\n'  
print 'Applying angle() function:' 
print np.angle(a) 
print '\n'  
print 'Applying angle() function again (result in degrees)' 
print np.angle(a, deg = True)