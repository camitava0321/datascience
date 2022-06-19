# -*- coding: utf-8 -*-
#author : Amitava Chakraborty

#Sympy has much smaller still extremely useful statistics module
#enables symbolic manipulation of statistical quantities
from sympy import stats

X = stats.Normal('x',0,10) # create normal random variable

#Obtain the probability density function in equation form
from sympy.abc import x
stats.density(X)(x)

#Evaluate the cumulative density function as the following,
stats.cdf(X)(0)

#Note that you can evaluate this numerically by using the evalf() method on the output. 
#Sympy provides intuitive ways to consider standard probability questions 
#by using the stats.P function
stats.P(X>0) # prob X >0?

#There is a corresponding expectation function, stats.E 
#one can use to compute complicated expectations using all of Sympy’s powerful built-in integration machinery
#we can compute, E(√|X|) in the following,
stats.E(abs(X)**(1/2)).evalf()