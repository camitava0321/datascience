# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 16:39:51 2018

@author: Amitava Chakraborty
"""

#Create a fictitious data file for classification with following fields
#paramA - numeric
#paramB - numeric
#category - A,B,C,D,E

import random
import amcfakerutils
#from faker import Faker
#fake = Faker()    #Default usage


#%% - Open csv to write and write the header 
datawriter = open('data.csv', 'w')
datawriter.write('paramA, paramB, category\n')


#%% - create training data

# No.of Data - 1000
for index in range(50):
   paramA = random.randint(1,100) 
   paramB = random.randint(1,1000)
   if paramA+paramB < 400:
       category='A'
   else:
       category='B'
   
   row = str(paramA)+","+str(paramB)+","+category+"\n"
   print (row)
   datawriter.write(row);

datawriter.close()