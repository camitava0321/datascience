# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
Statistical Functions
"""
import pandas as pd
import numpy as np

#Statistical methods help in the understanding and analyzing the behavior of data. 

#Percent_change
#Series, DatFrames and Panel, all have the function pct_change(). 
#This function compares every element with its prior element and computes the change percentage.
s = pd.Series([1,2,3,4,5,4])
print s.pct_change()

df = pd.DataFrame(np.random.randn(5, 2))
print df.pct_change()

#By default, the pct_change() operates on columns; 
#if you want to apply the same row wise, then use axis=1() argument.

#Covariance
#Covariance is applied on series data. 
#The Series object has a method cov to compute covariance between series objects. NA will be excluded automatically.
s1 = pd.Series(np.random.randn(10))
s2 = pd.Series(np.random.randn(10))
print s1.cov(s2)

#Covariance method when applied on a DataFrame, computes cov between all the columns.
frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
print frame['a'].cov(frame['b'])
print frame.cov()
#Observe the cov between a and b column in the first statement and the same is the value returned by cov on DataFrame.

#Correlation
#Correlation shows the linear relationship between any two array of values (series). 
#There are multiple methods to compute the correlation like pearson(default), spearman and kendall.
frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
print frame['a'].corr(frame['b'])
print frame.corr()
#If any non-numeric column is present in the DataFrame, it is excluded automatically.

#Data Ranking
#Data Ranking produces ranking for each element in the array of elements. In case of ties, assigns the mean rank.
s = pd.Series(np.random.np.random.randn(5), index=list('abcde'))
s['d'] = s['b'] # so there's a tie
print s.rank()
#Rank optionally takes a parameter ascending which by default is true; 
#when false, data is reverse-ranked, with larger values assigned a smaller rank.
#Rank supports different tie-breaking methods, specified with the method parameter −
#average − average rank of tied group
#min − lowest rank in the group
#max − highest rank in the group
#first − ranks assigned in the order they appear in the array