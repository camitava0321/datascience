# Title: Make a Video Describer
#
# Description:
# This is a full project that combines everything we've learned so far.
# It creates a "Video Describer" that can watch a video and tell you what happens in it.
#
# The Workflow:
# 1. User uploads a video (Streamlit).
# 2. We extract frames from the video (OpenCV), e.g., one image every 2 seconds.
# 3. We ask a Vision Model (Llava) to describe EACH frame individually.
# 4. We collect all these descriptions into a single text block.
# 5. We ask a Language Model (Llama 3) to summarize these descriptions into one coherent story.
#
# Installation:
# pip install opencv-python ollama streamlit
#
# How to run:
# streamlit run 12.py

import cv2          # For video processing (extracting frames)
import ollama       # For AI (Llava for vision, Llama 3 for text)
import streamlit as st  # For the Web UI
import os           # For file path handling

# --- Function 1: Extract Frames ---
# This function extracts one frame every 2 seconds from the video.
def video_to_frames(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Calculate frame skip interval (2 seconds worth of frames)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * 2)

    frame_count = 0
    saved_frame_count = 0

    while True:
        ret, frame = cap.read()
        
        # Stop loop if video ends
        if not ret:
            break

        # If we are at the correct interval (0s, 2s, 4s...)
        if frame_count % frame_interval == 0:
            filename = f"frame_{saved_frame_count}.jpg"
            
            # Add the filename to our global list 'frames' so we can find them later
            frames.append(filename)
            
            # Save the actual image file to disk
            cv2.imwrite(filename, frame)
            
            print(f"Saved {filename}")
            saved_frame_count += 1

        frame_count += 1
        
    print(frame_count)
    cap.release() # Close the video file
    print(f"Total frames saved: {saved_frame_count}")


# --- Function 2: Save Upload ---
# Saves the uploaded video from Streamlit RAM to the hard drive.
def save_uploaded_file(uploaded_file):
    save_path = os.getcwd()
    file_path = os.path.join(save_path, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return st.success(f"Saved file: {uploaded_file.name} to {save_path}")


st.title("Video Describer!")

# Allow user to upload an MP4 video
uploaded_file = st.file_uploader("Choose an video", type=["mp4"])

if uploaded_file is not None:
    # 1. Save the video file locally
    save_uploaded_file(uploaded_file)
    print(uploaded_file.name)
    print(type(uploaded_file.name))
    
    # Initialize an empty list to store frame filenames.
    # Note: This list 'frames' is used inside the 'video_to_frames' function.
    frames = []
    
    video_path = uploaded_file.name
    
    # 2. Extract frames from the video
    # This populates the 'frames' list with filenames like 'frame_0.jpg', 'frame_1.jpg'.
    video_to_frames(video_path)
    
    descriptions = ""
    
    # 3. Analyze each frame with Llava
    for i in frames:
        # st.image(i, caption='Uploaded Image.', use_column_width=True) # Optional: Show frame
        
        # Ask Llava to describe the current frame
        response = ollama.chat(model='llava:7b',
                               messages=[{'role': 'user',
                                          'content': 'Describe the image with one sentence.',
                                          'images': [i]}])

        # 4. Collect descriptions
        # Append the new description to our long string of text.
        # descriptions += "Frame 1: A man walking...\nFrame 2: He enters a door..."
        descriptions += f"\n{response['message']['content']}\n"
        # print(response['message']['content'])

    # 5. Summarize with Llama 3
    # We now have a list of disjointed descriptions.
    # We ask Llama 3 to read them all and write a smooth summary.
    prompt = f"Write a general explaination about what is going on in the video by using the following descriptions of the frames of the video. \n {descriptions}"
    
    answer = ollama.generate(model='llama3.1',
                             prompt=prompt)

    # 6. Display Result
    st.markdown("Description of the video!")
    st.markdown(answer["response"])

#Run this file as
# C:/Users/AMITAVA/.conda/envs/ds_ml/python.exe -m streamlit run h:/DevelopmentWorkspaces/gitProjects/datascience/211-Ollama/009.py
