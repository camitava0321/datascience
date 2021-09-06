# -*- coding: utf-8 -*-
# Author: Amitava Chakraborty
#Machine Learning Classifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier

#Training data - a set of vectors (height, weight, shoe size) and the class this vector belongs to:
#{height, weights, shoe size}
X = [[190,70,44],[166,65,45],[190,90,47],[175,64,39],[171,75,40],[177,80,42],[160,60,38],[144,54,37]]
#We predict if it’s a male or female given vector data.
Y = ['male','male','male','male','female','female','female','female']

#Define a vector for the prediction in the same format (height, weight, size). 
#Predict for this vector (height, wieghts, shoe size)
P = [[190,80,46]]

#Then we fit the training data and predict in this style:
#c = Classifier()
#c = c.fit(X,Y)
#print "\nPrediction : " + str(c.predict(P))

#{Decision Tree Model}
clf = DecisionTreeClassifier()
clf = clf.fit(X,Y)
print "\n1) Using Decision Tree Prediction is " + str(clf.predict(P))

#{K Neighbors Classifier}
knn = KNeighborsClassifier()
knn.fit(X,Y)
print "2) Using K Neighbors Classifier Prediction is " + str(knn.predict(P))

#{using MLPClassifier}
mlpc = MLPClassifier()
mlpc.fit(X,Y)
print "3) Using MLPC Classifier Prediction is " + str(mlpc.predict(P))

#{using MLPClassifier}
rfor = RandomForestClassifier()
rfor.fit(X,Y)
print "4) Using RandomForestClassifier Prediction is " + str(rfor.predict(P)) +"\n"
