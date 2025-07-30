import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the model
model = joblib.load("model.pkl")

# Title
st.title("Cardiovascular Health Predictor ")
st.markdown("Enter your health details to predict the risk of heart disease.")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120, value=30)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (trestbps)", value=120)
chol = st.number_input("Cholesterol (chol)", value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1])
restecg = st.selectbox("Resting ECG (restecg)", [0, 1, 2])
thalach = st.number_input("Max Heart Rate (thalach)", value=150)
exang = st.selectbox("Exercise-induced angina (exang)", [0, 1])
oldpeak = st.number_input("Oldpeak", value=1.0)
slope = st.selectbox("Slope", [0, 1, 2])
ca = st.selectbox("Number of major vessels (ca)", [0, 1, 2, 3])
thal = st.selectbox("Thal", [0, 1, 2, 3])

# Convert categorical to numeric
sex = 1 if sex == "Male" else 0

# Predict
if st.button("Predict"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                            exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error(" High Risk of Heart Disease")
    else:
        st.success(" Low Risk of Heart Disease")