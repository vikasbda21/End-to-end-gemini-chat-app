from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

def generate_text(prompt):
    try:
        api_key = os.getenv("GOOGLE_API_KEY")
        # Use the API key as needed
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)

        return response.Text
    except Exception as e:
        # Handle the error appropriately
        print(f"An error occurred: {e}")
        return None

def process_image():
    pass
