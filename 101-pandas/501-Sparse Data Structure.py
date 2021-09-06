# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
"""
"""
Sparse data structures
"""
import numpy as np
import pandas as pd
#%% - “sparse” versions of Series and DataFrame. 
#These are not sparse in the typical “mostly 0”. 
#Rather, you can view these objects as being “compressed” 
#where any data matching a specific value (NaN / missing value, though any value can be chosen) is omitted. 
#A special SparseIndex object tracks where data has been “sparsified”. 
#All of the standard pandas data structures have a to_sparse method:

ts = pd.Series(np.random.randn(10))
ts[2:-2] = np.nan
sts = ts.to_sparse()
sts

#%% - The to_sparse method takes a kind argument (for the sparse index, see below) and a fill_value. 
#So if we had a mostly zero Series, we could convert it to sparse with fill_value=0:
ts.fillna(0).to_sparse(fill_value=0)

#%% - The sparse objects exist for memory efficiency reasons. Suppose you had a large, mostly NA DataFrame:
df = pd.DataFrame(np.random.randn(10000, 4))
df.iloc[:9998] = np.nan
sdf = df.to_sparse()
sdf
sdf.density

#As you can see, the density (% of values that have not been “compressed”) is extremely low. 
#This sparse object takes up much less memory on disk (pickled) and in the Python interpreter. 
#Functionally, their behavior should be nearly identical to their dense counterparts.

#%% - Any sparse object can be converted back to the standard dense form by calling to_dense:
sts.to_dense()

#%% - SparseArray is the base layer for all of the sparse indexed data structures. 
#It is a 1-dimensional ndarray-like object storing only values distinct from the fill_value:
arr = np.random.randn(10)
arr[2:5] = np.nan; arr[7:8] = np.nan
sparr = pd.SparseArray(arr)
sparr

#%% - Like the indexed objects (SparseSeries, SparseDataFrame), 
#a SparseArray can be converted back to a regular ndarray by calling to_dense:
sparr.to_dense()

#%% - SparseIndex objects
#Two kinds of SparseIndex are implemented, block and integer. 
#block is recommended as it’s more memory efficient. 
#The integer format keeps an arrays of all of the locations where the data are not equal to the fill value. 
#The block format tracks only the locations and sizes of blocks of data.

#Sparse Dtypes
#Sparse data should have the same dtype as its dense representation. 
#Currently, float64, int64 and bool dtypes are supported. Depending on the original dtype, fill_value default changes:
#float64: np.nan
#int64: 0
#bool: False
s = pd.Series([1, np.nan, np.nan])
s
s.to_sparse()

s = pd.Series([1, 0, 0])
s
s.to_sparse()

s = pd.Series([True, False, True])
s
s.to_sparse()

#You can change the dtype using .astype(), the result is also sparse. 
#Note that .astype() also affects to the fill_value to keep its dense representation.
s = pd.Series([1, 0, 0, 0, 0])
s

ss = s.to_sparse()
ss

ss.astype(np.float64)

#It raises if any value cannot be coerced to specified dtype.
ss = pd.Series([1, np.nan, np.nan]).to_sparse()
ss.astype(np.int64)

#%% - Sparse Calculation
#One can apply NumPy ufuncs to SparseArray and get a SparseArray as a result.
arr = pd.SparseArray([1., np.nan, np.nan, -2., np.nan])
np.abs(arr)

#The ufunc is also applied to fill_value. This is needed to get the correct dense result.
arr = pd.SparseArray([1., -1, -1, -2., -1], fill_value=-1)
np.abs(arr)

np.abs(arr).to_dense()

#%% - Interaction with scipy.sparse
#SparseDataFrame - New in version 0.20.0.
#Pandas supports creating sparse dataframes directly from scipy.sparse matrices.
from scipy.sparse import csr_matrix
arr = np.random.random(size=(1000, 5))
arr[arr < .9] = 0
sp_arr = csr_matrix(arr)
sp_arr

sdf = pd.SparseDataFrame(sp_arr)
sdf

#All sparse formats are supported, 
#but matrices that are not in COOrdinate format will be converted, copying data as needed. 
#To convert a SparseDataFrame back to sparse SciPy matrix in COO format, you can use the SparseDataFrame.to_coo() method:
sdf.to_coo()

#%% - SparseSeries
#A SparseSeries.to_coo() method is implemented for transforming a SparseSeries indexed by a MultiIndex to a scipy.sparse.coo_matrix.
#The method requires a MultiIndex with two or more levels.
s = pd.Series([3.0, np.nan, 1.0, 3.0, np.nan, np.nan])
s.index = pd.MultiIndex.from_tuples([(1, 2, 'a', 0),
                                     (1, 2, 'a', 1),
                                     (1, 1, 'b', 0),
                                     (1, 1, 'b', 1),
                                     (2, 1, 'b', 0),
                                     (2, 1, 'b', 1)],
                                     names=['A', 'B', 'C', 'D'])


s
# SparseSeries
ss = s.to_sparse()
ss

#Now we transform the SparseSeries to a sparse representation of a 2-d array 
#by specifying that the first and second MultiIndex levels define labels for the rows and 
#the third and fourth levels define labels for the columns. 
#We also specify that the column and row labels should be sorted in the final sparse representation.
A, rows, columns = ss.to_coo(row_levels=['A', 'B'],
                              column_levels=['C', 'D'],
                              sort_labels=True)
 

A

A.todense()

rows

columns

#Specifying different row and column labels (and not sorting them) yields a different sparse matrix:
A, rows, columns = ss.to_coo(row_levels=['A', 'B', 'C'],
                              column_levels=['D'],
                              sort_labels=False)
 
A

A.todense()

rows

columns

#A convenience method SparseSeries.from_coo() is implemented for creating a SparseSeries from a scipy.sparse.coo_matrix.
from scipy import sparse
A = sparse.coo_matrix(([3.0, 1.0, 2.0], ([1, 0, 0], [0, 2, 3])),
                       shape=(3, 4))
 
A

A.todense()

#The default behaviour (with dense_index=False) simply returns a SparseSeries containing only the non-null entries.
ss = pd.SparseSeries.from_coo(A)
ss

#Specifying dense_index=True will result in an index that is the Cartesian product of the row and columns coordinates of the matrix. 
#Note that this will consume a significant amount of memory (relative to dense_index=False) 
#if the sparse matrix is large (and sparse) enough.
ss_dense = pd.SparseSeries.from_coo(A, dense_index=True)
ss_dense