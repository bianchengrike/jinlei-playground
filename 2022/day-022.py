def load_model_file(model_save_path, model_name):
    read_model = open(os.path.join(model_save_path, model_name), 'rb')
    loaded_model = pickle.load(read_model)
    read_model.close()

    print('Model successfully loaded')

    return loaded_model