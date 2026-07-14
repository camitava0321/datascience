# Title: Integrate LLM Model to Streamlit
#
# Description:
# This script connects the local Ollama LLM to a Streamlit web interface.
# It allows users to enter a prompt in the browser, sends that prompt to the
# local Llama 3.1 model, and displays the AI's generated response on the web page.
#
# Installation:
# You need both the 'streamlit' library for the UI and the 'ollama' library for the AI model.
#
# Command to install the libraries:
# pip install streamlit==1.33.0 ollama==0.2.1
#
# How to run this app:
# streamlit run 4.py

import streamlit as st  # Import Streamlit for the web UI
import ollama           # Import Ollama to interact with the local LLM

# Set the title of the web application
st.title("Ollama!")

# Create a text area for the user to input their question or prompt
prompt = st.text_area(label="Write your prompt to generate.")

# Create a "Submit" button
button = st.button("Okay")

# Check if the button was clicked
if button:
    # Check if the user actually typed a prompt
    if prompt:
        # Call the Ollama generate function.
        # model='llama3.1': Specifies the model to use (must be pulled locally).
        # prompt=prompt: Passes the user's text input to the model.
        response = ollama.generate(model='tinyllama:latest', prompt=prompt)

        # The 'response' object is a dictionary. We access the actual text
        # of the answer using the key ["response"].
        # st.markdown() renders the text, supporting rich formatting like bolding or lists.
        print(response["response"])
        st.markdown(response["response"])


#Run this file as
# C:/Users/AMITAVA/.conda/envs/ds_ml/python.exe -m streamlit run h:/DevelopmentWorkspaces/gitProjects/datascience/211-Ollama/003.py        
