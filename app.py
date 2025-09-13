# app.py
import streamlit as st
import joblib
import numpy as np

st.title("Iris Flower Classifier 🌸")
model = joblib.load("models/iris_model.joblib")

st.write("Enter flower measurements:")

sepal_length = st.slider("sepal length (cm)", 4.0, 8.0, 5.8, 0.1)
sepal_width  = st.slider("sepal width (cm)", 2.0, 4.5, 3.0, 0.1)
petal_length = st.slider("petal length (cm)", 1.0, 7.0, 4.35, 0.1)
petal_width  = st.slider("petal width (cm)", 0.1, 2.5, 1.3, 0.1)

if st.button("Predict"):
    X = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    pred = model.predict(X)[0]
    names = ["setosa", "versicolor", "virginica"]
    st.success(f"Predicted species: {names[pred]}")