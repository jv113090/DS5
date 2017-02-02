#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 20:10:02 2017

@author: JVena
"""
#import data

import pandas as pd
url = '../Project/ProjData.csv'
Data = pd.read_csv(url, sep=' ')

print Data.head()

# Add in code about dimensionality reduction

# K-means with 3 clusters
from sklearn.cluster import KMeans
km = KMeans(n_clusters=3, random_state=1)
km.fit(Data)

# review the cluster labels
km.labels_

# save the cluster labels and sort by cluster
Data['cluster'] = km.labels_
Data.sort_values('ZipCode')

# review the cluster centers
km.cluster_centers_

# calculate the mean of each feature for each cluster
Data.groupby('cluster').mean()

# save the DataFrame of cluster centers
centers = Data.groupby('cluster').mean()

type(centers)

# allow plots to appear in the notebook
%matplotlib inline
import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 14

# create a "colors" array for plotting
import numpy as np
colors = np.array(['red', 'green', 'blue', 'yellow'])

# scatter plot of calories versus alcohol, colored by cluster (0=red, 1=green, 2=blue)
plt.scatter(beer.ZipCode, beer.Income, c=colors[beer.cluster], s=50)

# cluster centers, marked by "+"
plt.scatter(centers.ZipCode, centers.Income, linewidths=3, marker='+', s=300, c='black')

# add labels
plt.xlabel('Income')
plt.ylabel('ZipCode')

# scatter plot matrix (0=red, 1=green, 2=blue)
pd.scatter_matrix(X, c=colors[beer.cluster], figsize=(10,10), s=100)



###Evaluating the model




# calculate Silhouette Coefficient for K=3
from sklearn import metrics
metrics.silhouette_score(X_scaled, km.labels_)

# calculate SC for K=2 through K=19
k_range = range(2, 20)
scores = []
for k in k_range:
    km = KMeans(n_clusters=k, random_state=1)
    km.fit(X_scaled)
    scores.append(metrics.silhouette_score(X_scaled, km.labels_))
    
# plot the results
plt.plot(k_range, scores)
plt.xlabel('Number of clusters')
plt.ylabel('Silhouette Coefficient')
plt.grid(True)

# K-means with 4 clusters on scaled data
km = KMeans(n_clusters=4, random_state=1)
km.fit(X_scaled)
Data['cluster'] = km.labels_
Data.sort_values('cluster')








