# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
Date Functionality
Extending the Time series, Date functionalities play major role in financial data analysis. 
While working with Date data, we will frequently come across the following −
    Generating sequence of dates
    Convert the date series to different frequencies

"""
import pandas as pd
#Create a Range of Dates
#Using the date.range() function by specifying the periods and the frequency, 
#we can create the date series. By default, the frequency of range is Days.
print pd.date_range('1/1/2011', periods=5)

#Change the Date Frequency

print pd.date_range('1/1/2011', periods=5,freq='M')


bdate_range

bdate_range() stands for business date ranges. Unlike date_range(), it excludes Saturday and Sunday.

import pandas as pd
print pd.bdate_range('1/1/2011', periods=5)

Its output is as follows −

DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03', '2011-01-04', '2011-01-05'],
dtype='datetime64[ns]', freq='D')

Observe, after 3rd March, the date jumps to 6th march excluding 4th and 5th. Just check your calendar for the days.

Convenience functions like date_range and bdate_range utilize a variety of frequency aliases. The default frequency for date_range is a calendar day while the default for bdate_range is a business day.

import pandas as pd
start = pd.datetime(2011, 1, 1)
end = pd.datetime(2011, 1, 5)
print pd.date_range(start, end)

Its output is as follows −

DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03', '2011-01-04', '2011-01-05'],
dtype='datetime64[ns]', freq='D')

Offset Aliases

A number of string aliases are given to useful common time series frequencies. We will refer to these aliases as offset aliases.
Alias 	Description 	Alias 	Description
B 	business day frequency 	BQS 	business quarter start frequency
D 	calendar day frequency 	A 	annual(Year) end frequency
W 	weekly frequency 	BA 	business year end frequency
M 	month end frequency 	BAS 	business year start frequency
SM 	semi-month end frequency 	BH 	business hour frequency
BM 	business month end frequency 	H 	hourly frequency
MS 	month start frequency 	T, min 	minutely frequency
SMS 	SMS semi month start frequency 	S 	secondly frequency
BMS 	business month start frequency 	L, ms 	milliseconds
Q 	quarter end frequency 	U, us 	microseconds
BQ 	business quarter end frequency 	N 	nanoseconds
QS 	quarter start frequency 		