import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

nav = st.sidebar.radio("Navigation",["About","Predict"])
df = pd.read_csv('insurance.csv')

if nav=="About":
    st.title("Health Insurance Premium Predictor")
    st.text(" ")
    st.text(" ")
    st.image('health_insurance.jpeg',width=600)
    

df.replace({'sex':{'male':0,'female':1}},inplace=True)

df.replace({'smoker':{'yes':0,'no':1}},inplace=True)

df.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}},inplace=True)


x = df.drop(columns='charges',axis=1)

y = df['charges']

rfr = RandomForestRegressor()

rfr.fit(x,y)

if nav=="Predict":
    st.title("Enter Details")

    age = st.number_input("Age: ",step=1,min_value=0)

    sex = st.radio("Sex",("Male","Female"))

    if (sex == "Male"):
        s=0
    if (sex == "Female"):
        s=1
    bmi = st.number_input("BMI: ",min_value=0)

    children = st.number_input("Number of children: ",step=1,min_value=0)

    smoke = st.radio("Do you smoke",("Yes","No"))

    if (smoke=="Yes"):
        sm = 0
    if (smoke == "No"):
        sm = 1

    region = st.selectbox('Region',('SouthEast','SouthWest','NorthEast','NorthWest'))

    if (region == "SouthEast"):
        reg = 0
    if (region == "SouthWest"):
        reg = 1
    if (region == "NorthEast"):
        reg = 2
    if (region == "NorthWest"):
        reg = 3

    if st.button("Predict"):
        st.subheader("Predicted Premium")
        st.text(rfr.predict([[age,s,bmi,children,sm,reg]]))
    
