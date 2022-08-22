import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, decomposition


def load_data():
    iris = datasets.load_iris()
    return iris.data, iris.target


def plot_PCA(*data):
    X, y = data
    pca = decomposition.PCA(n_components=2)
    pca.fit(X)
    print(pca.explained_variance_ratio_)
    print(pca.components_)
    X_r = pca.transform(X)
    print(X_r)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    colors = ['red', 'green', 'blue']
    for i in range(X_r.shape[0]):
        ax.scatter(X_r[i, 0], X_r[i, 1], c=colors[y[i]], s=10)
    plt.show()


x, y = load_data()
print(x[:5])
plot_PCA(x, y)