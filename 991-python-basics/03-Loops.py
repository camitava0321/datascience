#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author : Amitava Chakraborty

#while loop
#Finite Loop
count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1


#Using else in while - Loops with Boundary
count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"

#Infinite Loop
var = 1
while var == 1 :  # This constructs an infinite loop
   num = raw_input("Enter a number  :")
   if int(num,10)>100:
       break
   print "You entered: ", num
                              
#For Loop
for letter in 'Python':     # First Example
   print 'Current Letter :', letter

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
   print 'Current fruit :', fruit

#Iterating by Sequence Index
#An alternative way of iterating through each item is by index offset into the sequence itself. Following is a simple example −
for index in range(len(fruits)):
   print 'Current fruit :', fruits[index]
   
#Using else Statement with Loops
for num in range(10,20):  #to iterate between 10 to 20
  if num%3 == 0:      #to determine if divisible by 3
     print '%d is divisible by 3' % num
  else:                  # else part of the loop
     print num, '%d is NOT divisible by 3' % num                                 