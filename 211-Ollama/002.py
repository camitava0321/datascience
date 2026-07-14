# Title: Use Streamlit
#
# Description:
# This script demonstrates how to create a simple web interface using Streamlit.
# It sets up a basic UI with a title, a text input area for the user prompt,
# and a button to submit the prompt. When the button is clicked, it simply
# displays the text back to the user (echo).
#
# Installation:
# To run this script, you need to install the Streamlit library.
#
# Command to install the library:
# pip install streamlit==1.33.0
#
# How to run this app:
# Streamlit apps are not run like normal Python scripts (python 3.py).
# Instead, you must run them using the streamlit command:
# streamlit run 3.py

import streamlit as st  # Import streamlit and alias it as 'st' for easier usage

# Set the title of the web application
st.title("Ollama!")

# Create a multi-line text input area where the user can type their prompt
# The 'label' argument provides instructions to the user.
prompt = st.text_area(label="Write your prompt.")

# Create a button labeled "Okay".
# The st.button() function returns True when clicked, and False otherwise.
button = st.button("Okay")

# Check if the button has been clicked
if button:
    # Check if the user has actually entered some text in the prompt area
    if prompt:
        # If both conditions are met, display the prompt text on the screen
        # st.markdown() is used to render text, supporting Markdown formatting.
        st.markdown(prompt)

#Run this file as
# C:/Users/AMITAVA/.conda/envs/ds_ml/python.exe -m streamlit run h:/DevelopmentWorkspaces/gitProjects/datascience/211-Ollama/002.py        
