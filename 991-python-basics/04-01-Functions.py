#!/usr/bin/python
#Python - Operators
#Author: Amitava Chakraborty

#%% - Adding new functions

#def is a keyword that indicates that this is a function definition. 
#function names - same as variable names
#first line of function definition is the header - end with a colon
def print_text():
#doesn’t take any arguments.
#the rest is body - has to be indented. 
    print("ABC DEF")
    print("A1B2C3")

#To end the function - enter an empty line.

#Defining a function creates a function object, which has type function:
print(print_text)
print type(print_text)
print_text()


#%% - A function can be used inside another function
def print_text_twice():
    print_text()
    print_text()

print_text_twice()



#%% - Recursion
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

#Now we call this function as
countdown(3)

#%% - Another example - a function that prints a string n times.
def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

#%% - Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


#%% - Factorial
def factorial(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    elif n == 0:
        return 1
    else:        
        recurse = factorial(n-1)
        result = n * recurse
        return result

factorial(1.5)

