import streamlit as st 
import pandas as pd

st.title("BMI Calculator")

height = st.slider("Enter your height (in cm):",100, 250, 175)
weight = st.slider("Enter your weight (in kg):",40, 200, 70)

bmi = weight / ((height/100) ** 2)

st.write(f"your BMI is {bmi:.2f}")

st.write("### BMI Categories ###")
st.write("_Underweight: BMI less than 18.5")
st.write("_Normal weight: BMI between 18.5 and 24.9")
st.write("_Overweight: BMI between 25 and 29.9")
st.write("_Obesity: BMI 30 or greater")
