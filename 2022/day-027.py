# 加载模型的方式

import pickle
import joblib

def load_model_file(model_save_path, model_name):
    read_model = open(os.path.join(model_save_path, model_name), 'rb')
    loaded_model = pickle.load(read_model)
    read_model.close()

    print('Model successfully loaded')

    return loaded_model


 class UserClustering:
    """
    用户聚类
    """

    def __init__(self, input_df: pd.DataFrame, model_path: str, scaler_path: str, ):
        """
        实例化时载入模型

        :param input_df: 输入数据 DataFrame
        :param model_path: 模型存储路径
        :param scaler_path: 转换器存储路径
        """
        self.df = input_df
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)


