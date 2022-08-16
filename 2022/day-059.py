import numpy as np 
import seaborn as sns

from sklearn.preprocessing import StandardScaler

s_uni = np.random.default_rng().uniform(-1,0,1000)
sns.histplot(s_uni)

scaler_uni = StandardScaler()
s_scaler_uni = scaler_uni.fit_transform(s_uni.reshape(1,-1)) # 这里 reshape 的参数给错了，画出来的图就会错
ss_uni = np.ravel(s_scaler_uni.reshape(-1,1))