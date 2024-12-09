from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

# Load the API key from the .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize the Gemini model
chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)

# Function to generate chatbot response
def chatbot_response(prompt):
    structured_prompt = f"Human: {prompt}\nAI:"
    response = chat_model([HumanMessage(content=structured_prompt)])
    return response.content.strip()
