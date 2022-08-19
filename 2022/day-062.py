import pandas as pd

df_revenue = df_input.groupby('account_id').engagements.unique().str.len().reset_index()
df_revenue.columns = ['account_id', 'E']
df_user = pd.merge(df_user, df_revenue, on='account_id')