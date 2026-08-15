# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

from subprocess import check_output
from sklearn import datasets, linear_model

#print(check_output(["ls", "*"]).decode("utf8"))

def linear_model_main(x,y,predict_value):
    regr = linear_model.LinearRegression()
    regr.fit(x, y)
    predict_outcome = regr.predict(predict_value)
    predictions = {}
    predictions['predicted_value'] = predict_outcome
    return predictions

data = pd.read_csv('usdinr2.csv')
date_parameter = []
price_parameter = []
for date ,price in zip(data['date'],data['price']):
    date_parameter.append([date])
    price_parameter.append(float(price))
    
print (date_parameter)
print (price_parameter)

year = [[2020]] #find value for this year
result = linear_model_main(date_parameter,price_parameter,year)

print("Predition for usd vs inr on :",year," value is ",result['predicted_value'])

# Any results you write to the current directory are saved as output.