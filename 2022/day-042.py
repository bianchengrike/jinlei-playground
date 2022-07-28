#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2022/7/28 15:30
# @Author   : Zhang JinLei
# @Describe :

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets

from sklearn_som.som import SOM

# Load iris data
iris = datasets.load_iris()
iris_data = iris.data
iris_label = iris.target

# Extract just two features (just for ease of visualization)
# iris_data = iris_data[:, :2]

# Build a 3x1 SOM (3 clusters)
som = SOM(m=1, n=6, dim=iris_data.shape[-1], random_state=1234)

# Fit it to the data
som.fit(iris_data)

# Assign each datapoint to its predicted cluster
predictions = som.predict(iris_data)

# Plot the results
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(5, 7))
x = iris_data[:, 0]
y = iris_data[:, 1]
colors = ['red', 'green', 'blue']

ax[0].scatter(x, y, c=iris_label, cmap=ListedColormap(colors))
ax[0].title.set_text('Actual Classes')
ax[1].scatter(x, y, c=predictions, cmap=ListedColormap(colors))
ax[1].title.set_text('SOM Predictions')

plt.show()
# plt.savefig('iris_example.png')
