# -*- coding: utf-8 -*-
# Author: Amitava Chakraborty
#%% - Learning and predicting
#In the case of the digits dataset, the task is to predict, 
#given an image, which digit it represents. 
#We are given samples of each of the 10 possible classes (the digits zero through nine) 
#on which we fit an estimator to be able to predict the classes to which unseen samples belong.

#In scikit-learn, an estimator for classification is a Python object that 
#implements the methods fit(X, y) and predict(T).

#An example of an estimator is the class sklearn.svm.SVC that implements support vector classification. 
#The constructor of an estimator takes as arguments the parameters of the model, 
#but for the time being, we will consider the estimator as a black box:

from sklearn import datasets
from sklearn import svm

clf = svm.SVC(gamma=0.001, C=100.)

#Choosing the parameters of the model
#In this example we set the value of gamma manually. 
#It is possible to automatically find good values for the parameters by using tools 
#such as grid search and cross validation.

#We call our estimator instance clf, as it is a classifier. 
#It now must be fitted to the model, that is, it must learn from the model. 
#This is done by passing our training set to the fit method. 
#As a training set, let us use all the images of our dataset apart from the last one. 
#We select this training set with the [:-1] Python syntax, 
#which produces a new array that contains all but the last entry of digits.data:

#Load the digits dataset
digits = datasets.load_digits()
clf.fit(digits.data[:-1], digits.target[:-1])  

#Now you can predict new values, in particular, 
#we can ask to the classifier what is the digit of our last image in the digits dataset, 
#which we have not used to train the classifier:
clf.predict(digits.data[-1:])

import matplotlib.pyplot as plt
#Display the first digit
plt.figure(1, figsize=(3, 3))
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
#As you can see, it is a challenging task: the images are of poor resolution. Do you agree with the classifier?