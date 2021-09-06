# -*- coding: utf-8 -*-
"""
@author: Amitava Chakraborty
"""
#Bookmaking Data
#Create a fictitious data file with following features
#bookname - String (a dummy name)
#pages - numeric
#price - float


from faker import Faker
import amcfakerutils as amf
import numpy as np
import pandas as pd

fake = Faker()    #Default usage

from scipy.stats import truncnorm

def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

def getIntegers(low=0, high=100, size=10):
    mean = low + (high-low)/2
    sd=(high-low)/2
    x = truncnorm((low - mean) / sd, (high - mean) / sd, loc=mean, scale=sd)
    values = x.rvs(size)
    values = values.astype(int)
    return values

#%% - Open csv to write and write the header 
sensexData=pd.read_csv('sensex.csv',index_col=['Date'])
datawriter = open('trades.csv', 'w')
datawriter.write('portfolio,sensex_index,ticker_code,original_price,close_price\n')



#%% - create data
portfolios = getIntegers(low=1,high=500,size=2000)
dates=pd.bdate_range(start='18/08/2017', end='17/08/2018')
tickers = ['AB','BC','CD','DE','EF','FG','GH']

#%% - No.of Data - 1000
for portfolio in portfolios:
    #select a random date from dates array
    date=dates[np.random.randint(0,len(dates))]
    date=date.strftime('%d-%b-%y')
    #Get the 'Close' value of sensex on that date
    sensexClose=sensexData.get(date)
   coverPriceFactor = coverPrices[coverIndex]
   price = 19000 + (page-np.min(pages))*(100+60*np.random.normal(0.5,0.28)) 
   price = price*coverPriceFactor
   bookname='Book'+str(abs(int(40*np.random.normal(0.5,.28))))
   row = bookname+","+str(page)+","+cover+","+str(price)+"\n"
   print row
   datawriter.write(row);

datawriter.close()

#%%- 
import numpy as np
print np.random.normal(size=5)
mu, sigma = 30, 1 # mean and standard deviation
print np.random.normal(mu, sigma, 10)
print np.random.normal(0.5, 0.28, 1)
print np.random.normal(0.5, 0.28)
print int(round(28.77)), int(round(28.45))


