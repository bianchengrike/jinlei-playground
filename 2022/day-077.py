import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt

mu, sigma = 20, 10 # mean and standard deviation

s_nor = np.random.default_rng().normal(mu, sigma, 10000)

sns.histplot(s_nor)


x, y = np.random.multivariate_normal(mean, cov, 5000).T
plt.plot(x, y, 'x')
# plt.set_size_inches(18, 7)
plt.axis('equal')
plt.show()

cov = np.array([[6, -3], [-3, 3.5]])
pts = np.random.multivariate_normal([0, 0], cov, size=800)

plt.plot(pts[:, 0], pts[:, 1], 'x', alpha=0.5)
plt.axis('equal')
plt.grid()
plt.show()