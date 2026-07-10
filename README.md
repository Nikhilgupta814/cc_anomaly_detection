# Credit Card Fraud Detection

## 💳 Credit Card Fraud Detection Pipeline

=======
## <<<<<<< docs/adding_readme
💳 Credit Card Fraud Detection Pipeline
>>>>>>> 4b582c2c346a174054e57846467d6adc96919839
This project provides an end-to-end machine learning pipeline for detecting fraudulent credit card transactions. It includes data preprocessing, model training with various algorithms, experiment tracking using MLFlow, and a user-friendly frontend interface built with Streamlit.

## 🎯 Objective

The primary objective of this project is to build an end-to-end machine learning pipeline capable of accurately detecting fraudulent credit card transactions. Because fraud data is highly imbalanced (very few transactions are actually fraudulent), this pipeline focuses on balancing precision and recall to minimize false negatives while keeping false alarms low.

## 🚀 Project Overview

The core of this system is a Random Forest Classifier trained to identify fraudulent patterns. The project utilizes a robust feature engineering process (including cyclical time encoding) and is containerized for easy deployment.

### Key Features:

* **Data Pipeline:** Automated preprocessing using Scikit-Learn Pipeline and ColumnTransformer.
* **Model Tracking:** Integration with MLFlow for logging model parameters, metrics, and artifacts.
* **Inference Interface:** A Streamlit web application for real-time risk assessment.
* **Deployment-Ready:** Fully containerized using Docker.

## 🛠 Tech Stack

* **Language:** Python 3.10
* **ML Libraries:** Scikit-Learn, Pandas, NumPy, TensorFlow/Keras
* **Tracking:** MLFlow
* **Frontend:** Streamlit
* **Containerization:** Docker

## 📋 Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd credit-card-fraud-detection

```

Install dependencies:
It is recommended to use a virtual environment.

```bash
pip install -r requirements.txt

```

## 🚀 Running the Project

### Training the Model

The model training and evaluation are handled in the provided Jupyter Notebook. Ensure you have your Kaggle credentials configured to download the dataset automatically via kagglehub.

### Launching the Frontend (Streamlit)

To start the web application and begin making predictions, run:

```bash
streamlit run main.py

```

**Note:** Ensure `RF_credit_fraud_model.pkl` is in the same directory as `main.py`.

### Running with Docker

To build and run the application as a container:

Build the image:

```bash
docker build -t fraud-detection-app .

```

Run the container:

```bash
docker run -p 8501:8501 fraud-detection-app

```

Access the app by navigating to `http://localhost:8501` in your browser.

## 📂 Project Structure

* **main.py:** The Streamlit web application code.
* **requirements.txt:** Project dependencies.
* **Dockerfile:** Configuration for containerizing the app.
* **RF_credit_fraud_model.pkl:** The serialized best-performing model (Random Forest).
* **Fraud_Detection_Notebook.ipynb:** Complete EDA, feature engineering, training, and logging code.

## 📈 Performance Summary

The model was evaluated against unseen test data, with the Random Forest Classifier demonstrating the best performance in balancing precision and recall for highly imbalanced transaction data.
=======
📈 Performance Summary
The model was evaluated against unseen test data, with the Random Forest Classifier demonstrating the best performance in balancing precision and recall for highly imbalanced transaction data.
=======

