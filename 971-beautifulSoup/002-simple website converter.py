# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty

Web scraping and Website Converter (de-cluttering a page)
"""

from bs4 import BeautifulSoup
import requests
url = "https://www.tutorialspoint.com/beautiful_soup/beautiful_soup_navigating_by_tags.htm"


def writeToFile(contents):
    f = open("abc.htm", "w")
    f.write(contents)
    f.close()
    
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

t = soup.find("div", {"id": "mainContent"})
t=t.wrap(soup.new_tag("body"))
t.insert(0,soup.new_tag("title","AMC Simple Website Converter"))
print(t)
writeToFile(t.prettify())

#print(soup.title)
#print(soup.head)
#print (soup.body)
#print (soup.body.h2)
#print (soup.find_all("h2"))
#print (len(soup.contents))
#print(len(list(soup.children)))
#print(len(list(soup.descendents)))

#%% - One common task is to extract all the URLs within a webpage. 
#For that we just need to add the below line of code −
for link in soup.find_all('a'):
    print (link.get('href'))

for link in soup.find_all('img'):
    print (link.get('src'))
    
    
#%% - 
for string in soup.strings:
    print(repr(string))
#%% - To remove extra whitespace, use .stripped_strings generator −
for string in soup.stripped_strings:
    print(repr(string))
#%% - prettify
print (soup.body.prettify())
#%% - True
#True will return all tags that it can find, but no strings on their own −
print(soup.find_all(True))
for tag in soup.find_all(True):
    print (tag.name)
#%% - 
url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"
content = requests.get(url)
soup = BeautifulSoup(content.text, 'html.parser')

#Extract title Page
print(soup.find('title'))

#Extracting main heading
for heading in soup.find_all('h1'):
   print("H1: "+heading.text)

#Extracting sub-heading
for heading in soup.find_all('h2'):
   print("H2: "+heading.text)    
#Extracting sub-heading
for heading in soup.find_all('h3'):
   print("H3: "+heading.text)    

#%% - 
#find_parents(name, attrs, string, limit, **kwargs)
#find_parent(name, attrs, string, **kwargs)

a_string = soup.find(string="The Godfather")
print (a_string.find_parents('a'))

print (a_string.find_parent('tr'))
print (a_string.find_parents('td'))

#%% - Beautiful Soup - Parsing only section of a document
#There are situations where we want to extract specific types of information (only <a> tags) using Beautifulsoup4. 
#The SoupStrainer class in Beautifulsoup allows us to parse only specific part of an incoming document.

#One way is to create a SoupStrainer and pass it on to the Beautifulsoup4 constructor as the parse_only argument.
#A SoupStrainer tells BeautifulSoup what parts extract, and the parse tree consists of only these elements. 
#If you narrow down your required information to a specific portion of the HTML, this will speed up your search result.

#product = SoupStrainer('div',{'id': 'products_list'})
#soup = BeautifulSoup(html,parse_only=product)
#Above lines of code will parse only the titles from a product site, which might be inside a tag field.

#Below are some of the examples −
from bs4 import BeautifulSoup, SoupStrainer

#Only "a" tags
only_a_tags = SoupStrainer("a")

#Will parse only the below mentioned "ids".
parse_only = SoupStrainer(id=["first", "third", "my_unique_id"])
soup = BeautifulSoup(content.text, "html.parser", parse_only=only_a_tags)

print (soup)
#parse only where string length is less than 10
def is_short_string(string):
   return len(string) < 10
   
only_short_strings =SoupStrainer(string=is_short_string)
