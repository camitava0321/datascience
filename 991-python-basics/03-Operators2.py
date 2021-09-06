'''
Created on May 23, 2016

@author: ibm
'''

#Python - Operators
amount=int(input("Enter amount: "))

if amount<1000:
    discount=amount*0.05
    print ("Discount",discount)
else:
    discount=amount*0.10
    print ("Discount",discount)
    
print ("Net payable:",amount-discount)







#Nested If-Else
num=int(input("enter number"))
if num%2==0:
    if num%3==0:
        print ("Divisible by 3 and 2")
    else:
        print ("divisible by 2 not divisible by 3")
else:
    if num%3==0:
        print ("divisible by 3 not divisible by 2")
    else:
        print  ("not Divisible by 2 not divisible by 3")

#%% -
x=45        
if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')

#%% - Chained conditionals
#more than two branches - a chained conditional:
x=40
y=30
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')        

#%% - Nested conditionals
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')


#Logical operators often provide a simplified way to write nested conditional 
#statements. For example,we can rewrite the following code using a single 
#conditional:
if 0 < x:
    if x < 10:
        print('x is a positive single-digit number.')

#The print statement runs only if we make it past both conditionals, 
#so we can get the same effect with the and operator:

if 0 < x and x < 10:
    print('x is a positive single-digit number.')

#A more concise option:
if 0 < x < 10:
    print('x is a positive single-digit number.')













































    