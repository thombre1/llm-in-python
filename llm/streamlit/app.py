import streamlit as st
import pandas as pd
import numpy as np

st.write("Hello world!")
st.title("Heading Below Text")

data = {
    "name" :["Aditya", "Coding", "100x Engineer", "Youtuber"],
    "age" : [21,22,23,24]

}
st.write(pd.DataFrame(data))

age = st.slider("Enter your age",0,100,21)
st.write(age)

subjects = ["C++","Python","Javascript","Java","Rust","Elixr"]
st.selectbox("Placeholder for subject, i guess...",subjects)

bin = st.file_uploader("Choose some file bro",type="csv")

if bin is not None:
    read_file =  pd.read_csv(bin)
    st.write(read_file)