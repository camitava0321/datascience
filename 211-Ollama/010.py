# Title: Chat with PDF using Ollama LLM
#
# Description:
# This script demonstrates a basic "Retrieval-Augmented Generation" (RAG) concept.
# It allows users to upload a PDF document, extracts the text from it,
# and then lets the user ask questions about that specific document.
# The AI answers the question using the text of the PDF as its source material.
#
# Installation:
# pip install streamlit==1.33.0 ollama==0.2.1 PyMuPDF==1.24.10
#
# Note: The library name for import is 'fitz', but the install name is 'PyMuPDF'.
#
# How to run:
# streamlit run 13.py

import streamlit as st  # Web UI
import ollama           # Local LLM
import fitz             # PyMuPDF, used for reading PDF files
import os               # File path handling

# --- Function 1: Extract Text ---
# This function reads the PDF file and converts all its pages into a single string of text.
def extract_text_from_pdf(uploaded_file):
    # fitz.open() opens the PDF document.
    # It can handle file streams directly from Streamlit in many cases.
    doc = fitz.open(uploaded_file)
    text = ""
    
    # Loop through every page in the document
    for page in doc:
        # .get_text("text") explicitly requests plain text format as a string.
        # This ensures type safety and avoids potential type mismatches.
        page_text = page.get_text("text")
        if isinstance(page_text, str):
            text += page_text
        
    return text


# --- Function 2: Save File ---
# Standard function to save the uploaded file to the local disk.
# While 'fitz' can often read from memory, saving is a good practice for debugging
# and ensures consistent behavior.
def save_uploaded_file(uploaded_file):
    save_path = os.getcwd()
    file_path = os.path.join(save_path, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return st.success(f"Saved file: {uploaded_file.name} to {save_path}")


st.title("Chat with PDF!")

# File uploader restricted to .pdf files
uploaded_file = st.file_uploader("Upload your PDF file", type="pdf")
# print(uploaded_file)

if uploaded_file is not None:
    # 1. Save the file locally
    save_uploaded_file(uploaded_file)
    
    # 2. Extract the text content from the PDF
    # This turns the binary PDF into a long Python string variable 'pdf_text'.
    pdf_text = extract_text_from_pdf(uploaded_file)

    # Optional: Display the text to verify extraction worked
    # st.subheader("PDF Content:")
    # st.markdown(pdf_text)

    # 3. User Q&A Interface
    prompt = st.text_area(label="Ask a question based on the PDF content.")
    button = st.button("Okay")

    if button:
        if prompt:
            # 4. Construct the Prompt (Context Injection)
            # This is the core "RAG" trick. We don't train the model on the PDF.
            # Instead, we paste the ENTIRE PDF text into the prompt before the question.
            #
            # Format:
            # "Based on the following content: [ALL PDF TEXT] ... Question: [USER QUESTION]"
            combined_prompt = f"Based on the following content: {pdf_text}\n\nQuestion: {prompt}"
            
            # 5. Generate Answer
            # The model reads the context we provided and answers based on it.
            response = ollama.generate(model='llama3:latest', prompt=combined_prompt)
            
            # Display result
            st.markdown(response["response"])

#Run this file as
# C:/Users/AMITAVA/.conda/envs/ds_ml/python.exe -m streamlit run h:/DevelopmentWorkspaces/gitProjects/datascience/211-Ollama/010.py
