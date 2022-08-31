import numpy as np
from matplotlib import pyplot as plt

from sklearn.linear_model import LinearRegression

x = np.array([4,5,7,10,12,14,17,20,24,26,27,29,31,34])[:, np.newaxis]

y = np.array([1000.056,
                  1000.123,
                  1000.130,
                  1000.122,
                  1000.144,
                  1000.171,
                  1000.255,
                  1000.280,
                  1000.240,
                  1000.316,
                  1000.310,
                  1000.325,
                  1000.385,
                  1000.391,])[:, np.newaxis]

reg = LinearRegression().fit(x, y)
reg.coef_
reg.intercept_