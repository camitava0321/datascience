# Title: Make Llava Describe the Image
#
# Description:
# This script demonstrates "Multimodal" capabilities using Ollama.
# Multimodal means the model can understand more than just text—in this case,
# it can see and describe images.
#
# We use the 'llava' model (Large Language-and-Vision Assistant), which is
# specifically designed for image understanding.
#
# Installation:
# 1. Install the Python library:
#    pip install ollama
#
# 2. Pull the multimodal model (Required!):
#    Run this command in your terminal:
#    ollama pull llava:7b
#
# Note: Ensure you have a file named 'image.jpg' in the same folder as this script.
#
# How to run:
# python 8.py

import ollama  # Import the Ollama library

# Call the ollama.chat function.
# Unlike text-only models, we pass an extra 'images' list in the message.
response = ollama.chat(
    model='llava:7b',  # We MUST use a vision-capable model like 'llava'. 'llama3' will not work for images.
        messages=[
            {
                'role': 'user',
            'content': 'Describe the image.', # The text prompt asking the model what to do with the image.
            'images': ['image.jpg']           # A list of paths to image files. The model will analyze this file.
            }
        ]
    )

# Print the model's textual description of the image.
print(response['message']['content'])
#Run this file as
# C:/Users/AMITAVA/.conda/envs/ds_ml/python.exe -m streamlit run h:/DevelopmentWorkspaces/gitProjects/datascience/211-Ollama/005.py        
