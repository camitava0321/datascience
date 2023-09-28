# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 21:48:19 2016

@author: Amitava
NLTK: Words Tokenizing with Stop Words
"""

import nltk
#Append the nltk folder in the data path
nltk.data.path.append("D:\\DevelopmentWorkspaces\\Python\\Canopy\\nltk")

from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#Let us first get the sentences
EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

#Filtering out STOP WORDS.
#NLTK has a bunch of words that they consider to be stop words
#we access it via the NLTK corpus with: from nltk.corpus import stopwords
mystopwords = set(stopwords.words('english'))

#Now we tokenize words
word_tokens = word_tokenize(EXAMPLE_TEXT)
filtered_sentence = [w    for w in word_tokens  if not w in mystopwords]
"""
The above complex statement can be broken down like..
filtered_sentence = []
for w in word_tokens:
    if w not in mystopwords:
        filtered_sentence.append(w)
"""
print(word_tokens)
print(filtered_sentence)
#%%

#Read a file and then extract sentences with a training model
train_text=state_union.raw("2005-GWBush.txt")
sample_text=state_union.raw("2006-GWBush.txt")
#Create a custom sentence tokenizer with training text
custom_sentence_tokenizer=PunktSentenceTokenizer(train_text)
#tokenize the sample text with the custom sentence tokenizer
tokenized=custom_sentence_tokenizer.tokenize(sample_text)

#A function to deduce & print the POS tags from the sample text
def process_content():
    try:
        for i in tokenized:
            words=nltk.word_tokenize(i)
            filtered_sentence = [w    for w in words  if not w in mystopwords]
            print(filtered_sentence)
            
        
    except Exception as e:
        print(str(e))

#invoke the function
process_content()
