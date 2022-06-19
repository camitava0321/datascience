# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 21:48:19 2016

@author: Amitava
NLTK: POS Tagging
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
print(nltk.pos_tag(filtered_sentence))
    





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
            tagged=nltk.pos_tag(words)
            print(tagged)
        
        
    except Exception as e:
        print(str(e))

#invoke the POS tagging function
process_content()
"""
POS Tags

Alphabetical list of part-of-speech tags used in the Penn Treebank Project:
Number
	
Tag
	
Description
1. 	CC 	Coordinating conjunction
2. 	CD 	Cardinal number
3. 	DT 	Determiner
4. 	EX 	Existential there
5. 	FW 	Foreign word
6. 	IN 	Preposition or subordinating conjunction
7. 	JJ 	Adjective
8. 	JJR 	Adjective, comparative
9. 	JJS 	Adjective, superlative
10. 	LS 	List item marker
11. 	MD 	Modal
12. 	NN 	Noun, singular or mass
13. 	NNS 	Noun, plural
14. 	NNP 	Proper noun, singular
15. 	NNPS 	Proper noun, plural
16. 	PDT 	Predeterminer
17. 	POS 	Possessive ending
18. 	PRP 	Personal pronoun
19. 	PRP$ 	Possessive pronoun
20. 	RB 	Adverb
21. 	RBR 	Adverb, comparative
22. 	RBS 	Adverb, superlative
23. 	RP 	Particle
24. 	SYM 	Symbol
25. 	TO 	to
26. 	UH 	Interjection
27. 	VB 	Verb, base form
28. 	VBD 	Verb, past tense
29. 	VBG 	Verb, gerund or present participle
30. 	VBN 	Verb, past participle
31. 	VBP 	Verb, non-3rd person singular present
32. 	VBZ 	Verb, 3rd person singular present
33. 	WDT 	Wh-determiner
34. 	WP 	Wh-pronoun
35. 	WP$ 	Possessive wh-pronoun
36. 	WRB 	Wh-adverb

"""
