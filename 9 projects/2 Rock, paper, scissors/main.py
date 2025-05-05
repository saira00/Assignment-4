import random
import streamlit as st

# Custom styling
st.markdown("""
    <style>
        .st-radio > label {
            font-size: 18px;
            font-weight: bold;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 10px;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🪨📄✂️ Rock, Paper, Scissors Game")

choices = ["🪨 Rock", "📄 Paper", "✂️ Scissors"]

# User selection
user_choice = st.radio("Choose one:", choices)

# Mapping user choice
choice_map = {"🪨 Rock": "Rock", "📄 Paper": "Paper", "✂️ Scissors": "Scissors"}
user_choice_clean = choice_map[user_choice]

# Generate computer's choice
if st.button("Play"):  
    computer_choice = random.choice(list(choice_map.values()))
    
    # Determine winner
    if user_choice_clean == computer_choice:
        result = "It's a tie! 🤝"
    elif (user_choice_clean == "Rock" and computer_choice == "Scissors") or \
         (user_choice_clean == "Paper" and computer_choice == "Rock") or \
         (user_choice_clean == "Scissors" and computer_choice == "Paper"):
        result = "You win! 🎉"
    else:
        result = "You lose! 😢"
    
    # Display results with better formatting
    st.markdown(f"<h3>Computer chose: {computer_choice}</h3>", unsafe_allow_html=True)
    st.subheader(result)
