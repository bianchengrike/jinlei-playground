import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn as sns

from interpret.glassbox import ExplainableBoostingClassifier
from interpret import set_visualize_provider
from interpret.provider import InlineProvider

from interpret import show

data = pd.read_csv('campaign_data.csv')

train_cols = data.columns[0:-1]
label = data.columns[-1]
X = data[train_cols]
y = data[label]


ebm = ExplainableBoostingClassifier(random_state=seed)
ebm.fit(X_train, y_train)


set_visualize_provider(InlineProvider())


ebm_global = ebm.explain_global()
show(ebm_global)