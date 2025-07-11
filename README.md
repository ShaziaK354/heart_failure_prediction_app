# Heart Failure Risk Prediction using ANN (Flask App)

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-FF6F00.svg?logo=tensorflow)](https://www.tensorflow.org/)
[![Flask](https://img.shields.io/badge/Flask-WebApp-000000.svg?logo=flask)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> Predict the risk of heart failure using patient data. Built with TensorFlow, Flask, and SMOTE oversampling.

---

##  Features
- Deep learning model trained on real heart failure dataset
- Oversampling using SMOTE for minority class balancing
- Interactive web UI with Flask
- High precision and ROC AUC

## Overview
This project is a machine learning web application that predicts the risk of death due to heart failure based on clinical records. It uses an Artificial Neural Network (ANN) model trained on the [Heart Failure Clinical Records Dataset](https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data) and provides predictions through a Flask web interface.

## Model Summary
- Balanced using SMOTE
- ANN model with:
  - 2 hidden layers (64 + 32 neurons)
  - Dropout regularization
  - Trained for 100 epochs
- **Final Test Results:**
  - Accuracy: `86%`
  - ROC AUC: `0.9445`
  - F1-Score (Minority): `0.85`

##  Features Used
```
['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes',
 'ejection_fraction', 'high_blood_pressure', 'platelets',
 'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time']
```

##  How to Run the App Locally
```bash
# Clone the repo
git clone https://github.com/yourusername/heart-failure-predictor.git
cd heart-failure-predictor

# Create a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

## Example Input
- `age`: 60
- `sex`: 1
- `serum_creatinine`: 1.2  
Prediction: `High Risk (Prob: 0.87)`

## UI Preview
![App UI Preview](ui_preview.png)


## File Structure
```
├── app.py
├── final_ann_model.h5
├── scaler.pkl
├── templates/
│   └── index.html
├── static/
│   └── (if needed)
├── requirements.txt
└── README.md
```

##  Credits
- Data: Kaggle - Heart Failure Clinical Records Dataset
- Built by: Shazia Kashif
