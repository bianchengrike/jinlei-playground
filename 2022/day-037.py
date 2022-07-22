#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2022/7/22 10:22
# @Author   : Zhang JinLei
# @Describe :
from sklearn import datasets
from pyclustertend import hopkins
from sklearn.preprocessing import scale

X = scale(datasets.load_iris().data)
hopkins(X, 150)
