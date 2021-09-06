# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 23:17:21 2017

@author: Amitava
Indexing and Slicing
"""


import numpy as np

#Contents of ndarray object can be accessed and modified by indexing or slicing
#Items in ndarray object follows zero-based index. 
#Three types of indexing methods are available − field access, basic slicing and advanced indexing.



#Single indexing is the way, you will most probably expect it:

F = np.array([1, 1, 2, 3, 5, 8, 13, 21])
# print the first element of F, i.e. the element with the index 0
print(F[0])
# print the last element of F
print(F[-1])
B = np.array([ [[111, 112], [121, 122]],
               [[211, 212], [221, 222]],
               [[311, 312], [321, 322]] ])
print(B[0][1][0])

#Indexing multidimensional arrays:

A = np.array([ [3.4, 8.7, 9.9], 
               [1.1, -7.8, -0.7],
               [4.1, 12.3, 4.8]])
print(A[1][0])
#We accessed the element in the second row, i.e. the row with the index 1, and the first column (index 0). 
#We accessed it the same way, we would have done with an element of a nested Python list. 

#Alternative Method 
#We use only one pair of square brackets and all the indices are separated by commas:
print(A[1, 0])

#You have to be aware of the fact, that the second way is more efficient. In the first case, we create an intermediate array A[1] from which we access the element with the index 0. So it behaves similar to this:

tmp = A[1]
print(tmp)
print(tmp[0])

#In numpy, the syntax of Basic Slicing is the same as that of lists and tuples for 1d arrays, 
#but it can be applied to multiple dimensions as well.

#The general syntax for a one-dimensional array A looks like this:
#A[start:stop:step]
#A Python slice object is constructed by giving start, stop, and step parameters to the built-in slice function. 
#This slice object is passed to the array to extract a part of array.

#slicing of a one-dimensional array:
a = np.arange(10)  #prepare an ndarray object
s = slice(2,7,2)   #define a slice object with start, stop, and step values
print a[s]         #this slice object is passed to the ndarray
#a part of it starting with index 2 up to 7 with a step of 2 is sliced.

#identical result can also be obtained 
#by giving the slicing parameters separated by a colon : (start:stop:step) directly to the ndarray object.
b = a[2:7:2] 
print b

#select a piece of an array from the index 3(4th element) to 7(8th element) that extracts the elements 3 through 6 
a = np.arange(9)
a[3:7]

#select elements from the index 0 to 7 with a step of two
a[:7:2]
#negative indices and reverse the array
a[::-1]

#If only one parameter is put, a single item corresponding to the index will be returned. 
#If a : is inserted in front of it, all items from that index onwards will be extracted. 
#If two parameters (with : between them) is used, 
#items between the two indexes (not including the stop index) with default step one are sliced.
b = a[5] 
print b

# slice items starting from index 
print a[2:]
# slice items between indexes 
print a[2:5]

#More Examples
S = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(S[2:5])
print(S[:4])
print(S[6:])
print(S[:])

#We will illustrate the multidimensional slicing in the following examples. The ranges for each dimension are separated by commas:
a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 
print a  

# slice items starting from index
print a[1:]
#Slicing can also include ellipsis (…) 
#to make a selection tuple of the same length as the dimension of an array. 
#If ellipsis is used at the row position, it will return an ndarray comprising of items in rows.
#this returns array of items in the second column 
print a[...,1] 

#Now we will slice all items from the second row 
print a[1,...] 

#Now we will slice all items from column 1 onwards 
print a[...,1:]







A = np.array([
[11,12,13,14,15],
[21,22,23,24,25],
[31,32,33,34,35],
[41,42,43,44,45],
[51,52,53,54,55]])
print(A[:3,2:])

print(A[3:,:])

print(A[:,4:])

#The following two examples use the third parameter "step". The reshape function is used to construct the two-dimensional array. We will explain reshape in the following subchapter:

X = np.arange(28).reshape(4,7)
print(X)

print(X[::2, ::3])

print(X[::, ::3])

#Warning Comment
#Attention: Whereas slicings on lists and tuples create new objects, a slicing operation on an array creates a view on the original array. So we get an another possibility to access the array, or better a part of the array. From this follows that if we modify a view, the original array will be modified as well.

A = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
S = A[2:6]
S[0] = 22
S[1] = 23
print(A)

#Doing the similar thing with lists, we can see that we get a copy:

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst2 = lst[2:6]
lst2[0] = 22
lst2[1] = 23
print(lst)

#If you want to check, if two array names share the same memory block, you can use the function np.may_share_memory.
np.may_share_memory(A, B)

#To determine if two arrays A and B can share memory the memory-bounds of A and B are computed. The function returns True, if they overlap and False otherwise. The function may give false positives, i.e. if it returns True it just means that the arrays may be the same.

np.may_share_memory(A, S)

#The following code shows a case, in which the use of may_share_memory is quite useful:

A = np.arange(12)
B = A.reshape(3, 4)
A[0] = 42
print(B)

#We can see that A and B share the memory in some way. The array attribute "data" is an object pointer to the start of an array's data. Looking at the data attribute returns something surprising:

print(A.data)
print(B.data)
print(A.data == B.data)

#Let's check now on equality of the arrays:

print(A == B)

#Which makes sense, because they are different arrays concerning their structure:

print(A)
print(B)

#But we saw that if we change an element of one array the other one is changed as well. This fact is reflected by may_share_memory:

np.may_share_memory(A, B)

#The result above is "false positive" example for may_share_memory in the sense that somebody may think that the arrays are the same, which is not the case.








#Advanced Indexing
#It is possible to make a selection from ndarray that is a non-tuple sequence, 
#ndarray object of integer or Boolean data type, 
#or a tuple with at least one item being a sequence object. 
#Advanced indexing always returns a copy of the data. 
#As against this, the slicing only presents a view.

#Two types of advanced indexing − Integer and Boolean.
#Integer Indexing
#This mechanism helps in selecting any arbitrary item in an array based on its Ndimensional index. 
#Each integer array represents the number of indexes into that dimension. 
#When the index consists of as many integer arrays as the dimensions of the target ndarray, 
#it becomes straightforward.

x = np.array([[1, 2], [3, 4], [5, 6]]) 
#one element of specified column from each row of ndarray object is selected. 
#Hence, the row index contains all row numbers, and the column index specifies the element to be selected.
y = x[[0,1,2], [0,1,0]] 
print x
print y
#The selection includes elements at (0,0), (1,1) and (2,0) from the first array.

x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 
print 'Our array is:' 
print x 
#The row indices of selection are [0, 0] and [3,3] 
rows = np.array([[0,0],[3,3]])
#the column indices are [0,2] and [0,2].
cols = np.array([[0,2],[0,2]]) 
#elements placed at corners of a 4X3 array are selected. 
y = x[rows,cols] 
print 'The corner elements of this array are:' 
print y
#The resultant selection is an ndarray object containing corner elements.

#Advanced and basic indexing can be combined by using one slice (:) or ellipsis (…) with an index array. 
#The following example uses slice for row and advanced index for column. 
#The result is the same when slice is used for both. 
#But advanced index results in copy and may have different memory layout.
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 
print 'Our array is:' 
print x 
# slicing 
z = x[1:4,1:3] 
print 'After slicing, our array becomes:' 
print z 
# using advanced index for column 
y = x[1:4,[1,2]] 
print 'Slicing using advanced index for column:' 
print y

#Boolean Array Indexing
#This type of advanced indexing is used when the resultant object is meant to be the result of Boolean operations
#such as comparison operators.

#In this example, items greater than 5 are returned as a result of Boolean indexing.
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 
print 'Our array is:' 
print x 
# Now we will print the items greater than 5 
print 'The items greater than 5 are:' 
print x[x > 5]

#In this example, NaN (Not a Number) elements are omitted by using ~ (complement operator).
a = np.array([np.nan, 1,2,np.nan,3,4,5]) 
print a[~np.isnan(a)]

#The following example shows how to filter out the non-complex elements from an array.
a = np.array([1, 2+6j, 5, 3.5+5j]) 
print a[np.iscomplex(a)]


#Fancy indexing
#Fancy indexing is indexing that does not involve integers or slices, which is normal indexing
#we will apply fancy indexing to set the diagonal values of the face(scipy) image to 0. 
#This will draw black lines along the diagonals, crossing it through, 
import scipy.misc as scp
import matplotlib.pyplot as plt

face = scp.face()
face.shape
xmax = face.shape[0]
ymax = face.shape[1]
#The array is not readonly - make all of them updatable
face.flags['WRITEABLE']=True

#Set the values of the first diagonal to 0
#we need to define two different ranges for the x and y values
face[range(xmax), range(768)]
#Now, set the values of the other diagonal to 0
#we require a different set of ranges - principles stay the same
face[range(xmax-1,-1,-1), range(768)] = 0
#At the end we get the following image with the diagonals crossed out
plt.imshow(face)
plt.show()

#Indexing with a list of locations
#We use the ix_() function to shuffle the Face(scipy) image. 
#This function creates a mesh from multiple sequences. 
#As arguments, we give one-dimensional sequences, and the function returns a tuple of NumPy arrays. 
np.ix_([0,1], [2,3])
#To index the array with a list of locations, perform the following steps:
#Shuffle the array indices
#Create a random indices array with the shuffle() function of the numpy.random module
#The function changes the array inplace
def shuffle_indices(size):
    arr = np.arange(size)
    np.random.shuffle(arr)
    return arr

xindices = shuffle_indices(xmax)
np.testing.assert_equal(len(xindices), xmax)
yindices = shuffle_indices(ymax)
np.testing.assert_equal(len(yindices), ymax)

#Now plot the shuffled indices as follows:
plt.imshow(face[np.ix_(xindices, yindices)])
plt.show()
#we get a completely scrambled image


#Indexing arrays with Booleans
#Boolean indexing is indexing based on a Boolean array
#falls in the category of fancy indexing
#i.e., indexing happens with the help of a special iterator object
face = scp.face()
#Perform the following steps to index an array:
#First, we create an image with dots on the diagonal
#This time we select modulo four points on the diagonal of the image
def get_indices(size):
    arr = np.arange(size)
    return arr % 4 == 0

#Then we just apply this selection and plot the points
face1 = face.copy()
xindices = get_indices(face.shape[0])
yindices = get_indices(face.shape[1])
yindices = 192
face1[xindices, yindices] = 0

#Select array values between a quarter and three-quarters of the maximum value, 
#and set them to 0
face2 = face.copy()
face2[(face > face.max()/4) & (face < 3 * face.max()/4)] = 0

#The plot with the two new images
plt.subplot(211)
plt.imshow(face1)
plt.subplot(212)
plt.imshow(face2)
plt.show()
