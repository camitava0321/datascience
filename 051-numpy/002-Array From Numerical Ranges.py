# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 15:56:26 2017

@author: Amitava
Array From Numerical Ranges
"""
import numpy as np
#Diff between np.arange and range of python
#arange - numpy fn - returns ndarray
a = np.arange(1,100,3)
#range - python fn - returns vector
x = range(1,100,3)
print(a)
print (x)
print(list(x))


#create an array from numerical ranges.
#numpy.arange(start, stop, step, dtype)
#returns an ndarray object containing evenly spaced values within a given range. 
#Sr.No. 	Parameter & Description
#1 start The start of an interval. If omitted, defaults to 0
#2 stop  The end of an interval (not including this number)
#3 step  Spacing between values, default is 1
#4 dtype Data type of resulting ndarray. If not given, data type of input is used
x = np.arange(5) 
print x

# dtype set 
x = np.arange(5, dtype = float)
print x

x = np.arange(10.4)
print(x)

# start and stop parameters set 
x = np.arange(10,20,2) 
print x

# some more arange examples:
x = np.arange(0.5, 10.4, 0.8)
print(x)
x = np.arange(0.5, 10.4, 0.8, int)
print(x)


#numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype)
#linspace returns an ndarray, 
#consisting of 'num' equally spaced samples in the closed interval [start, stop] 
#or the half-open interval start/stop 
#Whether a closed or a half-open interval is returned depends on whether 'endpoint' is True or False. 
#'start' - start value of the sequence 
#'stop' - end value of the sequence, unless 'endpoint' is set to False. 
#In the latter case, the resulting sequence will consist of all but the last of 'num + 1' evenly spaced samples. 
#This means that 'stop' is excluded. 
#Note that the step size changes when 'endpoint' is False. 
#The number of samples to be generated can be set with 'num', which defaults to 50. 
#If the optional parameter 'endpoint' is set to True (the default), 'stop' will be the last sample of the sequence. 
#Otherwise, it is not included.
#Sr.No. 	Parameter & Description
#1 start The starting value of the sequence
#2 stop  The end value of the sequence, included in the sequence if endpoint set to true
#3 num   The number of evenly spaced samples to be generated. Default is 50
#4 endpoint True by default, hence the stop value is included in the sequence. If false, it is not included
#5 retstep If true, returns samples and step between the consecutive numbers
#6 dtype Data type of output ndarray, default float

# 50 values between 1 and 10:
print(np.linspace(1, 10))
# 7 values between 1 and 10:
print(np.linspace(1, 10, 7))
# excluding the endpoint:
print(np.linspace(1, 10, 7, endpoint=False))
x = np.linspace(10,20,5) 
print x
# endpoint set to false 
x = np.linspace(10,20, 5, endpoint = False) 
print x
# find retstep value 
x = np.linspace(1,2,5, retstep = True) 
print x 
# retstep here is 0.25
#An interesting parameter 'retstep':
#If the optional parameter 'retstep' is set, 
#the function will also return the value of the spacing between adjacent values. 
#So, the function will return a tuple ('samples', 'step'):
samples, spacing = np.linspace(1, 10, retstep=True)
print(spacing)
samples, spacing = np.linspace(1, 10, 20, endpoint=True, retstep=True)
print(spacing)
samples, spacing = np.linspace(1, 10, 20, endpoint=False, retstep=True)
print(spacing)

#numpy.logspace(start, stop, num, endpoint, base, dtype)
#returns an ndarray object that contains the numbers that are evenly spaced on a log scale. 
#Start and stop endpoints of the scale are indices of the base, usually 10.
#Sr.No. 	Parameter & Description
#1 start The starting point of the sequence is basestart
#2 stop  The final value of sequence is basestop
#3 num   The number of values between the range. Default is 50
#4 endpoint If true, stop is the last value in the range
#5 base  Base of log space, default is 10
#6 dtype Data type of output array. If not given, it depends upon other input arguments

# default base is 10 
a = np.logspace(1.0, 2.0, num = 10) 
print a
# set base of log space to 2 
a = np.logspace(1,10,num = 10, base = 2) 
print a