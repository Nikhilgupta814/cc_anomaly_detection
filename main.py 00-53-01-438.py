import streamlit as st
import pandas as pd
import numpy as np
import joblib
from flask import Flask

st.set_page_config(page_title="Credit Card Fraud Detection", layout="centered")
st.title("💳 Credit Card Fraud Detection Pipeline")
st.write("Enter the transaction details below to evaluate the probability of fraud.")

@st.cache_resource
def load_model():
    return joblib.load('RF_credit_fraud_model.pkl')

try:
    pipeline = load_model()
except Exception as e:
    st.error("Could not load the model pipeline file. Please ensure 'best_fraud_model_pipeline.joblib' is in your directory.")
    st.stop()

with st.form("fraud_prediction_form"):
    st.subheader("Transaction Details")
    
    amt = st.number_input("Transaction Amount ($)", min_value=0.01, max_value=50000.0, value=25.00, step=0.1)
    age = st.number_input("Customer Age", min_value=18, max_value=110, value=35, step=1)
    city_pop = st.number_input("City Population", min_value=1, value=50000, step=500)
    zip_code = st.number_input("ZIP Code", min_value=0, max_value=99999, value=12345, step=1)

    st.markdown("---")
    st.subheader("Categorical Features")
    
    gender = st.selectbox("Gender", options=["M", "F"])
    
    category = st.selectbox("Transaction Category", options=[
        "entertainment", "food_dining", "gas_transport", "grocery_net", 
        "grocery_pos", "health_fitness", "home", "kids_pets", "misc_net", 
        "misc_pos", "personal_care", "shopping_net", "shopping_pos", "travel"
    ])
    
    merchant = st.text_input("Merchant Name", value="fraud_proof_shop")
    job = st.text_input("Customer Job Profession", value="Engineer")

    st.markdown("---")
    st.subheader("Date & Time Calculations")
    
    transaction_date = st.date_input("Transaction Date")
    transaction_time = st.time_input("Transaction Time")
    
    submit_button = st.form_submit_button(label="Analyze Transaction")

if submit_button:
    hour = transaction_time.hour
    day_of_week = transaction_date.weekday() # 0 = Monday, 6 = Sunday
    
    hour_sin = np.sin(2 * np.pi * hour / 24.0)
    hour_cos = np.cos(2 * np.pi * hour / 24.0)
    day_sin = np.sin(2 * np.pi * day_of_week / 7.0)
    day_cos = np.cos(2 * np.pi * day_of_week / 7.0)
    
    input_data = pd.DataFrame([{
        'merchant': merchant,
        'category': category,
        'gender': gender,
        'job': job,
        'age': age,
        'amt': amt,
        'zip': zip_code,
        'city_pop': city_pop,
        'hour_sin': hour_sin,
        'hour_cos': hour_cos,
        'day_sin': day_sin,
        'day_cos': day_cos
    }])
    
    # Prediction Execution
    try:
        prediction = pipeline.predict(input_data)[0]
        prediction_proba = pipeline.predict_proba(input_data)[0][1]
        
        st.markdown("### Risk Analysis Report")
        if prediction == 1:
            st.error(f"🚨 **High Risk Flagged!** This transaction mimics known fraud signatures.")
            st.metric(label="Fraud Risk Probability", value=f"{prediction_proba * 100:.2f}%")
        else:
            st.success(f"✅ **Transaction Approved.** Low fraud markers found.")
            st.metric(label="Fraud Risk Probability", value=f"{prediction_proba * 100:.2f}%")
            
    except Exception as err:
        st.error(f"Prediction failed. Ensure feature names match pipeline inputs exactly. Error details: {err}")
