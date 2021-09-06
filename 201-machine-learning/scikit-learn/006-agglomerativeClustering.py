# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 23:16:56 2019

@author: AMITAVA
"""

import numpy as np
from sklearn.cluster import MeanShift
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

#%% - Use sample generator of sklearn to create a dataset
centers = [[1,1],[5,5],[3,10]]
X, _ = make_blobs(n_samples = 500, centers = centers, cluster_std = 1)
		
#Make the example data set - 500 randomized samples - centered around three center-points - with a standard deviation of 1
#One at 1,1, another at 5,5 and the other at 3,10. 
#From here, we generate the sample, unpacking to X and y. 
#X is the dataset, and y is the label of each data point according to the sample generation.

#Unpacking to y is necessary, since the make_blobs returns a label, 
#but we do not actually use y, other than to test the accuracy of the algorithm. 
#Unsupervised learning does not actually train against data and labels, 
#it derives structure and labels on its own.

#%% - Visualize the data set
plt.scatter(X[:,0],X[:,1])
plt.show()
		
#We can already identify the major clusters. 
#There are some points in between the clusters that we do not know exactly where they belong

#%% - The machine can see this data set, without knowing how many clusters there ought to be, 
#and identify the same three clusters - with MeanShift

#initialize MeanShift
ms = MeanShift()
#fit according to the dataset, "X."
ms.fit(X)
#Populate labels and cluster_centers with the machine-chosen labels and cluster centers. 
#the labels are the ones the machine has chosen, these are not the same labels as the unpacked-to "y" variable above.
labels = ms.labels_
cluster_centers = ms.cluster_centers_

#One may compare the two for an accuracy measurement, 
#but this may not be very useful as we have synthetically generated the data. 
#If we were to set our standard deviation to, say, 10, there would be signficant overlap. 
#Even if the data originally came from from one cluster, it might actually be a better fit into another. 
#This isn't really a fault of the machine learning algorithm in any way. 
#The data is actually a better fit elsewhere and you were too wild with the standard deviation in the generation.

#Instead, it might be a bit better of an accuracy measurement to compare the cluster_centers 
#with the actual cluster centers you started with (centers = [[1,1],[5,5],[3,10]]) to create the random data. 
#We'll see how accurate this is, 
#though it should be a given that: 
#The more samples you have, and the less standard deviation, the more accurate your predicted cluster centers should be 
#compared to the actual ones used to generate the randomized data. 

#We can see the cluster centers and grab the total number of clusters by doing the following:
print(cluster_centers)
n_clusters_ = len(np.unique(labels))
print("Number of estimated clusters:", n_clusters_)
		

#%% - To graph the results, we need a list of colors
colors = 10*['r.','g.','b.','c.','k.','y.','m.']

#A simple list of red, green, blue, cyan, black, yellow, and magenta multiplied by ten. 
#We should be confident that we're only going to need three colors, 
#but, with hierarchical clustering, we are allowing the machine to choose, we'd like to have plenty of options. 
#This allows for 70 clusters, so that should be good enough.

#Plotting 
for i in range(len(X)):
#Iterating through all of the sample data points, plotting their coordinates, 
#and coloring by their label # as an index value in our color list.
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)

#scatter plot the cluster centers.
plt.scatter(cluster_centers[:,0],cluster_centers[:,1],
            marker="x",color='k', s=150, linewidths = 5, zorder=10)

plt.show()

#Thus, the machine did the clustering - 

#Our original centers are slightly different, 
#The centers will be different every time we run it
#Since there is a degree of randomness with the sample generation. 