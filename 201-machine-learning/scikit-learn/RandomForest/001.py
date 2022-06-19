# -*- coding: utf-8 -*-
# Author: Amitava Chakraborty
from sklearn.ensemble import RandomForestClassifier

# Basic - is that you have data, fit it to an estimator, then predict
#Step 1: Initialise an estimator
clf = RandomForestClassifier(random_state=0)
#%% - Sep 2 - Organise data - Training and Test Data
X = [[ 1,  2,  3, 4, 5],  # 3 samples, 5 features
      [11, 12, 13, 14, 15],
      [100, 101, 102, 103, 104]]
y = [0, 1, 2]  # classes of each sample

testX1 = [[ 1,  3,  2, 6, 5],  # 3 samples, 5 features
      [12, 14, 16, 11, 13],
      [1, 8, 2, 3, 7]]

testX2 = [[ 11,  13,  12, 16, 15],  # 2 samples, 5 features
      [13, 15, 18, 12, 12]]

testX3 = [[ 101,  103,  102, 106, 105]]  # 1 sample, 5 features

#%% - Step 3 - Fit, Learning
clf.fit(X, y)
#%% - Step 4 - Predict
print (clf.predict(X))  # predict classes of the training data
print (clf.predict(testX1))  # predict classes of the training data
print (clf.predict(testX2))  # predict classes of the training data
print (clf.predict(testX3))  # predict classes of the training data
print (clf.predict([[4, 5, 6, 1, 3], [14, 15, 16, 17, 19]]))  # predict classes of new data

#%% - Transformers and pre-processors
#Machine learning workflows are often composed of different parts. 
#A typical pipeline consists of a pre-processing step that transforms or imputes the data, 
#and a final predictor that predicts target values.

#In scikit-learn, pre-processors and transformers follow the same API as the estimator objects 
#(they actually all inherit from the same BaseEstimator class). 
#The transformer objects don’t have a predict method but rather a transform method 
#that outputs a newly transformed sample matrix X:

from sklearn.preprocessing import StandardScaler
# scale data according to computed scaling values
scaledX = StandardScaler().fit(X).transform(X)
print (scaledX)
# Sometimes, you want to apply different transformations to different features: 
#the ColumnTransformer is designed for these use-cases
clf.fit(X, y)
print (clf.predict(X))  # predict classes of the training data
print (clf.predict(testX2))  # predict classes of the training data
