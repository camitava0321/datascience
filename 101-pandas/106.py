# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
Function Application
"""
import pandas as pd
import numpy as np
"""
To apply your own or another library’s functions to Pandas objects, you should be aware of the three important methods. 
    Table wise Function Application: pipe()
    Row or Column Wise Function Application: apply()
    Element wise Function Application: applymap()
The appropriate method to use depends on whether your function expects to operate 
on an entire DataFrame, row- or column-wise, or element wise.
"""
#%% - Table-wise Function Application
#Custom operations can be performed by passing the function and 
#the appropriate number of parameters as pipe arguments. 
#Thus, operation is performed on the whole DataFrame.

#For example, add a value 2 to all the elements in the DataFrame. Then,
#adder function
#The adder function adds two numeric values as parameters and returns the sum.
def adder(ele1,ele2):
    return ele1+ele2

#Let us now use the custom function to conduct operation on the DataFrame.
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.pipe(adder,2)
print df.apply(np.mean)

#%% - Row or Column Wise Function Application
#Arbitrary functions can be applied along the axes of a DataFrame or Panel 
#using the apply() method, which, 
#like the descriptive statistics methods, takes an optional axis argument. 
#By default, the operation performs column wise, taking each column as an array-like.

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(np.mean)
print df.apply(np.mean)

#By passing axis parameter, operations can be performed row wise.
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(np.mean,axis=1)
print df.apply(np.mean)

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(lambda x: x.max() - x.min())
print df.apply(np.mean)

#%% - Element Wise Function Application
#Not all functions can be vectorized (neither the NumPy arrays which return another array nor any value), 
#the methods applymap() on DataFrame and analogously map() on Series 
#accept any Python function taking a single value and returning a single value.

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
# My custom function
df['col1'].map(lambda x:x*100)
print df.apply(np.mean)