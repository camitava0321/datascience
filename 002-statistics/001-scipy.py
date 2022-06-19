# -*- coding: utf-8 -*-
#author : Amitava Chakraborty

#basic statistical functions - Numpy
#the real repository for statistical functions is scipy.stats. 
#> 80 continuous probability distributions implemented in scipy.stats
#> 10 discrete distributions, along with many other supplementary statistical functions

import scipy.stats # might take awhile
n = scipy.stats.norm(0,10) # create normal distrib

#The n variable is an object that represents a normally distributed random variable
#with mean zero and standard deviation, σ = 10. 
#more general term for these two parameters is location and scale, respectively. 
#Now that we have this defined, we can compute mean
n.mean()

#higher order moments as
n.moment(4)

#The main public methods for continuous random variables are
#1 - rvs: random variates
#One can create samples from this distribution
array = n.rvs(10)
print (array)
    
#2 - pdf: probability density function
#value of the pdf at a specific point.
n.pdf(0)

#3 - cdf: cumulative distribution function
#value of the cdf at a specific point.
n.cdf(0)

#4 - sf: survival Function (1-CDF)
#5 - ppf: percent point function (Inverse of CDF)
#6 - isf: inverse survival function (Inverse of SF)
#7 - stats: mean, variance, (Fisher’s) skew, or (Fisher’s) kurtosis
#8 - moment: non-central moments of the distribution

#Many common statistical tests are already built-in. 
#For example, Shapiro-Wilks tests the null hypothesis that 
#the data were drawn from a normal distribution
print (scipy.stats.shapiro(n.rvs(100)))
#The second value in the tuple is the p-value.

#%% - Convergence
#Almost Sure Convergence 
#we get random values corresponding to a uniform distribution 
from scipy import stats
u=stats.uniform()
xn = lambda i: u.rvs(i).max()
xn(5)

#xn is same as the X(n) random variable
#we estimate the probability for n = 60 over 1000 realizations,
import numpy as np
np.mean([xn(60) > 0.95 for i in range(1000)])

np.mean([xn(90) > 0.95 for i in range(1000)])

#%% - Convergence in Probability
#Example : Let {X1, X2, X3, . . .} be the indicators of the corresponding intervals,
#(0, 1], (0, 1/2], (1/2 , 1], (0, 1/3], (1/3, 2/3], (2/3 , 1]
#i.e., keep splitting the unit interval into equal chunks and enumerate those chunks with Xi. 
#Because each Xi is an indicator function, it takes only two values: zero and one. 
#For example, 
#for X2 = 1 if 0 < x ≤ 1/2 and 0 otherwise. so P(X2 = 1) = 1/2. 
#The following is a function to compute the different subintervals
make_interval= lambda n: np.array(zip(range(n+1),range(1,n+1)))/n

#Now, we can use this function to create a Numpy array of intervals
intervals= np.vstack([make_interval(i) for i in range(1,5)])
print (intervals)

#%% - Simulate coin flipping.
from scipy.stats import bernoulli
p_true=1/2.0 # estimate this!
fp=bernoulli(p_true) # create bernoulli random variate
xs = fp.rvs(100) # generate some samples
print (xs[:30]) # see first 30 samples

#Now, we write out the likelihood function using Sympy. 
#Note that we give the Sympy variables the positive=True attribute upon construction 
#because this eases Sympy’s internal simplification algorithms.
import sympy
x,p,z=sympy.symbols('x p z', positive=True)
phi=p**x*(1-p)**(1-x) # distribution function
print (phi)
L=np.prod([phi.subs(x,i) for i in xs]) # likelihood function
print (L) # approx 0.5?
