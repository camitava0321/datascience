# -*- coding: utf-8 -*-
"""
Scipy Examples
@author: AMITAVA
SciPy - Cluster
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

"""
K-means clustering is a method for finding clusters and cluster centers in a set of unlabelled data. 
Intuitively, we might think of a cluster as – comprising of a group of data points, 
whose inter-point distances are small compared with the distances to points outside of the cluster. 
Given an initial set of K centers, the K-means algorithm iterates the following two steps −
    For each center, the subset of training points (its cluster) that is closer to it 
    is identified than any other center.

    The mean of each feature for the data points in each cluster are computed, 
    and this mean vector becomes the new center for that cluster.

These two steps are iterated until the centers no longer move or the assignments no longer change. 
Then, a new point x can be assigned to the cluster of the closest prototype. 
The SciPy library provides a good implementation of the K-Means algorithm through the cluster package. 
"""
#%%
#Import K-Means
from scipy.cluster.vq import kmeans,vq,whiten

#Data generation
#We have to simulate some data to explore the clustering.
from numpy import vstack,array
from numpy.random import rand

# data generation with three features
data = vstack((rand(100,3) + array([.5,.5,.5]),rand(100,3)))

print (data)
#%% - Whiten the data, Normalize a group of observations on a per feature basis. 
#The data is not normalized. 
#Before running K-Means, it is beneficial to rescale each feature dimension of the observation set 
#with whitening. Each feature is divided by its standard deviation across all observations to give it unit variance.
data = whiten(data)

#Compute K-Means with Three Clusters

# computing K-Means with K = 3 (2 clusters)
centroids,_ = kmeans(data,3)

#The above code performs K-Means on a set of observation vectors forming K clusters. 
#The K-Means algorithm adjusts the centroids until sufficient progress cannot be made, 
#i.e. the change in distortion, since the last iteration is less than some threshold. 
#Here, we can observe the centroid of the cluster by printing the centroids variable using the code given below.
print(centroids)

#%% - Assign each value to a cluster by using the code given below.

# assign each sample to a cluster
clusters,_ = vq(data,centroids)

#The vq function compares each observation vector in the ‘M’ by ‘N’ obs array with the centroids and 
#assigns the observation to the closest cluster. 
#It returns the cluster of each observation and the distortion. 
#We can check the distortion as well. 
#Let us check the cluster of each observation using the following code.

# check clusters of observation
print (clusters)