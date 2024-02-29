# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 17:07:47 2024

@author: AMITAVA
"""

from sklearn import linear_model
from sklearn import svm
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import Dense
#from xgboost import XGBRegressor

def selectModel(modelName):

    if modelName==1:
        model = linear_model.LinearRegression()
    elif modelName==2:
        model = linear_model.Ridge(alpha=.5, solver='auto')
        linear_model.Lasso(alpha=0.1)
    elif modelName==3:
        model = linear_model.Lasso(alpha=0.1)
    elif modelName==4:
        model = linear_model.LassoLars(alpha=.1)
    elif modelName==6:
        model = linear_model.SGDClassifier()


#When we are uncertain about whether the relationship between features and the target variable is linear or non-linear, 
#it's often a good idea to start with more flexible models that can capture complex patterns. 
#Following regressor models can handle both linear and non-linear relationships:

    #Random Forest Regressor: versatile and powerful ensemble methods that can capture non-linear relationships and 
    #handle complex interactions between features.
    elif modelName==101:
        model = RandomForestRegressor()
    elif modelName==102:
        model = RandomForestRegressor(n_estimators=100, random_state=42)

    #Gradient Boosting Regressor: Gradient Boosting model, powerful and can capture complex relationships. 
    #They build trees sequentially, each correcting the errors of the previous one.
    elif modelName==110:
        model = GradientBoostingRegressor()

    #Support Vector Machines (SVM) for Regression: SVMs can be used for regression tasks, and 
    #they are capable of capturing non-linear patterns by using different kernel functions.
    elif modelName==120:
        model = svm.SVR(kernel='rbf')

    #Neural Networks (Deep Learning): Neural networks, especially deep learning models, 
    #are highly flexible and can learn complex non-linear relationships. 
    #Libraries like TensorFlow and PyTorch provide tools for building neural network models.
#    elif modelName==130:
#        num_features=4
#        model = Sequential([
#            Dense(32, activation='relu', input_shape=(num_features,)),
#            Dense(1)  # Output layer for regression task
#            ])
    
    #XGBoost Regressor: XGBoost is another gradient boosting library that is known for its speed and performance. 
    #It is an extension of gradient boosting that is designed to be efficient and effective.
#    elif modelName==140:
#        model = XGBRegressor()

    #CAUTION: more complex models may overfit the data. 
    #Additionally, performing cross-validation and tuning hyperparameters can help in finding the best model 
    #for a specific dataset.
    #Experimenting with different models and comparing their performance using cross-validation 
    #should be performed to in selecting the most suitable regressor for the task at hand

    elif modelName==-1:
        model = None
    return model
