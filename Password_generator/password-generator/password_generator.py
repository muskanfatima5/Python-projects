import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))
# _ is used when we dont know how many times we want to run the loop

st.title("Password Generator")

length = st.slider("Select the length of password", min_value=6, max_value=30, value=12)

use_digits = st.checkbox("Use Digits")

use_special = st.checkbox("Use Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password : `{password}`")
