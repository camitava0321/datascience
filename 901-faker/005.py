# -*- coding: utf-8 -*-
"""
@author: Amitava Chakraborty
"""
#Classification Data
#Create a fictitious data file with following features
#FA - numeric
#FB - String
#FC - numeric
#FD - String
#FE - numeric
#FF - String
#FG - numeric
#FH - String
#FIA - numeric - correlated to FA
#FJB - numeric - correlated to FB
#FKC - String - correlated to FC
#FLD - String - correlated to FD


import random
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
datawriter = open('data.csv', 'w')
datawriter.write('FA,FB,FC,FD,FE,FF,FG,FH,FIA,FJB,FKC,FLD\n')



#%% - create data
FA = getIntegers(low=16,high=85,size=200)
print FA
FIA = FA * 3.2
print FIA    

#%% - No.of Data - 1000
for index in range(1000):
   row = str(fieldname)+","+"\n"
   print row
   datawriter.write(row);

datawriter.close()


#%%- 
import numpy as np
print np.random.normal(size=5)
mu, sigma = 30, 1 # mean and standard deviation
print np.random.normal(mu, sigma, 10)
print int(round(28.77)), int(round(28.45))


