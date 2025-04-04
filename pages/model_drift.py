import streamlit as st

def model_drift(df):
    st.title("📉 Model Drift Analysis")
    if df is not None:
        st.write("### Dataset Summary")
        st.write(df.describe())
    else:
        st.warning("⚠ Please upload a dataset first.")
