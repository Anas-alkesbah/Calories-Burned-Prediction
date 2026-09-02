import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load("model.pkl")

# App title
st.title("Calories Burned Prediction App")

st.write("Enter your information to predict the calories burned.")

# User inputs
age = st.number_input("Age", min_value=1, max_value=100, value=20)

height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=170.0)

weight = st.number_input("Weight (kg)", min_value=20.0, max_value=200.0, value=70.0)

duration = st.number_input(
    "Exercise Duration (minutes)",
    min_value=1.0,
    max_value=300.0,
    value=30.0
)

heart_rate = st.number_input(
    "Heart Rate (bpm)",
    min_value=40.0,
    max_value=220.0,
    value=100.0
)

body_temp = st.number_input(
    "Body Temperature (°C)",
    min_value=30.0,
    max_value=45.0,
    value=37.0
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

# Convert gender to numerical value
if gender == "Male":
    gender_value = 1
else:
    gender_value = 0

# Prediction button
if st.button("Predict Calories"):

    # Create input data in the same order as training
    input_data = np.array([[
        gender_value,
        age,
        height,
        weight,
        duration,
        heart_rate,
        body_temp
    ]])

    # Make prediction
    prediction = model.predict(input_data)

    # Display result
    st.success(
        f"Predicted Calories Burned: {prediction[0]:.2f} kcal"
    )