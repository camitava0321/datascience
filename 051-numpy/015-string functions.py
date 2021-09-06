# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
"""

String Functions
Advertisements
Previous Page
Next Page  

The following functions are used to perform vectorized string operations for arrays of dtype numpy.string_ or numpy.unicode_. They are based on the standard string functions in Python's built-in library.
Sr.No. 	Function & Description
1 	add()

Returns element-wise string concatenation for two arrays of str or Unicode
2 	multiply()

Returns the string with multiple concatenation, element-wise
3 	center()

Returns a copy of the given string with elements centered in a string of specified length
4 	capitalize()

Returns a copy of the string with only the first character capitalized
5 	title()

Returns the element-wise title cased version of the string or unicode
6 	lower()

Returns an array with the elements converted to lowercase
7 	upper()

Returns an array with the elements converted to uppercase
8 	split()

Returns a list of the words in the string, using separatordelimiter
9 	splitlines()

Returns a list of the lines in the element, breaking at the line boundaries
10 	strip()

Returns a copy with the leading and trailing characters removed
11 	join()

Returns a string which is the concatenation of the strings in the sequence
12 	replace()

Returns a copy of the string with all occurrences of substring replaced by the new string
13 	decode()

Calls str.decode element-wise
14 	encode()

Calls str.encode element-wise

These functions are defined in character array class (numpy.char). The older Numarray package contained chararray class. The above functions in numpy.char class are useful in performing vectorized string operations.