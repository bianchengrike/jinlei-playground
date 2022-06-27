class FileNotExist(Exception):
    """当用户无法找到文件时抛出该异常"""
    pass


def data_read(data_path, file_name, ):
    """
    读取数据
    :param data_path:
    :param file_name:
    :return:
    """
    df_path = os.path.join(data_path, file_name)
    # column_names = ['user_id', 'query_time', 'query_content', 'query_type', 'query_result']

    if os.path.exists(df_path) and df_path.endswith('.xlsx'):
        df = pd.read_excel(df_path)
        # df.columns = column_names
        return df
    elif os.path.exists(df_path) and df_path.endswith('.csv'):
        df = pd.read_csv(df_path)
        # df.columns = column_names
        return df
    else:
        raise FileNotExist(f'wrong path or file name：{df_path}')
