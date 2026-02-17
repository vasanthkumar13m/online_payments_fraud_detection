from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("payments.pkl")

# Home page
@app.route('/')
def home():
    return render_template("home.html")

# Prediction input page
@app.route('/predict')
def predict():
    return render_template("predict.html")

# Submit page (RESULT)
@app.route('/submit', methods=['POST'])
def submit():
    step = float(request.form['step'])
    tx_type = request.form['type']
    amount = float(request.form['amount'])
    oldbalanceOrg = float(request.form['oldbalanceOrg'])
    newbalanceOrig = float(request.form['newbalanceOrig'])
    oldbalanceDest = float(request.form['oldbalanceDest'])
    newbalanceDest = float(request.form['newbalanceDest'])

    type_CASH_IN  = 1 if tx_type == "CASH_IN" else 0
    type_CASH_OUT = 1 if tx_type == "CASH_OUT" else 0
    type_DEBIT    = 1 if tx_type == "DEBIT" else 0
    type_PAYMENT  = 1 if tx_type == "PAYMENT" else 0
    type_TRANSFER = 1 if tx_type == "TRANSFER" else 0

    # Model expects input as 2D array
    features = np.array([[step,amount,
                           oldbalanceOrg,
                           newbalanceOrig,
                           oldbalanceDest,
                           newbalanceDest,type_CASH_IN,
                           type_CASH_OUT,
                           type_DEBIT,
                           type_PAYMENT,
                           type_TRANSFER]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        result = "🚨 Fraud Transaction Detected"
    else:
        result = "✅ Normal Transaction"

    return render_template("submit.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)