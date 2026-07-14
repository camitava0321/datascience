# Title: Describe Multiple Images
#
# Description:
# This script improves upon the previous image describer by fixing the file path issue.
# It explicitly SAVES the uploaded image from RAM to the local hard drive.
# This ensures that Ollama can reliably find and read the file, regardless of where it came from.
#
# Installation:
# pip install streamlit ollama
#
# How to run:
# streamlit run 10.py

import ollama  # For AI interaction
import streamlit as st  # For Web UI
import os  # For handling file paths and saving

# pip install streamlit==1.24.0 (Optional version reference)

# --- Helper Function: Save File ---
# This function handles the logic of taking the file from Streamlit (RAM)
# and writing it to the disk.
def save_uploaded_file(uploaded_file):
    # Get the current working directory (where this script is running).
    save_path = os.getcwd()
    
    # Create the full absolute path (e.g., C:\Projects\Ollama\image.jpg).
    # os.path.join is safer than string concatenation ("/") because it handles
    # Windows/Mac/Linux path separators automatically.
    file_path = os.path.join(save_path, uploaded_file.name)

    # Save the file.
    # "wb" mode stands for "Write Binary". Images are binary files, not text.
    with open(file_path, "wb") as f:
        # .getbuffer() gets the raw bytes of the uploaded file.
        f.write(uploaded_file.getbuffer())

    # Display a success message to the user.
    return st.success(f"Saved file: {uploaded_file.name} to {save_path}")


st.title("Image Describer!")

# Allow user to upload multiple images.
uploaded_files = st.file_uploader("Choose an image", accept_multiple_files=True, type=["jpg", "jpeg", "png"])

# Debug print
print(uploaded_files)

if len(uploaded_files) != 0:
    for uploaded_file in uploaded_files:
        # 1. Save the file locally first!
        # This is the crucial fix compared to the previous lesson.
        # Now the file definitely exists on the disk at 'uploaded_file.name'.
        save_uploaded_file(uploaded_file)
        
        # Debug prints
        print(uploaded_file.name)
        print(type(uploaded_file.name))

        # Display the uploaded image.
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

        # 2. Send to Ollama
        # Since we just saved the file to the current working directory,
        # Ollama can now find it using just the filename.
        response = ollama.chat(
            model='llava:7b',
            messages=[
                {
                    'role': 'user',
                    'content': 'Describe the following images separately',
                    'images': [uploaded_file.name] # This path is now valid.
                }
            ]
        )

        # Display the description.
        st.markdown(response['message']['content'])
        print(response['message']['content'])

#Run this file as
# C:/Users/AMITAVA/.conda/envs/ds_ml/python.exe -m streamlit run h:/DevelopmentWorkspaces/gitProjects/datascience/211-Ollama/007.py
