# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 15:18:19 2017

@author: Amitava
Minimal Examples
"""
#statsmodels is a Python module that provides classes and functions 
#for the estimation of many different statistical models, 
#as well as for conducting statistical tests, and 
#statistical data exploration. 
#An extensive list of result statistics are available for each estimator. 
#The results are tested against existing statistical packages to ensure that they are correct. 
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Load data
dat = sm.datasets.get_rdataset("Guerry", "HistData").data

# Fit regression model (using the natural log of one of the regressors)
results = smf.ols('Lottery ~ Literacy + np.log(Pop1831)', data=dat).fit()

# Inspect the results
print(results.summary())
#Warnings:
#Standard Errors assume that the covariance matrix of the errors is correctly specified.

#You can also use numpy arrays instead of formulas:

# Generate artificial data (2 regressors + constant)
nobs = 100
X = np.random.random((nobs, 2))
X = sm.add_constant(X)
beta = [1, .1, .5]
e = np.random.random(nobs)
y = np.dot(X, beta) + e

# Fit regression model
results = sm.OLS(y, X).fit()

# Inspect the results
print(results.summary())
#Warnings:
#Standard Errors assume that the covariance matrix of the errors is correctly specified.
