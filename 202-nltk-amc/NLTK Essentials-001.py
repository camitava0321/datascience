# -*- coding: utf-8 -*-
#author : Amitava Chakraborty
import urllib2
import re
import nltk
import 
import 
#Some example text content - from 
#Gutenberg - Sense and Sensibility by Jane Austen : http://www.gutenberg.org/files/161/161-h/161-h.htm
#urllib2 is use to download the html content of the web link
response = urllib2.urlopen('http://www.gutenberg.org/files/161/161-h/161-h.htm')
#Read the entire content of a file using read() method
html = response.read()
print len(html)

#%% - exploratory data analysis (EDA)
#What are the topics? How frequent they are? 
#a pure Python way 
#Step 1: cleaning the html tags
#One ways to do this - select just the tokens, including numbers and character. 
#Regular expression based split the string
tokens = [tok for tok in html.split()]
print "Total no of tokens :"+ str(len(tokens))
# First 100 tokens
print tokens[0:100]

#an excess of html tags and other unwanted characters
#A cleaner version of the same task - using the split function
tokens = re.split('\W+',html)
print len(tokens)
print tokens[0:100]

#looks much cleaner - but still we need to remove noises
#So we,
#clean some HTML tags
#look for word length as a criteria and 
#remove words that have a length one—it will remove elements like 7, 8, and so on,
#which are just noise in this case
#We will use NLTK for these tasks
#clean_html() for cleaning all the html noise
clean = nltk.clean_html(html)
clean = bs.get_text(html)
tokens = [tok for tok in clean.split()]
print tokens[:100]












