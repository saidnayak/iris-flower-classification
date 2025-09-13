# Iris Flower Classification 🌸

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-brightgreen)

A machine learning project to classify Iris flowers into different species using **scikit-learn** and a **Streamlit** web app.

## 🚀 Features
- Train a model on the classic Iris dataset
- Save and load trained models (`joblib`)
- Interactive web interface with Streamlit
- Predict species based on user input

## 📂 Project Structure
├── app.py # Streamlit web app
├── train.py # Script to train and save the model
├── iris_classification.ipynb # Jupyter notebook for experimentation
├── iris_model.joblib # Saved ML model
├── requirements.txt # Dependencies
├── README.md # Project documentation
└── LICENSE # MIT License

## 🛠️ Installation
Clone the repository:
```bash
git clone https://github.com/saidnayak/iris-flower-classification.git
cd iris-flower-classification

## Create and activate a virtual environment:
python -m venv venv
.\venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux

## Install dependencies:
pip install -r requirements.txt

## ▶️ Usage
Run the Streamlit app:
streamlit run app.py

## 📜 License
This project is licensed under the MIT License