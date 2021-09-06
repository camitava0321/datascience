#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author: Amitava Chakraborty

'''
List of primary regular expressions
. (a period): This expression matches any single character except newline \n.
\w: This expression will match a character or a digit equivalent to [a-z A-Z
0-9]
\W (upper case W) matches any non-word character.
\s: This expression (lowercase s) matches a single whitespace character -
space, newline, return, tab, form [\n\r\t\f].
\S: This expression matches any non-whitespace character.
\t: This expression performs a tab operation.
\n: This expression is used for a newline character.
\r: This expression is used for a return character.
\d: Decimal digit [0-9].
^: This expression is used at the start of the string.
$: This expression is used at the end of the string.
\: This expression is used to nullify the specialness of the special character.
'''
#A substring search is one of the common use-cases of the re module
import re
mystring = 'Python is a constrictor!!'
if re.search('Python',mystring):
    print "We found python "
else:
    print "NO "

#Find all the patterns in a string - findall. 
#gives a list of all the matched objects:
import re
print re.findall('!',mystring)