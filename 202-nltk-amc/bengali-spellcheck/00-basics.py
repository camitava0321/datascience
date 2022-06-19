# -*- coding: utf-8 -*-
from spellchecker import SpellChecker

spell = SpellChecker()

#%%
print(spell.correction('বিদ্যলয়'))

#%% find those words that may be misspelled
misspelled = spell.unknown(['আমর', 'দেশ', 'বাংলাদশ'])

for word in misspelled:
    # Get the one `most likely` answer
    print(spell.correction(word))

    # Get a list of `likely` options
    print(spell.candidates(word))
    # output: বাংলাদেশ {'বাংলাদেশ'}
#%% - If the Word Frequency list is not to your liking, you can add additional text 
#to generate a more appropriate list for your use case.

from spellchecker import SpellChecker

spell = SpellChecker()  # loads default word frequency list
spell.word_frequency.load_text_file('my_free_text_doc.txt')

# if I just want to make sure some words are not flagged as misspelled
spell.word_frequency.load_words(['microsoft', 'apple', 'google'])
spell.known(['microsoft', 'google'])  # will return both now!

    