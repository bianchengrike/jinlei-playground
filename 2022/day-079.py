
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler



X = [['Male', ], ['Female', ], ['Female', ], ['unknow'],
     ['Male', ], ['Female', ], ['Female', ], ['unknow'],]

enc.fit_transform(X)
res = enc.fit_transform(X)
scaler = StandardScaler()
scaler.fit_transform(res) # 报错