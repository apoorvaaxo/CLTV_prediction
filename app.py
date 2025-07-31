# app.py

import streamlit as st
import pandas as pd
import os
import json
from lifetimes import BetaGeoFitter, GammaGammaFitter

# --- Load the saved models and data ---
@st.cache_resource
def load_models():
    # Load the trained BG/NBD and Gamma-Gamma models
    try:
        bgf = BetaGeoFitter()
        bgf.load_model('models/bgf.json')
        
        ggf = GammaGammaFitter()
        ggf.load_model('models/ggf.json')
        
        return bgf, ggf
    except FileNotFoundError:
        st.error("Model files not found. Please ensure bgf.json and ggf.json are in the 'models/' folder.")
        return None, None

@st.cache_data
def load_data():
    # Load the final summary CSV with business recommendations
    try:
        summary_path = 'data/processed/final_cltv_summary.csv'
        df_summary = pd.read_csv(summary_path, index_col='Segment')
        return df_summary
    except FileNotFoundError:
        st.error("Summary file not found. Please ensure final_cltv_summary.csv is in 'data/processed/'.")
        return pd.DataFrame()

bgf, ggf = load_models()
df_summary = load_data()


# --- Streamlit App UI and Logic ---
st.set_page_config(page_title="CLTV Prediction & Optimization", layout="wide")

st.title("Customer Lifetime Value (CLTV) Predictor")

st.markdown("""
This app predicts the Customer Lifetime Value for a new or existing customer based on their
Recency, Frequency, and Monetary (RFM) behavior. It leverages a probabilistic model
(BG/NBD and Gamma-Gamma) to forecast future revenue.
""")

st.markdown("---")

# --- Sidebar for User Input ---
st.sidebar.header("Enter Customer RFM Data")

with st.sidebar.form("rfm_form"):
    # Input fields for a customer's RFM and Tenure
    recency = st.number_input("Recency (Days since last purchase)", min_value=0, value=30)
    frequency = st.number_input("Frequency (Number of total purchases)", min_value=0, value=3)
    monetary = st.number_input("Total Monetary Value (Total spend)", min_value=0.0, value=500.0)
    tenure = st.number_input("Tenure (Customer Age in days)", min_value=0, value=150)
    
    # Check if the inputs are valid before predicting
    submitted = st.form_submit_button("Predict CLTV")

if submitted and bgf and ggf:
    # --- Prediction Logic ---
    # The lifetimes models require Frequency and Recency to be adjusted slightly
    # Frequency is (total purchases - 1) for repeat buyers.
    # Recency is the duration between the first and last purchase.
    # We will use the input values as a proxy for the models, but in a real app,
    # we would apply the same feature engineering logic used in the notebook.
    
    # Adjust frequency for the model:
    frequency_model = frequency - 1 if frequency > 0 else 0
    
    # Calculate a proxy for Recency_Model:
    recency_model = tenure - recency if tenure > recency else 0
    
    # Predict the number of future purchases (from BG/NBD model)
    predicted_purchases = bgf.conditional_expected_number_of_purchases_up_to_time(
        365, frequency_model, recency_model, tenure
    )
    
    # Predict the average monetary value per purchase (from Gamma-Gamma model)
    # The model should only be used for repeat buyers (frequency > 0)
    if frequency > 0:
        predicted_monetary_value = ggf.conditional_expected_average_profit(
            frequency, monetary
        )
    else:
        predicted_monetary_value = monetary  # For a single purchase, the average is the total spend

    # Calculate final CLTV
    predicted_cltv = predicted_purchases * predicted_monetary_value
    
    # --- Display Results ---
    st.success(f"### Predicted CLTV for the next 12 months: **${predicted_cltv:,.2f}**")
    st.write(f"This customer is predicted to make **{predicted_purchases:,.2f}** purchases.")
    st.write(f"The average monetary value per purchase is predicted to be **${predicted_monetary_value:,.2f}**.")
    st.balloons()

st.markdown("---")

# --- Display Final Recommendations from the Project ---
if not df_summary.empty:
    st.header("Project Recommendations Summary")
    st.markdown("""
    Based on the full customer analysis, the following segments and their characteristics were identified.
    The table below provides the average metrics and proposed strategies for each group.
    """)
    st.dataframe(df_summary)