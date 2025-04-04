import streamlit as st

def etl_visualization(df):
    st.title("📊 ETL Visualization")
    if df is not None:
        st.write("### Dataset Preview")
        st.dataframe(df.head())
    else:
        st.warning("⚠ Please upload a dataset first.")
