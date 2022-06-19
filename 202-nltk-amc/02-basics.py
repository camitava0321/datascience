# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 21:48:19 2016

@author: Amitava
NLTK: Words Tokenizing
"""

import nltk
#Append the nltk folder in the data path
nltk.data.path.append("nltk-data")

from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer 
from nltk.tokenize import sent_tokenize, word_tokenize

#Let us first get the sentences
EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
#One does not need to extract sentences first to extract words
print(word_tokenize(EXAMPLE_TEXT))

#punctuation is treated as a separate token
#word "shouldn't" is separated into "should" and "n't." 
#"pinkish-blue" is treated like 'one word'

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
            print(words)
        
        
    except Exception as e:
        print(str(e))

#invoke the word tokenize function
process_content()