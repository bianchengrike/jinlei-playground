import numpy as np
import matplotlib.pyplot as plt

random_data = np.random.randint(1, 7, 60000)
print(random_data)
print('均值为：  ', random_data.mean())
print('标准差为：', random_data.std())
plt.hist(random_data, bins=50, normed=0)
plt.show()

sample_100 = []
for i in range(0, 100):
    sample_100.append(random_data[int(np.random.random() * len(random_data))])

print(sample_100)
print('样本均值为：  ', np.mean(sample_100))
print('样本标准差为：', np.std(sample_100, ddof=1))

samples_100_mean = []
for i in range(0, 50000):
    sample = []
    for j in range(0, 100):
        sample.append(random_data[int(np.random.random() * len(random_data))])
    samples_100_mean.append(np.mean(sample))
    samples_many_mean = np.mean(samples_100_mean)
print('多次抽取样本的总均值：', samples_many_mean)
plt.hist(samples_100_mean, bins=200, normed=0)
plt.show()