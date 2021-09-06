# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Plotting Wide Form Data
"""
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
#It is always preferable to use ‘long-from’ or ‘tidy’ datasets. 
#But at times when we are left with no option rather than to use a ‘wide-form’ dataset, 
#same functions can also be applied to “wide-form” data in a variety of formats, 
#including Pandas Data Frames or two-dimensional NumPy arrays. 
#These objects should be passed directly to the data parameter the x and y variables must be specified as strings
df = sb.load_dataset('iris')
sb.boxplot(data = df, orient = "h")
plt.show()
#Additionally, these functions accept vectors of Pandas or NumPy objects rather than variables in a DataFrame.

sb.boxplot(data = df, orient = "v")
plt.show()
#The major advantage of using Seaborn for many developers in Python world is 
#because it can take pandas DataFrame object as parameter.