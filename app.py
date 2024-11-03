from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Charger le modèle depuis le fichier
model_path = "LR_model.pkl"  # Chemin du modèle
model = pickle.load(open(model_path, "rb"))

# Fonction pour effectuer la prédiction avec les colonnes dans l'ordre attendu
def model_pred(features):
    # Assurer l'ordre des caractéristiques pour le modèle
    feature_order = ["loan_amt_outstanding", "total_debt_outstanding", "income", "years_employed", "fico_score", "credit_lines_outstanding"]
    test_data = pd.DataFrame([features], columns=feature_order)
    prediction = model.predict(test_data)
    return int(prediction[0])

# Page d'accueil
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Route pour faire la prédiction
@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Récupération des variables depuis le formulaire
        credit_lines_outstanding = int(request.form["credit_lines_outstanding"])
        loan_amt_outstanding = float(request.form["loan_amt_outstanding"])
        total_debt_outstanding = float(request.form["total_debt_outstanding"])
        income = float(request.form["income"])
        years_employed = int(request.form["years_employed"])
        fico_score = int(request.form["fico_score"])

        # Organiser les variables dans l'ordre attendu par le modèle
        features = [
            loan_amt_outstanding,
            total_debt_outstanding,
            income,
            years_employed,
            fico_score,
            credit_lines_outstanding
        ]

        # Effectuer la prédiction
        prediction = model_pred(features)

        # Afficher le résultat de la prédiction
        if prediction == 1:
            return render_template(
                "index.html",
                prediction_text="Le client pourrait être en défaut de paiement."
            )
        else:
            return render_template(
                "index.html", prediction_text="Le client ne présente pas de risque de défaut."
            )
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
