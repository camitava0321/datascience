# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
Working with Text Data
"""

In this chapter, we will discuss the string operations with our basic Series/Index. In the subsequent chapters, we will learn how to apply these string functions on the DataFrame.

Pandas provides a set of string functions which make it easy to operate on string data. Most importantly, these functions ignore (or exclude) missing/NaN values.

Almost, all of these methods work with Python string functions (refer: https://docs.python.org/3/library/stdtypes.html#string-methods). So, convert the Series Object to String Object and then perform the operation.

Let us now see how each operation performs.
S.No 	Function 	Description
1 	lower() 	Converts strings in the Series/Index to lower case.
2 	upper() 	Converts strings in the Series/Index to upper case.
3 	len() 	Computes String length().
4 	strip() 	Helps strip whitespace(including newline) from each string in the Series/index from both the sides.
5 	split(' ') 	Splits each string with the given pattern.
6 	cat(sep=' ') 	Concatenates the series/index elements with given separator.
7 	get_dummies() 	Returns the DataFrame with One-Hot Encoded values.
8 	contains(pattern) 	Returns a Boolean value True for each element if the substring contains in the element, else False.
9 	replace(a,b) 	Replaces the value a with the value b.
10 	repeat(value) 	Repeats each element with specified number of times.
11 	count(pattern) 	Returns count of appearance of pattern in each element.
12 	startswith(pattern) 	Returns true if the element in the Series/Index starts with the pattern.
13 	endswith(pattern) 	Returns true if the element in the Series/Index ends with the pattern.
14 	find(pattern) 	Returns the first position of the first occurrence of the pattern.
15 	findall(pattern) 	Returns a list of all occurrence of the pattern.
16 	swapcase 	Swaps the case lower/upper.
17 	islower() 	Checks whether all characters in each string in the Series/Index in lower case or not. Returns Boolean
18 	isupper() 	Checks whether all characters in each string in the Series/Index in upper case or not. Returns Boolean.
19 	isnumeric() 	Checks whether all characters in each string in the Series/Index are numeric. Returns Boolean.

Let us now create a Series and see how all the above functions work.

import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])

print s

Its output is as follows −

0            Tom
1   William Rick
2           John
3        Alber@t
4            NaN
5           1234
6    Steve Smith
dtype: object

lower()

import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])

print s.str.lower()

Its output is as follows −

0            tom
1   william rick
2           john
3        alber@t
4            NaN
5           1234
6    steve smith
dtype: object

upper()

import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])

print s.str.upper()

Its output is as follows −

0            TOM
1   WILLIAM RICK
2           JOHN
3        ALBER@T
4            NaN
5           1234
6    STEVE SMITH
dtype: object

len()

import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])
print s.str.len()

Its output is as follows −

0    3.0
1   12.0
2    4.0
3    7.0
4    NaN
5    4.0
6   10.0
dtype: float64

strip()

import pandas as pd
import numpy as np
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print s
print ("After Stripping:")
print s.str.strip()

Its output is as follows −

0            Tom
1   William Rick
2           John
3        Alber@t
dtype: object

After Stripping:
0            Tom
1   William Rick
2           John
3        Alber@t
dtype: object

split(pattern)

import pandas as pd
import numpy as np
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print s
print ("Split Pattern:")
print s.str.split(' ')

Its output is as follows −

0            Tom
1   William Rick
2           John
3        Alber@t
dtype: object

Split Pattern:
0   [Tom, , , , , , , , , , ]
1   [, , , , , William, Rick]
2   [John]
3   [Alber@t]
dtype: object

cat(sep=pattern)

import pandas as pd
import numpy as np

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print s.str.cat(sep='_')

Its output is as follows −

Tom _ William Rick_John_Alber@t

get_dummies()

import pandas as pd
import numpy as np

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print s.str.get_dummies()

Its output is as follows −

   William Rick   Alber@t   John   Tom
0             0         0      0     1
1             1         0      0     0
2             0         0      1     0
3             0         1      0     0

contains ()

import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print s.str.contains(' ')

Its output is as follows −

0   True
1   True
2   False
3   False
dtype: bool

replace(a,b)

import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print s
print ("After replacing @ with $:")
print s.str.replace('@','$')

Its output is as follows −

0   Tom
1   William Rick
2   John
3   Alber@t
dtype: object

After replacing @ with $:
0   Tom
1   William Rick
2   John
3   Alber$t
dtype: object

repeat(value)

import pandas as pd

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print s.str.repeat(2)

Its output is as follows −

0   Tom            Tom
1   William Rick   William Rick
2                  JohnJohn
3                  Alber@tAlber@t
dtype: object

count(pattern)

import pandas as pd
 
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print ("The number of 'm's in each string:")
print s.str.count('m')

Its output is as follows −

The number of 'm's in each string:
0    1
1    1
2    0
3    0

startswith(pattern)

import pandas as pd

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print ("Strings that start with 'T':")
print s.str. startswith ('T')

Its output is as follows −

0  True
1  False
2  False
3  False
dtype: bool

endswith(pattern)

import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print ("Strings that end with 't':")
print s.str.endswith('t')

Its output is as follows −

Strings that end with 't':
0  False
1  False
2  False
3  True
dtype: bool

find(pattern)

import pandas as pd

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print s.str.find('e')

Its output is as follows −

0  -1
1  -1
2  -1
3   3
dtype: int64

"-1" indicates that there no such pattern available in the element.
findall(pattern)

import pandas as pd

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print s.str.findall('e')

Its output is as follows −

0 []
1 []
2 []
3 [e]
dtype: object

Null list([ ]) indicates that there is no such pattern available in the element.
swapcase()

import pandas as pd

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])
print s.str.swapcase()

Its output is as follows −

0  tOM
1  wILLIAM rICK
2  jOHN
3  aLBER@T
dtype: object

islower()

import pandas as pd

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])
print s.str.islower()

Its output is as follows −

0  False
1  False
2  False
3  False
dtype: bool

isupper()

import pandas as pd

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])

print s.str.isupper()

Its output is as follows −

0  False
1  False
2  False
3  False
dtype: bool

isnumeric()

import pandas as pd

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])

print s.str.isnumeric()