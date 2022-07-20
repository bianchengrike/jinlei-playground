#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2022/7/20 19:44
# @Author   : Zhang JinLei
# @Describe :

import os
import pickle
from enum import Enum
from enum import unique

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


@unique
class FileName(Enum):
    """数据文件名"""
    PIPELINE_MODEL_NAME = 'pipeline_model.pkl'


class PathName(Enum):
    """路径配置"""
    PIPELINE_MODEL_SAVE_PATH = '/your_path/models'


def save_model_file(trained_estimator, model_save_path, model_name):
    if not os.path.exists(model_save_path):
        os.makedirs(model_save_path)
    save_model = open(os.path.join(model_save_path, model_name), 'wb')
    pickle.dump(trained_estimator, save_model, 0)
    save_model.close()

    print('Model successfully saved')

    return True


def load_model_file(model_save_path, model_name):
    read_model = open(os.path.join(model_save_path, model_name), 'rb')
    loaded_model = pickle.load(read_model)
    read_model.close()

    print('Model successfully loaded')

    return loaded_model


X, y = make_classification(random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
pipe = make_pipeline(StandardScaler(), LogisticRegression())
pipe.fit(X_train, y_train)  # apply scaling on training data

save_model_file(pipe,
                PathName.PIPELINE_MODEL_SAVE_PATH.value,
                FileName.PIPELINE_MODEL_NAME.value)

pipe_model = load_model_file(PathName.PIPELINE_MODEL_SAVE_PATH.value,
                             FileName.PIPELINE_MODEL_NAME.value)

# same to pipe.score(X_test, y_test) = 0.96
pipe_model.score(X_test, y_test)  # apply scaling on testing data, without leaking training data.0.96
