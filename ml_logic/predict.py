import joblib
import numpy as np
import pandas as pd

    #primeiro passo: fazer o load do modelo
    #segundo passo: model.predict   (predict proba)
    #terceir opasso: retornar o output


model_path = 'models/best_xgb_5.sav' #OU JOBLIB?


def load_model(model_path):
    """Load the trained model from a file."""
    return joblib.load(model_path)



def predict_main(model_path, data):
    """Main function to load the model and make predictions."""
    # Carregar o modelo
    model = load_model(model_path)

    # Verificar se os dados estão no formato correto
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Data should be a pandas DataFrame.")

    # Fazer várias predições reutilizando o mesmo modelo carregado
    result = model.predict(data)

    probabilities = model.predict_proba(data)

    max_probability = probabilities.max(axis=1)

    return result, max_probability
