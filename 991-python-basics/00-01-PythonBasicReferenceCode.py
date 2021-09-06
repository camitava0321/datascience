#!/usr/bin/python
#Author: Amitava Chakraborty

#%% - Section:1 - Comments in Python
#This entire line is a comment
print 'Hello User!'  #This is a side comment
text = "# This is not a comment because it's inside quotes."

#Multiline Comments
'''
This entire paragraph
is a
multi-line comment
'''


#%%-Section:2 - Quotes in Python
word='word' #Single quotes - in same line
sentence="This is a sentence" #double quotes - in same line
#triple quotes - spans multiple lines - indentation does not matter
paragraph="""This is a paragraph.
It is made up of
    multiple lines""" 

#%% - Section:3 - Input from user - Keyboard input
str=raw_input("\n\nEnter any Real Number : ")

#If we expect the user to type an integer -
#If the user types something other than a string of digits - this will throw an error:
real=int(raw_input("\n\nEnter any Real Number : "))



#%% - Section:4 - Variables
#4.1 - Standard Datatype
#4.1.1Number Datatype
#4.1.1.1 - int (signed integers)
counter = 100       #integer assignment
negativeNo = -443
#4.1.1.2 - long (long integers, they can also be represented in octal and hexadecimal)
longNo=51924361L
#4.1.1.3 - float (floating point real values)
miles = 1000.0      #float assignment
#4.1.1.4 - complex (complex numbers)
complexNo = 2+113j

#%% - 4.1.2 - String Datatype
name = "Amitava"    #string assignment
str = 'Hello World!'

#%% - 4.1.3 - List Datatype
list = [100,-443,1234L,234.86,3+2j,'Amitava',"Chakraborty"]

#%% - 4.1.4 - Tuple Datatype -  Immutable
#A tuple is a sequence data type - similar to list. 
#A tuple consists of a number of values separated by commas. 
#Unlike lists, however, tuples are enclosed within parentheses.

#The main differences between lists and tuples are: 
#Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, 
#while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. 
#Tuples can be thought of as read-only lists.
tuple = (100,-443,1234L,234.86,3+2j,'Amitava',"Chakraborty")
a = b = c = 1       #Multiple assignments
d,e,f = 9,10.3,"Chakraborty"    #Multiple assignments

#%% - 4.1.5 - Dictionary
#Python's dictionaries are kind of hash table type. 
#They work like associative arrays or hashes found in Perl and consist of key-value pairs. 
#A dictionary key can be almost any Python type, but are usually numbers or strings. 
#Values, on the other hand, can be any arbitrary Python object.

#Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([]).
dict = {"one":"network theory","two":"network science"}

#%% - 4.2 - Printing Variables
print real, counter, negativeNo
print longNo
print miles
print complexNo
print name
print list
print tuple
print dict


#%% - 4.3 - Variable Deletion
del a,b,c,d,e,f
#print a   #will produce runtime error

#4.3 - Variable Conversion
#4.3.1 - from String
print 'Original String: 443',' - converted to: ',int("443",10)

#Section:2 - Python Keywords
#And	exec	Not Assert finally or Break for pass Class from print
#Continue global raise def if return del import try elif in while
#else is with except lambda yield


#In Python, the 'null' object is the singleton None.
#The best way to check things for "Noneness" is to use the identity operator, is:
if foo is None:
 #   ...

