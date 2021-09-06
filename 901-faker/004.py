# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 16:39:51 2018

@author: Amitava Chakraborty
"""
#Market Research Data
#Create a fictitious data file with following fields
#time - numeric
#customer name - First Name + Last Name
#age - numeric
#edu - educational qualification
#rating - 1-10
#credit score - 1-10
#spend - numeric
#income - numeric



import random
from faker import Faker
import amcfakerutils as amf
import numpy as np

noOfRecords=2000000
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
datawriter.write('index,customer,age,edu,rating,creditscore,spend,income, sellbonus\n')


#%% - create training data
age = []
age = getIntegers(low=16,high=85,size=noOfRecords+1)
print age
    

#%% - No.of Data - 1000
for index in range(noOfRecords):
   customer=amf.mask(fake.name())
   #age=random.randint(16,85)   #produce age between 16 to 85
   #edu can be numbers 0, 1 - non matric,2-UG,3-G,4-PG,5-super
   if (age[index] < 22):
       edu = random.randint(0,2)   #produce score 0 to 1
   else:
       edu = random.randint(0,5)   #produce score 0 to 1        
   rating = int((edu + random.randint(1,5))/2)   #produce score 1 to 5
   creditscore = int((edu + random.randint(1,5))/2)   #produce score 1 to 5
   
   income = 5000 + (edu+1)*random.randint(1,5)*5000 + rating*5000 + creditscore * 5000
   spend = 1000 + 0.2 * income * (rating + random.randint(1,4)) /100 + 2000 * random.randint(0,50)/100 
   row = str(index)+","+str(customer)+","+str(age)+","+str(edu)+","+str(rating)+","+str(creditscore)+","+str(spend)+","+str(income)+"\n"
   print row
   datawriter.write(row);

datawriter.close()


#%%- 
import numpy as np
print np.random.normal(size=5)
mu, sigma = 30, 1 # mean and standard deviation
print np.random.normal(mu, sigma, 10)
print int(round(28.77)), int(round(28.45))


