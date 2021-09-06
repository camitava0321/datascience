#!/usr/bin/python
#Author : Amitava Chakraborty

import math
#%% - Mathematical Constants
#pi	The mathematical constant pi.
#e	The mathematical constant e.

#%% - Mathematical Functions

#Uses math.log10 to compute a signal-to-noise ratio in decibels
signal_power = 40 
noise_power = 5
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
print decibels

print math.sqrt(2) / 2.0


#Use following functions to perform mathematical calculations.
#ceil(x)	The ceiling of x: the smallest integer not less than x
print (math.ceil(16.189))
#floor(x)The floor of x: the largest integer not greater than x
print (math.floor(16.189))
#cmp(x, y)	-1 if x < y, 0 if x == y, or 1 if x > y
#exp(x)	The exponential of x: ex
print(math.exp(4))
#fabs(x)	The absolute value of x.
print(math.fabs(23-59))
#log(x)	The natural logarithm of x, for x> 0
print(math.log(4))
#log10(x)	The base-10 logarithm of x for x> 0 .
print(math.log10(4))
#modf(x)	The fractional and integer parts of x in a two-item tuple. Both parts have the same sign as x. The integer part is returned as a float.
#pow(x, y)	The value of x**y.
#round(x [,n])	x rounded to n digits from the decimal point. Python rounds away from zero as a tie-breaker: round(0.5) is 1.0 and round(-0.5) is -1.0.
#sqrt(x)	The square root of x for x > 0

#%% - Composition
