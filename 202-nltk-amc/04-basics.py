# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 21:38:03 2016

@author: Amitava
NLTK: Stemming
"""

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
example_words=["go", "went", "going", "goed", "good", "gosh", "gode", "gone"]

for w in example_words:
    print(ps.stem(w))
#We see for some words (like went, gone) the stemming did not do well
    
example_words=["make", "made", "bite", "bit", "bitten", "biting", "making", "going"]

for w in example_words:
    print(ps.stem(w))

#Let us see how many types of stem it can detect correctly    
example_words = ["python","pythoner","pythoning","pythoned","pythonly"]
for w in example_words:
    print(ps.stem(w))

#Let us try a sentence now
new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
words = word_tokenize(new_text)
for w in words:
    print(ps.stem(w))


    