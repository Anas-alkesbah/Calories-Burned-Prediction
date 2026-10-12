# Calories Burned Prediction

A Machine Learning application that predicts the number of calories burned during exercise based on user and activity information.

The project uses a **Random Forest Regressor** and provides an interactive web interface built with **Streamlit**.

## Features

- Predict calories burned during exercise.
- Interactive interface for entering user information.
- Machine Learning model trained using exercise data.
- Model evaluation using regression metrics.

## Input Features

- Gender
- Age
- Height (cm)
- Weight (kg)
- Exercise Duration (minutes)
- Heart Rate (bpm)
- Body Temperature (°C)

## Model Performance

The Random Forest Regressor achieved the following results on the test dataset:

| Metric | Score |
|---|---:|
| Mean Absolute Error (MAE) | 1.76 |
| Mean Squared Error (MSE) | 7.83 |
| R² Score | 0.9979 |

These results represent the model's performance on the test split used during development. Performance on new real-world data may differ.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

## How to Run

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## Project Structure

- `app.py` — Streamlit application.
- `model.pkl` — Saved Random Forest model.
- `requirements.txt` — Project dependencies.
- `task2.ipynb` — Data analysis, model training, and evaluation notebook.

## Future Improvements

- Improve model validation on unseen data.
- Add visualizations for model performance.
- Improve input validation and user experience.
## Prediction Example

The application predicts the calories burned in kcal based on the entered user data.
