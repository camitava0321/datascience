# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
Window Functions
"""

#For working on numerical data, 
#Pandas provide few variants like rolling, expanding and exponentially moving weights for window statistics. 
#Among these are sum, mean, median, variance, covariance, correlation, etc.

#We will now learn how each of these can be applied on DataFrame objects.
#.rolling() Function
#This function can be applied on a series of data. Specify the window=n argument and apply the appropriate statistical function on top of it.
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print df.rolling(window=3).mean()

Its output is as follows −

                    A           B           C           D
2000-01-01        NaN         NaN         NaN         NaN
2000-01-02        NaN         NaN         NaN         NaN
2000-01-03   0.434553   -0.667940   -1.051718   -0.826452
2000-01-04   0.628267   -0.047040   -0.287467   -0.161110
2000-01-05   0.398233    0.003517    0.099126   -0.405565
2000-01-06   0.641798    0.656184   -0.322728    0.428015
2000-01-07   0.188403    0.010913   -0.708645    0.160932
2000-01-08   0.188043   -0.253039   -0.818125   -0.108485
2000-01-09   0.682819   -0.606846   -0.178411   -0.404127
2000-01-10   0.688583    0.127786    0.513832   -1.067156
#Note − Since the window size is 3, for first two elements there are nulls and from third the value will be the average of the n, n-1 and n-2 elements. Thus we can also apply various functions as mentioned above.

#.expanding() Function
#This function can be applied on a series of data. Specify the min_periods=n argument and apply the appropriate statistical function on top of it.
print df.expanding(min_periods=3).mean()

Its output is as follows −

                   A           B           C           D
2000-01-01        NaN         NaN         NaN         NaN
2000-01-02        NaN         NaN         NaN         NaN
2000-01-03   0.434553   -0.667940   -1.051718   -0.826452
2000-01-04   0.743328   -0.198015   -0.852462   -0.262547
2000-01-05   0.614776   -0.205649   -0.583641   -0.303254
2000-01-06   0.538175   -0.005878   -0.687223   -0.199219
2000-01-07   0.505503   -0.108475   -0.790826   -0.081056
2000-01-08   0.454751   -0.223420   -0.671572   -0.230215
2000-01-09   0.586390   -0.206201   -0.517619   -0.267521
2000-01-10   0.560427   -0.037597   -0.399429   -0.376886

#.ewm() Function
#ewm is applied on a series of data. Specify any of the com, span, halflife argument and apply the appropriate statistical function on top of it. It assigns the weights exponentially.
print df.ewm(com=0.5).mean()

Its output is as follows −

                    A           B           C           D
2000-01-01   1.088512   -0.650942   -2.547450   -0.566858
2000-01-02   0.865131   -0.453626   -1.137961    0.058747
2000-01-03  -0.132245   -0.807671   -0.308308   -1.491002
2000-01-04   1.084036    0.555444   -0.272119    0.480111
2000-01-05   0.425682    0.025511    0.239162   -0.153290
2000-01-06   0.245094    0.671373   -0.725025    0.163310
2000-01-07   0.288030   -0.259337   -1.183515    0.473191
2000-01-08   0.162317   -0.771884   -0.285564   -0.692001
2000-01-09   1.147156   -0.302900    0.380851   -0.607976
2000-01-10   0.600216    0.885614    0.569808   -1.110113

#Window functions are majorly used in finding the trends within the data graphically by smoothing the curve. 
#If there is lot of variation in the everyday data and a lot of data points are available, 
#then taking the samples and plotting is one method and 
#applying the window computations and plotting the graph on the results is another method. 
#By these methods, we can smooth the curve or the trend.