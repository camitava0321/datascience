# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
Timedelta
"""
#Timedeltas are differences in times, expressed in difference units, 
#for example, days, hours, minutes, seconds. They can be both positive and negative.

#We can create Timedelta objects using various arguments as shown below −
#String - By passing a string literal
import pandas as pd
print pd.Timedelta('2 days 2 hours 15 minutes 30 seconds')

#Integer - By passing an integer value with the unit, an argument creates a Timedelta object.
print pd.Timedelta(6,unit='h')

#Data Offsets - Data offsets such as - weeks, days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds can also be used in construction.

import pandas as pd

print pd.Timedelta(days=2)

Its output is as follows −

2 days 00:00:00

to_timedelta()

Using the top-level pd.to_timedelta, you can convert a scalar, array, list, or series from a recognized timedelta format/ value into a Timedelta type. It will construct Series if the input is a Series, a scalar if the input is scalar-like, otherwise will output a TimedeltaIndex.

import pandas as pd

print pd.Timedelta(days=2)

Its output is as follows −

2 days 00:00:00

Operations

You can operate on Series/ DataFrames and construct timedelta64[ns] Series through subtraction operations on datetime64[ns] Series, or Timestamps.

Let us now create a DataFrame with Timedelta and datetime objects and perform some arithmetic operations on it −

import pandas as pd

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))
print df

Its output is as follows −

            A      B
0  2012-01-01 0 days
1  2012-01-02 1 days
2  2012-01-03 2 days

Addition Operations

import pandas as pd

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))
df['C']=df['A']+df['B']

print df

Its output is as follows −

           A      B          C
0 2012-01-01 0 days 2012-01-01
1 2012-01-02 1 days 2012-01-03
2 2012-01-03 2 days 2012-01-05

Subtraction Operation

import pandas as pd

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))
df['C']=df['A']+df['B']
df['D']=df['C']+df['B']
print df