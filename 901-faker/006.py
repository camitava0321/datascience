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
datawriter = open('bookdata.csv', 'w')
datawriter.write('name,pages,price\n')



#%% - create data
pages = getIntegers(low=80,high=500,size=2000)
covers = ['PB','HB','Gel','Gelcover']
coverPrices = [1,2,1.7,2.4]

#%% - No.of Data - 1000
for page in pages:
   coverIndex=np.random.randint(0,3) 
   cover = covers[coverIndex]
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


