# -*- coding: utf-8 -*-
#author : Amitava Chakraborty

#Create a Python dictionary
#key - a collection of i and j - value i+j
d={(i,j):i+j for i in range(1,7) for j in range(1,7)}
print (d)

#next step - collect all of the (i,j) pairs that sum to each of the possible value from 2 to 12

#we use defaultdict object from the built-in collections module 
from collections import defaultdict
dinv = defaultdict(list)
#creates dictionaries with default values when it encounters a new key. 
#Otherwise, we would have had to create default values manually for a regular dictionary.
for i,j in d.items():
    dinv[j].append(i)

#How do dinv look
for key in dinv.keys() :
    print (key, " : ", dinv[key])
#e.g, dinv[7] contains the list of pairs that sum to seven 

#next step - compute the probability measured for each of these items.
#i.e., - we have to compute the sum of the products of the individual item probabilities in dinv. 
#See that dinv has in total 36 elements and each outcome is equally likely, 
#So the probability of every term in the sum equals 1/36. 
#Thus we have to count the number of items in the corresponding list 
#for each key in dinv and divide by 36. 
#For example, dinv[11] contains [(5, 6), (6, 5)] - 11 is the probability of this set 
#since, 5+6=6+5=11
#Hence P(11) = P({(5, 6)})+P({(6, 5)}) = 1/36+1/36 = 2/36. 
#Repeating this procedure for all the elements, we derive the probability mass function
X={i:len(j)/36.0 for i,j in dinv.items() }
print (X)

#%% - With the same framework, we ask
#what is the probability that half the product of 3 dice will exceed the their sum?

#First, let’s create the first mapping,
d={(i,j,k):((i*j*k)/2>i+j+k) for i in range(1,7)
for j in range(1,7)
for k in range(1,7)}

print (d)

#keys of this dictionary d : the triples and 
#values : logical values of whether or not half the product of three dice exceeds their sum 
#Now, we do the inverse mapping to collect the corresponding lists,
dinv = defaultdict(list)
for i,j in d.iteritems(): 
    dinv[j].append(i)

#dinv contains only two keys, True and False - and all total 63 elements
#The dice readings are independent - so probability of any triple is 1/63. 
#Finally, we collect this for each outcome as in the following,
X={i:len(j)/6.0**3 for i,j in dinv.iteritems() }
print (X)

#Thus, the probability of half the product of three dice exceeding their sum is
#136/(6.0**3) = 0.63. 
#The set that is induced by the random variable has only two elements in it, 
#True and False, with 
#P(True) = 136/216 and 
#P(False) = 1 − 136/216.

#%% - Using Pandas instead of Python dictionaries. 
#We construct a DataFrame object with an index of tuples consisting of all pairs of possible dice outcomes.
from pandas import DataFrame
d=DataFrame(index=[(i,j) for i in range(1,7) for j in range(1,7)], columns=['sm','d1','d2','pd1','pd2','p'])

#Now, we can populate the columns that we set up above 
#where the outcome of the first die is the d1 column and the outcome of the second die is d2,
d.d1=[i[0] for i in d.index]
d.d2=[i[1] for i in d.index]

#Next, we compute the sum of the dices in the sm column,
d.sm=map(sum,d.index)

#With that established, the DataFrame now looks like the following:
d.head(5) # show first five lines

#Next, we fill out the probabilities for each face of the unfair die (d1) and the fair die (d2),
d.loc[d.d1<=3,'pd1']=1/9.
d.loc[d.d1 > 3,'pd1']=2/9.
d.pd2=1/6.
d.head(10)

#Finally, we can compute the joint probabilities for the sum of the shown faces as the following:
d.p = d.pd1 * d.pd2
d.head(5)

#With all that established, we can compute the density of all the dice outcomes 
#by using groupby as in the following,
d.groupby('sm')['p'].sum()
print (sm)
