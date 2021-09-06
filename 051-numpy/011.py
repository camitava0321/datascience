# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Correlations
"""

import numpy as nd

a = nd.arange(2)
print "a = ", a
m = nd.array([nd.arange(100), nd.arange(10)])
print "m = ",m

b = nd.arange(1000).reshape(10,100)
print "b = ",b
print b.shape
c = nd.matrix(nd.random.rand(1000,100000))
c=100*c
print "c = ",c
print c.shape

#ravel - Return a contiguous flattened 1-D array, 
#containing the elements of the input (A copy is made only if needed.)
d = b.ravel()
slice1 = d[11:21]
slice2 = d[21:31]
print b.shape
print slice1.shape
print "slice1 = "
print slice1, slice2


corr = nd.correlate(slice1,slice2)
print corr

#Return Pearson product-moment correlation coefficients
corr2 = nd.corrcoef(slice1,slice2)
print corr2

d = c.ravel()
print "d = ",d, d.shape, c.shape
slice1 = d[1:100]
slice2 = d[2001L:3001L]
print "attribute 1 = ",slice1, "attribute2 = ",slice2

e = nd.hsplit(c,100000)
f = e[0:1]
g = e[1:2]
f = nd.squeeze(nd.asarray(f))
g = nd.squeeze(nd.asarray(g))
print "f = ",f
print "g = ",g

corr2 = nd.corrcoef(f,g)
print "Correlation = ",corr2