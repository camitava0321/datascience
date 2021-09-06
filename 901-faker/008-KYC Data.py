# -*- coding: utf-8 -*-
"""
@author: Amitava Chakraborty
"""
#KYC Data
#Create a fictitious data file with following features
#application number - integer counter
#name - String 30
#surname - String 30
#FatherOrSpouseName - String 60
#FatherSpouse  - String 1 F,S
#Gender   - String 1 M,F
#MaritalStatus   - String 1 M,S
#DOB - Date
#Nationality - String 30
#ResidentialStatus - String 1 R,N
#PAN - String 10
#UID - String 10
#CorrespondenceAddressType - String 20
#CorrespondenceAddressFlatNo - String 5
#CorrespondenceAddressApartmentName - String 30
#CorrespondenceAddressStret - String 50
#CorrespondenceAddressCityTownVillage - String 30
#CorrespondenceAddressPin - String 6
#CorrespondenceAddressState - String 30
#CorrespondenceAddressCountry - String 30
#ContactISD - integer
#ContactSTD - integer
#ContactNo - integer
#ContactEmail - String 50
#PermanentAddressType - String 20
#PermanentAddressFlatNo - String 5
#PermanentAddressApartmentName - String 30
#PermanentAddressStret - String 50
#PermanentAddressCityTownVillage - String 30
#PermanentAddressPin - String 6
#PermanentAddressState - String 30
#PermanentAddressCountry - String 30
#GrossAnnualIncome - integer
#NetWorth - integer
#NetWorth - Date
#Occupation - String
#PEP - Boolean 

#Augmented KYC Features
#SpendIndicator - String H,M,L
#AnnualSpend - integer
#AnnualIncome - integer
#AnnualTax - integer

#Calculated Fields
#CreditScore - integer
#Age - integer


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

def getCreditScore (data,avgIncome):
    creditScore=0
    # Create the pandas DataFrame 
    data = pd.DataFrame(data, columns = ['MaritalStatus', 'Nationality', 'ResidentialStatus', 'GrossAnnualIncome', 'PEPIndicator', 'SpendIndicator', 'NetWorth','Age'])

#better score for single 
    if data['MaritalStatus'][0]=='S':
        creditScore = creditScore+1
    
#better score for Indian 
    if data['Nationality'][0]=='Indian':
        creditScore = creditScore+1
        
#better score for residents
    if data['ResidentialStatus'][0]=='R':
        creditScore = creditScore+1

#better score for more Income 
    if data['GrossAnnualIncome'][0] > avgIncome:
        creditScore = creditScore+1

#better score for a PEP true
    if data['PEPIndicator'][0]==True :
        creditScore = creditScore+1

#better score for a better SpendIndicator
    if data['SpendIndicator'][0]=='L':
        creditScore = creditScore+1

#better score for beter Networth
    if data['NetWorth'][0] > 5000000:
        creditScore = creditScore+1

#better score for young generation
    if data['Age'][0]<50:
        creditScore = creditScore+1
    return creditScore

def getAgeCorrectedValue (age, value, avgValue):
    #Correction is ones aged less than 60 years
    rich='N'
    if age<60:
        value = value + (avgValue * age/17.0)/10.0
        if age<40:
            #probability of being rich is less
            rich = amf.getProbabilisticBoolean(['Y','N'],.1)
            if rich=='N':
                value=value/2
    return value
#%% - Open csv to write and write the header 
datawriter = open('kyc.csv', 'w')
datawriter.write('applicationNumber,name,surname,FatherOrSpouseName,FatherSpouseIndicator,Gender,MaritalStatus,DOB,Nationality,ResidentialStatus,PAN,UID,')
datawriter.write('CorrespondenceAddressType,CorrespondenceAddressFlatNo,CorrespondenceAddressApartmentName,CorrespondenceAddressStreet,CorrespondenceAddressCityTownVillage,CorrespondenceAddressPin,CorrespondenceAddressState,CorrespondenceAddressCountry,')
datawriter.write('ContactISD,ContactSTD,ContactNo,ContactEmail,')
datawriter.write('GrossAnnualIncome,NetWorth,NetWorthDate,Occupation,PEPIndicator,')
datawriter.write('SpendIndicator,AnnualSpend,AnnualIncome,AnnualTax,')
datawriter.write('CreditScore,Age\n')






#%% - create data
#portfolios based on a variation of gross annual income between 50000 and 5000000
no_rows=1000
portfolios = getIntegers(low=50000,high=5000000,size=no_rows)
ages = getIntegers(low=17,high=90,size=no_rows)
avgIncome = portfolios.mean()
dates=pd.bdate_range(start='18/08/2017', end='17/08/2018')

#%% - No.of Data - 100
import  random as rn
from datetime import date
import datetime 

counter=0
for portfolio in portfolios:
    applicationNumber=counter+1
    FatherSpouseIndicator = amf.getProbabilisticBoolean(['S','F'], .7)
    Gender = amf.getProbabilisticBoolean(['M','F'], .6)
    if Gender=='F':
        name, surname = amf.getNameSurname(fake.name_female())
        FatherOrSpouseName = fake.first_name_male()
    else:
        name, surname = amf.getNameSurname(fake.name_male())
        if FatherSpouseIndicator == 'S':
            FatherOrSpouseName = fake.first_name_female()
        else:
            FatherOrSpouseName = fake.first_name_male()
            
    FatherOrSpouseName = FatherOrSpouseName+' '+surname
        
    list='MSMSSMMSSSMMMSSSS'
    if FatherSpouseIndicator=='S':
        MaritalStatus = 'M'
    else:
        MaritalStatus = amf.getProbabilisticBoolean(['M','S'], .3)
        
    currDate = date.today()
    #Age - truncated normal distribution
    age = int(ages[counter])    
    #age = int(np.random.normal(mu, sigma, 1)[0])    
    #Age - Uniform Distribution
    #age = rn.randrange(30,80,1)
    
    DOB = currDate+datetime.timedelta(days=-age*365)
    PAN = ''
    nationalityProbability = rn.random()
    if nationalityProbability>.7 :
        ResidentialStatus='N'
    else:
        ResidentialStatus='Y'
        PAN = amf.getPAN(surname)
        ContactISD='091'
    
    if nationalityProbability>.8 :
        nationalityList=['UK','US','France']
        Nationality = rn.choice(nationalityList)
        ResidentialStatus='N'
        ContactISD='001'
    else:
        Nationality='India'
    
    UID = fake.ssn()
    
    addressType = ['passport','voter id','aadhaar','bank statement']
    CorrespondenceAddressType = rn.choice(addressType)
    CorrespondenceAddressFlatNo = rn.randint(1,100)
    CorrespondenceAddressApartmentName = fake.word()
    CorrespondenceAddressStreet = fake.street_address()
    CorrespondenceAddressCityTownVillage = fake.city()
    CorrespondenceAddressPin = fake.zipcode()
    CorrespondenceAddressState = fake.state()
    CorrespondenceAddressCountry = Nationality

    ContactSTD='{:03d}'.format(rn.randint(11,891))
    ContactNo=rn.randint(9030000000,9899999999)
    ContactEmail=name+'.'+surname+'@'+fake.free_email_domain()

    GrossAnnualIncome=getAgeCorrectedValue(age, portfolio, avgIncome)
    #declared Assets 
    declaredAssets = rn.randrange(0,10000000,1)
    NetWorth=portfolio * .5 * age/17.0 + declaredAssets
    NetWorthDate=currDate
    Occupation=fake.job().replace(',','-')
    PEPIndicator=amf.getProbabilisticBoolean(['Y','N'],.1)
    
    list='HHMMMMMLLL'
    SpendIndicator = rn.choice(list)
    AnnualTaxable=np.clip(GrossAnnualIncome-200000, 0, GrossAnnualIncome-200000)
    savedTax = getAgeCorrectedValue(age,0,100000)
    AnnualTax = AnnualTaxable * 0.33 + savedTax
    if SpendIndicator=='H' :
        AnnualSpend=(GrossAnnualIncome-AnnualTax)*(1.0/rn.randint(2,3))
    if SpendIndicator=='M' :
        AnnualSpend=(GrossAnnualIncome-AnnualTax)*(1.0/rn.randint(4,5))
    if SpendIndicator=='L' :
        AnnualSpend=(GrossAnnualIncome-AnnualTax)*(1.0/rn.randint(6,7))
    AnnualIncome=GrossAnnualIncome-AnnualTax
    
    data = [[MaritalStatus, Nationality, ResidentialStatus, GrossAnnualIncome, PEPIndicator, SpendIndicator, NetWorth, age]]
    CreditScore = getCreditScore(data,avgIncome)
    
    row = str(applicationNumber)+','+name+','+surname+','+ \
    FatherOrSpouseName+','+ \
    FatherSpouseIndicator+','+ \
    Gender+','+ \
    MaritalStatus+','+ \
    DOB.strftime('%d-%b-%y')+','+  \
    Nationality+','+  \
    ResidentialStatus+','+  \
    PAN+','+  \
    UID+','+  \
    CorrespondenceAddressType+','+  \
    str(CorrespondenceAddressFlatNo)+','+  \
    CorrespondenceAddressApartmentName+','+  \
    CorrespondenceAddressStreet+','+  \
    CorrespondenceAddressCityTownVillage+','+  \
    str(CorrespondenceAddressPin)+','+  \
    CorrespondenceAddressState+','+  \
    CorrespondenceAddressCountry+','+  \
    str(ContactISD)+','+  \
    str(ContactSTD)+','+  \
    str(ContactNo)+','+  \
    ContactEmail+','+  \
    str(GrossAnnualIncome)+','+  \
    str(NetWorth)+','+  \
    NetWorthDate.strftime('%d-%b-%y')+','+  \
    Occupation+','+  \
    PEPIndicator+','+  \
    SpendIndicator+','+  \
    str(AnnualSpend)+','+  \
    str(AnnualIncome)+','+  \
    str(AnnualTax)+','+  \
    str(CreditScore)+','+  \
    str(age)+"\n"
    print row
    datawriter.write(row);
    counter=counter+1



#%%- 
datawriter.close()
