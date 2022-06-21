import dill
import os
import json
import logging

import pandas as pd


path = os.environ.get('PROJECT_PATH', '.')
model_path = os.path.join(path, 'data', 'models')
test_path = os.path.join(path, 'data', 'test')
prediction_path = os.path.join(path, 'data', 'predictions')

def predict():
    model_filename = os.path.join(model_path, os.listdir(model_path)[-1])
    with open(model_filename, 'rb') as file:
        model = dill.load(file)

    test_filenames = os.listdir(test_path)
    tests = []

    for test_filename in test_filenames:
        test_filename = os.path.join(test_path, test_filename)
        with open(test_filename, 'rb') as file:
            tests.append(json.load(file))

    X = pd.DataFrame.from_dict(tests)
    X['price_category'] = model.predict(X)
    X = X[['id', 'price_category']].rename(columns={"id": "car_is"})
    print(X)
    prediction_filename = os.path.join(prediction_path, 'prediction_' + model_filename[-16: -4]+'.csv')
    X.to_csv(prediction_filename, index=False)
    logging.info(f'Predictions is saved as {prediction_filename}')


if __name__ == '__main__':
    predict()
