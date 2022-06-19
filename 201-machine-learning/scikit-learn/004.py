# -*- coding: utf-8 -*-
# Author: Amitava Chakraborty
#%% - Conventions
#scikit-learn estimators follow certain rules to make their behavior more predictive.

#Type casting
#Unless otherwise specified, input will be cast to float64:
import numpy as np
from sklearn import random_projection

rng = np.random.RandomState(0)
X = rng.rand(10, 2000)
X = np.array(X, dtype='float32')
X.dtype

transformer = random_projection.GaussianRandomProjection()
X_new = transformer.fit_transform(X)
X_new.dtype

#In this example, X is float32, which is cast to float64 by fit_transform(X).

#Regression targets are cast to float64, classification targets are maintained:
from sklearn import datasets
from sklearn.svm import SVC
iris = datasets.load_iris()
clf = SVC()
clf.fit(iris.data, iris.target)  
list(clf.predict(iris.data[:3]))
#Here, predict() returns an integer array, since iris.target (an integer array) was used in fit. 

clf.fit(iris.data, iris.target_names[iris.target])  

list(clf.predict(iris.data[:3]))  

rng = np.random.RandomState(0)
X = rng.rand(100, 10)
y = rng.binomial(1, 0.5, 100)
X_test = rng.rand(5, 10)

clf = SVC()
#The default kernel rbf is changed to linear after the estimator has been constructed via SVC() 
clf.set_params(kernel='linear').fit(X, y)  
clf.predict(X_test)

#kernel is now changed back to rbf to refit the estimator and to make a second prediction.
clf.set_params(kernel='rbf').fit(X, y)  
clf.predict(X_test)
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer
X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
y = [0, 0, 1, 1, 2]

classif = OneVsRestClassifier(estimator=SVC(random_state=0))
classif.fit(X, y).predict(X)

#In the above case, 
#the classifier is fit on a 1d array of multiclass labels and 
#the predict() method therefore provides corresponding multiclass predictions. 

#It is also possible to fit upon a 2d array of binary label indicators:
y = LabelBinarizer().fit_transform(y)
classif.fit(X, y).predict(X)
#Here, the classifier is fit() on a 2d binary label representation of y, 
#using the LabelBinarizer. 
#In this case predict() returns a 2d array representing the corresponding multilabel predictions.

#Note that the fourth and fifth instances returned all zeroes, 
#indicating that they matched none of the three labels fit upon. 
#With multilabel outputs, it is similarly possible for an instance to be assigned multiple labels:
from sklearn.preprocessing import MultiLabelBinarizer
y = [[0, 1], [0, 2], [1, 3], [0, 2, 3], [2, 4]]
y = MultiLabelBinarizer().fit_transform(y)
classif.fit(X, y).predict(X)

#In this case, the classifier is fit upon instances each assigned multiple labels. 
#The MultiLabelBinarizer is used to binarize the 2d array of multilabels to fit upon. 
#As a result, predict() returns a 2d array with multiple predicted labels for each instance.