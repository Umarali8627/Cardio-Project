🫀 Heart Disease Prediction — Machine Learning & Flask Web App
📖 Overview

This project is a Machine Learning-powered web application that predicts the likelihood of heart disease based on patient medical parameters such as age, blood pressure, cholesterol, etc.

The project is divided into two main parts:

Model Development – Data preprocessing, training, and evaluation (in Jupyter Notebook)

Web Deployment – A Flask-based app for real-time predictions through a simple HTML form

🎯 Features

✅ Predict heart disease risk based on health metrics
✅ Interactive web form for easy data input
✅ High-performance ML model with ROC-AUC: 0.994
✅ Flask backend for serving predictions
✅ Modular and scalable code structure

📂 Project Structure
.
├── Cardio_Project.ipynb           # Jupyter Notebook: Data analysis, model training, evaluation
├── app.py                          # Flask application
├── Heart disease prediction.pkl    # Trained ML model
├── templates/
│   └── index.html                  # HTML frontend
├── static/                         # (Optional) CSS/JS files
└── requirements.txt                # Python dependencies

🧠 Machine Learning Pipeline

Data Preprocessing

Handling missing values

Feature scaling & encoding

Train-test split

Model Training

Logistic Regression (or chosen ML model)

Hyperparameter tuning (if applicable)

Evaluation Metrics

Accuracy

Precision, Recall, F1-score

ROC-AUC Score (0.994 in final model)

Confusion Matrix

Model Serialization

Trained model saved using pickle
