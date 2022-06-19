# -*- coding: utf-8 -*-
"""
Scipy Examples
@author: AMITAVA
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import special

"""
#Special functions (scipy.special) - numerous special functions of mathematical physics. 
Available functions include airy, elliptic, bessel, gamma, beta, hypergeometric, 
parabolic cylinder, mathieu, spheroidal wave, struve, and kelvin. 
Most of these functions can take array arguments and return array results 
following the same broadcasting rules as other math functions in Numerical Python. 
Many of these functions also accept complex numbers as input. 
For a complete list of the available functions with a one-line description type 
"""
help(special)

#%% - Functions not in scipy.special
#The binary entropy function:
def binary_entropy(x):
    return -(sc.xlogy(x, x) + sc.xlog1py(1 - x, -x))/np.log(2)

#A rectangular step function on [0, 1]:
def step(x):
    return 0.5*(np.sign(x) + np.sign(1 - x))

#Translating and scaling can be used to get an arbitrary step function.
#The ramp function:
def ramp(x):
    return np.maximum(0, x)
    #to obtain an N-point approximation to the o-th derivative at a given point.