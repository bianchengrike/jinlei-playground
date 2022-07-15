#  Selecting columns based on dtype

def __outlier_data_filter(self, df: pd.DataFrame) -> pd.DataFrame:

    """

    :type df: pd.DataFrame
    :param df:
    :return:
    """

    df_deep = df.copy()
    for col in df.columns:
        df_deep[col] = pd.qcut(df_deep[col], 5, duplicates='drop', labels=False)

    return df_deep