# -*- coding: utf-8 -*-
#Author: Amitava Chakraborty
#kmeans clustering centroid
#The KMeans clustering algorithm can be used to cluster observed data automatically. 
#All the centroids of KMEans Algo are stored in the attribute cluster_centers.
from sklearn.cluster import KMeans
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt

# clustering dataset
x1 = np.array([3, 2, 7, 4, 1, 1, 2, 1, 6, 6, 6, 5, 6, 7, 8, 9, 8, 9, 9, 8])
x2 = np.array([5, 2, 4, 5, 4, 6, 6, 5, 8, 6, 7, 6, 7, 1, 2, 1, 2, 3, 2, 3])

# create new plot and data
plt.plot()
X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)
colors = ['b', 'g', 'c']
markers = ['o', 'v', 's']

# KMeans algorithm 
K = 3
kmeans_model = KMeans(n_clusters=K).fit(X)

print(kmeans_model.cluster_centers_)
#Convert the attribute to a numpy array:
centers = np.array(kmeans_model.cluster_centers_)

plt.plot()
plt.title('k means centroids')

for i, l in enumerate(kmeans_model.labels_):
    plt.plot(x1[i], x2[i], color=colors[l], marker=markers[l],ls='None')
    plt.xlim([0, 10])
    plt.ylim([0, 10])

#This array is one dimensional
#So we use scatter plot
plt.scatter(centers[:,0], centers[:,1], marker="x", color='r')
plt.show()