# -*- coding: utf-8 -*-
# Author: Amitava Chakraborty
#Difficult Data (low # of features, low # of instances)
#6 linear Classifiers
#We’ll use simple arrays as data - 
#In practice we will have large datasets to make good predictions.

from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegressionCV
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.linear_model import Perceptron
from sklearn.linear_model import RidgeClassifierCV

from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
clf = tree.DecisionTreeClassifier()
clfLR = LogisticRegression(random_state=0)
clfLRCV = LogisticRegressionCV(cv=3, random_state=0)
clfPA = PassiveAggressiveClassifier(max_iter=1000, random_state=0,tol=1e-3)
clfPerceptron = Perceptron(tol=1e-3, random_state=0)
clfRCCV = RidgeClassifierCV(alphas=[1e-3, 1e-2, 1e-1, 1])
# Always scale the input. The most convenient way is to use a pipeline.
clfSGDC = make_pipeline(StandardScaler(),
                    SGDClassifier(max_iter=1000, tol=1e-3))


#The training data for the classifier
#[height, hair-length, voice-pitch]                                             
XTrain = [[180, 15,1],
      [180, 25,5],
      [180, 35,2],
      [180, 20,4],
      [167, 42,1],                                                              
      [160, 22,2],                                                              
      [136, 35,3],                                                              
      [136, 35,2],                                                              
      [174, 15,2],                                                              
      [173, 39,5],                                                              
      [141, 28,6]]                                                              

#2-class
YTrain = ['man', 'woman', 'woman', 'man','woman', 'man','woman', 'man','man', 'woman','woman']
#3-class
#YTrain = ['m', 'f', 't', 'm','t', 'm','f', 'm','t', 'f','f']
YTrain = ['m', 'f', 'm', 'm','t', 'm','f', 'm','t', 'f','f']

clf = clf.fit(XTrain, YTrain)   
#clfLR = clfLR.fit(XTrain, YTrain)   
#clfLRCV = clfLRCV.fit(XTrain, YTrain)   
clfPA = clfPA.fit(XTrain, YTrain)   
clfPerceptron = clfPerceptron.fit(XTrain, YTrain)   
clfRCCV = clfRCCV.fit(XTrain, YTrain)   
clfSGDC = clfSGDC.fit(XTrain, YTrain)   
#%%
#Test Data
#[height, hair-length, voice-pitch]                                             
XTest = [ [181, 15,1],
      [182, 25,4],
      [183, 35,2],
      [174, 20,4],
      [165, 42,1],                                                              
      [166, 22,4],                                                              
      [137, 35,3],                                                              
      [138, 47,2],                                                              
      [179, 15,5]]                                                              

YTest = ['man', 'man', 'woman', 'man','man', 'woman','woman', 'woman','woman']
#3-class
YTest = ['t', 'm', 'f', 't','m', 'f','f', 't','f']
                                                          
#prediction = clf.predict([[163, 27,1]])                                         
#for 2-Class only
#predicted_LR = clfLR.predict(XTest)                                         
#predicted_LRCV = clfLRCV.predict(XTest)                                         
#print('Logistic Regression Prediction   : ',predicted_LR)  
#print('Logistic Regression CV Prediction: ',predicted_LRCV)  

#for both 2,3 class
predicted_Tree = clf.predict(XTest)                                         
predicted_PA = clfPA.predict(XTest)                                         
predicted_Perceptron = clfPerceptron.predict(XTest)                                         
predicted_RCCV = clfRCCV.predict(XTest)                                         
predicted_SGDC = clfSGDC.predict(XTest)                                         
print('Decision Tree Prediction         : ',predicted_Tree)  
print('Passive Aggressive Prediction    : ',predicted_PA)  
print('Perceptron Prediction            : ',predicted_Perceptron)  
print('Ridge Classifier CV Prediction   : ',predicted_RCCV)  
print('SGDC Classifier CV Prediction    : ',predicted_SGDC)  
#%%
from sklearn.metrics import accuracy_score
#for 2-Class only
#score_LR=accuracy_score(YTest, predicted_LR)
#score_LRCV=accuracy_score(YTest, predicted_LRCV)
#print('Logistic Regression Accuracy: ',score_LR)  
#print('Logistic Regression CV Accuracy: ',score_LRCV)  

#for both 2,3 class
score_Tree=accuracy_score(YTest, predicted_Tree)
score_PA=accuracy_score(YTest, predicted_PA)
score_Perceptron=accuracy_score(YTest, predicted_Perceptron)
score_RCCV=accuracy_score(YTest, predicted_RCCV)
score_SGDC=accuracy_score(YTest, predicted_SGDC)
print('Decision Tree Accuracy: ',score_Tree)  
print('Passive Aggressive Accuracy: ',score_PA)  
print('Perceptron Accuracy: ',score_Perceptron)  
print('Ridge Classifier CV Accuracy: ',score_RCCV)  
print('SGDC Classifier CV Accuracy: ',score_SGDC)  
