# -*- coding: utf-8 -*-
# Author: Amitava Chakraborty
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

#%%- Load the diabetes dataset
diabetes = datasets.load_diabetes()

trainingData = pd.read_csv('linearRegressionTrainingData.csv')
print (trainingData)
print (trainingData.describe())
print (trainingData.columns)
print (trainingData.shape)

testData = pd.read_csv('linearRegressionTestData.csv')
print (testData)
print (testData.describe())
print (testData.columns)
print (testData.shape)


#%%- 
print (diabetes)

#%%- Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
print (diabetes_X_train.shape)

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]
print (diabetes_y_train.shape)

# Create linear regression object
regr = linear_model.LinearRegression()
dataX = trainingData['bedrooms']
dataY = trainingData['sellprice']
#print dataX.shape

#dataX.reshape(100L,1L)






#dataY.reshape(100,1)
print (dataX.shape)
print (dataY.shape)


# Train the model using the training sets
#regr.fit(diabetes_X_train, diabetes_y_train)
regr.fit(dataX, dataY)

#%%- Make predictions using the testing set
#diabetes_y_pred = regr.predict(diabetes_X_test)

testDataX = testData['bedrooms']
testDataY = testData['sellprice']
testDataY_predicted = regr.predict(testDataX)


# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(testDataY, testDataY_predicted))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(testDataY, testDataY_predicted))

# Plot outputs
plt.scatter(testDataX, testDataY,  color='black')
plt.plot(testDataX, testDataY_predicted, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
