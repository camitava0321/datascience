# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2021
@author: Amitava
ISBN
"""
import pandas as pd
import numpy as np
staticNumber="9789387857"
lastNumber=36
isbn13 = staticNumber+str(lastNumber+1)
print ("ISBN13  without check digit: "+isbn13)

#%% - Calculate Check Digit
count=0
multiplier = 3
isbnSum = 0
while (count < len(isbn13)):
    number = int(isbn13[count])
    if (count%2==0):
        multiplier=1
    else:
        multiplier=3
    isbnSum = isbnSum + number*multiplier
    print(count, number, multiplier)
    count = count + 1

remainder = isbnSum % 10
checkDigit = 10 - remainder

isbn13 = isbn13+str(checkDigit)
print ("ISBN13 with check digit: "+isbn13)
        
    
