# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
Categorical Data - a Pandas data type
"""

#Features like gender, country, and codes are always repetitive. These are the examples for categorical data.
#Categorical variables can take on only a limited, and usually fixed number of possible values. 
#Besides the fixed length, categorical data might have an order but cannot perform numerical operation. 

#The categorical data type is useful in the following cases −
#    A string variable consisting of only a few different values. 
#    Converting such a string variable to a categorical variable will save some memory.
#    The lexical order of a variable is not the same as the logical order (“one”, “two”, “three”). 
#    By converting to a categorical and specifying an order on the categories, sorting and min/max will use the logical order instead of the lexical order.
#    As a signal to other python libraries that this column should be treated as a categorical variable (e.g. to use suitable statistical methods or plot types).

#Object Creation
#Categorical object can be created in multiple ways. 
#1. category
#By specifying the dtype as "category" in pandas object creation.
import pandas as pd
s = pd.Series(["a","b","c","a"], dtype="category")
print s
#The number of elements passed to the series object is four, 
#but the categories are only three. Observe the same in the output Categories.

#2. pd.Categorical
#Using the standard pandas Categorical constructor, we can create a category object.
#pandas.Categorical(values, categories, ordered)
cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'])
print cat

cat = cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'])
print cat
#Here, the second argument signifies the categories. 
#Thus, any value which is not present in the categories will be treated as NaN.

cat = cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'],ordered=True)
print cat
#Logically, the order means that, a is greater than b and b is greater than c.

#3. Description
#Using the .describe() command on the categorical data, we get similar output to a Series or DataFrame of the type string.
import numpy as np

cat = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
df = pd.DataFrame({"cat":cat, "s":["a", "c", "c", np.nan]})
print df.describe()
print df["cat"].describe()

#Get the Properties of the Category
#obj.cat.categories command is used to get the categories of the object.
s = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
print s.categories

#obj.ordered command is used to get the order of the object.
cat = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
print cat.ordered
#The function returned false because we haven't specified any order.

#Renaming Categories
#Renaming categories is done by assigning new values to the series.cat.categoriesseries.cat.categories property.
s = pd.Series(["a","b","c","a"], dtype="category")
s.cat.categories = ["Group %s" % g for g in s.cat.categories]
print s.cat.categories
#Initial categories [a,b,c] are updated by the s.cat.categories property of the object.

#Appending New Categories
#Using the Categorical.add.categories() method, new categories can be appended.
s = pd.Series(["a","b","c","a"], dtype="category")
s = s.cat.add_categories([4])
print s.cat.categories

#Removing Categories
#Using the Categorical.remove_categories() method, unwanted categories can be removed.
s = pd.Series(["a","b","c","a"], dtype="category")
print ("Original object:")
print s

print ("After removal:")
print s.cat.remove_categories("a")

#Comparison of Categorical Data
#Comparing categorical data with other objects is possible in three cases −
#    comparing equality (== and !=) to a list-like object (list, Series, array, ...) of the same length as the categorical data.
#    all comparisons (==, !=, >, >=, <, and <=) of categorical data to another categorical Series, when ordered==True and the categories are the same.
#    all comparisons of a categorical data to a scalar.
cat = pd.Series([1,2,3]).astype("category", categories=[1,2,3], ordered=True)
cat1 = pd.Series([2,2,2]).astype("category", categories=[1,2,3], ordered=True)

print cat>cat1