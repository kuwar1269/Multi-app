import streamlit as st
import shap
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

def shap_explainability(df):
    st.title("📈 SHAP Explainability")

    if df is not None:
        st.write("### Dataset Preview")
        st.dataframe(df.head())

        # Select Target Column
        target_column = st.selectbox("🎯 Select the Target Column", df.columns)

        if target_column:
            X = df.drop(columns=[target_column])
            y = df[target_column]

            # Train Model
            model = RandomForestClassifier()
            model.fit(X, y)

            # SHAP Explanation
            explainer = shap.Explainer(model, X)
            shap_values = explainer(X)

            # Plot SHAP Summary
            st.write("### SHAP Summary Plot")
            fig, ax = plt.subplots()
            shap.summary_plot(shap_values, X, show=False)
            st.pyplot(fig)

        else:
            st.warning("⚠ Please select a valid target column.")

    else:
        st.warning("⚠ Please upload a dataset first.")
