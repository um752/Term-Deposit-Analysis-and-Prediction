import json
import pickle

import numpy as np

__data_columns = None
__model = pickle.load(open('./stacked.pickle', 'rb'))


def get_saved_artifacts():
    return __data_columns


def get_subscribed_status(age, job, default, balance, housing, month, duration, poutcome):
    x = np.zeros(8)
    x[0] = age
    x[1] = job
    x[2] = default
    x[3] = balance
    x[4] = housing
    x[5] = month
    x[6] = duration
    x[7] = poutcome
    print(x)
    test = __model.predict([x])[0]
    print(test)
    if test == 0:
        return "Given customer will NOT SUBSCRIBE."
    else:
        return "Given customer will SUBSCRIBE."


def load_saved_artifacts():
    print("Loading saved artifacts..")
    global __data_columns
    global __model
    with open("./columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
    with open("./stacked.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("Loading saved artifacts completed")


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_saved_artifacts())
    print(get_subscribed_status(1, 2, 0, 2, 0, 1, 977, 1))
