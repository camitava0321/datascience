# -*- coding: utf-8 -*-
#Author: Amitava Chakraborty
#Naive Bayes classifier - a supervised learning classifier.

#Usage in:  text categorization (spam or not spam) and competes with 
#advanced classifiers like support vector machines.
from sklearn.naive_bayes import GaussianNB

#The training set (X) 
#consits of length, weight and shoe size. Y contains the associated labels (male or female).
# create dataset
X = [[121, 80, 44], [180, 70, 43], [166, 60, 38], [153, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [174, 71, 40], [159, 52, 37], [171, 76, 42], [183, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']

#create naive bayes classifier
gaunb = GaussianNB()

#train classifier with dataset
gaunb = gaunb.fit(X, Y)

#predict using classifier
prediction = gaunb.predict([[190, 70, 43]])
print(prediction)

#We predict for another set like [166, 65, 33],
prediction = gaunb.predict([[166, 65, 33]])
print(prediction)
