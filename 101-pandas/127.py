# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
Comparison with SQL
"""
import pandas as pd
#url = 'https://raw.github.com/pandasdev/pandas/master/pandas/tests/data/tips.csv'
#tips=pd.read_csv(url)
tips=pd.read_csv('tips.csv')
print tips.head()

#SELECT
#In SQL, selection is done using a comma-separated list of columns that you select (or a * to select all columns) −
#SELECT total_bill, tip, smoker, time
#FROM tips
#LIMIT 5;

#With Pandas, column selection is done by passing a list of column names to your DataFrame −
tips[['total_bill', 'tip', 'smoker', 'time']].head(5)

#WHERE
#SELECT * FROM tips WHERE time = 'Dinner' LIMIT 5;
#DataFrames can be filtered in multiple ways; 
#the most intuitive of which is using Boolean indexing.
tips[tips['time'] == 'Dinner'].head(5)
#The above statement passes a Series of True/False objects to the DataFrame, returning all rows with True.

#GroupBy
#SELECT sex, count(*) FROM tips GROUP BY sex;
#The Pandas equivalent would be −
tips.groupby('sex').size()

#Top N rows
#SELECT * FROM tips LIMIT 5 ;
#The Pandas equivalent would be −
tips.head(5)