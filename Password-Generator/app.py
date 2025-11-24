import streamlit as st
import random
import string

# --- Custom CSS for Styling ---
st.markdown("""
    <style>
        .main-title {
            font-size: 40px !important;
            font-weight: 800;
            text-align: center;
            color: #4CAF50;
        }
        .subtext {
            text-align: center;
            color: #555;
            font-size: 18px;
            margin-bottom: 20px;
        }
        .password-box {
            padding: 15px;
            background: #f0f2f6;
            border-radius: 10px;
            border: 2px solid #ddd;
            font-size: 22px;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Password Generator Function ---
def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# --- Streamlit UI ---
st.markdown("<div class='main-title'>🔒 Password Generator</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>Create strong & secure passwords instantly!</div>", unsafe_allow_html=True)

st.divider()

# --- Vertical Layout ---
st.markdown("### 📏 Select Password Length")
length = st.slider("", min_value=6, max_value=32, value=12)

st.markdown("### 🔧 Customize Your Password")
use_uppercase = st.checkbox("🔠 Include Uppercase Letters", value=True)
use_numbers = st.checkbox("🔢 Include Numbers", value=True)
use_special_chars = st.checkbox("✨ Include Special Characters", value=True)

st.divider()

# --- Generate Button ---
if st.button("🚀 Generate Password", use_container_width=True):
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    st.success("🎉 Your Strong Password is Ready!")
    st.markdown(f"<div class='password-box'>{password}</div>", unsafe_allow_html=True)
    st.code(password)
