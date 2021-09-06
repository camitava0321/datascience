# -*- coding: utf-8 -*-
"""
Created on Mar 13 00:50:08 2017
@author: Amitava
Time Series / Date functionality
"""
#%% - imports
import pandas as pd
import numpy as np

"""
With time series data, we will frequently need to:
  generate sequences of fixed-frequency dates and time spans
  conform or convert time series to a particular frequency
  compute “relative” dates based on various non-standard time increments 
  (e.g. 5 business days before the last business day of the year), or 
  “roll” dates forward or backward

Create a range of dates:
"""

#%% - 72 hours starting with midnight Jan 1st, 2017
rng = pd.date_range('1/1/2017', periods=72, freq='H')
print rng[:5]

#%% Index pandas objects with dates:
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print ts.head()

#%% - Change frequency and fill gaps:
#to 45 minute frequency and forward fill
converted = ts.asfreq('45Min', method='pad')
print converted.head()

#%% -Resample:
# Daily means
print ts.resample('D').mean()
