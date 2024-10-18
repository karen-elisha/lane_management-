import cv2
import os

# Function to preprocess images
def preprocess_images(dataset_path, output_path):
    # Check if output directory exists, create if not
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Preprocess all images in the dataset
    for image_name in os.listdir(dataset_path):
        image_path = os.path.join(dataset_path, image_name)
        
        # Load the image
        image = cv2.imread(image_path)
        if image is not None:
            # Resize the image
            resized_image = cv2.resize(image, (224, 224))  # Resize to 224x224 pixels
            
            # Convert to grayscale
            gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
            
            # Normalize the image
            normalized_image = gray_image / 255.0  # Normalize to [0, 1]
            
            # Apply Gaussian blur
            blurred_image = cv2.GaussianBlur(normalized_image, (5, 5), 0)

            # Save the preprocessed image
            output_image_name = f"processed_{image_name}"  # Prefix to distinguish processed images
            cv2.imwrite(os.path.join(output_path, output_image_name), (blurred_image * 255).astype(np.uint8))

    print("Preprocessing completed for all images.")

# Main execution
if __name__ == '__main__':
    # Specify the paths
    dataset_path = 'path/to/dataset_folder'  # Change this to your dataset folder path
    output_path = 'path/to/output_folder'  # Change this to your desired output folder path

    # Call the preprocessing function
    preprocess_images(dataset_path, output_path)

