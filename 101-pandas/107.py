# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
Reindexing 
"""
#changes the row labels and column labels of a DataFrame. 
#To reindex means to conform the data to match a given set of labels along a particular axis.

#Multiple operations can be accomplished through indexing like −
#    Reorder the existing data to match a new set of labels.
#    Insert missing value (NA) markers in label locations where no data for the label existed.
import pandas as pd
import numpy as np

N=20
df = pd.DataFrame({
   'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   'x': np.linspace(0,stop=N-1,num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
})

#reindex the DataFrame
df_reindexed = df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])

print df_reindexed

#Reindex to Align with Other Objects
#One may wish to take an object and reindex its axes to be labeled the same as another object. 
df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])

df1 = df1.reindex_like(df2)
print df1

#Note: df1 DataFrame is altered and reindexed like df2. 
#The column names should be matched or else NAN will be added for the entire column label.

#Filling while ReIndexing
#reindex() takes an optional parameter method which is a filling method with values as follows −
#    pad/ffill − Fill values forward
#    bfill/backfill − Fill values backward
#    nearest − Fill from the nearest index values
df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])

# Padding NAN's
print df2.reindex_like(df1)

# Now Fill the NAN's with preceding Values
print ("Data Frame with Forward Fill:")
print df2.reindex_like(df1,method='ffill')

#Note: The last four rows are padded.

#Limits on Filling while Reindexing
#The limit argument provides additional control over filling while reindexing. 
#Limit specifies the maximum count of consecutive matches. 
df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])

# Padding NAN's
print df2.reindex_like(df1)

# Now Fill the NAN's with preceding Values
print ("Data Frame with Forward Fill limiting to 1:")
print df2.reindex_like(df1,method='ffill',limit=1)

#Note: only the 7th row is filled by the preceding 6th row. 
#Then, the rows are left as they are.

#Renaming
#The rename() method allows you to relabel an axis based on some mapping 
#(a dict or Series) or an arbitrary function.

df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
print df1

print ("After renaming the rows and columns:")
print df1.rename(columns={'col1' : 'c1', 'col2' : 'c2'},
index = {0 : 'apple', 1 : 'banana', 2 : 'durian'})

#The rename() method provides an inplace named parameter, 
#which by default is False and copies the underlying data. Pass inplace=True to rename the data in place.