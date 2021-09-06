# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Sunspot data
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
#annual sunspot data from http://www.quandl.com/SIDC/SUNSPOTS_A-Sunspot-Numbers-Annual
#from Belgian Solar Influences Data Analysis Center
#data goes back to 1700 and contains more than 300 annual averages
#to determine sunspot cycles, scientists used the Hilbert-Huang transform
#http://en.wikipedia.org/wiki/Hilbert%E2%80%93Huang_transform
#major part of this transform is Empirical Mode Decomposition (EMD) method. 
#EMD reduces data to a group of Intrinsic Mode Functions (IMF).
#compare : the way Fast Fourier Transform decomposes a signal in a superposition of sine and cosine terms.

#Extracting IMFs is done via a sifting process. 
#The sifting of a signal is related to separating out components of a signal one at a time. 
#The first step of this process is identifying local extrema. 

#We will perform the first step and plot the data with the extrema we found. 

data = np.loadtxt('SIDC-SUNSPOTS_A.csv', delimiter=',', usecols=(1,), unpack=True, skiprows=1)
#reverse order
data = data[::-1]
#find the indices of the local minima and maxima
mins = signal.argrelmin(data)[0]
maxs = signal.argrelmax(data)[0]
#Now we need to concatenate these arrays and 
#use the indices to select the corresponding values. 
extrema = np.concatenate((mins, maxs))
year_range = np.arange(1700, 1700 + len(data))
plt.plot(1700 + extrema, data[extrema], 'go')
plt.plot(year_range, data)
plt.show()
#In the plot, we see the extrema indicated with dots.

#%% - next steps in the sifting process
#interpolate with a cubic spline of the minima and maxima
#This creates an upper envelope and a lower envelope, which should surround the data
#The mean of the envelopes is needed for the next iteration of the EMD process

from scipy import interpolate
#interpolate minima
spl_min = interpolate.interp1d(mins, data[mins], kind='cubic')
min_rng = np.arange(mins.min(), mins.max())
l_env = spl_min(min_rng)
#Similarly, interpolate the maxima
spl_max = interpolate.interp1d(maxs, data[maxs], kind='cubic')
max_rng = np.arange(maxs.min(), maxs.max())
u_env = spl_max(max_rng)
#interpolation results are only valid within the range over which we are interpolating
#This range is defined by the first occurrence of a minima/maxima and 
#ends at the last occurrence of a minima/maxima
#Unfortunately, the interpolation ranges we can define in this way for the maxima and minima do not match perfectly. 
#So, for the purpose of plotting, 
#we extract a shorter range that lies within both the maxima and minima interpolation ranges. 
inclusive_rng = np.arange(max(min_rng[0], max_rng[0]), min(min_rng[-1], max_rng[-1]))
mid = (spl_max(inclusive_rng) + spl_min(inclusive_rng))/2
plt.plot(year_range, data)
plt.plot(1700 + min_rng, l_env, '-x')
plt.plot(1700 + max_rng, u_env, '-x')
plt.plot(1700 + inclusive_rng, mid, '--')
plt.show()
#we see the observed data, with computed envelopes and mid line.
#negative values do not make any sense in this context. 
#However, for the algorithm we only need to care about the mid line of the upper and lower envelopes.
#In these first two sections, we performed the first iteration of the EMD

#%% - Moving averages
#plot the simple moving average for the 11- and 22-year sunspot cycle:

#Moving averages are tools commonly used to analyze time-series data
#A moving average defines a window of previously seen data that is averaged each time 
#the window slides forward one period. 
#The different types of moving average differ essentially in the weights used for averaging. 
#The exponential moving average - has exponentially decreasing weights with time
#This means that older values have less influence than newer values

#We can express an equal-weight strategy for the simple moving average
#weights = np.exp(np.linspace(-1., 0., N))
#weights /= weights.sum()

#A simple moving average uses equal weights
def sma(arr, n):
    weights = np.ones(n) / n
    return np.convolve(weights, arr)[n-1:-n+1]

sma11 = sma(data, 11)  #11 year
sma22 = sma(data, 22)  #22 year
plt.plot(year_range, data, label='Data')
plt.plot(year_range[10:], sma11, '-x', label='SMA 11')
plt.plot(year_range[21:], sma22, '--', label='SMA 22')
plt.legend()
plt.show()

#In the plot, we see the original data and the simple moving averages for 11- and 22-year periods. 
#we see that moving averages are not a good fit for this data
#this is generally the case for sinusoidal data.

#%% - Smoothing functions
#Smoothing can help us get rid of noise and outliers in raw data
#makes it easier to spot trends in the data
#NumPy has a number of smoothing functions
#These functions can calculate weights in a sliding window 
#(as we did in the previous example)
#http://en.wikipedia.org/wiki/Window_function

#These functions, except the kaiser function, require only one parameter—the size of the window
#we will set 22 as the size of the window - for the middle cycle of the sunspot data

#The kaiser function also needs a beta parameter
#With beta parameter, the kaiser function can mimic the other functions

#The NumPy documentation recommends a starting value of 14 for the beta parameter
#the data here is limited to the last 50 years - for easier comparison in the plots
def smooth(weights, arr):
    return np.convolve(weights/weights.sum(), arr)

#Select last 50 years
data50 = data[-50:]
year_range = np.arange(1963, 2013)
print len(data), len(year_range)
plt.plot(year_range, data50, label="Data")
plt.plot(year_range, smooth(np.hanning(22), data50)[21:], 'x',label='Hanning 22')
plt.plot(year_range, smooth(np.bartlett(22), data50)[21:], 'o',label='Bartlett 22')
plt.plot(year_range, smooth(np.blackman(22), data50)[21:], '--',label='Blackman 22')
plt.plot(year_range, smooth(np.hamming(22), data50)[21:], '^',label='Hamming 22')
plt.plot(year_range, smooth(np.kaiser(22, 14), data50)[21:], ':',label='Kaiser 22')
plt.legend()
plt.show()
#In the plot, we see that the result of the window functions doesn't differ much

#%% - Forecasting with an ARMA model
#ARMA is a generalization of autoregressive models that adds an extra component—the moving average
#ARMA models are frequently used to predict values of a time-series
#they combine autoregressive and moving-average models. 
#Autoregressive models predict values by assuming that a linear combination is formed by the previously encountered values. 

#we would be looking at the number of sunspots one year before and 
#two years before the period we are predicting. 
#In an ARMA model, we try to model the residues that we cannot explain from the previous period data 
#(also known as unexpected components). 
#Here, a linear combination is assumed again. 
#So an ARMA (ARMA(2, 1)) model, which we will attempt here is 
#the sum of an AR(2) model and a linear combination of the first order residues 
#http://en.wikipedia.org/wiki/Autoregressive%E2%80%93moving-average_model
#we use the statsmodels functions for this analysis

#We will also be using the sample sunspot data that is a part of the statsmodels distribution
#the dataset might not be up to date
#Forecasting can be done with the following steps:
#Step 1 - Load the data in a pandas DataFrame
#We also specify the available year ranges and get rid of the Year column
import statsmodels.api as sm
import pandas as pd
df = pd.DataFrame(data)
df.index = pd.Index(sm.tsa.datetools.dates_from_range('1700','2017'))
df
df = sm.datasets.sunspots.load_pandas().data
df.index = pandas.Index(sm.tsa.datetools.dates_from_range('1700','2008'))
del df["YEAR"]
2. Fit the data to an ARMA(2,1) model using the following code:
model = sm.tsa.ARMA(df, (2,1)).fit()
3. Do a forecast using the following code:
prediction = model.predict('1984', str(year_today), dynamic=True)
The following code is the complete code listing with plotting:
import numpy as np
from scipy import stats
import pandas
import matplotlib.pyplot as plt
import statsmodels.api as sm
import datetime
df = sm.datasets.sunspots.load_pandas().data
df.index = pandas.Index(sm.tsa.datetools.dates_from_range('1700',
'2008'))
del df["YEAR"]
model = sm.tsa.ARMA(df, (2,1)).fit()
year_today = datetime.date.today().year
#Big Brother is watching you!
prediction = model.predict('1984', str(year_today), dynamic=True)
df.plot()
prediction.plot(style='--', label='Prediction');
plt.legend();
plt.show()
www.it-ebooks.info
Chapter 5
[ 107 ]
Refer to the following chart of prediction and actual data: