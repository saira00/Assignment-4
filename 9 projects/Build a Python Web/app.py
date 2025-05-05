import streamlit as st

# Custom CSS to apply white text with black background
st.markdown("""
    <style>
    html, body, [data-testid="stApp"] {
        background-color: black !important;
        color: white !important;
    }
    .main, .block-container, .stTextInput, .stTextInput input {
        background-color: black !important;
        color: white !important;
    }
    div.stButton > button {
        background-color: #222222 !important;
        color: white !important;
        border: 1px solid white;
    }
    .stRadio > div {
        color: white !important;
    }
    h1, h2, h3, h4, h5, h6 {
        color: white !important;
    }
    p, label, .stTextInput input {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit App Content
st.title("💻 Build a Python Website with Streamlit")
st.subheader("Welcome to your first Streamlit web app!")

name = st.text_input("Enter your name:")
if st.button("Greet Me"):
    st.success(f"Hello, {name}! 👋 Welcome to Streamlit.")

st.markdown("### 🔽 Select your mood:")
mood = st.radio("How are you feeling today?", ["Happy", "Excited", "Curious", "Tired"])

if mood:
    st.write(f"You are feeling **{mood}** today — awesome! 😄")
