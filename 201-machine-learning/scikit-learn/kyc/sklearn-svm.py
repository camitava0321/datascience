# -*- coding: utf-8 -*-
# Author: Amitava Chakraborty
#%% - Learning and predicting
#In the case of the KYC dataset, the task is to predict, 
#given a data, which class it represents. 
#We are given samples of each of the 2 possible classes (the Good and the Bad customers) 
#on which we fit an estimator to be able to predict the classes to which unseen samples belong.

#In scikit-learn, an estimator for classification is a Python object that 
#implements the methods fit(X, y) and predict(T).

#An example of an estimator is the class sklearn.svm.SVC that implements support vector classification. 
#The constructor of an estimator takes as arguments the parameters of the model, 
#but for the time being, we will consider the estimator as a black box:

from sklearn import datasets
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
#Load the KYC dataset
data = [[1, 2, 3], [1, 10, 20], [2, 4, 3], [3, 30, 40], [3, 11, 5], [4, 40, 60]]
targets = ['B','G','B','G','B','G']
testdata1 = [[9, 50, 300]]
testdata2 = [[9, 11, 13]]


#digits = datasets.load_digits()
print data
clf.fit(data, targets)  
#clf.fit(digits.data[:-1], digits.target[:-1])  

#Now you can predict new values, in particular, 
#we can ask to the classifier what is the digit of our last image in the digits dataset, 
#which we have not used to train the classifier:
clf.predict(testdata1)
clf.predict(testdata2)
#clf.predict(digits.data[-1:])

#%%
import numpy
import seaborn as sb
from matplotlib import pyplot as plt
#Kernel Density Estimation (KDE) is a way to estimate the probability density function 
#of a continuous random variable. 
#It is used for non-parametric analysis.

#Setting the hist flag to False in distplot will yield the kernel density estimation plot.
A = numpy.array(data)
a = A[:,0]
b = A[:,1]
sb.distplot(a,hist=False)
plt.show()

#Fitting Parametric Distribution
#distplot() is used to visualize the parametric distribution of a dataset.
sb.distplot(b)
plt.show()

#Plotting Bivariate Distribution
#Bivariate Distribution is used to determine the relation between two variables. 
#This mainly deals with relationship between two variables and how one variable is behaving with respect to the other.

#The best way to analyze Bivariate Distribution in seaborn is by using the jointplot() function.
#Jointplot creates a multi-panel figure that projects the bivariate relationship 
#between two variables and also the univariate distribution of each variable on separate axes.
sb.jointplot(a,b,kind='kde')
plt.show()

#It is a kind of Scatter Plot
#Scatter plot is the most convenient way to visualize the distribution 
#where each observation is represented in two-dimensional plot via x and y axis.

#The plot shows the relationship between the petal_length and petal_width in the Iris data. 
#A trend in the plot says that positive correlation exists between the variables under study.

#Hexbin Plot
#Hexagonal binning is used in bivariate data analysis when the data is sparse in density 
#i.e., when the data is very scattered and difficult to analyze through scatterplots.

sb.swarmplot(a,b)
plt.show()

sb.regplot(a,b)
sb.lmplot(a,b)
plt.show()
