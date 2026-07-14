# Title: Separate a Video into Frames
#
# Description:
# This script demonstrates how to process a video file using the OpenCV library.
# The goal is to extract individual images (frames) from the video at specific intervals.
# In this example, we capture one frame every 2 seconds.
#
# This is a preparatory step for building a "Video Describer" AI. Since most
# LLMs cannot watch a video stream directly, we convert the video into a series
# of images, which we can then ask the vision model (Llava) to describe one by one.
#
# Installation:
# pip install opencv-python==4.11.0.86
#
# How to run:
# python 11.py
# (Ensure you have a file named 'video.mp4' in the same folder)

import cv2  # Import OpenCV, the standard library for computer vision

def video_to_frames(video_path):
    # Create a VideoCapture object. This opens the video file for reading.
    cap = cv2.VideoCapture(video_path)

    # Safety check: Ensure the video file was opened successfully.
    # If the path is wrong or the file is corrupted, this will fail.
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Get the Frames Per Second (FPS) of the video.
    # Example: If FPS is 30, the video displays 30 images every second.
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # Calculate the interval for capturing frames.
    # We want to save a frame every 2 seconds.
    # Formula: FPS * 2 seconds = Number of frames to skip.
    # E.g., 30 FPS * 2 = 60 frames. We will save every 60th frame.
    frame_interval = int(fps * 2)

    frame_count = 0        # Counter for the total frames passed
    saved_frame_count = 0  # Counter for how many frames we actually saved

    # Start an infinite loop to read through the video
    while True:
        # cap.read() returns two values:
        # 1. ret: A boolean (True/False) indicating if the frame was read successfully.
        # 2. frame: The image data (a NumPy array).
        ret, frame = cap.read()

        # If 'ret' is False, it means we reached the end of the video or an error occurred.
        if not ret:
            break

        # Check if the current frame count is a multiple of our interval.
        # The modulo operator (%) checks for the remainder.
        # If frame_count % 60 == 0, it means we are at frame 0, 60, 120, etc.
        if frame_count % frame_interval == 0:
            # Create a unique filename for this frame (e.g., frame_0.jpg, frame_1.jpg).
            filename = f"frame_{saved_frame_count}.jpg"
            
            # Save the image data to a file on the disk.
            cv2.imwrite(filename, frame)
            
            print(f"Saved {filename}")
            saved_frame_count += 1

        # Increment the total frame counter
        frame_count += 1
        
    # Print the total number of frames processed (for debugging).
    print(frame_count)

    # Release the video file to free up system resources.
    # This is important to prevent memory leaks or file locking issues.
    cap.release()

    print(f"Total frames saved: {saved_frame_count}")


# Example usage
# Define the path to the video file we want to process.
video_path = 'Introduction.mp4'  # Replace with your video file path if different.
video_to_frames(video_path)