import json
import pickle
import numpy as np

__columns = None
__locations = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)

def load_all_data():
    global __columns
    global __locations
    print("data is loading")
    with open("./essentials/columns.json" , "r") as f:
        __columns = json.load(f)["data_columns"]
        __locations = __columns[3:]
    global __model
    if __model is None:
        with open("./essentials/price_prediction_model.pickle" , "rb") as f:
                 __model = pickle.load(f)
    print("model is loaded")

def get_location_names():
    return __locations

def get_columns():
    return __columns

if __name__ == '__main__':
    load_all_data()
