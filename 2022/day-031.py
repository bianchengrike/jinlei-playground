#  向量点积

import math
import numpy as np 

def geometric_dot_product(x, y, theta):
    x_norm = np.linalg.norm(x)
    y_norm = np.linalg.norm(y)

    return x_norm * y_norm * math.cos(math.radians(theta))

def dot_product_algebraic(x, y):
    result = 0
    for i in range(len(x)):
        result += x[i] * y[i]

    return result


x = [5, 5]
y = [8, 0]

theta = 45

geometric_dot_product(x, y, theta)

dot_product_algebraic(x, y)
