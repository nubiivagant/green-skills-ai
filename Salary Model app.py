import streamlit as st
import pandas as pd

st.write("First Streamlit App")
df = pd.read_csv(r"C:\Users\HP\OneDrive\green skilling\June '25\Salary_Data.csv")
st.write(df)
st.line_chart(df)
