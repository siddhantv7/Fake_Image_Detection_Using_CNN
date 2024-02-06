import cv2
import os
import numpy as np

def extract_and_store_frames(video_path, output_folder, num_frames):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    print(f"Video FPS: {fps}")
    print(f"Total Frames: {total_frames}")

    # Calculate frame indices to extract
    frame_indices = [int(i * total_frames / num_frames) for i in range(num_frames)]

    # Store frames and file paths in lists
    frames = []
    file_paths = []
    for i, frame_index in enumerate(frame_indices):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = cap.read()
        if ret:
            frames.append(frame)

            # Save the frame to the output folder
            image_name = f"frame_{i + 1}.jpg"
            image_path = os.path.join(output_folder, image_name)
            cv2.imwrite(image_path, frame)
            file_paths.append(image_path)

    # Release the video capture object
    cap.release()

    print(f"{num_frames} frames extracted and stored successfully.")

    return frames, file_paths

def process_images(image_paths):
    for image_path in image_paths:
        # Your processing logic here
        print(f"Processing image: {image_path}")

if __name__ == "__main__":
    # Provide the path to your video file
    video_path = "video1.mp4"

    # Provide the output folder where images will be saved
    output_folder = "output_images"

    # Set the number of frames to extract and store
    num_frames = 3

    # Call the function to extract and store frames
    stored_frames, stored_file_paths = extract_and_store_frames(video_path, output_folder, num_frames)

    # Call the function to process the stored images
    process_images(stored_file_paths)
