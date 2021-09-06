#!/usr/bin/python
#Author : Amitava Chakraborty

#Random Number Functions
#Random numbers are used for games, simulations, testing, 
#security, and privacy applications. 
#Use following commonly used functions

#choice(seq) 	A random item from a list, tuple, or string.
#randrange ([start,] stop [,step])     A randomly selected element from range(start, stop, step)
#random()	A random float r, such that 0 is less than or equal to r and r is less than 1
#seed([x])	Sets the integer starting value used in generating random numbers. Call this function before calling any other random module function. Returns None.
#shuffle(lst)	Randomizes the items of a list in place. Returns None.
#uniform(x, y)	A random float r, such that x is less than or equal to r and r is less than y 

import  random as rn
list='FSFFSFSSSFSFSFFSFFSFS'
print rn.choice(list)
