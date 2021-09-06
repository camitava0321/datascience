# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 15:18:19 2017

@author: Amitava
Data Types
"""
import numpy as np
#NumPy supports a much greater variety of numerical types than Python does. 
#The following table shows different scalar data types defined in NumPy.
#Sr.No. 	Data Types & Description
#1 bool_  Boolean (True or False) stored as a byte
#2 int_   Default integer type (same as C long; normally either int64 or int32)
#3 intc   Identical to C int (normally int32 or int64)
#4 intp   Integer used for indexing (same as C ssize_t; normally either int32 or int64)
#5 int8   Byte (-128 to 127)
#6 int16  Integer (-32768 to 32767)
#7 int32  Integer (-2147483648 to 2147483647)
#8 int64  Integer (-9223372036854775808 to 9223372036854775807)
#9 uint8  Unsigned integer (0 to 255)
#10 uint16 Unsigned integer (0 to 65535)
#11 uint32 Unsigned integer (0 to 4294967295)
#12 uint64 Unsigned integer (0 to 18446744073709551615)
#13 float_ Shorthand for float64
#14 float16 Half precision float: sign bit, 5 bits exponent, 10 bits mantissa
#15 float32 Single precision float: sign bit, 8 bits exponent, 23 bits mantissa
#16 float64 Double precision float: sign bit, 11 bits exponent, 52 bits mantissa
#17 complex_ Shorthand for complex128
#18 complex64 Complex number, represented by two 32-bit floats (real and imaginary components)
#19 complex128 Complex number, represented by two 64-bit floats (real and imaginary components)

#NumPy numerical types are instances of dtype objects
#The dtypes are available as np.bool_, np.float32, etc.

#Data Type Objects (dtype)
#A data type object describes interpretation of fixed block of memory corresponding to an array, 
#depending on the following aspects −
#    Type of data (integer, float or Python object)
#    Size of data
#    Byte order (little-endian or big-endian)
#    In case of structured type, the names of fields, 
#       data type of each field and part of the memory block taken by each field.
#    If data type is a subarray, its shape and data type

#A dtype object is constructed using the following syntax −
#numpy.dtype(object, align, copy)
#parameters
#    Object − To be converted to data type object
#    Align − If true, adds padding to the field to make it similar to C-struct
#    Copy − Makes a new copy of dtype object. If false, the result is reference to builtin data type object

# using array-scalar type 
dt = np.dtype(np.int32) 
print dt
print dt.itemsize #how many bytes ?

#int8, int16, int32, int64 can be replaced by equivalent string 'i1', 'i2','i4', etc. 
dt = np.dtype('i4')
print dt 

#Each built-in data type has a character code that uniquely identifies it
#Character codes are included for backward compatibility with Numeric. 
#Their use is not recommended, but the codes are provided here because they pop up in several places. 
#One should instead use the dtype objects. 
#The following table shows different data types and character codes associated with them:
#    'b' − boolean
#    'i' − (signed) integer
#    'u' − unsigned integer
#    'f' − floating-point
#    'c'/D − complex-floating point
#    'm' − timedelta
#    'M' − datetime
#    'O' − (Python) objects
#    'S', 'a' − (byte-)string
#    'U' − Unicode
#    'V' − raw data (void)

a = np.arange(7, dtype='D')
print a
#But there is no fill-function for data-type for every datatype
a = np.arange(7, dtype='S')

#A listing of all data type names
print np.sctypeDict.keys()

#dtype attributes
#information about the character code of a data type
t = np.dtype('Float64')
t.char

#type of object of array elements:
t.type

#string representation of a data type
#starts with a character '<' or '>' representing endianness, if appropriate, then a character code, 
#followed by a number corresponding to the number of bytes that each array item requires
#endianness : the way bytes are ordered within a 32- or 64-bit word. 
#In the big-endian order, the most significant byte is stored first, which is indicated by '>'.
#In the little-endian order, the least significant byte is stored first, which is indicated by < .
t.str
#The byte order is decided by prefixing '<' or '>' to data type. 
#'<' means that encoding is little-endian (least significant is stored in smallest address). 
#'>' means that encoding is big-endian (most significant byte is stored in smallest address).
# using endian notation 
dt = np.dtype('>i4') 
print dt



#Creating structured data type. 
#Here, the field name and the corresponding scalar data type is to be declared.
# first create structured data type 
dt = np.dtype([('age',np.int8)]) 
print dt 
# now apply it to ndarray object 
a = np.array([(10,),(20,),(30,)], dtype = dt) 
print a
# file name can be used to access content of age column 
print a['age']
print a['age'][2]

#Creating a record data type
#A record data type is a heterogeneous data type—think of it as representing a row in
#a spreadsheet or a database.

#The following examples define a structured data type called student with a string field 'name', 
#an integer field 'age' and a float field 'marks'. This dtype is applied to ndarray object.
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
print student
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
print a

#record daratype for a shop inventory
#This record contains 
#name of an item represented by a 40-character string
#number of items in the store represented by a 32-bit integer
#price of the item represented by a 32-bit float
t = np.dtype([('name', np.str_, 40), ('numitems', np.int32), ('price',np.float32)])
t

#So what is the type of a field of the datatype?
t['name']

#If you don't give the array() function a data type, 
#it will assume that it is dealing with floating point
#To create an array now, we really have to specify the data type
itemz = np.array([('Meaning of life DVD', 42, 3.14), ('Butter', 13, 2.72)], dtype=t)
itemz
itemz[1]





