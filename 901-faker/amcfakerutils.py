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
    dummy = dummy+''.join([random.choice(string.ascii_uppercase) for n in xrange(2)])
    dummy = dummy+'P'+surname[0]+"{:04d}".format((random.randint(0,9999)))
    dummy = dummy+random.choice(string.ascii_uppercase)
    PAN=dummy
    return PAN

def getProbabilisticBoolean(list, probabilityOfFirst):
    import random
    newList = list[0]*int(probabilityOfFirst*10) + list[1]*int((1-probabilityOfFirst)*10)
    retValue = random.choice(newList)
    return retValue