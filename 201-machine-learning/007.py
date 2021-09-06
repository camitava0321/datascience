# -*- coding: utf-8 -*-
# Author: Amitava Chakraborty
#Neural Network Example
#A classifier using an artificial neural network.
from sklearn.neural_network import MLPClassifier

#Training data:
#Array	Contains	Size
#X	training samples represented as floating point feature vectors	size (n_samples, n_features)
#y	class labels for the training samples	size (n_samples,)
X = [[0., 0.], [1., 1.]]
y = [0, 1]
 
#Create the classifier:
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                     hidden_layer_sizes=(5, 2), random_state=1)
 
#Train the classifier with training data:
clf.fit(X, y)

#Predict
print( clf.predict([[2., 2.], [-1., -2.]]) )
