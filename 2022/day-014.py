import numpy as np


def hypothesis(x, w):
    return np.sign(np.dot(x, w))


def perceptron(x, y, w):
    for i in range(len(x)):
        if hypothesis(x[i], w) != y[i]:
            w = w + y[i] * x[i]
    return w


def perceptron_with_margin(x, y, w, margin):
    for i in range(len(x)):
        if hypothesis(x[i], w) != y[i]:
            w = w + y[i] * x[i]
            if np.dot(x[i], w) < margin:
                w = w - y[i] * x[i]
    return w


def perceptron_learning_algorithm(x, y, w, epochs):
    for i in range(epochs):
        w = perceptron(x, y, w)
    return w
