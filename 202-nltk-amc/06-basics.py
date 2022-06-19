# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 21:48:19 2016

@author: Amitava
NLTK: Chunking - Group words into meaningful chunks
Main goal - group 'noun phrases.' - idea is to group nouns with the words that are in relation to them.

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
tagged = nltk.pos_tag(filtered_sentence)
    
#In order to chunk, we combine the part of speech tags with regular expressions.
#Create a chunkgram
#1. <RB.?>* = "0 or more of any tense of adverb," followed by:
#2. <VB.?>* = "0 or more of any tense of verb," followed by:
#3. <NNP>+ = "One or more proper nouns," followed by
#4. <NN>? = "zero or one singular noun."
chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
chunkParser = nltk.RegexpParser(chunkGram)
chunked = chunkParser.parse(tagged)
#See the chunking visually
chunked.draw()

#Access chunking data
#"chunked" variable is an NLTK tree. 
#Each "chunk" and "non chunk" is a "subtree" of the tree. 
#We can reference these by doing something like chunked.subtrees. 
for subtree in chunked.subtrees():
                print(subtree)

#Filter-out the non-chunks
for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
    print(subtree)                
