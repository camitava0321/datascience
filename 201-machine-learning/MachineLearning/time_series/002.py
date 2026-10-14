"""
Amitava Chakraborty
"""
#Time Series - Naive Methods
#Introduction
#Naive Methods such as assuming the predicted value at time t to be the actual value of the variable 
#at time t-1 or rolling mean of series, are used to weigh how well do the statistical models and 
#machine learning models can perform and emphasize their need.

#In this chapter, let us try these models on one of the features of our time-series data.
#First we shall see the mean of the temperature feature of our data and the deviation around it. 
#It is also useful to see maximum and minimum temperature values. We can use the functionalities 
#of numpy library here.
#%%
import numpy
import pandas
import datetime
from ts import getDataFrame
#All these things we have done in 001.py
df = getDataFrame()

df.DateTime = df.DateTime.apply(lambda x: datetime.datetime.strptime(x, '%d/%m/%Y %H.%M.%S'))
df.index = df.DateTime
#%%
print (
   'Mean: ',numpy.mean(df['T']), '; Standard Deviation: ',numpy.std(df['T']),\
    '; \nMaximum Temperature: ',max(df['T']),'; Minimum Temperature: ',min(df['T'])
)
#We have the statistics for all 9357 observations across equi-spaced timeline which are useful for us 
#to understand the data.

#Now we will try the first naive method, setting the predicted value at present time equal to actual value 
#at previous time and calculate the root mean squared error(RMSE) for it to quantify the performance of 
#this method.

#Showing 1st naive method
df['T']
df['T_t-1'] = df['T'].shift(1)
df_naive = df[['T','T_t-1']][1:]
#%%
from sklearn import metrics
from math import sqrt

true = df_naive['T']
prediction = df_naive['T_t-1']
error = sqrt(metrics.mean_squared_error(true,prediction))
print ('RMSE for Naive Method 1: ', error)

#%%
#Let us see the next naive method, where predicted value at present time is equated to the mean of the time 
#periods preceding it. We will calculate the RMSE for this method too.

#Showing 2nd naive method
df['T_rm'] = df['T'].rolling(3).mean().shift(1)
df_naive = df[['T','T_rm']].dropna()

true = df_naive['T']
prediction = df_naive['T_rm']
error = sqrt(metrics.mean_squared_error(true,prediction))
print ('RMSE for Naive Method 2: ', error)
#%%
#Here, you can experiment with various number of previous time periods also called lags you want to consider, 
#which is kept as 3 here. In this data it can be seen that as you increase the number of lags and 
#error increases. If lag is kept 1, it becomes same as the nave method used earlier.

#Points to Note
#1. You can write a very simple function for calculating root mean squared error. 
#Here, we have used the mean squared error function from the package sklearn and then taken its square root.
#2. In pandas df[column_name] can also be written as df.column_name, however for this dataset df.T will not 
#work the same as df[T] because df.T is the function for transposing a dataframe. 
#So use only df[T] or consider renaming this column before using the other syntax.