# -*- coding: utf-8 -*-
# Author: Amitava Chakraborty
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

#%%- Load the KYC dataset
trainingData = pd.read_csv('kyc.csv')
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

#Get the interestng columns from the training set
trainingData.columns
df = trainingData[['Gender','MaritalStatus','Nationality','Occupation','GrossAnnualIncome','NetWorth','SpendIndicator','AnnualSpend','AnnualIncome','AnnualTax','CreditScore','Age']]


fig, axes = plt.subplots(nrows=5, ncols=3,figsize=(30,30))
fig.suptitle('Categorical Plotting')
fig.subplots_adjust(wspace=.2)
fig.subplots_adjust(hspace=.3)

#Gender Bias of the data
data = df['Gender'].value_counts()
print (data.index, data)
#plot bar plot
axes[0][0].bar(data.index,data)
axes[0][0].set_title('Gender Bias')

#Marital Status Bias of the data
data = df['MaritalStatus'].value_counts()
#plot bar plot
axes[0][1].bar(data.index,data)
axes[0][1].set_title('Marital Status Bias')

#Nationality Bias of the data
data = df['Nationality'].value_counts()
#plot box plot
axes[0][2].bar(data.index,data)
axes[0][2].set_title('Nationality Bias')

#Gender Bias of the data
axes[1][0].scatter(df['Gender'], df['Age'])
axes[1][0].set_title('Gender vs Age')

#Marital Status Bias of the data
axes[1][1].scatter(df['MaritalStatus'], df['Age'])
axes[1][1].set_title('MaritalStatus vs Age')

#SpendIndicator Bias of the data
axes[1][2].scatter(df['SpendIndicator'], df['Age'])
axes[1][2].set_title('SpendIndicator vs Age')

df.plot(x='Age', y='CreditScore', linewidth=0, marker='o', color='000', ax=axes[2,0])
df.plot(x='Age', y='GrossAnnualIncome', linewidth=0, marker='o', color='000', ax=axes[2,1])
df.plot(x='Age', y='AnnualSpend', linewidth=0, marker='^', color='r', ax=axes[2,2])

df.plot(x='Age', y='AnnualTax', linewidth=0, marker='D', color='r', ax=axes[3,0])
df.plot(x='Age', y='NetWorth', linewidth=0, marker='s', color='r', ax=axes[3,1])
#trainingData.plot(x='AnnualIncome', y='AnnualSpend', linewidth=0, marker='o', fillstyle='none',color='g', ax=ax[1,2])
df.plot(x='AnnualIncome', y='AnnualSpend', linewidth=0, marker='o', color='g', ax=axes[3,2])

df.plot(x='NetWorth', y='AnnualSpend', linewidth=0, marker='h', color='r', ax=axes[4,0])
plt.show()

#OR



#%%- Predict age vs spend
# Create linear regression object
regr = linear_model.LinearRegression()
listA = ['Age','AnnualSpend']
dataX = trainingData[listA].as_matrix()
dataX = trainingData.as_matrix(columns=['Age'])  #selects 'age' only
dataY = trainingData['AnnualSpend'].values

# Train the model using the training sets
#regr.fit(diabetes_X_train, diabetes_y_train)
regr.fit(dataX, dataY)

#Make predictions using the testing set
testDataX = testData[listA]
testDataX = testData.as_matrix(columns=['Age'])  #selects 'age' only
testDataY = testData['AnnualSpend']
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
plt.scatter(testDataX, testDataY,  color='black')
plt.plot(testDataX, testDataY_predicted, color='blue', linewidth=3)

fig.suptitle('test title', fontsize=20)
plt.xlabel('age', fontsize=18)
plt.ylabel('spend', fontsize=16)
plt.xticks(())
plt.yticks(())
fig.savefig('test.jpg')
plt.show()

#%%- Predict all vs spend
# Create linear regression object
regr = linear_model.LinearRegression()
listA = ['Age','GrossAnnualIncome','NetWorth','AnnualIncome']
dataX = trainingData[listA].as_matrix()
#dataX = trainingData.as_matrix(columns=trainingData.columns[2:3])  #selects 'age' only
dataY = trainingData['AnnualSpend'].values

# Train the model using the training sets
#regr.fit(diabetes_X_train, diabetes_y_train)
regr.fit(dataX, dataY)

#Make predictions using the testing set
testDataX = testData[listA]
#testDataX = testData.as_matrix(columns=testData.columns[2:3])
testDataY = testData['AnnualSpend']
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
plt.plot(testDataX['Age'], testDataY_predicted, color='yellow', marker='^', linewidth=0)

fig.suptitle('test title', fontsize=20)
fig.dpi=80
fig.set_size_inches(11,6)
plt.xlabel('Age', fontsize=18)
plt.ylabel('AnnualSpend', fontsize=16)
plt.xticks(())
plt.yticks(())

scat = ax.scatter(testData['Age'], testDataY, c=testData['AnnualIncome'], s=170, marker='o')
colorbar=fig.colorbar(scat, cmap='RdBu')
colorbar.ax.set_title('AnnualIncome')
fig.savefig('test.png', dpi=300)
plt.show()

#%%
from sklearn import svm
#Choosing the parameters of the model
#In this example we set the value of gamma manually. 
#It is possible to automatically find good values for the parameters by using tools 
#such as grid search and cross validation.
clf = svm.SVC(gamma=0.001, C=100.)

#We call our estimator instance clf, as it is a classifier. 
#It now must be fitted to the model, that is, it must learn from the model. 
#This is done by passing our training set to the fit method. 

#As a training set - we use the generated KYC data 
listA = ['Age','GrossAnnualIncome','NetWorth','AnnualIncome','AnnualSpend']
data = trainingData[listA].as_matrix()
#data = [[1, 2, 3], [1, 10, 20], [2, 4, 3], [3, 30, 40], [3, 11, 5], [4, 40, 60]]
counter=0
avg_Income = trainingData['GrossAnnualIncome'].mean()
#Set the classes - Good vs Bad customers
targets=['B']* len(data)
for datum in data:
    #targets[counter]='B'
    if datum[0]<50 :
        if datum[1] > avg_Income:
            annualSpend = datum[4]
            annualIncome = datum[3]
            if annualSpend > annualIncome/2.5:
                print (str(counter) +" : " + str(datum)+ " : "+ str(datum[1]))
                targets[counter]='G'
    counter = counter+1
    
print (targets)
#targets = ['B','G','B','G','B','G']

clf.fit(data, targets)  

testdata = testData[listA].as_matrix()
#testdata1 = [[9, 50, 300]]
#testdata2 = [[9, 11, 13]]


print (testdata)

#Now you can predict new values, in particular, 
#we can ask to the classifier what is the digit of our last image in the digits dataset, 
#which we have not used to train the classifier:
testClasses = clf.predict(testdata)

#%% - Data Creation for QSVM
#We create two Dicts - training dict and test dict
#Focus to create the dicts is to have maximally separated classes
counter=0
avg_Income = trainingData['GrossAnnualIncome'].mean()
#Set the classes - Good vs Bad customers
badTrainingCustomers = [] * len(data)
goodCustomers = [] * len(data)

for datum in data:
    #targets[counter]='B'
    if datum[0]<50 :
        if datum[1] > avg_Income:
            annualSpend = datum[4]
            annualIncome = datum[3]
            if annualSpend > annualIncome/2.5:
                print (str(counter) +" : " + str(datum)+ " : "+ str(datum[1]))
                goodCustomer=[datum[0],datum[1]]
                goodCustomers.append(goodCustomer)

    if datum[0]>50 :
        if datum[1] < avg_Income:
            print (str(counter) +" : " + str(datum)+ " : "+ str(datum[1]))
            badCustomer=[datum[0],datum[1]]
            badTrainingCustomers.append(badCustomer)
    
    counter = counter+1
print (goodCustomers)
print (badTrainingCustomers)

trainingDict = {'G':goodCustomers, 'B':badTrainingCustomers}

counter=0
avg_Income = testdata['GrossAnnualIncome'].mean()
#Set the classes - Good vs Bad customers
badCustomers = [] * len(testdata)
goodCustomers = [] * len(testdata)

for datum in testdata:
    #targets[counter]='B'
    if datum[0]<50 :
        if datum[1] > avg_Income:
            annualSpend = datum[4]
            annualIncome = datum[3]
            if annualSpend > annualIncome/2.5:
                print (str(counter) +" : " + str(datum)+ " : "+ str(datum[1]))
                goodCustomer=[datum[0],datum[1]]
                goodCustomers.append(goodCustomer)

    if datum[0]>50 :
        if datum[1] < avg_Income:
            print (str(counter) +" : " + str(datum)+ " : "+ str(datum[1]))
            badCustomer=[datum[0],datum[1]]
            badCustomers.append(badCustomer)
    
    counter = counter+1
print (goodCustomers)
print (badCustomers)

testDict = {'G':goodCustomers, 'B':badCustomers}


#%%
N = len(testdata)

#Age vs testClasses
x = testData['Age']
y = testClasses
#x, y = np.random.rand(2, N)
c = np.random.randint(1, 10, size=N)
#s = np.random.randint(10, 220, size=N)
s = testData['AnnualIncome']
s_min=min(s)
s_max=max(s)
s_norm = ((s-s_min)/(s_max-s_min))*10
a=s
s=np.interp(a, (a.min(), a.max()), (1, 300))
s=s.astype(int)
fig, ax = plt.subplots(figsize=(15,15))

scatter = ax.scatter(y, x, c=c, s=s)

# produce a legend with the unique colors from the scatter
legend1 = ax.legend(*scatter.legend_elements(),
                    loc="lower left", title="Classes")
ax.add_artist(legend1)

# produce a legend with a cross section of sizes from the scatter
handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)
legend2 = ax.legend(handles, labels, loc="upper right", title="Sizes")

plt.show()



