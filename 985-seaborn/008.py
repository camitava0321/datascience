# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Distribution of Observations
"""
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('iris')

#In categorical scatter plots the approach becomes limited in the information 
#it can provide about the distribution of values within each category. 
#Now, going further, let us see what can facilitate us with performing comparison with in categories.

#Box Plots
#Boxplot is a convenient way to visualize the distribution of data through their quartiles.
#Box plots usually have vertical lines extending from the boxes which are termed as whiskers. 
#These whiskers indicate variability outside the upper and lower quartiles, 
#hence Box Plots are also termed as box-and-whisker plot and box-and-whisker diagram. 
#Any Outliers in the data are plotted as individual points.


#Violin Plots
#Violin Plots are a combination of the box plot with the kernel density estimates. 
#So, these plots are easier to analyze and understand the distribution of the data.
#We use tips dataset to study violin plots. 
#This dataset contains the information related to the tips given by the customers in a restaurant.
df = sb.load_dataset('tips')
sb.violinplot(x = "day", y = "total_bill", data=df)
plt.show()

#The above plot shows the distribution of total_bill on four days of the week. 

#The quartile and whisker values from the boxplot are shown inside the violin. 
#As the violin plot uses KDE, the wider portion of violin indicates the higher density and 
#narrow region represents relatively lower density. 
#The Inter-Quartile range in boxplot and higher density portion in kde 
#fall in the same region of each category of violin plot.

#Now we want to see how the distribution behaves with respect to sex
sb.violinplot(x = "day", y = "total_bill",hue = 'sex', data = df)
plt.show()

#Now we can clearly see the spending behavior between male and female. 
#We can easily say that, men make more bill than women by looking at the plot.

#And, if the hue variable has only two classes, 
#we can beautify the plot by splitting each violin into two instead of two violins on a given day. 
#Either parts of the violin refer to each class in the hue variable.
sb.violinplot(x = "day", y="total_bill",hue = 'sex', data = df)
plt.show()
