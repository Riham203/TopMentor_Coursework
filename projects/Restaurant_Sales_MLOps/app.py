import os
import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from data_generator import generate_restaurant_data
from ml_pipeline import create_features, train_and_log_model

st.set_page_config(
    page_title="Restaurant Sales MLOps Dashboard", page_icon="🍽️", layout="wide"
)

st.title("🍽️ Restaurant Sales Analysis & MLOps Platform")
st.caption("End-to-End Automated Forecasting, Model Audit & Deployment")


# Load Artifacts
@st.cache_resource
def load_pipeline():
    if not os.path.exists("model_artifacts/model.pkl"):
        df = generate_restaurant_data()
        df.to_csv("restaurant_sales.csv", index=False)
        train_and_log_model()

    model = joblib.load("model_artifacts/model.pkl")
    feature_cols = joblib.load("model_artifacts/feature_cols.pkl")
    return model, feature_cols


model, feature_cols = load_pipeline()

# Sidebar Control Center
st.sidebar.header("🕹️ MLOps Operations")
op_mode = st.sidebar.radio(
    "Select Mode", ["Sales Dashboard", "Real-time Inference", "Model Retraining"]
)

# Mode 1: Dashboard
if op_mode == "Sales Dashboard":
    st.subheader("📊 Historical Sales Overview")
    df = pd.read_csv("restaurant_sales.csv")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Recorded Days", len(df))
    col2.metric("Average Daily Revenue", f"${df['daily_sales'].mean():,.2f}")
    col3.metric("Peak Daily Revenue", f"${df['daily_sales'].max():,.2f}")

    st.markdown("### Daily Revenue Trend")
    st.line_chart(df.set_index("date")["daily_sales"])

# Mode 2: Inference
elif op_mode == "Real-time Inference":
    st.subheader("🔮 Predict Tomorrow's Sales")

    df = pd.read_csv("restaurant_sales.csv")
    last_known = df.iloc[-1]

    col1, col2 = st.columns(2)
    with col1:
        is_weekend = st.selectbox("Is Weekend?", [0, 1], index=0)
        promotion = st.selectbox("Active Promotion?", [0, 1], index=0)
        avg_order_val = st.slider(
            "Expected Avg Order Value ($)", 15.0, 50.0, 28.5
        )

    with col2:
        month = st.slider("Month", 1, 12, 9)
        day_of_week = st.slider("Day of Week (0=Mon, 6=Sun)", 0, 6, 2)

    if st.button("🚀 Generate Sales Forecast", type="primary"):
        # Synthesize real-time feature row
        lag_1 = float(last_known["daily_sales"])
        lag_7 = float(df.iloc[-7]["daily_sales"])
        lag_14 = float(df.iloc[-14]["daily_sales"])
        rolling_mean = float(df["daily_sales"].tail(7).mean())
        rolling_std = float(df["daily_sales"].tail(7).std())

        input_data = pd.DataFrame(
            [
                {
                    "day_of_week": day_of_week,
                    "month": month,
                    "is_weekend": is_weekend,
                    "promotion": promotion,
                    "average_order_value": avg_order_val,
                    "day_of_year": 250,
                    "quarter": (month - 1) // 3 + 1,
                    "sales_lag_1": lag_1,
                    "sales_lag_7": lag_7,
                    "sales_lag_14": lag_14,
                    "rolling_mean_7": rolling_mean,
                    "rolling_std_7": rolling_std,
                }
            ]
        )

        prediction = model.predict(input_data[feature_cols])[0]
        st.success(
            f"💰 Estimated Revenue Forecast: **${prediction:,.2f}**"
        )

# Mode 3: Model Retraining
elif op_mode == "Model Retraining":
    st.subheader("🔄 Automated Continuous Retraining")
    st.info(
        "Triggers synthetic data refresh, feature engineering, and MLflow logging."
    )

    if st.button("⚡ Trigger Model Retrain"):
        with st.spinner("Re-generating data and re-training XGBoost..."):
            df = generate_restaurant_data()
            df.to_csv("restaurant_sales.csv", index=False)
            model, feature_cols = train_and_log_model()
            st.cache_resource.clear()
            st.success("✅ Model retrained and redeployed successfully!")