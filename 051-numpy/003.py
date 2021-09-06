# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 23:05:04 2017

@author: Amitava
"""

#linspace
#Syntax : linspace(start, stop, num=50, endpoint=True, retstep=False)

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

import numpy as np
# 50 values between 1 and 10:
print(np.linspace(1, 10))
# 7 values between 1 and 10:
print(np.linspace(1, 10, 7))
# excluding the endpoint:
print(np.linspace(1, 10, 7, endpoint=False))

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