from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# -------------------------------
# Load Saved Model & Objects
# -------------------------------
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
label_encoders = pickle.load(open("label_encoders.pkl", "rb"))
feature_names = pickle.load(open("feature_names.pkl", "rb"))

# -------------------------------
# Home Page Route
# -------------------------------
@app.route('/')
def home():
    return render_template('index.html')

# -------------------------------
# Prediction Route
# -------------------------------
@app.route('/predict', methods=['POST'])
def predict():
    # Get form inputs
    data = {
        'loan_amount': float(request.form['loan_amount']),
        'annual_income': float(request.form['annual_income']),
        'credit_score': float(request.form['credit_score']),
        'employment_years': float(request.form['employment_years']),
        'home_ownership': request.form['home_ownership'],
        'loan_purpose': request.form['loan_purpose'],
        'dti_ratio': float(request.form['dti_ratio']),
        'num_of_open_accounts': float(request.form['num_of_open_accounts']),
        'delinq_2yrs': float(request.form['delinq_2yrs']),
        'revol_util': float(request.form['revol_util'])
    }

    # Convert to DataFrame
    df = pd.DataFrame([data])

    # Encode categorical columns
    for col in ['home_ownership', 'loan_purpose']:
        df[col] = label_encoders[col].transform(df[col])

    # Scale numeric columns
    df = df[feature_names]
    df[df.columns] = scaler.transform(df)

    # Make prediction
    pred = model.predict(df)[0]
    risk = "⚠️ Default Risk" if pred == 1 else "✅ Low Risk"

    return render_template('index.html', prediction_text=f"Predicted Risk Level: {risk}")

# -------------------------------
# Run Flask App
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
