def discrete_data_visualization():
    try:
        df = data_read(PathName.VISUALIZATION_DATA_PATH.value, FileName.VISUALIZATION_DATA_NAME.value)
    except FileNotExist as e:
        print(e)
        exit(1)

    visualization_data_col = ["job",
                              "marital",
                              "education",
                              "credit",
                              "housing",
                              "loan", ]

    df_plot = pd.DataFrame()
    df_temp = pd.DataFrame()
    df_visualization_data = df[visualization_data_col]
    for col in df_visualization_data.columns:
        categories, count = df_visualization_data[col].value_counts().index, df_visualization_data[
            col].value_counts().values
        df_temp[col + 'categories'] = categories
        df_temp[col + '_count'] = count

        df_plot = pd.concat([df_plot, df_temp])
        df_temp = pd.DataFrame()

    df_plot.to_csv(
        os.path.join(PathName.VISUALIZATION_DATA_PATH.value, FileName.DISCRETE_DATA_NAME.value),
        index=False)