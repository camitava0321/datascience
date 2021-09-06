# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
Iteration
"""

The behavior of basic iteration over Pandas objects depends on the type. When iterating over a Series, it is regarded as array-like, and basic iteration produces the values. Other data structures, like DataFrame and Panel, follow the dict-like convention of iterating over the keys of the objects.

In short, basic iteration (for i in object) produces −

    Series − values

    DataFrame − column labels

    Panel − item labels

Iterating a DataFrame

Iterating a DataFrame gives column names. Let us consider the following example to understand the same.

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

for col in df:
   print col

Its output is as follows −

A
C
D
x
y

To iterate over the rows of the DataFrame, we can use the following functions −

    iteritems() − to iterate over the (key,value) pairs

    iterrows() − iterate over the rows as (index,series) pairs

    itertuples() − iterate over the rows as namedtuples

iteritems()

Iterates over each column as key, value pair with label as key and column value as a Series object.

import pandas as pd
import numpy as np
 
df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
for key,value in df.iteritems():
   print key,value

Its output is as follows −

col1 0    0.802390
1    0.324060
2    0.256811
3    0.839186
Name: col1, dtype: float64

col2 0    1.624313
1   -1.033582
2    1.796663
3    1.856277
Name: col2, dtype: float64

col3 0   -0.022142
1   -0.230820
2    1.160691
3   -0.830279
Name: col3, dtype: float64

Observe, each column is iterated separately as a key-value pair in a Series.
iterrows()

iterrows() returns the iterator yielding each index value along with a series containing the data in each row.

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])
for row_index,row in df.iterrows():
   print row_index,row

Its output is as follows −

0  col1    1.529759
   col2    0.762811
   col3   -0.634691
Name: 0, dtype: float64

1  col1   -0.944087
   col2    1.420919
   col3   -0.507895
Name: 1, dtype: float64
 
2  col1   -0.077287
   col2   -0.858556
   col3   -0.663385
Name: 2, dtype: float64
3  col1    -1.638578
   col2     0.059866
   col3     0.493482
Name: 3, dtype: float64

Note − Because iterrows() iterate over the rows, it doesn't preserve the data type across the row. 0,1,2 are the row indices and col1,col2,col3 are column indices.
itertuples()

itertuples() method will return an iterator yielding a named tuple for each row in the DataFrame. The first element of the tuple will be the row’s corresponding index value, while the remaining values are the row values.

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])
for row in df.itertuples():
    print row

Its output is as follows −

Pandas(Index=0, col1=1.5297586201375899, col2=0.76281127433814944, col3=-
0.6346908238310438)

Pandas(Index=1, col1=-0.94408735763808649, col2=1.4209186418359423, col3=-
0.50789517967096232)

Pandas(Index=2, col1=-0.07728664756791935, col2=-0.85855574139699076, col3=-
0.6633852507207626)

Pandas(Index=3, col1=0.65734942534106289, col2=-0.95057710432604969,
col3=0.80344487462316527)

Note − Do not try to modify any object while iterating. Iterating is meant for reading and the iterator returns a copy of the original object (a view), thus the changes will not reflect on the original object.

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])

for index, row in df.iterrows():
   row['a'] = 10
print df
