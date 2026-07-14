#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 11:14:36 2025

@author: camitava
"""

# !pip install scikit-fuzzy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import skfuzzy as fuzz
from sklearn.preprocessing import StandardScaler

###Load and explore the dataset
data = pd.read_csv("customers.csv")

# Display the first few rows of the dataset and check for missing values
print(data.head(),"\n")
print(data.info())

# Preprocess the data
#Spending Score '' is between 1-100
X = data[['annual_income', 'spending_score']].values
print(X)

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled)

#Apply Fuzzy C Means clustering
n_clusters = 5  # Number of clusters
m = 2  # Fuzziness parameter

cntr, u, u0,d,jm,p, fpc = fuzz.cluster.cmeans(
    X_scaled.T, n_clusters, m, error=0.005, maxiter=1000, init=None
)

# Visualize the clusters
cluster_membership = np.argmax(u, axis=0)

plt.figure(figsize=(8, 6))
for i in range(n_clusters):
    plt.scatter(X[cluster_membership == i, 0], X[cluster_membership == i, 1], label=f'Cluster {i+1}')

plt.scatter(cntr[0], cntr[1], marker='x', color='black', label='Centroids')

plt.title('Fuzzy C-Means Clustering on Mall Customer Data')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.grid(True)
plt.show()