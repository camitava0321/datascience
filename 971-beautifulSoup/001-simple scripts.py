# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty

Web scraping in Python using Beautiful Soup 4
""
getting data out of HTML, XML and other markup languages. 
We will try to scrap webpage from various different websites (including IMDB). 
searching and parsing HTML web page.

unstructured data/information (mostly web data) available freely. 
web scraping is very useful tool to transform unstructured data into structured data 
that is easier to read & analyze. 
one way to collect, organize and analyze this enormous amount of data is through web scraping. 

Web-scraping which is also known as web data extraction or web harvesting is the 
extraction of data from web. 

Why Web-scraping?
To automate most of the things a human does while browsing. 
Web-scraping is used in an enterprise in a variety of ways −

Data for Research - Smart analyst (like researcher or journalist) uses web scrapper 
instead of manually collecting and cleaning data from the websites.

Products prices & popularity comparison - Currently there are couple of services 
which use web scrappers to collect data from numerous online sites and use it to 
compare products popularity and prices.

SEO Monitoring - There are numerous SEO tools such as Ahrefs, Seobility, SEMrush, etc., 
which are used for competitive analysis and for pulling data from your client’s websites.

Search engines - There are some big IT companies whose business solely depends on 
web scraping.

Sales and Marketing - The data gathered through web scraping can be used by marketers 
to analyze different niches and competitors or by the sales specialist for 
selling content marketing or social media promotion services.

The Beautiful Soup is a python library which is named after a Lewis Carroll poem 
of the same name in “Alice’s Adventures in the Wonderland”. 
Beautiful Soup is a python package and as the name suggests, 
parses the unwanted data and helps to organize and format the messy web data by 
fixing bad HTML and present to us in an easily-traversible XML structures.

In short, Beautiful Soup is a python package which allows us to pull data out of HTML 
and XML documents.


"""
from bs4 import BeautifulSoup
import requests
url = "https://www.tutorialspoint.com/index.htm"
url = "https://en.wikipedia.org/wiki/Harry_Potter"

req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print(soup.title)
print(soup.head)
print (soup.body)
print (soup.body.h2)
print (soup.find_all("h2"))
print (len(soup.contents))
print(len(list(soup.children)))
print(len(list(soup.descendents)))

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
