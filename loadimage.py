import cv2
import os

# Specify the path to your dataset
dataset_path = 'path/to/dataset_folder'

# Example: Load a specific image
image_name = 'example_image.jpg'  # Change to your image file name
image_path = os.path.join(dataset_path, image_name)

# Load the image using OpenCV
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print(f"Error loading image: {image_name}")
else:
    print("Image loaded successfully.")
