# -*- coding: utf-8 -*-
# Author: Amitava Chakraborty
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

#%%- Load the bookdata dataset
trainingData = pd.read_csv('bookdata.csv')
print (trainingData)
print (trainingData.describe())
print (trainingData.columns)
print (trainingData.shape)

#prepare test data
testData = trainingData.reindex(np.random.permutation(trainingData.index))

print (testData)
print (testData.describe())
print (testData.columns)
print (testData.shape)

#%% - First Look at the Training Data
#Plot all the columns with 'spend'

fig, ax = plt.subplots(nrows=2, ncols=3,figsize=(15,15))


fig.subplots_adjust(wspace=.2)
fig.subplots_adjust(hspace=.3)

trainingData.plot(x='pages', y='price', linewidth=0, marker='o', color='000', ax=ax[0,0])
#trainingData.plot(x='edu', y='spend', linewidth=0, marker='^', color='r', ax=ax[0,1])
#trainingData.plot(x='rating', y='spend', linewidth=0, marker='o', fillstyle='none',color='g', ax=ax[0,2])

#trainingData.plot(x='creditscore', y='spend', linewidth=0, marker='h', fillstyle='none', color='r', ax=ax[1,0])
#trainingData.plot(x='income', y='spend', linewidth=0, marker='D', color='r', ax=ax[1,1])
#trainingData.plot(x='age', y='income', linewidth=0, marker='s', color='r', ax=ax[1,2])
plt.show()

#OR

from pandas.plotting import scatter_matrix
scatter_matrix(trainingData, alpha=0.8, figsize=(10, 10), diagonal='kde')


#%%- Predict price vs pages
# Create linear regression object
regr = linear_model.LinearRegression()
listA = ['pages']
dataX = trainingData[listA].as_matrix()
dataX = trainingData.as_matrix(columns=trainingData.columns[1])  #selects 'age' only
dataY = trainingData['price'].values

# Train the model using the training sets
#regr.fit(diabetes_X_train, diabetes_y_train)
regr.fit(dataX, dataY)

#Make predictions using the testing set
testDataX = testData[listA]
testDataX = testData.as_matrix(columns=testData.columns[2:3])
testDataY = testData['price']
testDataY_predicted = regr.predict(testDataX)

y=regr.predict(100)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(testDataY, testDataY_predicted))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(testDataY, testDataY_predicted))

# Plot outputs
fig = plt.figure()
plt.scatter(testDataX, testDataY,  color='pink')
plt.plot(testDataX, testDataY_predicted, color='blue', linewidth=3)

fig.suptitle('test title', fontsize=20)
plt.xlabel('age', fontsize=18)
plt.ylabel('spend', fontsize=16)
plt.xticks(())
plt.yticks(())
fig.savefig('test.png', dpi=300)
plt.show()

#%%- Predict all vs spend
# Create linear regression object
regr = linear_model.LinearRegression()
listA = ['age','edu','rating','creditscore','spend','income']
dataX = trainingData[listA].as_matrix()
#dataX = trainingData.as_matrix(columns=trainingData.columns[2:3])  #selects 'age' only
dataY = trainingData['spend'].values

# Train the model using the training sets
#regr.fit(diabetes_X_train, diabetes_y_train)
regr.fit(dataX, dataY)

#Make predictions using the testing set
testDataX = testData[listA]
#testDataX = testData.as_matrix(columns=testData.columns[2:3])
testDataY = testData['spend']
testDataY_predicted = regr.predict(testDataX)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(testDataY, testDataY_predicted))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(testDataY, testDataY_predicted))

# Plot outputs
fig = plt.figure()
fig, ax = plt.subplots()
#plt.scatter(testDataX, testDataY,  color='black')
plt.plot(testDataX['age'], testDataY_predicted, color='yellow', marker='^', linewidth=0)

fig.suptitle('test title', fontsize=20)
fig.dpi=80
fig.set_size_inches(11,6)
plt.xlabel('age', fontsize=18)
plt.ylabel('spend', fontsize=16)
plt.xticks(())
plt.yticks(())

scat = ax.scatter(testData['age'], testDataY, c=testData['income'], s=170, marker='o')
colorbar=fig.colorbar(scat, cmap='RdBu')
colorbar.ax.set_title('income')
fig.savefig('test.png', dpi=300)
plt.show()





