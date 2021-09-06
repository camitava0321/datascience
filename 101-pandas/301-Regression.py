# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
"""
"""
Linear Regression with pandas, statsmodel
"""
#%% - imports
from IPython.display import HTML, display

import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.sandbox.regression.predstd import wls_prediction_std

import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
sns.set_style("darkgrid")

import pandas as pd
import numpy as np

#%% - descriptive statistics and other related operations on DataFrame
root = '.'

housing_price_index = pd.read_csv(root + '/monthly-hpi.csv')
unemployment = pd.read_csv(root + '/unemployment-macro.csv')
federal_funds_rate = pd.read_csv(root + '/fed_funds.csv')
shiller = pd.read_csv(root + '/shiller.csv')
gross_domestic_product = pd.read_csv(root + '/gdp.csv')

#%% - pandas' merge - join the data together in a single dataframe
#Some data is reported monthly, others are reported quarterly. 
#We merge the dataframes on a certain column so each row is in its logical place for measurement purposes. 
#In this example, the best column to merge on is the date column.

# merge dataframes into single dataframe by date
df = (shiller.merge(housing_price_index, on='date')
                    .merge(unemployment, on='date')
                    .merge(federal_funds_rate, on='date')
                    .merge(gross_domestic_product, on='date'))

df.head()

#%% - ORDINARY LEAST SQUARES ASSUMPTIONS
#we analyze the variables (with plots and descriptive statistics) and 
#figure out the best predictors of our dependent variable.
#here we are skipiing the exploratory analysis. 

#We'll use ordinary least squares (OLS), a basic yet powerful way to assess our model.
"""
OLS measures the accuracy of a linear regression model.
It is built on assumptions which, if correct, indicate the model may be the correct one 
through which to interpret our data. 
If the assumptions don't hold, our model's conclusions lose their validity.

The OLS assumptions:
Linearity: A linear relationship exists between the dependent and predictor variables. 
If no linear relationship exists, linear regression isn't the correct model to explain our data.

No multicollinearity: Predictor variables are not collinear, i.e., they aren't highly correlated. 
If the predictors are highly correlated, try removing one or more of them. 
Since additional predictors are supplying redundant information, 
removing them shouldn't drastically reduce the Adj. R-squared (see below).

Zero conditional mean: The average of the distances (or residuals) between the observations and the trend line is zero. 
Some will be positive, others negative, but they won't be biased toward a set of values.

Homoskedasticity: The certainty (or uncertainty) of our dependent variable is equal across all values 
of a predictor variable; that is, there is no pattern in the residuals. 
In statistical jargon, the variance is constant.

No autocorrelation (serial correlation): Autocorrelation is when a variable is correlated with itself 
across observations. For example, a stock price might be serially correlated 
if one day's stock price impacts the next day's stock price.
"""

#SIMPLE LINEAR REGRESSION
#Using statsmodels' ols function, 
#we construct our model setting housing_price_index as a function of total_unemployed. 
#We assume that an increase in the total number of unemployed people 
#will have downward pressure on housing prices. 

#The code below shows how to set up a simple linear regression model with 
#total_unemploymentas our predictor variable.

# fit our model with .fit() and show results
# we use statsmodels' formula API to invoke the syntax below,
# where we write out the formula using ~
housing_model = ols("housing_price_index ~ total_unemployed", data=df).fit()

# summarize our model
housing_model_summary = housing_model.summary()

# convert our table to HTML and add colors to headers for explanatory purposes
html = HTML(
(housing_model_summary
    .as_html()
    .replace('<th>  Adj. R-squared:    </th>', '<th style="background-color:#aec7e8;"> Adj. R-squared: </th>')
    .replace('<th>coef</th>', '<th style="background-color:#ffbb78;">coef</th>')
    .replace('<th>std err</th>', '<th style="background-color:#c7e9c0;">std err</th>')
    .replace('<th>P>|t|</th>', '<th style="background-color:#bcbddc;">P>|t|</th>')
    .replace('<th>[0.025</th>    <th>0.975]</th>', '<th style="background-color:#ff9896;">[0.025</th>    <th style="background-color:#ff9896;">0.975]</th>'))
)
print housing_model_summary

"""
Explanations
1. Adj. R-squared -> 95% of housing prices can be explained by our predictor variable, total_unemployed.

2. The regression coefficient (coef) -> the change in the dependent variable resulting from a one unit change in the predictor variable, all other variables being held constant. 
In our model, a one unit increase in total_unemployed reduces housing_price_index by 8.33. 
In line with our assumptions, an increase in unemployment appears to reduce housing prices.

3. The standard error (std err) measures the accuracy of total_unemployed's coefficient 
by estimating the variation of the coefficient if the same test were run on a different sample of our population. 
Our standard error, 0.41, is low and therefore appears accurate.

4. The p-value (P>|t|) means the probability of an 8.33 decrease in housing_price_index due to a one unit increase in total_unemployed is 0%, 
assuming there is no relationship between the two variables. 
A low p-value indicates that the results are statistically significant, 
that is in general the p-value is less than 0.05.

5. The confidence interval [0.025 0.975] is a range within which our coefficient is likely to fall. 
We can be 95% confident that total_unemployed's coefficient will be within our confidence interval, [-9.185, -7.480].
"""
#%% - REGRESSION PLOTS
# This produces our four regression plots for total_unemployed

fig = plt.figure(figsize=(15,8))

# pass in the model as the first parameter, then specify the 
# predictor variable we want to analyze
fig = sm.graphics.plot_regress_exog(housing_model, "total_unemployed", fig=fig)
"""
Explanation
1. The “Y and Fitted vs. X” graph plots the dependent variable against our predicted values with a confidence interval.
The inverse relationship in our graph indicates that housing_price_index and total_unemployed 
are negatively correlated, i.e., when one variable increases the other decreases.

2. The “Residuals versus total_unemployed” graph shows our model's errors versus the specified predictor variable. 
Each dot is an observed value; the line represents the mean of those observed values. 
Since there's no pattern in the distance between the dots and the mean value, 
the OLS assumption of homoskedasticity holds.

3. The “Partial regression plot” shows the relationship between housing_price_index and total_unemployed, 
taking in to account the impact of adding other independent variables on our existing total_unemployed coefficient. 
We'll see later how this same graph changes when we add more variables.

4. The Component and Component Plus Residual (CCPR) plot is an extension of the partial regression plot, 
but shows where our trend line would lie after adding the impact of adding our other independent variables 
on our existing total_unemployed coefficient.
"""

#%% - The next plot graphs our trend line (green), the observations (dots), and our confidence interval (red).

# predictor variable (x) and dependent variable (y)
x = df[['total_unemployed']]
y = df[['housing_price_index']]

# Retrieve our confidence interval values
# _ is a dummy variable since we don't actually use it for plotting but need it as a placeholder
# since wls_prediction_std(housing_model) returns 3 values
_, confidence_interval_lower, confidence_interval_upper = wls_prediction_std(housing_model)

fig, ax = plt.subplots(figsize=(10,7))

# plot the dots
# 'o' specifies the shape (circle), we can also use 'd' (diamonds), 's' (squares)
ax.plot(x, y, 'o', label="data")

# plot the trend line
# g-- and r-- specify the color to use
ax.plot(x, housing_model.fittedvalues, 'g--.', label="OLS")

# plot upper and lower ci values
ax.plot(x, confidence_interval_upper, 'r--')
ax.plot(x, confidence_interval_lower, 'r--')

# plot legend
ax.legend(loc='best');


