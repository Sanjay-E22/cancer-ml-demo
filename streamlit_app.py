from app.main import cancer_prediction
import streamlit as st

st.title("Cancer Detection ML Demo")

cell_size = st.number_input("Cell Size", min_value=0, max_value=10, value=5)
cell_shape = st.number_input("Cell Shape", min_value=0, max_value=10, value=5)

if st.button("Predict"):
    result = cancer_prediction(cell_size, cell_shape)
    st.success(f"Prediction: {result}")
