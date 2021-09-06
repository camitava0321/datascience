# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
"""
"""
pandas Cookbook
"""
import pandas as pd
#Parsing Unix timestamps
#It's not obvious how to deal with Unix timestamps in pandas -- 
#it took me quite a while to figure this out. 
#The file we're using here is a popularity-contest file I found on my system at /var/log/popularity-contest.

# Read it, and remove the last row
popcon = pd.read_csv('datetime.csv')
popcon.columns = ['fromtime', 'totime', 'package-name', 'mru-program', 'tag']
#The colums are the access time, created time, package name, recently used program, and a tag
popcon
popcon[:5]

#numpy datetimes are already stored as Unix timestamps. 
#So all we need to do is tell pandas that these integers are actually datetimes -- 
#it doesn't need to do any conversion at all.

#We convert these to ints to start:
popcon['atime'] = popcon['atime'].astype(int)
popcon['ctime'] = popcon['ctime'].astype(int)

#Every numpy array and pandas series has a dtype -- 
#this is usually int64, float64, or object. 
#Some of the time types available are datetime64[s], datetime64[ms], and datetime64[us]. 
#There are also timedelta types, similarly.

#We can use the pd.to_datetime function to convert our integer timestamps into datetimes. 
#This is a constant-time operation -- we're not actually changing any of the data, just how pandas thinks about it.
popcon['atime'] = pd.to_datetime(popcon['atime'], unit='s')
popcon['ctime'] = pd.to_datetime(popcon['ctime'], unit='s')

#If we look at the dtype now, it's <M8[ns]. 
#As far as I can tell M8 is secret code for datetime64.
popcon['atime'].dtype

#So now we can look at our atime and ctime as dates!
popcon[:5]

#Now suppose we want to look at all packages that aren't libraries.
#First, I want to get rid of everything with timestamp 0. 
#Notice how we can just use a string in this comparison, even though it's actually a timestamp on the inside? 
popcon = popcon[popcon['atime'] > '1970-01-01']
#Now we can use pandas' string abilities to just look at rows where the package name doesn't contain 'lib'.
nonlibraries = popcon[~popcon['package-name'].str.contains('lib')]
nonlibraries
#So if one have a timestamp in seconds or milliseconds or nanoseconds, 
#then they can just be "cast"ed to a 'datetime64' and pandas/numpy will take care of the rest.