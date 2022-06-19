# -*- coding: utf-8 -*-
import nltk

#Append the nltk folder in the data path
#nltk.data.path.append("D:\\DevelopmentWorkspaces\\Python\\Canopy\\nltk")
#nltk.data.path.append("C:\\Amitava\\DevelopmentWorkspaces\\Python\\Canopy\\nltk-amc\\nltk-data")
nltk.data.path.append("nltk-data")
#First step : load some texts to explore
#"from NLTK's book module, load all items."
#The book module contains all the data one needs for practice. 
#This command loads the text of several books
from nltk.book import *

#To find out about texts corresponding to a book
#just access the variable representing the book
text1  #Moby Dick by Herman Melville 1851
text2  #Sense and Sensibility by Jane Austen 1811

#%% - Searching Text
#Method1 : Examine the context of a text
#A concordance permits us to see words in context. 
#The first time use of concordance on a particular text - 
#builds an index so that subsequent searches are fast.
text1.concordance("monstrous")

#%% - Searching Text
#Method 2: access a broader range of text
#What other words appear in a similar range of contexts?
text1.similar("monstrous")
text2.similar("monstrous")
#Observe that we get different results for different texts. 
#For Austen this word has positive connotations, 
#and sometimes functions as an intensifier like the word very.

#%% - Searching Text
#Method 3: common_contexts 
#allows us to examine just the contexts that are shared by 
#two or more words, such as monstrous and very. 
text2.common_contexts(["monstrous", "very"])

#%% - Searching Text
#Method 4: Determine the location of a word in the text
#How many words from the beginning it appears. 
#This positional information can be displayed using a dispersion plot. 
#Each stripe represents an instance of a word, 
#and each row represents the entire text. 
#In the plot we see some striking patterns of word usage over the last 220 years
#You might like to try more words (e.g., liberty, constitution), and different texts. 
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
text4.dispersion_plot(["liberty","constitution"])

#%% - Vocabulary
#Counting Vocabulary - count the words in a text in a variety of ways. 
#The texts differ in the vocabulary they use. 
#Length of a text
print(len(text3))

#So Genesis has 44,764 words and punctuation symbols, or "tokens." 
#A token is the technical name for a sequence of characters — such as hairy, his, or :) 
#When we count the number of tokens in a text, say, the phrase to be or not to be, 
#we are counting occurrences of these sequences. 
#Thus, in our example phrase there are two occurrences of to, two of be, and one each of or and not. 
#But there are only four distinct vocabulary items in this phrase. 
#So, how many distinct words does the book of Genesis contain? 
#The vocabulary of a text is just the set of tokens that it uses,
#since in a set, all duplicates are collapsed together. 
sorted(set(text3))
print(len(set(text3)))
unique_item_types=len(set(text3))

#So, although the text text3 has 44,764 tokens, it has only 2,789 distinct words
#we will generally call these unique items types instead of word types.

#Lexical richness of a text: 
#each word is used 16 times on average
print(float(len(set(text3)))/len(text3))

#On particular words
#Count how often a word occurs in a text, 
#Then compute what percentage of the text is taken up by a specific word
print(text3.count("smote"))
print(100 * float(text4.count('a'))/len(text4))
print(100 * float(text5.count('lol'))/len(text5))

#%% - 
#We want to repeat such calculations on several texts
#So we will have our own function 'lexical_diversity'
#so that we can re-use it
def lexical_diversity(text):
    return float(len(set(text)))/len(text)
def percentage(count, total):
    return 100 * count/total

lexical_diversity(text4)
lexical_diversity(text7)
percentage(float(text6.count('a')),len(text6))

#%% - Sentences
#Some sentences have been defined for exxperiments - opening sentence of each of our texts
#sent1 … sent9. 
sent1
sent2
lexical_diversity(sent1)
lexical_diversity(sent1+sent9)


#%% - Indexing Lists
#A text in Python is a list of words
#represented using a combination of brackets and quotes
#We can pick out the 1st, 173rd, or even 14,278th word in a printed text. 
#The number that represents this position is the item's index. 
#show us the item that occurs at an index 173 in a text
text4[173]
#Or the converse; given a word, find the index of when it first occurs:
text4.index('awaken')

#Extract manageable pieces of language from large texts - slicing.
text5[16715:16735]
text6[1600:1625]
my_sentnc=text2[141525:]
#Sort it - Remember that capitalized words appear before lowercase words in sorted lists.
sorted(text2[141525:])

#%% - Computing with Language: Simple Statistics
#What makes a text distinct
#Use automatic methods to find characteristic words and expressions of a text.
tokens=set(my_sentnc)
tokens=sorted(tokens)
tokens[-2:]

#Before continuing further, you might like to check your understanding of the last section by predicting the output of the following code. You can use the interpreter to check whether you got it right. If you're not sure how to do this task, it would be a good idea to review the previous section before continuing further.