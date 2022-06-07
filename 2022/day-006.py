# Evaluate pairwise distances or affinity 

import numpy as np
from sklearn.metrics import pairwise_distances
from sklearn.metrics.pairwise import pairwise_kernels
X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

pairwise_distances(X, Y, metric='manhattan')

pairwise_distances(X, metric='manhattan')

pairwise_kernels(X, Y, metric='linear')

	 	