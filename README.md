# Calories Burned Prediction App

## Project Description

This project is a Machine Learning application that predicts the number of calories burned based on user information and exercise data.

The model was developed using Random Forest Regression and deployed as an interactive web application using Streamlit.

## Input Features

- Gender
- Age
- Height (cm)
- Weight (kg)
- Exercise Duration (minutes)
- Heart Rate (bpm)
- Body Temperature (°C)

## Machine Learning Model

The project uses a Random Forest Regressor to predict calories burned.

The trained model is saved as:

model.pkl

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

## How to Run

Install the required libraries:

pip install -r requirements.txt

Then run the Streamlit application:

streamlit run app.py

## Prediction Example

The application predicts the calories burned in kcal based on the entered user data.