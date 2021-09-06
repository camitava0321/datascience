# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
Indexing and Selecting Data
"""

In this chapter, we will discuss how to slice and dice the date and generally get the subset of pandas object.

The Python and NumPy indexing operators "[ ]" and attribute operator "." provide quick and easy access to Pandas data structures across a wide range of use cases. However, since the type of the data to be accessed isn’t known in advance, directly using standard operators has some optimization limits. For production code, we recommend that you take advantage of the optimized pandas data access methods explained in this chapter.

Pandas now supports three types of Multi-axes indexing; the three types are mentioned in the following table −
Indexing 	Description
.loc() 	Label based
.iloc() 	Integer based
.ix() 	Both Label and Integer based
.loc()

Pandas provide various methods to have purely label based indexing. When slicing, the start bound is also included. Integers are valid labels, but they refer to the label and not the position.

.loc() has multiple access methods like −

    A single scalar label
    A list of labels
    A slice object
    A Boolean array

loc takes two single/list/range operator separated by ','. The first one indicates the row and the second one indicates columns.
Example 1

#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

#select all rows for a specific column
print df.loc[:,'A']

Its output is as follows −

a   0.391548
b  -0.070649
c  -0.317212
d  -2.162406
e   2.202797
f   0.613709
g   1.050559
h   1.122680
Name: A, dtype: float64

Example 2

# import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# Select all rows for multiple columns, say list[]
print df.loc[:,['A','C']]

Its output is as follows −

            A           C
a    0.391548    0.745623
b   -0.070649    1.620406
c   -0.317212    1.448365
d   -2.162406   -0.873557
e    2.202797    0.528067
f    0.613709    0.286414
g    1.050559    0.216526
h    1.122680   -1.621420

Example 3

# import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# Select few rows for multiple columns, say list[]
print df.loc[['a','b','f','h'],['A','C']]

Its output is as follows −

           A          C
a   0.391548   0.745623
b  -0.070649   1.620406
f   0.613709   0.286414
h   1.122680  -1.621420

Example 4

# import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# Select range of rows for all columns
print df.loc['a':'h']

Its output is as follows −

            A           B          C          D
a    0.391548   -0.224297   0.745623   0.054301
b   -0.070649   -0.880130   1.620406   1.419743
c   -0.317212   -1.929698   1.448365   0.616899
d   -2.162406    0.614256  -0.873557   1.093958
e    2.202797   -2.315915   0.528067   0.612482
f    0.613709   -0.157674   0.286414  -0.500517
g    1.050559   -2.272099   0.216526   0.928449
h    1.122680    0.324368  -1.621420  -0.741470

Example 5

# import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# for getting values with a boolean array
print df.loc['a']>0

Its output is as follows −

A  False
B  True
C  False
D  False
Name: a, dtype: bool

.iloc()

Pandas provide various methods in order to get purely integer based indexing. Like python and numpy, these are 0-based indexing.

The various access methods are as follows −

    An Integer
    A list of integers
    A range of values

Example 1

# import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# select all rows for a specific column
print df.iloc[:4]

Its output is as follows −

           A          B           C           D
0   0.699435   0.256239   -1.270702   -0.645195
1  -0.685354   0.890791   -0.813012    0.631615
2  -0.783192  -0.531378    0.025070    0.230806
3   0.539042  -1.284314    0.826977   -0.026251

Example 2

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# Integer slicing
print df.iloc[:4]
print df.iloc[1:5, 2:4]

Its output is as follows −

           A          B           C           D
0   0.699435   0.256239   -1.270702   -0.645195
1  -0.685354   0.890791   -0.813012    0.631615
2  -0.783192  -0.531378    0.025070    0.230806
3   0.539042  -1.284314    0.826977   -0.026251

           C          D
1  -0.813012   0.631615
2   0.025070   0.230806
3   0.826977  -0.026251
4   1.423332   1.130568

Example 3

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# Slicing through list of values
print df.iloc[[1, 3, 5], [1, 3]]
print df.iloc[1:3, :]
print df.iloc[:,1:3]

Its output is as follows −

           B           D
1   0.890791    0.631615
3  -1.284314   -0.026251
5  -0.512888   -0.518930

           A           B           C           D
1  -0.685354    0.890791   -0.813012    0.631615
2  -0.783192   -0.531378    0.025070    0.230806

           B           C
0   0.256239   -1.270702
1   0.890791   -0.813012
2  -0.531378    0.025070
3  -1.284314    0.826977
4  -0.460729    1.423332
5  -0.512888    0.581409
6  -1.204853    0.098060
7  -0.947857    0.641358

.ix()

Besides pure label based and integer based, Pandas provides a hybrid method for selections and subsetting the object using the .ix() operator.
Example 1

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# Integer slicing
print df.ix[:4]

Its output is as follows −

           A          B           C           D
0   0.699435   0.256239   -1.270702   -0.645195
1  -0.685354   0.890791   -0.813012    0.631615
2  -0.783192  -0.531378    0.025070    0.230806
3   0.539042  -1.284314    0.826977   -0.026251

Example 2

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
# Index slicing
print df.ix[:,'A']

Its output is as follows −

0   0.699435
1  -0.685354
2  -0.783192
3   0.539042
4  -1.044209
5  -1.415411
6   1.062095
7   0.994204
Name: A, dtype: float64

Use of Notations

Getting values from the Pandas object with Multi-axes indexing uses the following notation −
Object 	Indexers 	Return Type
Series 	s.loc[indexer] 	Scalar value
DataFrame 	df.loc[row_index,col_index] 	Series object
Panel 	p.loc[item_index,major_index, minor_index] 	p.loc[item_index,major_index, minor_index]

Note − .iloc() & .ix() applies the same indexing options and Return value.

Let us now see how each operation can be performed on the DataFrame object. We will use the basic indexing operator '[ ]' −
Example 1

import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
print df['A']

Its output is as follows −

0  -0.478893
1   0.391931
2   0.336825
3  -1.055102
4  -0.165218
5  -0.328641
6   0.567721
7  -0.759399
Name: A, dtype: float64

Note − We can pass a list of values to [ ] to select those columns.
Example 2

import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

print df[['A','B']]

Its output is as follows −

           A           B
0  -0.478893   -0.606311
1   0.391931   -0.949025
2   0.336825    0.093717
3  -1.055102   -0.012944
4  -0.165218    1.550310
5  -0.328641   -0.226363
6   0.567721   -0.312585
7  -0.759399   -0.372696

Example 3

import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
print df[2:2]

Its output is as follows −

Columns: [A, B, C, D]
Index: []

Attribute Access

Columns can be selected using the attribute operator '.'.
Example

import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

print df.A