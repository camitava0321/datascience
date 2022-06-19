'''
Created on May 23, 2016

@author: Amitava Chakraborty
'''
from builtins import int


if __name__ == '__main__':

    print("Hello Python")


# this is the first comment
spam = 1  # and this is an inline second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."
tax = 12.5 / 100
price = 100.50
price * tax
#price +=_
#round(_, 2)

#Python Number
counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
complexVar1 = 3.14j    # A Complex Number

var1 = 1
var2 = 10


#Python Strings
name    = "John"       # A string
str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

#Python Lists
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)          # Prints complete list
print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd 
print (list[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (list + tinylist) # Prints concatenated lists


#Multiple assignment
a=b=c=1;
d,e,f=2,3,"john"


#delete variables
del var1, var2


#Python Tuples
#A tuple is a sequence data type - similar to list. 
#A tuple consists of a number of values separated by commas. 
#Unlike lists, however, tuples are enclosed within parentheses.

#The main differences between lists and tuples are: 
#Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, 
#while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. 
#Tuples can be thought of as read-only lists.
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)           # Prints complete tuple
print (tuple[0])        # Prints first element of the tuple
print (tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print (tuple[2:])       # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints tuple two times
print (tuple + tinytuple) # Prints concatenated tuple


#Python Dictionary
#Python's dictionaries are kind of hash table type. 
#They work like associative arrays or hashes found in Perl and consist of key-value pairs. 
#A dictionary key can be almost any Python type, but are usually numbers or strings. 
#Values, on the other hand, can be any arbitrary Python object.

#Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([]).
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values


print (counter)
print (miles)
print (name)

'spam eggs'  # single quotes
'spam eggs'
'doesn\'t'  # use \' to escape the single quote...
"doesn't"
"doesn't"  # ...or use double quotes instead
"doesn't"
'"Yes," he said.'
'"Yes," he said.'
"\"Yes,\" he said."
'"Yes," he said.'
'"Isn\'t," she said.'
'"Isn\'t," she said.'

#Python - Data Type Conversion
#To convert between types, one simply use the type name as a function.
#There are several built-in functions to perform conversion from one data type to another. 
#These functions return a new object representing the converted value.

#int(x [,base]) - Converts x to an integer. base specifies the base if x is a string.
print(int("123")) #default base is decimal
print(int("1011010",base=2)) #converts binary to integer

#float(x) - Converts x to a floating-point number.
#complex(real [,imag]) - Creates a complex number.
print(complex(3,2))
#str(x) - Converts object x to a string representation.
#repr(x) - Converts object x to an expression string. - printable representation of an object
#eval(str) - Evaluates a string and returns an object.
#tuple(s) - Converts s to a tuple.
#list(s) - Converts s to a list.
#set(s) - Converts s to a set.
#dict(d) - Creates a dictionary. d must be a sequence of (key,value) tuples.
#frozenset(s) - Converts s to a frozen set.
#chr(x) - Converts an integer to a character.
#unichr(x) - Converts an integer to a Unicode character.
#ord(x) - Converts a single character to its integer value.
#hex(x) - Converts an integer to a hexadecimal string.
#oct(x) - Converts an integer to an octal string.