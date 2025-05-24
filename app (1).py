# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
from catboost import CatBoostRegressor
from sklearn.preprocessing import StandardScaler
import joblib

# Load model and scaler
model = joblib.load(r"model_catboost.pkl")
scaler = joblib.load(r"scaler.pkl")
numeric_features = joblib.load(r"features.pkl")

# Page setup
st.set_page_config(page_title="🔥 Calorie Prediction App", layout="centered")
st.title("🔥 Calories Prediction App")
st.markdown("Enter your workout details to estimate **calories burned**.")

# Sidebar with GIF and tip
st.sidebar.image(
    "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTNuemhucDRhaTUwcXh0ZmZ4eXltZzg0YmNrNWdxdHJ6YWdjN2lzaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IT4fLZjxyDu24/giphy.gif",
    use_container_width=True
)
st.sidebar.markdown("💡 **Tip:** Increase duration to see calorie impact!")

# User input
age = st.number_input("Age", min_value=1, max_value=120)
height = st.number_input("Height (cm)", min_value=50, max_value=250)
weight = st.number_input("Weight (kg)", min_value=20, max_value=200)
duration = st.number_input("Duration (min)", min_value=1, max_value=300)
heart_rate = st.number_input("Heart Rate (bpm)", min_value=30, max_value=220)
body_temp = st.number_input("Body Temperature (°C)", min_value=30.0, max_value=42.0)
sex = st.selectbox("Sex", ["male", "female"])

if body_temp > 39.5:
    st.warning("⚠️ High body temperature detected. Please recheck.")

# Prepare input data
sex_encoded = 0 if sex == "male" else 1
input_data = pd.DataFrame([[age, height, weight, duration, heart_rate, body_temp, sex_encoded]],
                          columns=['Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp', 'Sex'])
input_data[numeric_features] = scaler.transform(input_data[numeric_features])

# Prediction
if st.button("🔥 Predict Calories Burned"):
    prediction = model.predict(input_data)
    calories = round(prediction[0], 2)

    st.metric(label="Estimated Calories Burned", value=f"{calories} kcal")
    st.success(
        f"✅ You exercised for {duration} minutes.\n"
        f"✅ Heart rate: {heart_rate} bpm.\n"
        f"✅ You burned approximately **{calories} kcal**."
    )

    # Optional text summary about typical average burn
    avg_burn = round(duration * 6, 2)
    st.info(
        f"ℹ️ For reference, an average person burns about **{avg_burn} kcal** "
        f"over {duration} minutes using a general rule of 6 kcal per minute. "
        "Your predicted burn is personalized based on your inputs."
    )
