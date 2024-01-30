from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
# Use the API key as needed
genai.configure(api_key=api_key)

def generate_text(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)

    return response.text

def process_image():
    pass
