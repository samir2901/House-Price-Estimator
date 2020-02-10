import json
import pickle
import numpy as np

__location = None
__data_columns = []
__model = None

def load_tools():
    global __location
    global __data_columns
    global __model

    print("Loading Tools......")
    with open("columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[4:]

    with open("ml_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("Loading Tools Done")

def get_location_names():
    return __location

def predict_prices(location, total_sqft, bath, balcony, bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = balcony
    x[3] = bhk
    if loc_index>=0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)





