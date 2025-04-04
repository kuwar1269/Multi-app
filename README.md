Multi-Page Streamlit App
========================

🚀 Overview
-----------

This project is a **Multi-Page Streamlit App** that allows users to upload datasets once and perform various tasks such as:

-   **Model Training**

-   **Predictions**

-   **SHAP Explainability**

-   **Data Analysis** using Evidently AI

The application provides a user-friendly interface for training machine learning models and visualizing results with SHAP (SHapley Additive Explanations) for explainability.

🛠 Features
-----------

-   📂 **Upload Dataset Once**: Users can upload a dataset and use it across different pages without re-uploading.

-   📊 **Model Training**: Train machine learning models on the uploaded dataset.

-   🤖 **Predictions**: Generate predictions based on trained models.

-   🔍 **SHAP Explainability**: Understand model decisions with SHAP visualizations.

-   📈 **Evidently AI Integration**: Monitor and analyze model performance.

-   🔧 **User-Friendly Interface**: Built using **Streamlit** for easy interaction.

📌 Setup Instructions
---------------------

Follow these steps to set up and run the project locally:

### 1️⃣ **Clone the Repository**

```
git clone https://github.com/kuwar1269/Multi-app.git
cd Multi-app/streamlit-app

```

### 2️⃣ **Create a Virtual Environment & Activate It**

```
python -m venv venv
# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

```

### 3️⃣ **Install Dependencies**

```
pip install -r requirements.txt

```

### 4️⃣ **Run the Application**

```
streamlit run app.py

```

📂 Project Structure
--------------------

```
Multi-app/
│── streamlit-app/
│   ├── app.py                 # Main entry point
│   ├── pages/
│   │   ├── model_training.py  # Model training module
│   │   ├── predictions.py     # Prediction module
│   │   ├── shap_explainability.py  # SHAP explainability module
│   │   ├── data_analysis.py   # Data analysis using Evidently AI
│   ├── data/                 # Sample datasets (if any)
│   ├── assets/               # Static files
│   ├── requirements.txt      # Dependencies
│── README.md                 # Project documentation

```

📊 Example Dataset
------------------

You can use any dataset from [Kaggle](https://www.kaggle.com/) or your custom dataset. Ensure the dataset is in CSV format.

⚡️ Technologies Used
--------------------

-   **Python**

-   **Streamlit**

-   **Scikit-learn**

-   **SHAP**

-   **Evidently AI**

-   **Pandas, Matplotlib, Seaborn**

🤝 Contributing
---------------

Feel free to contribute by submitting issues or pull requests.

📜 License
----------

This project is licensed under the [MIT License](https://chatgpt.com/c/LICENSE).

* * * * *

📧 For any queries, contact **Kunwarjot Singh** at [GitHub](https://github.com/kuwar1269). 🚀
