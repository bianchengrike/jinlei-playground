# 通过类保存流水线处理的中间结果

class ToyClass:

    def __init__(self):
        """
        实例初始化
        """
        self.__feature_df = None
        self.__pipeline_df = None

    def preprocess_pipeline(self, df: pd.DataFrame):
        """
        数据预处理流水线
        :param df: 数据 DataFrame
        """
        df_preprocessing = self.__data_preprocessing(df)
        df_cluster = self.__convert_to_cluster_feature(df_preprocessing)
        self.__feature_df = df_cluster

        df_filtered = self.__outlier_data_filter(df_cluster)
        self.__pipeline_df = df_filtered

    def a():
        df = self.__pipeline_df
        pass

    def b():
        df = self.__pipeline_df
        pass



