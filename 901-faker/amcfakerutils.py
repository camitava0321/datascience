# -*- coding: utf-8 -*-
#author : Amitava Chakraborty

def maskedName(locale='en_GB'):
    import faker
    import numpy as np
    
    fake = faker.Faker(locale)
    name = fake.name()
    
    indices = np.random.randint(1,len(name)-1,int(len(name)/1.3))
    for c in indices:
        name1 = name[0:c] + 'X' + name[c+1:]
        name=name1
    
    #name1 = re.sub('.',name,'X')
    return name

def mask(string, char='X',percent=70):
    import numpy as np
    
    #create n percent of the length of the string
    percent_length = (len(string)*1000.0)*percent/100
    percent_length = int(percent_length/1000)
    indices = np.random.randint(1,len(string)-1,percent_length)
    for c in indices:
        string1 = string[0:c] + char + string[c+1:]
        string=string1
    
    #name1 = re.sub('.',name,'X')
    return string
    
def getNameSurname(string):
    dummyInt=string.find(' ')
    name = string[:dummyInt]
    surname = string[dummyInt+1:]
    return name, surname

def getPAN(surname):
    #return a generated PAN for an individual - fourth digit is 'P'
    import random
    import string
    first_char = ['A','B','C','D','E','F']
    dummy = random.choice(first_char)
    dummy = dummy+''.join([random.choice(string.ascii_uppercase) for n in range(2)])
    dummy = dummy+'P'+surname[0]+"{:04d}".format((random.randint(0,9999)))
    dummy = dummy+random.choice(string.ascii_uppercase)
    PAN=dummy
    return PAN

def getProbabilisticBoolean(list, probabilityOfFirst):
    import random
    newList = list[0]*int(probabilityOfFirst*10) + list[1]*int((1-probabilityOfFirst)*10)
    retValue = random.choice(newList)
    return retValue

# Return Timeseries data
# Default behaviour : Return MultiVariate data with
#                            * Non-uniform timestamp YYYYMMDDHHMMSSmmmm 
#                            * 3 independent features (Two numeric N1, N2, One Class C1)
#                            * 2 dependent features (Numeric DN1, DN2)
#                            * 200 rows
def getTimeSeriesDataset(rows=200, timegapMillies=-1, featureDict={}):
    from datetime import datetime
    dataset = []
    if len(featureDict)==0:
        featureDict={0:["N1",0,0], 1:["N2",0,0],2:["C1",1,0],3:["DN1",0,"N1"],4:["DN2",0,"N2"]}   
    
    columnNames=["TIMESTAMP"]
    for i in featureDict:
        columnNames.append(featureDict[i][0])
    
    print(columnNames)
    dataset.append(columnNames)
    count=10
    rowcount=0
    while (count!=0):
        timestamp = datetime.today().strftime('%Y%m%d%H%M%S%f')
        timestamp = timestamp+str(rowcount).format("%00n")
        dataset.append([timestamp,1,1,1,1])
        count -= 1
        rowcount=rowcount+1
        
    return dataset