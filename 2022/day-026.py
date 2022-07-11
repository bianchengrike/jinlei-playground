# 向量在给定好一个坐标系之后可以确定
# 然后，向量不是不需要有坐标系
# 给定一条直线和角度也是可以确定一个向量的
# 因此，向量的核心属性是范数和角度
# 所以，范数对于向量来将是一个很重要的概念
# 对于向量角度的一个理解范例是由余弦公式的角度关系推导出余弦相似度

import numpy as np 
from scipy.linalg import norm

a = np.arange(9) - 4.0
b = a.reshape((3, 3))

norm(a)
norm(b)
