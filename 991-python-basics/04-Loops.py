#While loop
count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1

print ("Good bye!")

#Infinite loop
var = 1
while var == 1 :  # This constructs an infinite loop
   num = int(input("Enter a number  :"))
   print ("You entered: ", num)

print ("Good bye!")

#Else statement in loop
count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")
   
#while as a suite
flag = 1

while (flag): print ('Given flag is really true!')

print ("Good bye!")



#For Loops
#print range of a number
print(range(0,5))

for letter in 'Python':     # traversal of a string sequence
   print ('Current Letter :', letter)
print()
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # traversal of List sequence
   print ('Current fruit :', fruit)

print ("Good bye!")


#Iterating by Sequence Index
#An alternative way of iterating through each item is by index offset into the sequence itself

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('Current fruit :', fruits[index])

print ("Good bye!")   

#Using else Statement with Loops
numbers=[11,33,55,39,55,75,37,21,23,41,13]

for num in numbers:
    if num%2==0:
        print ('the list contains an even number')
        break
else:
    print ('the list doesnot contain even number')

#Nested loops
for i in range(1,11):
    for j in range(1,11):
        k=i*j
        print (k)
    print()

#Python - Loop Breaks
for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print ('Current Letter :', letter)
  
var = 10                    # Second Example
while var > 0:              
   print ('Current variable value :', var)
   var = var -1
   if var == 5:
      break

print ("Good bye!")

#Following program demonstrates use of break in a for loop iterating over a list. User inputs a number which is searched in the list. If found, loop terminates with 'found' message
no=int(input('any number: '))
numbers=[11,33,55,39,55,75,37,21,23,41,13]

for num in numbers:
    if num==no:
        print ('number found in list')
        break
else:
    print ('number not found in list')    
    
#Use of continue
for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print ('Current Letter :', letter)

var = 10                    # Second Example
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print ('Current variable value :', var)
print ("Good bye!")

#pass statement
#Used when a statement is required syntactically but you do not want any command or code to execute.
#The pass statement is a null operation; nothing happens when it executes. 
#The pass is also useful in places where your code will eventually go, but has not been written yet (e.g., in stubs for example):
for letter in 'Python': 
   if letter == 'h':
      pass
      print ('This is pass block')
   print ('Current Letter :', letter)

print ("Good bye!")    

#Iterator is an object which allows a programmer to traverse through all the elements of a collection, regardless of its specific implementation. In Python iterator object implements two methods : iter() and next()
#String, List or Tuple object can be used to create an Iterator

list=[1,2,3,4]
it = iter(list) # this builds an iterator object
print (next(it)) #prints next available element in iterator

#Iterator object can be traversed using regular for statement
for x in it:
   print (x, end=" ")

or using next() function

while True:
   try:
      print (next(it))
   except StopIteration:
      sys.exit() #you have to import sys module for this

#A generator is a function that produces or yields a sequence of values using yield method.
#When a generator function is called, it returns an generator object without even beginning execution of the function. When next() method is called for the first time, the function starts executing until it reaches yield statement which returns the yielded value. The yield keeps track of i.e. remembers last execution. And second next() call continues from previous value.
#Following example defines a generator which generates an iterator for all the Fibonacci numbers. 
import sys
def fibonacci(n): #generator function
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(5) #f is iterator object

while True:
   try:
      print (next(f), end=" ")
   except StopIteration:
      sys.exit()      
      