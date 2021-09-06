# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Introduction
"""
"""
In Analytics, the best way to get insights is by visualizing the data. 
Data can be visualized by representing it as plots which is easy to understand, explore and grasp. 
Such data helps in drawing the attention of key elements.

To analyse a set of data using Python, we make use of Matplotlib, a widely implemented 2D plotting library. 
Likewise, Seaborn is a visualization library in Python. It is built on top of Matplotlib.

Seaborn Vs Matplotlib
Matplotlib “tries to make easy things easy and hard things possible”, 
Seaborn tries to make a well-defined set of hard things easy too.”

Seaborn helps resolve the two major problems faced by Matplotlib; the problems are −
    Default Matplotlib parameters
    Working with data frames

As Seaborn compliments and extends Matplotlib, the learning curve is quite gradual. 
If you know Matplotlib, you are already half way through Seaborn.

Important Features of Seaborn
    Built in themes for styling matplotlib graphics
    Visualizing univariate and bivariate data
    Fitting in and visualizing linear regression models
    Plotting statistical time series data
    Seaborn works well with NumPy and Pandas data structures
    It comes with built in themes for styling Matplotlib graphics

In most cases, you will still use Matplotlib for simple plotting. 
The knowledge of Matplotlib is recommended to tweak Seaborn’s default plots.
"""
#Seaborn comes handy when dealing with DataFrames, which is most widely used data structure for data analysis.
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb

#Seaborn comes with a few important datasets in the library. 
#When Seaborn is installed, the datasets download automatically.
#One can use any of these datasets for learning. 
#With the help of the following function you can load the required dataset
#load_dataset()

#Importing Data as Pandas DataFrame
#This dataset loads as Pandas DataFrame by default. 
df = sb.load_dataset('tips')
print (df.head())

#To view all the available data sets in the Seaborn library, 
#you can use the following command with the get_dataset_names() function as shown below −
print (sb.get_dataset_names())

#following datasets are in seaborn
#[u'anscombe', u'attention', u'brain_networks', u'car_crashes', u'dots', 
#u'exercise', u'flights', u'fmri', u'gammas', u'iris', u'planets', u'tips', 
#u'titanic']

#DataFrames store data in the form of rectangular grids by which the data can be over viewed easily. 
#Each row of the rectangular grid contains values of an instance, and 
#each column of the grid is a vector which holds data for a specific variable. 
#This means that rows of a DataFrame do not need to contain, values of same data type, 
#they can be numeric, character, logical, etc. 
#DataFrames for Python come with the Pandas library, and 
#they are defined as two-dimensional labeled data structures with potentially different types of columns.