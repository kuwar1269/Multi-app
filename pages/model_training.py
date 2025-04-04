import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def model_training(df):
    st.title("🤖 Model Training")
    
    if df is not None:
        st.write("### Dataset Preview")
        st.dataframe(df.head())

        # Select Target Column Manually
        target_column = st.selectbox("🎯 Select the Target Column", df.columns)

        if target_column:
            X = df.drop(columns=[target_column])
            y = df[target_column]

            # Splitting data
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Train Model
            model = RandomForestClassifier()
            model.fit(X_train, y_train)
            
            st.success(f"✅ Model Trained Successfully using '{target_column}' as Target Column!")
        else:
            st.warning("⚠ Please select a valid target column.")

    else:
        st.warning("⚠ Please upload a dataset first.")
