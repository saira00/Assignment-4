import streamlit as st
import random
import string

st.title("🔐 Random Password Generator")

# User input
num_passwords = st.number_input("How many passwords?", min_value=1, step=1)
password_length = st.number_input("Length of each password?", min_value=4, step=1)

# Generate on button click
if st.button("Generate Passwords"):
    characters = string.ascii_letters + string.digits + string.punctuation
    st.subheader("Generated Passwords")
    for _ in range(num_passwords):
        password = ''.join(random.choice(characters) for _ in range(password_length))
        st.code(password)
