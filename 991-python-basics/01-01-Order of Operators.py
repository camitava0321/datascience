#!/usr/bin/python
#Author: Amitava Chakraborty

#%% - Section:1 - PEMDAS
#For mathematical operators, Python follows mathematical convention. 
#The acronym PEMDAS is a useful way to remember the rules
#Parentheses () - highest precedence
#Expressions in parentheses are evaluated first,
print 2 * (3-1)
print (1+1)**(5-2)

#Exponentiation - next highest
print 1 + 2**3
#result is 9, not 27
print 2 * 3**2
#result is 18, not 36.

#Multiplication and Division - higher precedence than Addition and Subtraction
print 2*3-1
#result is 5, not 4

print 6+4/2
#result is is 8, not 5.

#%% - Evaluation Direction
#Operators with the same precedence are evaluated from left to right
#(except exponentiation).
#So in the expression - the division happens first and the result is multiplied by pi. 
degrees = 60 
pi = 22/7
print degrees / 2 * pi
#To divide by 2p, you can use parentheses or write 
print degrees / 2 / pi
