# -*- coding: utf-8 -*-
# Amitava Chakraborty, 2022
import nltk
import re
from nltk.corpus import wordnet
   
R_patterns = [
   (r'\n', ' '),
   (r'\t', ' '),
   (r'won\'t', 'will not'),
   (r'can\'t', 'cannot'),
   (r'i\'m', 'i am'),
   (r'(\w+)\'ll', '\g<1> will'),
   (r'(\w+)n\'t', '\g<1> not'),
   (r'(\w+)\'ve', '\g<1> have'),
   (r'(\w+)\'s', '\g<1> is'),
   (r'(\w+)\'re', '\g<1> are')]

class REReplacer(object):
    def __init__(self, patterns=R_patterns):
        self.patterns = [(re.compile(regex), repl) for (regex, repl) in patterns]
    
    def replace(self, text):
        s = text
        for (pattern, repl) in self.patterns:
           s = re.sub(pattern, repl, s)
        return s

# Removal of repeating characters
# Sometimes we find ‘Hiiiiiiiiiiii ..’ in order to emphasize the word ‘Hi’. 
# But computer system does not know that ‘Hiiiiiiiiiiii’ is a variation of the word “Hi”. 
# Following class can be used for removing such repeating words.
class Rep_word_removal(object):
    def __init__(self):
        self.repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
        self.repl = r'\1\2\3'
    def replace(self, word):
        if wordnet.synsets(word):
            return word
        repl_word = self.repeat_regexp.sub(self.repl, word)
        if repl_word != word:
            return self.replace(repl_word)
        else:
            return repl_word