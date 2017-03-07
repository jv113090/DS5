#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 20:10:02 2017

@author: JVena
"""
#import data

import pandas as pd
url = '../Project/FinalProject/FinalProjData.csv'
Data = pd.read_csv(url, index_col=0)

Data.head()

#Convert string to categories 

Data['MetalLevel_2014'] = Data.MetalLevel_2014.map({'Low':0, 'High':1})
Data.head()

# create feature matrix (X)

feature_cols = ['State_Number', 'MetalLevel_2014', 'ChildAdultOnly_2014', 'Income', 'PlanID']
X = Data[feature_cols]
print(X.shape)

# Add in code about dimensionality reduction if time

# K-means with 2 clusters
from sklearn.cluster import KMeans
km = KMeans(n_clusters=2, random_state=1)
km.fit(X)

# review the cluster labels
km.labels_

# save the cluster labels and sort by cluster
X['cluster'] = km.labels_
Data.sort_values('Income')

# review the cluster centers
km.cluster_centers_

# calculate the mean of each feature for each cluster
X.groupby('cluster').mean()

# save the DataFrame of cluster centers
centers = X.groupby('cluster').mean()

type(centers)

# allow plots to appear in the notebook
%matplotlib inline
import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 14

# create a "colors" array for plotting
import numpy as np
colors = np.array(['red', 'green', 'blue', 'yellow'])

# scatter plot of PlanID versus Income, colored by cluster (0=red, 1=green, 2=blue)
plt.scatter(X.PlanID, X.Income, c=colors[X.cluster], s=50)

# cluster centers, marked by "+"
plt.scatter(centers.PlanID, centers.Income, linewidths=3, marker='+', s=300, c='black')

# add labels
plt.xlabel('PlanID')
plt.ylabel('Income')

# scatter plot matrix (0=red, 1=green, 2=blue)
pd.scatter_matrix(X, c=colors[X.cluster], figsize=(10,10), s=100)



###Evaluating the model


# calculate Silhouette Coefficient for K=3
from sklearn import metrics
metrics.silhouette_score(X, km.labels_)

# calculate SC for K=2 through K=5
k_range = range(2, 5)
scores = []
for k in k_range:
    km = KMeans(n_clusters=k, random_state=1)
    km.fit(X)
    scores.append(metrics.silhouette_score(X, km.labels_))
    
# plot the results
plt.plot(k_range, scores)
plt.xlabel('Number of clusters')
plt.ylabel('Silhouette Coefficient')
plt.grid(True)









