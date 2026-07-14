# Title: Make a Image Describer page on Streamlit
#
# Description:
# This script integrates the 'Llava' image-understanding model into a Streamlit web app.
# It allows users to:
# 1. Upload one or multiple images via the browser.
# 2. Display the uploaded images.
# 3. Have the local AI describe each image automatically.
#
# IMPORTANT:
# Streamlit keeps uploaded files in RAM (memory), but Ollama expects a file PATH
# on the hard drive.
# In this specific file, we pass 'uploaded_file.name' to Ollama.
# We assume that the image you upload ALREADY exists in the same folder as this script.
# Since the file is on the disk, Ollama can find it using just the filename.
#
# Installation:
# pip install streamlit ollama
#
# How to run:
# streamlit run 9.py

import ollama  # For AI interaction
import streamlit as st  # For Web UI
import os  # Standard library for OS interactions

# pip install streamlit==1.24.0 (Optional version pinning)

st.title("Image Describer!")

# Create a file uploader widget.
# accept_multiple_files=True allows the user to select more than one image at a time.
# type=[...] restricts uploads to image formats.
uploaded_files = st.file_uploader("Choose an image", accept_multiple_files=True, type=["jpg", "jpeg", "png"])

# Print the list of uploaded file objects to the terminal for debugging.
print(uploaded_files)

# Check if the user has uploaded at least one file.
if len(uploaded_files) != 0:
    # Loop through each uploaded file.
    for uploaded_file in uploaded_files:
        # Debug prints
        print(uploaded_file.name)
        print(type(uploaded_file.name))

        # Display the image on the webpage.
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

        # Send the image to Llava for description.
        # CRITICAL NOTE: 'uploaded_file.name' gives us the filename (e.g., "image.jpg").
        # Because we are uploading a file that is ALREADY in our project folder,
        # Ollama can find it by name. If you uploaded a file from a different folder,
        # this would fail because Ollama wouldn't know the full path.
        response = ollama.chat(
            model='llava:7b',
            messages=[
                {
                    'role': 'user',
                                          'content': 'Describe the following images separately',
                    'images': [uploaded_file.name] # Passing the filename to Ollama
                }
            ]
        )

        # Display the AI's description on the webpage.
        st.markdown(response['message']['content'])
        
        # Print the description to the terminal as well.
        print(response['message']['content'])
