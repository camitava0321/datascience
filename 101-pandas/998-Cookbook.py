# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
pandas Cookbook
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Make the graphs a bit prettier, and bigger
pd.set_option('display.mpl_style', 'default')
plt.rcParams['figure.figsize'] = (15, 5)
plt.rcParams['font.family'] = 'sans-serif'

# This is necessary to show lots of columns in pandas 0.12. 
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)

#One of the main problems with messy data is: how do you know if it's messy or not?
#We're going to use the NYC 311 service request dataset again here, since it's big and a bit unwieldy.

requests = pd.read_csv('../data/311-service-requests.csv')
requests['Incident Zip'].unique()
array([11432.0, 11378.0, 10032.0, 10023.0, 10027.0, 11372.0, 11419.0,
       11417.0, 10011.0, 11225.0, 11218.0, 10003.0, 10029.0, 10466.0,
       11219.0, 10025.0, 10310.0, 11236.0, nan, 10033.0, 11216.0, 10016.0,
       10305.0, 10312.0, 10026.0, 10309.0, 10036.0, 11433.0, 11235.0,
       11213.0, 11379.0, 11101.0, 10014.0, 11231.0, 11234.0, 10457.0,
       10459.0, 10465.0, 11207.0, 10002.0, 10034.0, 11233.0, 10453.0,
       10456.0, 10469.0, 11374.0, 11221.0, 11421.0, 11215.0, 10007.0,
       10019.0, 11205.0, 11418.0, 11369.0, 11249.0, 10005.0, 10009.0,
       11211.0, 11412.0, 10458.0, 11229.0, 10065.0, 10030.0, 11222.0,
       10024.0, 10013.0, 11420.0, 11365.0, 10012.0, 11214.0, 11212.0,
       10022.0, 11232.0, 11040.0, 11226.0, 10281.0, 11102.0, 11208.0,
       10001.0, 10472.0, 11414.0, 11223.0, 10040.0, 11220.0, 11373.0,
       11203.0, 11691.0, 11356.0, 10017.0, 10452.0, 10280.0, 11217.0,
       10031.0, 11201.0, 11358.0, 10128.0, 11423.0, 10039.0, 10010.0,
       11209.0, 10021.0, 10037.0, 11413.0, 11375.0, 11238.0, 10473.0,
       11103.0, 11354.0, 11361.0, 11106.0, 11385.0, 10463.0, 10467.0,
       11204.0, 11237.0, 11377.0, 11364.0, 11434.0, 11435.0, 11210.0,
       11228.0, 11368.0, 11694.0, 10464.0, 11415.0, 10314.0, 10301.0,
       10018.0, 10038.0, 11105.0, 11230.0, 10468.0, 11104.0, 10471.0,
       11416.0, 10075.0, 11422.0, 11355.0, 10028.0, 10462.0, 10306.0,
       10461.0, 11224.0, 11429.0, 10035.0, 11366.0, 11362.0, 11206.0,
       10460.0, 10304.0, 11360.0, 11411.0, 10455.0, 10475.0, 10069.0,
       10303.0, 10308.0, 10302.0, 11357.0, 10470.0, 11367.0, 11370.0,
       10454.0, 10451.0, 11436.0, 11426.0, 10153.0, 11004.0, 11428.0,
       11427.0, 11001.0, 11363.0, 10004.0, 10474.0, 11430.0, 10000.0,
       10307.0, 11239.0, 10119.0, 10006.0, 10048.0, 11697.0, 11692.0,
       11693.0, 10573.0, 83.0, 11559.0, 10020.0, 77056.0, 11776.0, 70711.0,
       10282.0, 11109.0, 10044.0, '10452', '11233', '10468', '10310',
       '11105', '10462', '10029', '10301', '10457', '10467', '10469',
       '11225', '10035', '10031', '11226', '10454', '11221', '10025',
       '11229', '11235', '11422', '10472', '11208', '11102', '10032',
       '11216', '10473', '10463', '11213', '10040', '10302', '11231',
       '10470', '11204', '11104', '11212', '10466', '11416', '11214',
       '10009', '11692', '11385', '11423', '11201', '10024', '11435',
       '10312', '10030', '11106', '10033', '10303', '11215', '11222',
       '11354', '10016', '10034', '11420', '10304', '10019', '11237',
       '11249', '11230', '11372', '11207', '11378', '11419', '11361',
       '10011', '11357', '10012', '11358', '10003', '10002', '11374',
       '10007', '11234', '10065', '11369', '11434', '11205', '11206',
       '11415', '11236', '11218', '11413', '10458', '11101', '10306',
       '11355', '10023', '11368', '10314', '11421', '10010', '10018',
       '11223', '10455', '11377', '11433', '11375', '10037', '11209',
       '10459', '10128', '10014', '10282', '11373', '10451', '11238',
       '11211', '10038', '11694', '11203', '11691', '11232', '10305',
       '10021', '11228', '10036', '10001', '10017', '11217', '11219',
       '10308', '10465', '11379', '11414', '10460', '11417', '11220',
       '11366', '10027', '11370', '10309', '11412', '11356', '10456',
       '11432', '10022', '10013', '11367', '11040', '10026', '10475',
       '11210', '11364', '11426', '10471', '10119', '11224', '11418',
       '11429', '11365', '10461', '11239', '10039', '00083', '11411',
       '10075', '11004', '11360', '10453', '10028', '11430', '10307',
       '11103', '10004', '10069', '10005', '10474', '11428', '11436',
       '10020', '11001', '11362', '11693', '10464', '11427', '10044',
       '11363', '10006', '10000', '02061', '77092-2016', '10280', '11109',
       '14225', '55164-0737', '19711', '07306', '000000', 'NO CLUE',
       '90010', '10281', '11747', '23541', '11776', '11697', '11788',
       '07604', 10112.0, 11788.0, 11563.0, 11580.0, 7087.0, 11042.0,
       7093.0, 11501.0, 92123.0, 0.0, 11575.0, 7109.0, 11797.0, '10803',
       '11716', '11722', '11549-3650', '10162', '92123', '23502', '11518',
       '07020', '08807', '11577', '07114', '11003', '07201', '11563',
       '61702', '10103', '29616-0759', '35209-3114', '11520', '11735',
       '10129', '11005', '41042', '11590', 6901.0, 7208.0, 11530.0,
       13221.0, 10954.0, 11735.0, 10103.0, 7114.0, 11111.0, 10107.0], dtype=object)


#How do we know if it's messy?
#We're going to look at a few columns here. 
#I know already that there are some problems with the zip code, so let's look at that first.
#To get a sense for whether a column has problems, I usually use .unique() to look at all its values. 
#If it's a numeric column, I'll instead plot a histogram to get a sense of the distribution.

#When we look at the unique values in "Incident Zip", it quickly becomes clear that this is a mess.
#Some of the problems:
#Some have been parsed as strings, and some as floats
#There are nans
#Some of the zip codes are 29616-0759 or 83
#There are some N/A values that pandas didn't recognize, like 'N/A' and 'NO CLUE'

#What we can do:
#Normalize 'N/A' and 'NO CLUE' into regular nan values
#Look at what's up with the 83, and decide what to do
#Make everything strings

requests['Incident Zip'].unique()

#Fixing the nan values and string/float confusion
#We can pass a na_values option to pd.read_csv to clean this up a little bit. 
#We can also specify that the type of Incident Zip is a string, not a float.
na_values = ['NO CLUE', 'N/A', '0']
requests = pd.read_csv('../data/311-service-requests.csv', na_values=na_values, dtype={'Incident Zip': str})
requests['Incident Zip'].unique()

#What's up with the dashes?
rows_with_dashes = requests['Incident Zip'].str.contains('-').fillna(False)
len(requests[rows_with_dashes])
5
requests[rows_with_dashes]

#I thought these were missing data and originally deleted them like this:
requests['Incident Zip'][rows_with_dashes] = np.nan

#But we see that 9-digit zip codes are normal. 
#Let's look at all the zip codes with more than 5 digits, make sure they're okay, and then truncate them.
long_zip_codes = requests['Incident Zip'].str.len() > 5
requests['Incident Zip'][long_zip_codes].unique()
array(['77092-2016', '55164-0737', '000000', '11549-3650', '29616-0759',
       '35209-3114'], dtype=object)
#Those all look okay to truncate to me.
requests['Incident Zip'] = requests['Incident Zip'].str.slice(0, 5)

#Earlier I thought 00083 was a broken zip code, 
#but turns out Central Park's zip code 00083! 
#Shows what I know. I'm still concerned about the 00000 zip codes, though: let's look at that.
requests[requests['Incident Zip'] == '00000']
#This looks bad to me. Let's set these to nan.
zero_zips = requests['Incident Zip'] == '00000'
requests.loc[zero_zips, 'Incident Zip'] = np.nan

#Great. Let's see where we are now:
unique_zips = requests['Incident Zip'].unique()
unique_zips.sort()
unique_zips
array([nan, '00083', '02061', '06901', '07020', '07087', '07093', '07109',
       '07114', '07201', '07208', '07306', '07604', '08807', '10000',
       '10001', '10002', '10003', '10004', '10005', '10006', '10007',
       '10009', '10010', '10011', '10012', '10013', '10014', '10016',
       '10017', '10018', '10019', '10020', '10021', '10022', '10023',
       '10024', '10025', '10026', '10027', '10028', '10029', '10030',
       '10031', '10032', '10033', '10034', '10035', '10036', '10037',
       '10038', '10039', '10040', '10044', '10048', '10065', '10069',
       '10075', '10103', '10107', '10112', '10119', '10128', '10129',
       '10153', '10162', '10280', '10281', '10282', '10301', '10302',
       '10303', '10304', '10305', '10306', '10307', '10308', '10309',
       '10310', '10312', '10314', '10451', '10452', '10453', '10454',
       '10455', '10456', '10457', '10458', '10459', '10460', '10461',
       '10462', '10463', '10464', '10465', '10466', '10467', '10468',
       '10469', '10470', '10471', '10472', '10473', '10474', '10475',
       '10573', '10803', '10954', '11001', '11003', '11004', '11005',
       '11040', '11042', '11101', '11102', '11103', '11104', '11105',
       '11106', '11109', '11111', '11201', '11203', '11204', '11205',
       '11206', '11207', '11208', '11209', '11210', '11211', '11212',
       '11213', '11214', '11215', '11216', '11217', '11218', '11219',
       '11220', '11221', '11222', '11223', '11224', '11225', '11226',
       '11228', '11229', '11230', '11231', '11232', '11233', '11234',
       '11235', '11236', '11237', '11238', '11239', '11249', '11354',
       '11355', '11356', '11357', '11358', '11360', '11361', '11362',
       '11363', '11364', '11365', '11366', '11367', '11368', '11369',
       '11370', '11372', '11373', '11374', '11375', '11377', '11378',
       '11379', '11385', '11411', '11412', '11413', '11414', '11415',
       '11416', '11417', '11418', '11419', '11420', '11421', '11422',
       '11423', '11426', '11427', '11428', '11429', '11430', '11432',
       '11433', '11434', '11435', '11436', '11501', '11518', '11520',
       '11530', '11549', '11559', '11563', '11575', '11577', '11580',
       '11590', '11691', '11692', '11693', '11694', '11697', '11716',
       '11722', '11735', '11747', '11776', '11788', '11797', '13221',
       '14225', '19711', '23502', '23541', '29616', '35209', '41042',
       '55164', '61702', '70711', '77056', '77092', '90010', '92123'], dtype=object)

#Amazing! This is much cleaner. 
#There's something a bit weird here, though -- I looked up 77056 on Google maps, and that's in Texas.
zips = requests['Incident Zip']
# Let's say the zips starting with '0' and '1' are okay, for now. (this isn't actually true -- 13221 is in Syracuse, and why?)
is_close = zips.str.startswith('0') | zips.str.startswith('1')
# There are a bunch of NaNs, but we're not interested in them right now, so we'll say they're False
is_far = ~(is_close) & zips.notnull()
zips[is_far]
requests[is_far][['Incident Zip', 'Descriptor', 'City']].sort('Incident Zip')

#Okay, there really are requests coming from LA and Houston! Good to know. 
#Filtering by zip code is probably a bad way to handle this -- we should really be looking at the city instead.
requests['City'].str.upper().value_counts()

#It looks like these are legitimate complaints, so we'll just leave them alone.

#Putting it together
#Here's what we ended up doing to clean up our zip codes, all together:
na_values = ['NO CLUE', 'N/A', '0']
requests = pd.read_csv('../data/311-service-requests.csv', 
                       na_values=na_values, 
                       dtype={'Incident Zip': str})
def fix_zip_codes(zips):
    # Truncate everything to length 5 
    zips = zips.str.slice(0, 5)
    
    # Set 00000 zip codes to nan
    zero_zips = zips == '00000'
    zips[zero_zips] = np.nan
    
    return zips
requests['Incident Zip'] = fix_zip_codes(requests['Incident Zip'])
requests['Incident Zip'].unique()