# -*- coding: utf-8 -*-
# Author: Amitava Chakraborty
#Automatic parameter searches
#All estimators have parameters (often called hyper-parameters in the literature) that can be tuned. 
#The generalization power of an estimator often critically depends on a few parameters. 
#For example a RandomForestRegressor has a n_estimators parameter that determines the number of trees in the forest, 
#and a max_depth parameter that determines the maximum depth of each tree. 
#Quite often, it is not clear what the exact values of these parameters should be since they depend on the data at hand.

#Scikit-learn provides tools to automatically find the best parameter combinations (via cross-validation). 
#In the following example, we randomly search over the parameter space of a random forest with a RandomizedSearchCV object. 
#When the search is over, the RandomizedSearchCV behaves as a RandomForestRegressor 
#that has been fitted with the best set of parameters. Read more in the User Guide:

from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import train_test_split
from scipy.stats import randint

X, y = fetch_california_housing(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# define the parameter space that will be searched over
param_distributions = {'n_estimators': randint(1, 5), 'max_depth': randint(5, 10)}

# now create a searchCV object and fit it to the data
search = RandomizedSearchCV(estimator=RandomForestRegressor(random_state=0),
                            n_iter=5,
                            param_distributions=param_distributions,
                            random_state=0)
search.fit(X_train, y_train)
#%% - 
print(search.best_params_)
# the search object now acts like a normal random forest estimator
# with max_depth=9 and n_estimators=4
print(search.score(X_test, y_test))
#Note In practice, you almost always want to search over a pipeline, instead of a single estimator. 
#One of the main reasons is that if you apply a pre-processing step to the whole dataset without using a pipeline, 
#and then perform any kind of cross-validation, 
#you would be breaking the fundamental assumption of independence between training and testing data. 
#Indeed, since you pre-processed the data using the whole dataset, 
#some information about the test sets are available to the train sets. 
#This will lead to over-estimating the generalization power of the estimator (you can read more in this Kaggle post).
#Using a pipeline for cross-validation and searching will largely keep you from this common pitfall.