Linear regression homework with Yelp votes
Introduction
This assignment uses a small subset of the data from Kaggle's Yelp Business Rating Prediction competition.
Description of the data:
yelp.json is the original format of the file. yelp.csv contains the same data, in a more convenient format. Both of the files are in this repo, so there is no need to download the data from the Kaggle website.
Each observation in this dataset is a review of a particular business by a particular user.
The "stars" column is the number of stars (1 through 5) assigned by the reviewer to the business. (Higher stars is better.) In other words, it is the rating of the business by the person who wrote the review.
The "cool" column is the number of "cool" votes this review received from other Yelp users. All reviews start with 0 "cool" votes, and there is no limit to how many "cool" votes a review can receive. In other words, it is a rating of the review itself, not a rating of the business.
The "useful" and "funny" columns are similar to the "cool" column.
Task 1
Read yelp.csv into a DataFrame.
In [19]:

# access yelp.csv using a relative path
import pandas as pd
yelp = pd.read_csv('../ClassRepo/ds-sea-05/data/yelp.csv')
yelp.head(1)
Out[19]:
business_id	date	review_id	stars	text	type	user_id	cool	useful	funny
0	9yKzy9PApeiPPOUJEtnvkg	2011-01-26	fWKvX83p0-ka4JS3dc6E5A	5	My wife took me here on my birthday for breakf...	review	rLtl8ZkDX5vH5nAx9C3q5Q	2	5	0
Task 1 (Bonus)
Ignore the yelp.csv file, and construct this DataFrame yourself from yelp.json. This involves reading the data into Python, decoding the JSON, converting it to a DataFrame, and adding individual columns for each of the vote types.
In [20]:

# read the data from yelp.json into a list of rows
# each row is decoded into a dictionary named "data" using using json.loads()
import json
with open('../ClassRepo/ds-sea-05/data/yelp.json', 'rU') as f:
    data = [json.loads(row) for row in f]
In [21]:

# show the first review
​
In [22]:

# convert the list of dictionaries to a DataFrame
​
In [23]:

# add DataFrame columns for cool, useful, and funny
​
In [24]:

# drop the votes column and then display the head
​
Task 2
Explore the relationship between each of the vote types (cool/useful/funny) and the number of stars.
In [25]:

# treat stars as a categorical variable and look for differences between groups by comparing the means of the groups
yelp.groupby('stars', as_index=False)['cool','useful', 'funny'].mean()
Out[25]:
stars	cool	useful	funny
0	1	0.576769	1.604806	1.056075
1	2	0.719525	1.563107	0.875944
2	3	0.788501	1.306639	0.694730
3	4	0.954623	1.395916	0.670448
4	5	0.944261	1.381780	0.608631
In [26]:

# display acorrelation matrix of the vote types (cool/useful/funny) and stars
%matplotlib inline
import seaborn as sns
sns.heatmap(yelp.corr())
Out[26]:
<matplotlib.axes._subplots.AxesSubplot at 0x111ff8290>

In [27]:

# display multiple scatter plots (cool, useful, funny) with linear regression line
sns.regplot(x="stars", y="cool", data=yelp)
sns.regplot(x="stars", y="useful", data=yelp)
sns.regplot(x="stars", y="funny", data=yelp)
Out[27]:
<matplotlib.axes._subplots.AxesSubplot at 0x11f7e5150>

Task 3
Define cool/useful/funny as the feature matrix X, and stars as the response vector y.
In [28]:

feature_cols = ['cool', 'useful', 'funny']
X = yelp[feature_cols]
print (X)
y = yelp.stars
print (y)
​
      cool  useful  funny
0        2       5      0
1        0       0      0
2        0       1      0
3        1       2      0
4        0       0      0
5        4       3      1
6        7       7      4
7        0       1      0
8        0       0      0
9        0       1      0
10       1       3      1
11       1       1      0
12       1       2      0
13       1       2      0
14       1       1      0
15       0       2      0
16       3       4      2
17       0       0      0
18       5       6      4
19       1       1      1
20       2       4      1
21       1       1      2
22       0       0      0
23       0       1      1
24       0       1      0
25       0       0      0
26       0       0      0
27       2       4      1
28       1       1      1
29       0       1      0
...    ...     ...    ...
9970     0       0      0
9971     1       2      1
9972     0       0      0
9973     0       0      0
9974     0       0      0
9975     1       1      0
9976     0       0      0
9977     3       6      3
9978     0       1      0
9979     2       2      1
9980     6       6      4
9981    10       9      5
9982     0       0      0
9983     1       4      1
9984     0       1      2
9985     0       0      0
9986     0       0      0
9987     0       0      0
9988     0       2      0
9989     0       1      0
9990     1       1      1
9991     1       1      0
9992     2       3      2
9993     1       1      0
9994     1       2      1
9995     1       2      0
9996     0       0      0
9997     0       0      0
9998     0       0      0
9999     0       0      0

[10000 rows x 3 columns]
0       5
1       5
2       4
3       5
4       5
5       4
6       5
7       4
8       4
9       5
10      5
11      5
12      5
13      4
14      4
15      2
16      3
17      5
18      3
19      4
20      3
21      5
22      5
23      1
24      5
25      4
26      5
27      4
28      4
29      4
       ..
9970    5
9971    5
9972    4
9973    5
9974    2
9975    5
9976    3
9977    5
9978    5
9979    5
9980    5
9981    5
9982    4
9983    3
9984    1
9985    4
9986    4
9987    1
9988    4
9989    5
9990    5
9991    5
9992    5
9993    4
9994    5
9995    3
9996    4
9997    4
9998    2
9999    5
Name: stars, dtype: int64
Task 4
Fit a linear regression model and interpret the coefficients. Do the coefficients make intuitive sense to you? Explore the Yelp website to see if you detect similar trends.
In [29]:

from sklearn.linear_model import LinearRegression
​
regr = LinearRegression()
​
regr.fit(X, y)
Out[29]:
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
Task 5
Evaluate the model by splitting it into training and testing sets and computing the RMSE. Does the RMSE make intuitive sense to you?
In [30]:

from sklearn.cross_validation import train_test_split
from sklearn import metrics
import numpy as np
In [35]:

# define a function that accepts a list of features and returns testing RMSE
metrics.mean_squared_error(yelp['stars'], yelp['cool'])
Out[35]:
13.9009
In [36]:

# calculate RMSE with all three features
metrics.mean_squared_error(yelp['funny'], yelp['cool'], yelp['useful'])
Out[36]:
38.732207478890231
Task 6
Try removing some of the features and see if the RMSE improves.
In [37]:

metrics.mean_squared_error(yelp['funny'], yelp['cool'])
Out[37]:
1.9157
Task 7 (Bonus)
Think of some new features you could create from the existing data that might be predictive of the response. Figure out how to create those features in Pandas, add them to your model, and see if the RMSE improves.
In [ ]:

# new feature: 
In [ ]:

# new features: 
​
In [ ]:

# add new features to the model and calculate RMSE
​
Task 8 (Bonus)
Compare your best RMSE on the testing set with the RMSE for the "null model", which is the model that ignores all features and simply predicts the mean response value in the testing set.
In [ ]:

​
