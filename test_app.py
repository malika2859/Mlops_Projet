import pytest
from app import model_pred
import pandas as pd
import pickle

# Charger le modèle depuis le fichier pour le test
model_path = "logistic_model.pkl" 
model = pickle.load(open(model_path, "rb"))

# Redéfinir la fonction model_pred pour utiliser le modèle chargé
def model_pred(features):
    test_data = pd.DataFrame([features])
    prediction = model.predict(test_data)
    return int(prediction[0])

# Exemple de données à tester
new_data = {
    'credit_lines_outstanding': 1,
    'loan_amt_outstanding': 3659.97,
    'total_debt_outstanding': 6785.83,
    'income': 62270.67,
    'years_employed': 5,
    'fico_score': 639,
}

def test_predict():
    prediction = model_pred(new_data)
    print(f"Prediction: {prediction}")  # Imprimez la prédiction pour débogage
    assert prediction == 0, "La prédiction est incorrecte, elle devrait être 0"
