import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('solar_rf_model.pkl')

st.set_page_config(page_title="Solar Power Predictor", page_icon="☀️")

st.title("☀️ Solar Power Output Predictor")
st.write(
    "This dashboard predicts solar plant AC power output based on weather conditions, "
    "using a Random Forest model trained on real solar plant data."
)

st.header("Enter Weather Conditions")

irradiation = st.slider(
    "Irradiation (solar energy intensity)",
    min_value=0.0, max_value=1.2, value=0.5, step=0.01
)

module_temp = st.slider(
    "Module Temperature (°C)",
    min_value=15.0, max_value=70.0, value=35.0, step=0.5
)

ambient_temp = st.slider(
    "Ambient Temperature (°C)",
    min_value=15.0, max_value=40.0, value=28.0, step=0.5
)

# Prepare input for prediction
input_data = np.array([[irradiation, module_temp, ambient_temp]])
prediction = model.predict(input_data)[0]

st.header("Predicted AC Power Output")
st.metric(label="Predicted Power", value=f"{prediction:.2f} units")

st.divider()

st.subheader("About this project")
st.write(
    "Built using a dataset of solar plant generation and weather sensor readings. "
    "A Random Forest Regressor was trained on irradiation, module temperature, and ambient "
    "temperature to predict AC power output, achieving an R² score of 0.986 on test data. "
    "Feature importance analysis showed irradiation alone accounts for over 99% of the "
    "model's predictive power, consistent with the physics of photovoltaic power generation."
)

st.caption("Project by [Your Name] | EEE Student")
