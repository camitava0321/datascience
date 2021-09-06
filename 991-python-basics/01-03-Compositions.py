#!/usr/bin/python
#Author : Amitava Chakraborty
#Python - Composition

#Almost anywhere you can put a value, you can put an arbitrary expression
#with one exception:
#the left side of an assignment statement has to be a variable name
#Any other expression on the left side is a syntax error 
hours = 6
minutes = hours * 60 
print minutes
# right
hours * 60 = minutes 
# wrong!
#(we will see exceptions to this rule later).
