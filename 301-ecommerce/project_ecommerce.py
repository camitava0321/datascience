# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 12:26:25 2018

@author: ibm
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#%%
"""
Get the Data

We'll work with the Ecommerce Customers csv file from the company. It has Customer info, suchas Email, Address, and their color Avatar. Then it also has numerical value columns:

    Avg. Session Length: Average session of in-store style advice sessions.
    Time on App: Average time spent on App in minutes
    Time on Website: Average time spent on Website in minutes
    Length of Membership: How many years the customer has been a member.

Read in the Ecommerce Customers csv file as a DataFrame.
"""
customers = pd.read_csv('Ecommerce Customers.csv')

#Lets check the head of customers
customers.head()
customers.info()
customers.describe()

#%%
#Exploratory Data Analysis
#For the rest of the exercise we'll only be using the numerical data of the csv file.

#Let's explore these types of relationships across the entire data set.
sns.pairplot(customers)

#%%
#Lets compare the Time on Website and Yearly Amount Spent columns.
sns.jointplot(x='Time on Website',y='Yearly Amount Spent',data=customers)

#Do the same but with the Time on App column instead. 
sns.jointplot(x='Time on App',y='Yearly Amount Spent',data=customers)
#%%
#Lets create a jointplot to create a 2D hex bin plot comparing Time on App and Length of Membership.
sns.jointplot(x='Time on App',y='Length of Membership',data=customers,kind='hex')

#Lets create a jointplot to create a 2D hex bin plot comparing Time on App and Length of Membership.
sns.jointplot(x='Avg. Session Length',y='Length of Membership',data=customers)

#%%
#Based off this plot what looks to be the most correlated feature with Yearly Amount Spent?
# Length of Membership
#A linear model plot of Yearly Amount Spent vs. Length of Membership.
sns.lmplot(x='Yearly Amount Spent',y='Length of Membership',data=customers)

sns.distplot(customers['Yearly Amount Spent'])
#%%
#Heatmap of the customers dataframe to check the correlation.
fig = plt.subplots(figsize=(12,8))
sns.heatmap(customers[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership','Yearly Amount Spent']].corr(),
annot=True,linewidth=0.5)
#%%
#Training and Testing Data
#Now that we've explored the data a bit, let's go ahead and split the data into training and testing sets.
customers.columns
X = customers[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']]
y = customers['Yearly Amount Spent']

X.head()
y.head()

#Lets split the data into training and testing sets.
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=101)

#Training the Model
#Now its time to train our model on our training data!
#Lets Import LinearRegression from sklearn.linear_model
from sklearn.linear_model import LinearRegression

#Lets Create an instance of a LinearRegression() model named lm.
lm = LinearRegression()

#Now Train/fit lm on the training data.
lm.fit(X_train,y_train)

#Lets check the coefficients of the model
lm.coef_

cdf = pd.DataFrame(lm.coef_,X_train.columns,columns=['Coeff'])

cdf

#%%
#Predicting Test Data
#Now that we have fit our model, let's evaluate its performance by predicting off the test values!
#Will use lm.predict() to predict off the X_test set of the data.
predictions = lm.predict(X_test)

predictions
#%%
#Scatterplot of the real test values versus the predicted values.
plt.scatter(y_test,predictions)
plt.title("Actual Vs Predicted Yearly Amount Spent")
plt.xlabel("Actual Yearly Amount Spent ")
plt.ylabel("Predicted Yearly Amount Spent")


#Evaluating the Model
#Let's evaluate our model performance by calculating the residual sum of squares and the explained variance score (R^2).
#Calculate the Mean Absolute Error, Mean Squared Error, and the Root Mean Squared Error.

from sklearn import metrics

# Mean Absolute Error
metrics.mean_absolute_error(y_test,predictions)

# Mean Squared Error
metrics.mean_squared_error(y_test,predictions)

# Root Mean Squared Error
np.sqrt(metrics.mean_squared_error(y_test,predictions))

# Variance score (R^2)
metrics.explained_variance_score(y_test,predictions)


#Residuals
#We have a very good model with a good fit. Let's quickly explore the residuals to make sure everything was okay with our data.
#Plot a histogram of the residuals and make sure it looks normally distributed.
sns.distplot((y_test-predictions),bins=50)










