# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 16:39:51 2018

@author: ibm
"""
from faker import Faker
fake = Faker()    #Default usage

#%% - bundled providers
# a fake.name() - name is the provoder for the default generator
#outputs a random name 
print fake.name()

#outputs a random address
print fake.address()

#outputs a random text
print fake.text()

#following are the bundled providers


#%% - 
#A list of names
for _ in range(10):
  print(fake.name())
  
#%% - using locale provider
fake = Faker('hi_IN')  #Using hindi locale
#Other locales that can be used..
#de_DE - German, el_GR - Greek, en_GB - English (Great Britain), en_US - English (United States)
#fr_FR - French, hi_IN - Hindi and many more
print fake.name()
print fake.address()
print fake.text()

#%% - Using a provider
#list of providers - https://faker.readthedocs.io/en/latest/providers.html

fake = Faker()  
#One can use the faking function from any bundled providers
#e.g., to use country_code from provider faker.providers.address - use
print fake.country_code()

#fake.license_plate() from faker.providers.automotive
print fake.license_plate()

#fake.iban() from faker.providers.bank
#print fake.iban()

#fake.credit_card_number(card_type=None) from faker.providers.credit_card
print fake.credit_card_number(card_type=None)

#fake.profile() from faker.providers.profile
print fake.profile(fields=None, sex=None)

