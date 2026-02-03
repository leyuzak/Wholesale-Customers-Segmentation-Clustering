import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Wholesale Customer Segmentation", page_icon="🛒", layout="centered")

@st.cache_resource
def load_artifacts():
    scaler = joblib.load("scaler.joblib")
    model = joblib.load("kmeans_wholesale.joblib")
    feature_names = joblib.load("feature_names.joblib")
    return scaler, model, feature_names

scaler, model, feature_names = load_artifacts()

st.title("🛒 Wholesale Customers Segmentation (K-Means)")
st.write("Enter annual spending values to predict the **customer segment (cluster)**.")

st.divider()

# input form
inputs = {}
for col in feature_names:
    inputs[col] = st.number_input(col, min_value=0.0, value=1000.0, step=100.0)

if st.button("Predict Cluster", use_container_width=True):
    x_input = pd.DataFrame([inputs])[feature_names]
    x_scaled = scaler.transform(x_input)
    cluster = int(model.predict(x_scaled)[0])

    st.subheader("Prediction")
    st.success(f"Predicted cluster: **{cluster}**")

    # optional: friendly label
    labels = {
        0: "balanced / low-to-medium spenders",
        1: "fresh-focused customers",
        2: "grocery & dairy heavy customers"
    }
    st.info(f"Segment description: **{labels.get(cluster, 'segment')}**")
