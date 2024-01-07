# Importing required packages
import streamlit as st 

# Streamlit header
st.header('Simple Addition')

# Taking user inputs
input_1 = st.sidebar.number_input('Number input 1:')
input_2 = st.sidebar.number_input('Number input 2:')

# Addition
result = input_1 + input_2

st.write('Addition result: ', result)
