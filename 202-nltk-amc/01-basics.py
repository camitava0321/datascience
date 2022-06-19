# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 21:48:19 2016

@author: Amitava
NLTK: Sentence Tokenizing
"""

import nltk
#Append the nltk folder in the data path
nltk.data.path.append("nltk-data")

from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer 
from nltk.tokenize import sent_tokenize

#Let us first get the sentences
EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
print(sent_tokenize(EXAMPLE_TEXT))


#Read a file and then extract sentences with a training model
train_text=state_union.raw("2005-GWBush.txt")
sample_text=state_union.raw("2006-GWBush.txt")
#Create a custom sentence tokenizer with training text
custom_sentence_tokenizer=PunktSentenceTokenizer(train_text)
#tokenize the sample text with the custom sentence tokenizer
tokenized=custom_sentence_tokenizer.tokenize(sample_text)

print(tokenized)
