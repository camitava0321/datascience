# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
pandas Cookbook
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.mpl_style', 'default')
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'

#pandas is really good at dealing with dates and with strings! 
#we read the weather data
gdp = pd.read_csv('gdp.csv', parse_dates=True, index_col='date')
gdp[:5]

price_index = gdp['producer_price_index']
is_more = price_index > 200
#is_more is a binary vector

#6.2 Use resampling to find the snowiest month
#If we wanted the median temperature each month, we could use the resample() method like this:
gdp['total_expenditures'].resample('M', how=np.median).plot(kind='bar')

#So we can think of snowiness as being a bunch of 1s and 0s instead of Trues and Falses:
is_more.astype(float)[:10]

#and then use resample to find the percentage of time it was more than 200
is_more.astype(float).resample('M', how=np.mean)
is_more.astype(float).resample('M', how=np.mean).plot(kind='bar')
