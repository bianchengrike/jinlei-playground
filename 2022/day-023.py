import pandas as pd

from sklearn.manifold import TSNE



def cluster_plot(df: pd.DataFrame, df_ratio: float = 0.8) -> None:
    # 分割数据集
    df_train = df[:int(len(df) * df_ratio)]
    df_test = df[int(len(df) * df_ratio):]

    # 绘制聚类图
    tsne = TSNE(n_components=2, random_state=1233)
    train_embedded = tsne.fit_transform(df_train[['id1', 'id2', 'id3', 'id4']])
    test_embedded = tsne.fit_transform(df_test[['id1', 'id2', 'id3', 'id4']])

    plt.figure(figsize=(10, 8))
    sns.scatterplot(x=train_embedded[:, 0], y=train_embedded[:, 1], hue=df_train['cluster'], s=50, palette='rainbow')
    plt.xlabel('train_embedded_0')
    plt.ylabel('train_embedded_1')
    plt.title('Scatter of train_cluster_embedded')
    plt.show()

    plt.figure(figsize=(10, 8))
    sns.scatterplot(x=test_embedded[:, 0], y=test_embedded[:, 1], hue=df_test['cluster'], palette='rainbow')
    # plt.legend(loc='upper right')
    plt.xlabel('test_embedded_0')
    plt.ylabel('test_embedded_1')
    plt.title('Scatter of test_cluster_embedded')
    plt.show()
