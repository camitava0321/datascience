#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author: Amitava Chakraborty

'''
A sequence of immutable Python objects. 
Tuples are sequences, just like lists - But READONLY and tuples use parentheses while lists use square brackets.
'''
#Create a tuple 
tup1 = ('engineering physics', 'mathematical physics', 53.67, 1970)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

#The empty tuple
empty_tup1 = ()

#A tuple containing a single value - 
#one must include a comma, even though there is only one value −
tup4 = (50,)

'''
Like string indices, tuple indices start at 0, 
#and they can be sliced, concatenated, and so on.
'''
#Access values in tuple
#use the square brackets for slicing with the index or indices 
print(tuple)           # Prints complete list
print (tuple[0])        # Prints first element of the list
print (tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print (tuple[2:])       # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints list two times
print (tuple + tinytuple) # Prints concatenated lists
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

#Updating Tuples - tuples cannot be updated as they are immutable
#One can only take portions of existing tuples to create new tuples 
tup5 = (12, 34.56)
tup6 = ('abc', 'xyz')

#Join tuples
tup7 = tup1 + tup2
print (tup7)

#Delete Tuple Elements - not possible
#Way out - create another tuple with the undesired elements discarded.

#Remove an entire tuple
del tup7;
print ("After deleting tup7 : ")
#print (tup7)
#The above, if unremarked, will issue an error
#NameError: name 'tup7' is not defined


#Basic Tuples Operations
#In fact, tuples respond to all of the general sequence operations used on strings

#+ and * operators much like strings; - for concatenation and repetition
#except that the result is a new tuple, not a string.

#Concatenation
tup7=(1, 2, 3)
tup8=(4, 5, 6)
print(tup7+tup8)
#Repetition
tup9=('Hi!',)
print(tup9* 4)

#Membership
print(3 in tup7)
#Iteration
for x in tup8: 
    print (x, end=' ')

#Indexing, Slicing, and Matrixes
#Because tuples are sequences, indexing and slicing work the same way 
#for tuples as they do for strings. 
T=('C++', 'Java', 'Python')
#Offsets start at zero
print(T[2]) 
#Negative: count from the right
print(T[-2])
#Slicing fetches sections
print(T[1:])


#Built-in Tuple Functions

#Compares elements of both tuples.
#If elements are of the same type, perform the compare and return the result. 
#If elements are different types, check to see if they are numbers.
#    If numbers, perform numeric coercion if necessary and compare.
#    If either element is a number, then the other element is "larger" (numbers are "smallest").
#    Otherwise, types are sorted alphabetically by name.

#If we reached the end of one of the tuples, the longer tuple is "larger." 
#If we exhaust both tuples and share the same data, the result is a tie, 
#meaning that 0 is returned.
tuple1, tuple2 = (123, 'xyz'), (456, 'abc')

print (tuple1 < tuple2)
print (tuple2 < tuple1)
tuple3 = tuple2 + (786,);
print (tuple2 > tuple3)

#Gives the total length of the tuple.
len(tuple)

#Returns item from the tuple with max value.
tuple1, tuple2 = ('maths', 'che', 'phy', 'bio'), (456, 700, 200)

print ("Max value element : ", max(tuple1))
print ("Max value element : ", max(tuple2))

#Returns item from the tuple with min value.
tuple1, tuple2 = ('maths', 'che', 'phy', 'bio'), (456, 700, 200)

print ("min value element : ", min(tuple1))
print ("min value element : ", min(tuple2))

#Converts a list into tuple.
L= ['maths', 'che', 'phy', 'bio']

T=tuple(L)
print ("tuple elements : ", T)


