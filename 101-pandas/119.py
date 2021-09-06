# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
Concatenation
"""
Pandas provides various facilities for easily combining together Series, DataFrame, and Panel objects.

 pd.concat(objs,axis=0,join='outer',join_axes=None,
ignore_index=False)

    objs − This is a sequence or mapping of Series, DataFrame, or Panel objects.

    axis − {0, 1, ...}, default 0. This is the axis to concatenate along.

    join − {‘inner’, ‘outer’}, default ‘outer’. How to handle indexes on other axis(es). Outer for union and inner for intersection.

    ignore_index − boolean, default False. If True, do not use the index values on the concatenation axis. The resulting axis will be labeled 0, ..., n - 1.

    join_axes − This is the list of Index objects. Specific indexes to use for the other (n-1) axes instead of performing inner/outer set logic.

Concatenating Objects

The concat function does all of the heavy lifting of performing concatenation operations along an axis. Let us create different objects and do concatenation.

import pandas as pd
one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
print pd.concat([one,two])

Its output is as follows −

    Marks_scored     Name   subject_id
1             98     Alex         sub1
2             90      Amy         sub2
3             87    Allen         sub4
4             69    Alice         sub6
5             78   Ayoung         sub5
1             89    Billy         sub2
2             80    Brian         sub4
3             79     Bran         sub3
4             97    Bryce         sub6
5             88    Betty         sub5

Suppose we wanted to associate specific keys with each of the pieces of the chopped up DataFrame. We can do this by using the keys argument −

import pandas as pd
one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
print pd.concat([one,two],keys=['x','y'])

Its output is as follows −

x  1  98    Alex    sub1
   2  90    Amy     sub2
   3  87    Allen   sub4
   4  69    Alice   sub6
   5  78    Ayoung  sub5
y  1  89    Billy   sub2
   2  80    Brian   sub4
   3  79    Bran    sub3
   4  97    Bryce   sub6
   5  88    Betty   sub5

The index of the resultant is duplicated; each index is repeated.

If the resultant object has to follow its own indexing, set ignore_index to True.

import pandas as pd
one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
print pd.concat([one,two],keys=['x','y'],ignore_index=True)

Its output is as follows −

    Marks_scored     Name    subject_id
0             98     Alex          sub1
1             90      Amy          sub2
2             87    Allen          sub4
3             69    Alice          sub6
4             78   Ayoung          sub5
5             89    Billy          sub2
6             80    Brian          sub4
7             79     Bran          sub3
8             97    Bryce          sub6
9             88    Betty          sub5

Observe, the index changes completely and the Keys are also overridden.

If two objects need to be added along axis=1, then the new columns will be appended.

import pandas as pd
one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
print pd.concat([one,two],axis=1)

Its output is as follows −

    Marks_scored    Name  subject_id   Marks_scored    Name   subject_id
1           98      Alex      sub1         89         Billy         sub2
2           90       Amy      sub2         80         Brian         sub4
3           87     Allen      sub4         79          Bran         sub3
4           69     Alice      sub6         97         Bryce         sub6
5           78    Ayoung      sub5         88         Betty         sub5

Concatenating Using append

A useful shortcut to concat are the append instance methods on Series and DataFrame. These methods actually predated concat. They concatenate along axis=0, namely the index −

import pandas as pd
one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
print one.append(two)

Its output is as follows −

    Marks_scored    Name  subject_id
1           98      Alex      sub1
2           90       Amy      sub2
3           87     Allen      sub4
4           69     Alice      sub6
5           78    Ayoung      sub5
1           89     Billy      sub2
2           80     Brian      sub4
3           79      Bran      sub3
4           97     Bryce      sub6
5           88     Betty      sub5

The append function can take multiple objects as well −

import pandas as pd

one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
            
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
print one.append([two,one,two])

Its output is as follows −

    Marks_scored   Name    subject_id
1           98     Alex          sub1
2           90      Amy          sub2
3           87    Allen          sub4
4           69    Alice          sub6
5           78   Ayoung          sub5
1           89    Billy          sub2
2           80    Brian          sub4
3           79     Bran          sub3
4           97    Bryce          sub6
5           88    Betty          sub5
1           98     Alex          sub1
2           90      Amy          sub2
3           87    Allen          sub4
4           69    Alice          sub6
5           78   Ayoung          sub5
1           89    Billy          sub2
2           80    Brian          sub4
3           79     Bran          sub3
4           97    Bryce          sub6
5           88    Betty          sub5

Time Series

Pandas provide a robust tool for working time with Time series data, especially in the financial sector. While working with time series data, we frequently come across the following −

    Generating sequence of time
    Convert the time series to different frequencies

Pandas provides a relatively compact and self-contained set of tools for performing the above tasks.
Get Current Time

datetime.now() gives you the current date and time.

import pandas as pd
print pd.datetime.now()

Its output is as follows −

2017-05-11 06:10:13.393147

Create a TimeStamp

Time-stamped data is the most basic type of timeseries data that associates values with points in time. For pandas objects, it means using the points in time. Let’s take an example −

import pandas as pd
print pd.Timestamp('2017-03-01')

Its output is as follows −

2017-03-01 00:00:00

It is also possible to convert integer or float epoch times. The default unit for these is nanoseconds (since these are how Timestamps are stored). However, often epochs are stored in another unit which can be specified. Let’s take another example

import pandas as pd
print pd.Timestamp(1587687255,unit='s')

Its output is as follows −

2020-04-24 00:14:15

Create a Range of Time

import pandas as pd

print pd.date_range("11:00", "13:30", freq="30min").time

Its output is as follows −

[datetime.time(11, 0) datetime.time(11, 30) datetime.time(12, 0)
datetime.time(12, 30) datetime.time(13, 0) datetime.time(13, 30)]

Change the Frequency of Time

import pandas as pd

print pd.date_range("11:00", "13:30", freq="H").time

Its output is as follows −

[datetime.time(11, 0) datetime.time(12, 0) datetime.time(13, 0)]

Converting to Timestamps

To convert a Series or list-like object of date-like objects, for example strings, epochs, or a mixture, you can use the to_datetime function. When passed, this returns a Series (with the same index), while a list-like is converted to a DatetimeIndex. Take a look at the following example −

import pandas as pd

print pd.to_datetime(pd.Series(['Jul 31, 2009','2010-01-10', None]))

Its output is as follows −

0  2009-07-31
1  2010-01-10
2         NaT
dtype: datetime64[ns]

NaT means Not a Time (equivalent to NaN)

Let’s take another example.

import pandas as pd
print pd.to_datetime(['2005/11/23', '2010.12.31', None])