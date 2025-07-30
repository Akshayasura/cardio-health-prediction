import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cardio Health Prediction", layout="centered")

st.title("🫀 Cardiovascular Health Prediction")
st.write("Fill in the details below to predict your heart condition.")

# User input form
with st.form("input_form"):
    age = st.slider("Age", 20, 80, 40)
    sex = st.selectbox("Sex", ("Male", "Female"))
    cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
    trestbps = st.slider("Resting Blood Pressure (trestbps)", 80, 200, 120)
    chol = st.slider("Cholesterol (chol)", 100, 400, 200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1])
    restecg = st.selectbox("Resting ECG Results (restecg)", [0, 1, 2])
    thalach = st.slider("Max Heart Rate Achieved (thalach)", 70, 210, 150)
    exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])
    oldpeak = st.slider("Oldpeak (ST depression)", 0.0, 6.0, 1.0, 0.1)
    slope = st.selectbox("Slope of the Peak Exercise ST Segment (slope)", [0, 1, 2])
    ca = st.selectbox("Major Vessels Colored by Fluoroscopy (ca)", [0, 1, 2, 3, 4])
    thal = st.selectbox("Thalassemia (thal)", [0, 1, 2, 3])

    submit = st.form_submit_button("Predict")

if submit:
    try:
        import joblib
        model = joblib.load("model.pkl")

        # Encode sex to numeric
        sex_encoded = 1 if sex == "Male" else 0

        # Input DataFrame
        input_data = pd.DataFrame([[
            age, sex_encoded, cp, trestbps, chol, fbs, restecg,
            thalach, exang, oldpeak, slope, ca, thal
        ]], columns=[
            "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
            "thalach", "exang", "oldpeak", "slope", "ca", "thal"
        ])

        # Predict
        prediction = model.predict(input_data)[0]

        if prediction == 1:
            st.error("⚠ High risk of heart disease. Please consult a doctor.")
        else:
            st.success("✅ Heart condition appears normal.")
    
    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")
