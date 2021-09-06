# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
Caveats (warnings) & Unseen Problems
"""
import pandas as pd
#Using If/Truth Statement with Pandas
#Pandas follows the numpy convention of raising an error when one tries to convert something to a bool. 
#This happens in an if or when using the Boolean operations, and, or, or not. 
#It is not clear what the result should be. 
#Should it be True because it is not zero-length? 
#False because there are False values? 
#It is unclear, so instead, Pandas raises a ValueError −

if pd.Series([False, True, False]):
   print ('I am True')

#In if condition, it is unclear what to do with it. 
#The error is suggestive of whether to use a None or any of those.

if pd.Series([False, True, False]).any():
   print("I am any")

#To evaluate single-element pandas objects in a Boolean context, use the method .bool() −
print (pd.Series([True]).bool())

#Bitwise Boolean
#Bitwise Boolean operators like == and != will return a Boolean series
s = pd.Series(range(5))
print s==4

#isin Operation
#This returns a Boolean series showing whether each element in the Series is exactly contained in the passed sequence of values.
s = pd.Series(list('abc'))
s = s.isin(['a', 'c', 'e'])
print s

#Reindexing vs ix Gotcha
#Many users will find themselves using the ix indexing capabilities as a concise means of selecting data from a Pandas object −
import numpy as np
df = pd.DataFrame(np.random.randn(6, 4), columns=['one', 'two', 'three', 'four'],index=list('abcdef'))

print df
print df.ix[['b', 'c', 'e']]

df = pd.DataFrame(np.random.randn(6, 4), columns=['one', 'two', 'three', 'four'],index=list('abcdef'))
print df
print df.reindex(['b', 'c', 'e'])

#Some might conclude that ix and reindex are 100% equivalent based on this. 
#This is true except in the case of integer indexing. 
#For example, the above operation can alternatively be expressed as −
df = pd.DataFrame(np.random.randn(6, 4), columns=['one', 'two', 'three','four'],index=list('abcdef'))

print df
print df.ix[[1, 2, 4]]
print df.reindex([1, 2, 4])

#Note: reindex is strict label indexing only. 
#This can lead to some potentially surprising results in pathological cases where an index contains, say, both integers and strings.