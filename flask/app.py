from flask import Flask, render_template, request
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        type_map = {"CASH_OUT": 1, "PAYMENT": 2, "CASH_IN": 3, "TRANSFER": 4, "DEBIT": 5}

        trans_type = request.form.get('type')
        trans_type_encoded = type_map.get(trans_type, 0)

        amount         = float(request.form.get('amount'))
        oldbalanceOrg  = float(request.form.get('oldbalanceOrg'))
        newbalanceOrig = float(request.form.get('newbalanceOrig'))
        balanceError   = oldbalanceOrg - amount - newbalanceOrig

        features = np.array([[trans_type_encoded, amount, oldbalanceOrg, newbalanceOrig, balanceError]])
        prediction = model.predict(features)[0]

        result = "FRAUD ⚠️" if prediction == 1 else "NOT FRAUD ✅"
        return render_template('submit.html', prediction_text=f"Prediction: This transaction is {result}")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)