# from transformers import pipeline
from src.models import generate_text, process_image
import os
import streamlit as st

def main():
    st.title("Text and Image Processing App")
    st.sidebar.title("Chat Clone")
    page = st.sidebar.radio("Select Option", ["Home", "Text Data", "Image Data"])

    if page == "Home":
        st.header("Welcome to the Home Page!")
        st.write("Please select an option from the sidebar.")

    elif page == "Text Data":
        st.header("Text Data Processing")
        user_input_text = st.text_area("Enter text data:")
        
        if st.button("Generate Text"):
            if user_input_text:
                generated_text = generate_text(user_input_text)
                st.subheader("Generated Text:")
                st.write(generated_text)
            else:
                st.warning("Please enter text data.")

    elif page == "Image Data":
        st.header("Image Data Processing")
        uploaded_file = st.file_uploader("Choose an image:", type=["jpg", "jpeg", "png"])
        
        if st.button("Process Image"):
            if uploaded_file:
                processed_image = process_image(uploaded_file)
                st.subheader("Processed Image:")
                st.image(processed_image, caption="Processed Image", use_column_width=True)
            else:
                st.warning("Please upload an image.")

if __name__ == "__main__":
    main()
