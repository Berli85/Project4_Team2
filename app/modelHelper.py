import pandas as pd
import numpy as np
import json
import pickle


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