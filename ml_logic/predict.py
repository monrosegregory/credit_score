import joblib
import numpy as np
import pandas as pd

    #1st: load model
    #2nd: model.predict   (predict proba)
    #3rd: return output


model_path = 'models/best_xgb_5.sav'


def load_model(model_path):
    """Load the trained model from a file."""
    return joblib.load(model_path)



def predict_main(model_path, data):
    """Main function to load the model and make predictions."""
    # Load model
    model = load_model(model_path)

    # Check if data it is correct
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Data should be a pandas DataFrame.")

    # Predict using load model
    result = model.predict(data)

    probabilities = model.predict_proba(data)

    max_probability = probabilities.max(axis=1)

    return result, max_probability
