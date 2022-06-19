# -*- coding: utf-8 -*-
# Author: Amitava Chakraborty
#Pipelines: chaining pre-processors and estimators
#Transformers and estimators (predictors) can be combined together into a single unifying object: a Pipeline. 
#The pipeline offers the same API as a regular estimator
#it can be fitted and used for prediction with fit and predict. 
#We will see later, using a pipeline will also prevent you from data leakage, 
#i.e. disclosing some testing data in your training data.

#In the following example, we load the Iris dataset, 
#split it into train and test sets, and compute the accuracy score of a pipeline on the test data:

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# create a pipeline object
pipe = make_pipeline(StandardScaler(), LogisticRegression())

# load the iris dataset and split it into train and test sets
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# fit the whole pipeline
pipe.fit(X_train, y_train)
#%% - we can now use it like any other estimator
score = accuracy_score(pipe.predict(X_test), y_test)
print (score)