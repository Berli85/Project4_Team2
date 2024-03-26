import pandas as pd
import numpy as np
import json
import pickle
from xgboost import XGBClassifier

# Load the model object from the file
with open ('wine_model.h5', 'rb') as file:
    loaded_model = pickle.load(file)

#Export to csv file for Tableau
df=pd.read_csv ("combined_datasets.csv")
df = df.drop(["wine_type", "quality"], axis=1) # keep ALL features except for the target

# input_pred = []

# X = np.array(input_pred)
# preds = loaded_model.predict_proba(X)
# preds_singular = loaded_model.predict(X)
# print(preds)

class ModelHelper():
    def __init__(self):
        pass

    def makePredictions(self, fixed_acidity, volatile_acidity, citric_acid, 
                    residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,
                   pH, sulphates, alcohol):
    
        input_pred = [[fixed_acidity, volatile_acidity, citric_acid, 
                    residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,
                   pH, sulphates, alcohol]]
    
        filename = 'wine_model.h5'
        loaded_model = pickle.load(open(filename, 'rb'))

        X = np.array(input_pred)
        preds = loaded_model.predict_proba(X)[0]
        preds_singular = loaded_model.predict(X)
    
        rtn = {"prob_white": float(preds[0]),
            "prob_red": float(preds[1]),
            "wine_pred": "red" if preds_singular[0] == 1 else "white"}

        return rtn