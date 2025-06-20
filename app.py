from flask import Flask, render_template, request
import numpy as np
import joblib
from keras.models import load_model

app = Flask(__name__)

# Load the Keras model and scaler
model = load_model("final_ann_model.h5")
scaler = joblib.load("scaler.pkl")

# List of features
features = [
    'age', 'anaemia', 'creatinine_phosphokinase', 'diabetes',
    'ejection_fraction', 'high_blood_pressure', 'platelets',
    'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time'
]

@app.route('/')
def index():
    return render_template('index.html', features=features, prediction=None)


@app.route('/predict', methods=['POST'])
def predict():
    input_data = [float(request.form[feature]) for feature in features]
    input_scaled = scaler.transform([input_data])
    prediction = model.predict(input_scaled)[0][0]
    outcome = "High Risk" if prediction >= 0.5 else "Low Risk"
    return f'Predicted Outcome: {outcome} (Prob: {prediction:.2f})'

if __name__ == '__main__':
    app.run(debug=True)