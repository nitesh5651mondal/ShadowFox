import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open('model/car_price_model.pkl', 'rb'))

st.title("🚗 Car Price Prediction")

# Inputs
present_price = st.number_input("Showroom Price (in lakhs)", min_value=0.0)
kms_driven = st.number_input("Kilometers Driven", min_value=0)
owner = st.selectbox("Number of Owners", [0, 1, 2, 3])
years_old = st.slider("Years Old", 0, 20)

fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel"])
seller = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

# 🔥 Predict Button (IMPORTANT)
if st.button("Predict Price"):

    input_data = {
        'Present_Price': present_price,
        'Kms_Driven': kms_driven,
        'Owner': owner,
        'Years_Old': years_old,

        'Fuel_Type_Diesel': 1 if fuel == "Diesel" else 0,
        'Fuel_Type_Petrol': 1 if fuel == "Petrol" else 0,

        'Seller_Type_Individual': 1 if seller == "Individual" else 0,

        'Transmission_Manual': 1 if transmission == "Manual" else 0
    }

    input_df = pd.DataFrame([input_data])

    # Fix feature mismatch
    model_features = model.feature_names_in_
    for col in model_features:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[model_features]

    # Prediction
    prediction = model.predict(input_df)

    st.success(f"💰 Estimated Price: ₹ {round(prediction[0], 2)} Lakhs")