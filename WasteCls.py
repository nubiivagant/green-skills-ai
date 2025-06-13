import streamlit as st
import pandas as pd
import joblib as jb
import numpy as np

st.title("Waste Clasifiyer...")
weight =st.number_input("Enter Weight: ", min_value=0, max_value=2)
Color = st.number_input("Enter Color: ", min_value=0, max_value=1)
Texture = st.number_input("Enter Texture: ", min_value=0, max_value=1)
Odor = st.number_input("Enter Odor: ", min_value=0, max_value=1)
new_data=[[weight,Color,Texture,Odor]]
if st.button("Calculate"):
    loaded_model = jb.load(r"C:\Users\HP\OneDrive\green skilling\June '25\Waste Classification_model.pkl")
    pred = loaded_model.predict(new_data)
    st.write(pred)