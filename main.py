import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("gemini_api_key")

# Configure Google Gemini API
genai.configure(api_key=api_key)

def get_poetry_feedback(poem):
    """Calls Google Gemini API to get feedback on the given poem."""
    model = genai.GenerativeModel("gemini-2.0-flash-lite")
    response = model.generate_content(f"Here is a poem:\n{poem}\nProvide feedback on its structure, imagery, and theme.")
    return response.text

# Streamlit UI
st.title("Poetry Feedback App")
st.write("Enter your poem below and get feedback!")

poem = st.text_area("Your Poem:")

if st.button("Get Feedback"):
    if poem.strip():
        if api_key:
            feedback = get_poetry_feedback(poem)
            st.subheader("Feedback:")
            st.write(feedback)
        else:
            st.error("API key not found. Please set GOOGLE_API_KEY as an environment variable.")
    else:
        st.warning("Please enter a poem before submitting.")
