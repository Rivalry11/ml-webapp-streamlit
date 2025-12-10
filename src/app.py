import streamlit as st
import numpy as np
import pandas as pd
import pickle
import os

st.set_page_config(page_title="Medical Insurance Predictor", layout="centered")

# Construir ruta absoluta al model.pkl
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

# Cargar el modelo
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

st.title("💰 Predicción del Costo de Seguro Médico")

st.write("Introduce los datos del paciente para estimar el costo del seguro.")

# Inputs
age = st.number_input("Edad", min_value=1, max_value=100, value=30)
bmi = st.number_input("Índice BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Número de hijos", min_value=0, max_value=10, value=0)

sex = st.selectbox("Sexo", ["male", "female"])
smoker = st.selectbox("¿Fumador?", ["yes", "no"])
region = st.selectbox("Región", ["southwest", "southeast", "northwest", "northeast"])

# === CORRECCIÓN AQUÍ ===
if st.button("Predecir costo"):
    input_data = pd.DataFrame([{
        "age": age,
        "bmi": bmi,
        "children": children,
        "sex": sex,
        "smoker": smoker,
        "region": region
    }])

    prediction = model.predict(input_data)[0]

    st.success(f"El costo estimado del seguro es: **${prediction:,.2f}**")