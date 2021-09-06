# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Histogram
"""
#Histograms represent the data distribution by forming bins along the range of the data and 
#then drawing bars to show the number of observations that fall in each bin.
#Seaborn comes with some datasets and we have used few datasets in our previous chapters. 
#We have learnt how to load the dataset and how to lookup the list of available datasets.

import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('iris')
sb.distplot(df['petal_length'],kde = False)
plt.show()
#Here, kde flag is set to False. 
#As a result, the representation of the kernel estimation plot will be removed and only histogram is plotted.