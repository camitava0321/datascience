# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
Sparse Data
"""
import pandas as pd
import numpy as np

#Sparse objects are “compressed” when any data matching a specific value 
#(NaN / missing value, though any value can be chosen) is omitted. 
#A special SparseIndex object tracks where data has been “sparsified”. 
#This will make much more sense in an example. All of the standard Pandas data structures apply the to_sparse method −
ts = pd.Series(np.random.randn(10))
ts[2:-2] = np.nan
sts = ts.to_sparse()
print sts

#The sparse objects exist for memory efficiency reasons.
#Let us now assume you had a large NA DataFrame and execute the following code −
df = pd.DataFrame(np.random.randn(10000, 4))
df.ix[:9998] = np.nan
sdf = df.to_sparse()
print sdf.density

#Any sparse object can be converted back to the standard dense form by calling to_dense −
ts = pd.Series(np.random.randn(10))
ts[2:-2] = np.nan
sts = ts.to_sparse()
print sts.to_dense()

#Sparse Dtypes
#Sparse data should have the same dtype as its dense representation. 
#Currently, float64, int64 and booldtypes are supported. Depending on the original dtype, fill_value default changes −
#float64 − np.nan
#int64 − 0
#bool − False
#Let us execute the following code to understand the same −
s = pd.Series([1, np.nan, np.nan])
print s
s.to_sparse()
print s