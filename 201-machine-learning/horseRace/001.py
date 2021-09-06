# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:48:12 2019

@author: AMITAVA
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing

df = pd.read_csv("Horse Race Probability.csv")
print (df)


fig=plt.figure()
fig.set_size_inches(12,8)
min_max_scaler = preprocessing.MinMaxScaler()
float_array = df['Expected return for $1'].values.astype(float)
float_array=float_array.reshape(-1,1)
scaled_array = min_max_scaler.fit_transform(float_array)
print(scaled_array)
plt.bar(df['Horse'], df['Calculated Winning Probablity'],label='CWP')
plt.plot(df['Horse'], scaled_array, 'g', label='return')
plt.plot(df['Horse'], scaled_array, 'go')
plt.plot(df['Horse'], df['roll'],'rs', label='roll')

leg = plt.legend(loc='best', ncol=3)
leg.get_frame().set_alpha(0.5)

plt.ylabel('expected return/Calc Win Prob/Roll')
plt.xlabel('Horse')
plt.grid(True)

