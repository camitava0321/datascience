#!/usr/bin/python
#Python - Operators
#Author: Amitava Chakraborty


#%% - Python Arithmetic Operators
var1, var2 = 10,21

print 'Addition : %d + %d = %d' % (var1,var2,var1+var2)
print 'Subtraction : %d - %d = %d' % (var1,var2,var1-var2)
print "Multiplication : %d * %d = %d" % (var1,var2,var1*var2)
print "Division : %d / %d = %f" % (var2,var1,var2/var1)
#modulus operator, %, - divides two numbers and returns the remainder.
print "Modulus : %d mod %d = %d" % (var2,var1,var2%var1)
print "Exponent : %d ** %d = %d" % (var2,var1,var2**var1);

#Floor Division - result is the quotient in which the digits after 
#the decimal point are removed. 
#But if one of the operands is negative, the result is floored, 
#i.e., rounded away from zero (towards negative infinity):     
#e.g., 9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0
print "Floor Division : %d // %d = %d" % (var2,20,var2//20) 

#%% - Python Assignment Operators
c=var1+var2
a=var1
c+=a
print("c+=a = ",c)
c-=a
print("c-=a = ",c)
c/=a
print("c/=a = ",c)
c**=a
print("c**=a = ",c)
c//=a
print("c//=a = ",c)

#%% - Python Comparison Operators - Boolean Expressions
a,b = 10,20
print("(a == b) : ",(a == b)) 
print("(a!= b) : ",(a!= b))
print("(a > b) : ",(a > b))
print("(a < b) : ",(a < b))
print("(a >= b) : ",(a >= b))
print("(a <= b) : ",(a <= b))


#%% - Python Bitwise Operators
#Bitwise operator works on bits and performs bit by bit operation. 
#Assume if a = 60 and b = 13 Now in binary format they will be as follows
a = 00111100
b = 00001101

print("a&b =",a&b)
print("a|b = ",a|b)
print("a^b = ",a^b)
print("~a  = ",~a)
#Bitwise operators supported by Python language
print("Binary AND : (a & b)",(a & b))
print("Binary OR : (a | b) = ",(a | b))
print("Binary XOR : (a ^ b) = ",(a ^ b))
print("Binary Ones Complement : (~a ) = ",~a)
print("Binary Left Shift : a << = 240 ",a<<1)
print("Binary Right Shift : a >> = 15 : ",a>>1)


#%% - Pyhton's built-in function bin() can be used to obtain binary representation of integer number.
print("Binary representation of a Number : bin(20) : ",bin(20))

#%% - Python Logical Operators
a,b = True, False
print("Logical AND : (a and b) : ",a and b)
print("Logical OR : (a or b) : ",a or b)
print("Logical NOT : not(a and b) : ", not(a and b))

#%% - Pythons membership operators test for membership in a sequence, such as strings, lists, or tuples 
#There are two membership operators as explained below
var = 30
sequence = (20, 30, 40, 50, 60)
print("var in sequence : ", var in sequence)
print("var not in sequence : ",var not in sequence)

#%% - Python Identity Operators
#Identity operators compare the memory locations of two objects. There are two Identity operators explained below:
a=b=10
d=30
print("a is b : ", a is b)
print("d is not b : ",d is not b)