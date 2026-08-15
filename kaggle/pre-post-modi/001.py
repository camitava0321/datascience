# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
"""
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb

df = pd.read_csv('DATA.csv')
print (df)

#Histograms represent the data distribution by forming bins along the range of the data and 
#then drawing bars to show the number of observations that fall in each bin.
#Seaborn comes with some datasets and we have used few datasets in our previous chapters. 
#We have learnt how to load the dataset and how to lookup the list of available datasets.
#df = sb.load_dataset('iris')
sb.set_style("whitegrid")
sb.distplot(df['electricity gas & water supply'],kde = False)
plt.show()
#Here, kde flag is set to False. 
#As a result, the representation of the kernel estimation plot will be removed and only histogram is plotted.

#Overriding the Elements
#If you want to customize the Seaborn styles, you can pass a dictionary of parameters to the set_style() function. Parameters available are viewed using axes_style() function.
print (sb.axes_style)
#Altering the values of any of the parameter will alter the plot style.
sb.set_style("darkgrid", {'axes.axisbelow': False})
#Scaling Plot Elements
sb.set_context('paper')
sb.set_palette("husl")
sb.distplot(df['construction'])
sb.distplot(df['construction'],kde = False)
sb.distplot(df['construction'],hist = False)
sb.despine()
current_palette = sb.color_palette()
#This function plots the color palette as horizontal array. 
sb.palplot(current_palette)
sb.palplot(sb.color_palette("Greens"))
plt.show()

sb.jointplot(x = 'construction',y = 'industry',data = df)
sb.jointplot(x = 'construction',y = 'industry',data = df, kind='hex')
sb.jointplot(x = 'construction',y = 'industry',data = df, kind='kde')
#stripplot() is used when one of the variable under study is categorical. 
#It represents the data in sorted order along any one of the axis.
sb.stripplot(x = "year", y = "per capita nnp", data = df)
#In the above plot, we can clearly see the difference of petal_length in each species. 
#But, the major problem with the above scatter plot is that the points on the scatter plot are overlapped. 
#We use the ‘Jitter’ parameter to handle this kind of scenario.

#Jitter adds some random noise to the data. This parameter will adjust the positions along the categorical axis.
sb.stripplot(x = "year", y = "per capita nnp", data = df, jitter=True)
#Swarmplot()
#Another option which can be used as an alternate to ‘Jitter’ is function swarmplot(). 
#This function positions each point of scatter plot on the categorical axis and thereby avoids overlapping points −
sb.swarmplot(x = "year", y = "per capita nnp", data = df)
plt.show()

sb.set(style="ticks")
g = sb.PairGrid(df); g.map(plt.scatter)

sb.pairplot(data=df,
                  y_vars=['year'],
                  x_vars=['manufacturing','electricity gas & water supply','construction','industry','per capita nnp','employment in public and private sector','gdp'])

current_palette = sb.color_palette()
sb.palplot(sb.color_palette("BrBG", 7))
plt.show()


