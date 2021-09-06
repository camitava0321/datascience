# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 16:39:51 2018

@author: Amitava Chakraborty
"""

#Create a fictitious data file with following fields
#time - numeric
#house name - First Name + Last Name
#bedrooms - numeric
#locality - 1-10
#quality - 1-10
#sell price - numeric
#category - A,B,C,D,E

import random
import amcfakerutils
from faker import Faker
fake = Faker()    #Default usage


#%% - Open csv to write and write the header 
datawriter = open('data.csv', 'w')
datawriter.write('index,housename,bedrooms,locality,quality,sellprice\n')


#%% - create training data

# No.of Data - 1000
for index in range(100):
   housename=amcfakerutils.maskedName()
   #ssn = amcfakerutils.mask(fake.ssn(),char='_', percent=80)
   bedrooms=random.randint(1,4)   #produce numbers 1 to 4
   locality = random.randint(1,10)   #produce score 1 to 10
   quality = random.randint(1,10)   #produce score 1 to 10
   
   baseprice = 9000+random.randint(1,11)*100
   bedroomPrice = bedrooms*10000+random.uniform(0.1,1.1)*1000
   qualityPrice = quality*5000+random.uniform(0.1,1.1)*2000
   localityPrice = locality*5000+random.uniform(0.1,1.1)*5000
   sellprice = baseprice + bedroomPrice + qualityPrice + localityPrice
   row = str(index)+","+str(housename)+","+str(bedrooms)+","+str(locality)+","+str(quality)+","+str(sellprice)+"\n"
   print row
   datawriter.write(row);

datawriter.close()