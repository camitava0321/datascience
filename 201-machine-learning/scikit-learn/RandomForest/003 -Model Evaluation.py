# -*- coding: utf-8 -*-
# Author: Amitava Chakraborty
#Model evaluation
#Fitting a model to some data does not entail that it will predict well on unseen data. 
#This needs to be directly evaluated. 
#We have just seen the train_test_split helper that splits a dataset into train and test sets, 
#but scikit-learn provides many other tools for model evaluation, in particular for cross-validation.

#We here briefly show how to perform a 5-fold cross-validation procedure, 
#using the cross_validate helper. 
#Note that it is also possible to manually iterate over the folds, 
#use different data splitting strategies, and 
#use custom scoring functions.

from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_validate

X, y = make_regression(n_samples=1000, random_state=0)
lr = LinearRegression()

result = cross_validate(lr, X, y)  # defaults to 5-fold CV
print (result['test_score'])  # r_squared score is high because dataset is easy