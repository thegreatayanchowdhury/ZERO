import streamlit as st
from main import chatbot_response
from dotenv import load_dotenv
import os

# Load the API key from the .env file
load_dotenv()

# Set up the page configuration and styling
st.set_page_config(page_title="ZERO", layout="wide")

def load_css():
    with open("style.css", "r") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

load_css()

# Image at the top-left corner (optional)
st.image("chatbot_banner.png", width=120)

# Title with centered styling
st.title("ZERO")

# Instruction for the user
st.markdown("### Ask me anything! 😊")

# Create a container for the chat
chat_container = st.empty()

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat Section - Input from the user
user_input = st.text_input("📝 Enter your message:", "", key="user_input")

# Create the fixed input box with Send button
with st.container():
    st.markdown("""<div class="input-container">""", unsafe_allow_html=True)
    if st.button("🚀 Send"):
        if user_input:
            # Add user message to session state
            st.session_state.messages.append(("user", user_input))
            
            # Get the chatbot response from the main.py
            response = chatbot_response(user_input)
            
            # Add ZERO response to session state
            st.session_state.messages.append(("ZERO", response))
            
            # Clear the input box by triggering a rerun
            st.rerun()  # Re-run the app to refresh the user input

        else:
            st.warning("Please enter a message before sending.")
    st.markdown("""</div>""", unsafe_allow_html=True)

# Render the chat container with all previous messages
with chat_container:
    chat_html = '<div class="chat-container">'
    
    for message_type, message in st.session_state.messages:
        if message_type == "user":
            chat_html += f'<div class="user-message">{message}</div>'
        elif message_type == "ZERO":
            chat_html += f'<div class="bot-message">{message}</div>'
    
    chat_html += '</div>'
    
    st.markdown(chat_html, unsafe_allow_html=True)
