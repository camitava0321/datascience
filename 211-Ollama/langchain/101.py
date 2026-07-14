# Title: Use Local LLM with Langchain
#
# Description:
# This script introduces "LangChain", a powerful framework for building applications with LLMs.
# While Ollama allows us to run models, LangChain provides the tools to connect those models
# to data, other tools, and complex workflows.
#
# In this simple example, we replace the direct 'ollama' library call with
# LangChain's 'Ollama' wrapper. This prepares us for more advanced features
# (like Chains and Agents) in future lessons.
#
# Installation:
# pip install streamlit==1.33.0 langchain==0.2.16 langchain-community==0.2.17
#
# How to run:
# streamlit run 15.py

import streamlit as st
from langchain.llms import Ollama  # Import the Ollama class from Langchain
# Note: In newer versions of LangChain, this might be:
# from langchain_community.llms import Ollama

st.title("Local LLM with Langchain!")

# Input for the prompt
prompt = st.text_area(label="Write your prompt.")
button = st.button("Okay")

if button:
    if prompt:
        # Initialize the local LLM using LangChain's wrapper.
        # This object acts like a standard function that takes text and returns text.
        # It automatically handles the connection to your local Ollama server.
        llm = Ollama(model='llama3.1')  # Specify your model here

        # Generate a response using the local LLM.
        # Unlike the native library which returns a dictionary {'response': '...'},
        # the LangChain wrapper typically returns the string directly.
        response = llm(prompt)

        # Display the response
        st.markdown(response)
