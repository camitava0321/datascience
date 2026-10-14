"""
Amitava Chakraborty
"""
#Time Series is a sequence of observations indexed in equi-spaced time intervals. 
#Hence, the order and continuity should be maintained in any time series.

#dataset - multi-variate time series having hourly data for approximately one year, 
#for air quality in a significantly polluted Italian city. 
#The dataset was downloaded from − 
#https://archive.ics.uci.edu/ml/datasets/air+quality.

#It is necessary to make sure that −
#The time series is equally spaced, and
#There are no redundant values or gaps in it.
#In case the time series is not continuous, we can upsample or downsample it.
#%%
import pandas

df = pandas.read_csv("01-data/AirQualityUCI.csv", sep = ";", decimal = ",")
# We will use pandas' integer-position-based indexer:
# to kees every row of the data but drop all columns 
#  except the first 14, reassigning the result back to df
 
#Now we know that 
# : (before the comma) — select all rows.
# 0:14 (after the comma) — select columns at positions 0 through 13 (14 is exclusive, so that's the first 14 columns).
df = df.iloc[ : , 0:14]
len(df)
#%%
df.head()

#%%
#For preprocessing the time series, we make sure there are no NaN(NULL) values in the dataset; 
#if there are, we can replace them with either 0 or average or preceding or succeeding values. 
#Replacing is a preferred choice over dropping so that the continuity of the time series is maintained. 
#However, in our dataset the last few values seem to be NULL and hence dropping will not affect the 
#continuity.
#So how many nulls we have in the data?
df.isna().sum()
#all are 114, i.e. all nulls are due to the Date being null.

#%%
#Dropping NaN(Not-a-Number) - select only those where the date is null
df = df[df['Date'].notnull()]

df.isna().sum()
#all are 0, i.e. we do not have any nulls in our dataset
#%%
#Time Series are usually plotted as line graphs against time. For that we will now combine the 
#date and time column and convert it into a datetime object from strings. 
#This can be accomplished using the datetime library.

#Converting to datetime object
df['DateTime'] = (df.Date) + ' ' + (df.Time)
print (df.DateTime[0], type(df.DateTime[0]))
#%%
#Now we will convert this text datetime into a timestamp type
import datetime

df.DateTime = df.DateTime.apply(lambda x: datetime.datetime.strptime(x, '%d/%m/%Y %H.%M.%S'))
print (df.DateTime[0], type(df.DateTime[0]))
#%%
#Let us see how some variables like temperature changes with change in time.

#Showing plots
df.index = df.DateTime
import matplotlib.pyplot as plt
#Let us plot total pollution
plt.plot(df['T'])
#%%
#Now let us plot only C6H6
plt.plot(df['C6H6(GT)'])

#%%
#Box-plots are another useful kind of graphs that allow you to condense a lot of information about a 
#dataset into a single graph. It shows the mean, 25% and 75% quartile and outliers of one or multiple 
#variables. In the case when number of outliers is few and is very distant from the mean, we can eliminate 
#the outliers by setting them to mean value or 75% quartile value.

#Showing Boxplots
plt.boxplot(df[['T','C6H6(GT)']].values)
#%%
#Since we will use this dataframe in subsequent advancements, we need this df over and over again. 
#Hence we will need this function
def getDataFrame():
    #All these things we have done in 001.py
    df = pandas.read_csv("01-data/AirQualityUCI.csv", sep = ";", decimal = ",")
    df = df.iloc[ : , 0:14]
    df = df[df['Date'].notnull()]
    df['DateTime'] = (df.Date) + ' ' + (df.Time)
    return df

