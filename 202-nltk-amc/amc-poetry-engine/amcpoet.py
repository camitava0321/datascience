#!/usr/bin/env python
"""
 AMC Poetry Engine
 author : Amitava Chakraborty, Feb 2018
   amcpoet.py [number of couplets] [approximate syllables per line] [rhyming depth]
   Defaults : [number of couplets] 2,  [approximate syllables per line] 7,  [rhyming depth] 2 
"""
import sys, re
from random import choice
import nltk
#Append the nltk folder in the data path
#nltk.data.path.append("D:\\DevelopmentWorkspaces\\Python\\Canopy\\nltk")
nltk.data.path.append("H:/DevelopmentWorkspaces/Python/datascience/202-nltk-amc/nltk-data")

from nltk.corpus import cmudict, gutenberg

#Standard dictionary, comes packaged in nltk
DICTIONARY = cmudict.dict()
REPOSITORY = {}
#The corpus to choose words from
CORPUS = [
            'bible-kjv.txt',
            'blake-poems.txt',
            'austen-sense.txt',
            'shakespeare-caesar.txt',
            'melville-moby_dick.txt',
            'whitman-leaves.txt',
            'burgess-busterbrown.txt',
            'milton-paradise.txt',
            'bryant-stories.txt',
            'chesterton-thursday.txt',
            'austen-emma.txt',
            'austen-persuasion.txt',
            'carroll-alice.txt',
            'chesterton-ball.txt',
            'chesterton-brown.txt',
            'edgeworth-parents.txt',
            'shakespeare-hamlet.txt',
            'shakespeare-macbeth.txt',
            'whitman-leaves.txt'

            # Feel free to add more texts here. For a full list of texts,
            # open the python shell, and run:
            #
            #  from nltk.corpus import gutenberg
            #  gutenberg.fileids()
        ]
USED_ENDINGS = []

#Main function
def main(num_couplets, num_syllables, rhyme_depth):
  
  #create the repository  
  print('Creating Repository...')
  for fileid in CORPUS: 
    for sentence in gutenberg.sents(fileid): 
      addSentence(sentence, rhyme_depth)  #add a valid sentence to the repository 
  
  #print REPOSITORY  
  for couplet_number in range(0, num_couplets):
    # Get a randomly selected couplet
    attempts = 0
    while True:
      couplet = getCouplet(num_syllables)
      if couplet is not None: break
      # Prevent an infinite loop if parameters are off
      attempts += 1
      if attempts == 1000: return
    couplet = [ pretty(line) for line in couplet ]

    #Punctuation and capitalization adjustments
    couplet[0] = couplet[0][0].upper() + couplet[0][1:] #Capitalise first letter
    if couplet[0][-1] == '.' or couplet[0][-1] == ',':
      couplet[0] = couplet[0][:-1] + ','
      char = couplet[1][0].upper() if couplet[1][:2] != 'I ' else 'I'
      couplet[1] = char + couplet[1][1:]
    else:
      couplet[1] = couplet[1][0].upper() + couplet[1][1:]

    #Print to stdout
    print (couplet[0])
    print (couplet[1])

#Checks a sentence for its validity, 
#cleans words of numbers
#manages DICTIONARY
#add each word in the repository based on its #of syllables and rhyming depth
def addSentence(sentence, rhyme_depth):
  """Analyze an array of words and add it to the sentence REPOSITORY."""
  #we do not need a sentence that has more than 20 words
  if len(sentence) > 20: return
  
  #Clean every occurences of digits from the word
  #\d - a shorthand character class, which matches all numbers; it is the same as [0-9]
  def _clean(word):
    return re.sub(r'\d+', '', word).lower()
  def _is_word(token):    #If the word exists in the dictionary
    return _clean(token) in DICTIONARY

  recognized_words = [ _clean(w) for w in sentence if _is_word(w) ]
  if len(recognized_words) < 3: return   #we do not want a list of words that is less than 3

  # pronounced = phonetic pronunciation and syllable count from CMUDict
  pronounced = [ DICTIONARY[w][0] for w in recognized_words ]

  # CMUDict format - a number as the last character 
  #represents a syllable (not the number of syllables, just the fact that one is present)
  syllables = [ len([ y for y in x if y[-1].isdigit() ]) for x in pronounced ]
  num_syllables = sum(syllables)

  # The rhyme ending is the last n phonemes from the pronunciation of the
  # last word. It's not perfect, but it works well enough.
  rhyme_ending = tuple(pronounced[-1][-rhyme_depth:])

  # Create a record for the sentence
  record = (recognized_words[-1], num_syllables, sentence)

  # Save this sentence keyed by the rhyme-ending
  if rhyme_ending not in REPOSITORY: REPOSITORY[rhyme_ending] = []
  REPOSITORY[rhyme_ending].append(record)


def getCouplet(num_syll):
  """Generate a couplet with an approximate number of syllables, or return None."""
  keyLength=len(REPOSITORY.keys())
  ending_index=choice(range(0,keyLength))
  ending = list(REPOSITORY.keys())[ending_index]
  if ending in USED_ENDINGS: return None        # used already? if so, abort
  line1 = choice(REPOSITORY[ending])            # two random lines with chosen rhyme ending
  line2 = choice(REPOSITORY[ending])
  if line1[0] == line2[0]: return None          # same last word in both lines
  if abs(line1[1] - num_syll) > 1: return None  # wrong syllable count +/- 1 syllable
  if abs(line2[1] - num_syll) > 1: return None  # wrong syllable count +/- 1 syllable
  USED_ENDINGS.append(ending)                   # don't use this rhyme ending again
  return (line1[-1], line2[-1])

def pretty(words):
  """Some heuristics to adjust punctuation and spacing in a word array."""
  words = ' '.join(words)
  words = re.sub('\s*([\'\?\;\-\!])\s*', '\\1', words)  # extraneous spaces
  words = re.sub('\s*([;\.,])\s*', '\\1 ', words)       # space before punctuation
  words = re.sub('^[\'"]|["\']$', '', words)            # beginning and ending quotes
  words = re.sub('[":`_\(\)]', '', words)               # punctuation we just don't like
  words = re.sub('\s\s*', ' ', words)                   # extraneous whitespace
  words = words.strip()                                 # leading and trailing whitespace
  return words

if __name__ == '__main__':
  numberOfCouplets = 2
  numberOfSyllables = 10
  rhymeDepth = 3
  if len(sys.argv) >= 2: numberOfCouplets = int(sys.argv[1])
  if len(sys.argv) >= 3: numberOfSyllables = int(sys.argv[2])
  if len(sys.argv) >= 4: rhymeDepth = int(sys.argv[3])
  main(numberOfCouplets, numberOfSyllables, rhymeDepth)
