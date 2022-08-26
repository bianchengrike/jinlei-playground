def get_best_k(self, min_clusters: int, max_clusters: int, feature_col: str) -> int:
    """
    获取最佳的聚类数
    :param min_clusters: 最小聚类数量
    :param max_clusters: 最大聚类数量
    :param feature_col: 指定特征列
    :return:
    """
    best_result = []
    for i in range(min_clusters, max_clusters + 1):
        kmeans = KMeans(n_clusters=i)
        clustering_results = kmeans.fit_predict(self.__feature_df[[feature_col]].values)
        silhouette_score_value = silhouette_score(self.__feature_df[[feature_col]], clustering_results)
        # print('Number of clusters:', i, 'Silhouette score:', silhouette_score_value)
        best_result.append((i, silhouette_score_value,))

    best_result.sort(key=lambda x: x[1], reverse=True)
    return best_result[0][0]