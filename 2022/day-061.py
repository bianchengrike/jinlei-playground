from sklearn.preprocessing import KBinsDiscretizer

def __data_bin(self, df: pd.DataFrame) -> pd.DataFrame:

"""

:type df: pd.DataFrame
:param df:
:return:
"""
est = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='kmeans')
df_bin = pd.DataFrame(est.fit_transform(df), index=df.index)
df_bin.columns = ['R', 'F', 'E', ]
df_bin['Rating'] = df_bin.sum(axis=1).astype('int')

return df_bin