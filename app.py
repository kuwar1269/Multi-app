import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Multi-Page Streamlit App", layout="wide")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to:", ["Home", "ETL Visualization", "Model Drift", "Model Training", "SHAP Explainability"])

# File Uploader - Dataset is stored in Session State
st.sidebar.subheader("📂 Upload a Dataset")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file:
    st.session_state["dataset"] = pd.read_csv(uploaded_file)
    st.sidebar.success("✅ Dataset Uploaded Successfully!")

# Load Dataset from Session State
if "dataset" in st.session_state:
    df = st.session_state["dataset"]
else:
    df = None

# Page Routing
if page == "Home":
    st.title("🏠 Home Page")
    st.write("Welcome to the Streamlit Multi-Page App!")

elif page == "ETL Visualization":
    from pages.etl_visualization import etl_visualization
    etl_visualization(df)

elif page == "Model Drift":
    from pages.model_drift import model_drift
    model_drift(df)

elif page == "Model Training":
    from pages.model_training import model_training
    model_training(df)

elif page == "SHAP Explainability":
    from pages.shap_explainability import shap_explainability
    shap_explainability(df)
