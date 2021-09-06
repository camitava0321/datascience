#Python - Data Type Conversion
#To convert between types, one simply use the type name as a function.
#There are several built-in functions to perform conversion from one data type to another. 
#These functions return a new object representing the converted value.



#Number Type Conversion
#Python converts numbers internally in an expression containing mixed types to a 
#common type for evaluation. 
#But sometimes, you need to coerce a number explicitly from one type to another 
#to satisfy the requirements of an operator or function parameter.

str="123"
print (int(str))    #int(x) - convert x to a plain integer.

#TODO: int(x [,base])
#Converts x to an integer. base specifies the base if x is a string.


str="123456789L"
print (long(str))   #long(x) - convert x to a long integer.

str="123.46" 
print (float(str))  #float(x) - convert x to a floating-point number.


img=3.23 
print complex(str) #complex(x) - convert x to a complex number with real part x and imaginary part zero.
print complex(float(str),img) #complex(x, y) - convert x and y to a complex number with real part x and imaginary part y. x and y are numeric expressions





#str(x)
#Converts object x to a string representation.

#repr(x)
#Converts object x to an expression string.


#eval(str)
#Evaluates a string and returns an object.

#tuple(s)
#Converts s to a tuple.

#list(s)
#Converts s to a list.


#set(s)
#Converts s to a set.

#dict(d)
#Creates a dictionary. d must be a sequence of (key,value) tuples.

#frozenset(s)
#Converts s to a frozen set.

#chr(x)
#Converts an integer to a character.

#unichr(x)
#Converts an integer to a Unicode character.

#ord(x)
#Converts a single character to its integer value.

#hex(x)
#Converts an integer to a hexadecimal string.

#oct(x)
#Converts an integer to an octal string.