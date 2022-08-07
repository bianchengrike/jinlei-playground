import numpy as np

target = np.arange(24).reshape(4, 2, 3)

target[0:3, :, 1:3]

np.hstack((target[0:3, :, 1:3], target[0:3, :, 1:3]))
np.concatenate((target[0:3, :, 1:3], target[0:3, :, 1:3]), axis=1)
