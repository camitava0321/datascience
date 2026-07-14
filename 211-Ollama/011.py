# Title: Chat with VIDEO using Ollama LLM and Whisper
#
# Description:
# This project enables users to "Chat with a Video".
# Unlike the previous "Video Describer" (which looked at images), this script
# listens to the AUDIO of the video.
#
# Workflow:
# 1. User uploads a video.
# 2. We extract the audio track from the video (using Pydub).
# 3. We transcribe the audio into text (using OpenAI's Whisper model).
# 4. We feed that text into Ollama (Llama 3) to answer user questions.
#
# Installation:
# pip install streamlit==1.33.0 ollama==0.2.1 openai-whisper==20240930 opencv-python==4.11.0.86 pydub==0.25.1 numpy==1.26.4
#
# Important Note:
# You also need 'ffmpeg' installed on your system for 'pydub' and 'whisper' to work.
# On Windows: Download from ffmpeg.org and add to PATH.
# On Mac: brew install ffmpeg
# On Linux: sudo apt install ffmpeg
#
# How to run:
# streamlit run 14.py

import streamlit as st
import os
import sys

# Configure ffmpeg/ffprobe path BEFORE importing pydub
# Get the conda environment path and set ffmpeg location
conda_env_path = os.path.dirname(sys.executable)
ffmpeg_bin_path = os.path.join(conda_env_path, "Library", "bin")
ffmpeg_path = os.path.join(ffmpeg_bin_path, "ffmpeg.exe")
ffprobe_path = os.path.join(ffmpeg_bin_path, "ffprobe.exe")

# Add ffmpeg directory to PATH so pydub can find both ffmpeg and ffprobe
if os.path.exists(ffmpeg_path) and os.path.exists(ffprobe_path):
    os.environ["PATH"] = ffmpeg_bin_path + os.pathsep + os.environ.get("PATH", "")
else:
    st.warning(f"ffmpeg or ffprobe not found at expected location: {ffmpeg_bin_path}")

import whisper          # OpenAI's speech-to-text model
import tempfile         # To create temporary files that handle themselves
import cv2              # OpenCV (not strictly used for audio here, but often part of video piping)
import numpy as np      # Numerical operations
from pydub import AudioSegment # For audio file manipulation (mp4 -> wav)
from pydub.utils import which  # To check for ffmpeg
import ollama           # Local LLM

# Load the Whisper model.
# "base" is a good balance between speed and accuracy.
# Options: "tiny", "base", "small", "medium", "large".
# The first time you run this, it will download the model weights (approx 140MB for base).
model = whisper.load_model("base")


# --- Function 1: Extract Audio ---
# This function handles the file conversion: Uploaded Video -> Saved MP4 -> Extracted WAV
def save_uploaded_video(uploaded_file):
    # Create a temporary file to save the video.
    # We use tempfile because we don't necessarily want to clutter the user's project folder permanently.
    # delete=False ensures the file stays there long enough for us to process it.
    temp_video_path = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4").name
    
    # Write the uploaded bytes to this temp file
    with open(temp_video_path, "wb") as f:
        f.write(uploaded_file.read())

    # Define the output audio path (changing extension from .mp4 to .wav)
    audio_path = temp_video_path.replace(".mp4", ".wav")
    
    # Use Pydub to load the video file and export just the audio track.
    # This relies on FFMPEG being installed on the system.
    video = AudioSegment.from_file(temp_video_path)
    video.export(audio_path, format="wav")

    return audio_path


# --- Function 2: Transcribe ---
# This function feeds the audio file to Whisper to get text.
def transcribe_audio(audio_path):
    # The .transcribe() method runs the neural network on the audio data.
    # It returns a dictionary.
    result = model.transcribe(audio_path)
    
    # We extract the 'text' string from the result.
    return result['text']


st.title("Video to Text and Q&A with LLM")

uploaded_file = st.file_uploader("Upload your video file", type=["mp4"])

if uploaded_file is not None:
    # 1. Save video and Convert to Audio
    audio_file_path = save_uploaded_video(uploaded_file)

    # 2. Transcribe (Audio -> Text)
    # This might take a few seconds depending on video length and CPU/GPU speed.
    transcribed_text = transcribe_audio(audio_file_path)

    # Display the full transcription to the user
    st.subheader("Transcribed Text:")
    st.write(transcribed_text)

    # 3. Chat Interface
    prompt = st.text_area(label="Ask a question based on the transcribed text.")
    button = st.button("Get Answer")

    if button:
        if prompt:
            # 4. Context Injection (RAG)
            # Similar to the PDF example, we paste the transcription into the prompt.
            combined_prompt = f"Based on the following content: {transcribed_text}\n\nQuestion: {prompt}"
            
            # 5. Generate Answer
            response = ollama.generate(model='llama3:latest', prompt=combined_prompt)
            st.markdown(response["response"])

#Run this file as
# C:/Users/AMITAVA/.conda/envs/ds_ml/python.exe -m streamlit run h:/DevelopmentWorkspaces/gitProjects/datascience/211-Ollama/011.py
